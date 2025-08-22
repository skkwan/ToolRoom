import os, ROOT
import cmsstyle as CMS

def addOverflow(h: ROOT.TH1F) -> ROOT.TH1F:
    """
    Add overflow to a histogram
    """
    h.SetBinContent(h.GetNbinsX(), h.GetBinContent(h.GetNbinsX()) + h.GetBinContent(h.GetNbinsX() + 1))
    return h


infile = ROOT.TFile.Open("/afs/cern.ch/work/s/skkwan/public/zhmet/CMSSW_14_0_21/src/luna-zhmet/postprocessing/TTTo2L2Nu-mini.root")

df = ROOT.RDataFrame("event_tree", infile)
xmax = 120.
h1 = df.Histo1D(("mt2", "mt2", 40, 0., xmax), "mt2_lb_nominal").GetValue()
h1 = addOverflow(h1)
h1.SetLineColor(ROOT.TColor.GetColor("#f89c20"))
h1.SetMarkerColor(0)
h1.SetLineWidth(2)
leg = CMS.cmsLeg(0.5, 0.89 - 0.05 * 7, 0.90, 0.89, textSize=0.04)
leg.AddEntry(h1, "ttbar events in one file", "l")

canv = CMS.cmsCanvas('TTbar events in one file', 0, xmax, 0, h1.GetMaximum() * 1.05,
                    nameXaxis = 'MT2(lb) [GeV]',
                    nameYaxis = 'Events',
                    square = CMS.kSquare, extraSpace=0.05, yTitOffset=1.6, iPos=0)
canv.SetRightMargin(0.05)
CMS.SetExtraText("Private work (CMS simulation)")
CMS.SetCmsTextFont(52)
CMS.SetCmsTextSize(0.75*0.76)
CMS.SetLumi("")
CMS.UpdatePad(canv)

CMS.cmsObjectDraw(h1, "HIST")
CMS.cmsObjectDraw(leg)

CMS.UpdatePad(canv)

name = "/eos/user/s/skkwan/www/higgsino/studies/fix-mt2/mt2_lb_nominal_ttbar"
canv.SaveAs(f"{name}.pdf")
canv.SaveAs(f"{name}.png")
