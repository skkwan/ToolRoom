import os, ROOT
import cmsstyle as CMS

def addOverflow(h: ROOT.TH1F) -> ROOT.TH1F:
    """
    Add overflow to a histogram
    """
    h.SetBinContent(h.GetNbinsX(), h.GetBinContent(h.GetNbinsX()) + h.GetBinContent(h.GetNbinsX() + 1))
    return h

variable = "trkHTScalarEmu"
xlabel = "HT [GeV]"
xmin = 0.
xmax = 800.
infile = ROOT.TFile.Open("/afs/cern.ch/work/s/skkwan/public/globalTrackTrigger/CMSSW_16_1_0_pre3/src/L1Trigger/L1TTrackMatch/test/GTTObjects_ttbar200PU_Spring23.root")

df = ROOT.RDataFrame("L1TrackNtuple/eventTree", infile)
h1 = df.Histo1D(("var", "var", 40, xmin, xmax), variable).GetValue()
h1 = addOverflow(h1)
h1.SetLineColor(ROOT.TColor.GetColor("#f89c20"))
h1.SetMarkerColor(0)
h1.SetLineWidth(2)
leg = CMS.cmsLeg(0.5, 0.89 - 0.05 * 7, 0.90, 0.89, textSize=0.04)
leg.AddEntry(h1, "ttbar events (200 PU)", "l")

CMS.SetLumi("")

canv = CMS.cmsCanvas('TTbar events', 0, xmax, 0, h1.GetMaximum() * 1.05,
                    nameXaxis = xlabel,
                    nameYaxis = 'Events',
                    square = CMS.kSquare, extraSpace=0.05, yTitOffset=1.6, iPos=0)
canv.SetRightMargin(0.05)
CMS.SetExtraText("Private work (CMS simulation)")
CMS.SetCmsTextFont(52)
CMS.SetCmsTextSize(0.75*0.76)
CMS.UpdatePad(canv)

CMS.cmsObjectDraw(h1, "HIST")
CMS.cmsObjectDraw(leg)

CMS.UpdatePad(canv)

name = f"/eos/user/s/skkwan/www/globalTrackTrigger/ht/{variable}"
canv.SaveAs(f"{name}.pdf")
canv.SaveAs(f"{name}.png")
