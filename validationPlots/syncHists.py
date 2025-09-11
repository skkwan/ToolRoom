import os, ROOT
import cmsstyle as CMS

def addOverflow(h: ROOT.TH1F) -> ROOT.TH1F:
    """
    Add overflow to a histogram
    """
    h.SetBinContent(h.GetNbinsX(), h.GetBinContent(h.GetNbinsX()) + h.GetBinContent(h.GetNbinsX() + 1))
    return h

variablesInfo = [
    ["pt_1", "Leading lepton p_{T} [GeV]", 0., 150.],
    ["pt_2", "Sub-leading lepton p_{T} [GeV]", 0., 150.],
    ["eta_1", "Leading lepton eta", -2.5, 2.5],
    ["eta_2", "Sub-leading lepton eta", -2.5, 2.5],
    ["phi_1", "Leading lepton phi", -3.14, 3.14],
    ["phi_2", "Sub-leading lepton eta", -3.14, 3.14],
    ["bpt_ak4_1", "Leading b-tag jet p_{T} [GeV]", 0., 150.],
    ["bpt_ak4_2", "Sub-leading b-tag jet p_{T} [GeV]", 0., 150.],
    ["beta_ak4_1", "Leading b-tag jet eta", -2.5, 2.5],
    ["beta_ak4_2", "Sub-leading b-tag jet eta", -2.5, 2.5],
    ["bphi_ak4_1", "Leading b-tag jet phi", -3.14, 3.14],
    ["bphi_ak4_2", "Sub-leading b-tag jet phi", -3.14, 3.14],

]

infile1 = ROOT.TFile.Open("/eos/cms/store/group/phys_susy/skkwan/condorPostProcessing/2025-08-26-02h10m-dataMC-2018-symm-MT2/DYJetsToLL_M-50/DYJetsToLL_M-50_0.root")
infile2 = ROOT.TFile.Open("/afs/cern.ch/work/s/skkwan/public/zhmet/CMSSW_14_0_21/src/luna-zhmet/skim/DYJetsToLL_M-50-mini.root")
df1 = ROOT.RDataFrame("event_tree", infile1)
df2 = ROOT.RDataFrame("event_tree", infile2)


for varInfo in variablesInfo:
    variable = varInfo[0]
    xlabel = varInfo[1]
    xmin = varInfo[2]
    xmax = varInfo[3]

    h1 = df1.Histo1D(("var", "var", 40, xmin, xmax), variable).GetValue()
    h2 = df2.Histo1D(("var", "var", 40, xmin, xmax), variable).GetValue()
    h1 = addOverflow(h1)
    h2 = addOverflow(h2)
    h1.SetLineColor(ROOT.TColor.GetColor("#f89c20"))
    h2.SetLineColor(ROOT.TColor.GetColor("#92dadd"))
    h1.SetMarkerColor(0)
    h1.SetLineWidth(2)
    h2.SetMarkerColor(0)
    h2.SetLineWidth(2)
    legYmin = 0.89 - 0.05 * 4
    legYmax = 0.89
    legXmin = 0.45
    legXmax = 0.45 + 0.4
    if ("eta" in variable) or ("phi" in variable):
        legYmin = 0.40 - 0.05 * 4
        legYmax = 0.40
        legXmin = 0.4
        legXmax = 0.4 + 0.4
    leg = CMS.cmsLeg(legXmin, legYmin, legXmax, legYmax, textSize=0.04)
    leg.SetHeader("DYJets, one file (same events)")
    leg.AddEntry(h1, "Before refactor", "l")
    leg.AddEntry(h2, "After", "l")

    CMS.SetLumi("")

    canv = CMS.cmsCanvas(variable, xmin, xmax, 0, max(h1.GetMaximum(), h2.GetMaximum()) * 1.05,
                        nameXaxis = xlabel,
                        nameYaxis = 'Events',
                        square = CMS.kSquare, extraSpace=0.05, yTitOffset=1.6, iPos=0)
    canv.SetRightMargin(0.05)
    CMS.SetExtraText("Private work (CMS simulation)")
    CMS.SetCmsTextFont(52)
    CMS.SetCmsTextSize(0.75*0.76)
    CMS.UpdatePad(canv)

    CMS.cmsObjectDraw(h1, "HIST")
    CMS.cmsObjectDraw(h2, "HIST SAME")
    CMS.cmsObjectDraw(leg)

    CMS.UpdatePad(canv)

    name = f"/eos/user/s/skkwan/www/higgsino/studies/sync/dyJets_{variable}"
    canv.SaveAs(f"{name}.pdf")
    canv.SaveAs(f"{name}.png")

    del(canv)
    del(leg)