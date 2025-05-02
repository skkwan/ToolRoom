import ROOT

histsToCheck = ["ZJ",
                "ttbar",
                "ST",
                "VV",
                "ggh_htt",
                "ggh_hww",
                "qqh_htt",
                "qqh_hww",
                "Zh_htt",
                "Zh_hww",
                "Wh_htt",
                "Wh_hww",
                "tth",
                "embedded",
                "data_obs",
                "fake"]

myFile = ROOT.TFile.Open("/eos/user/s/skkwan/hToAA/condorHistogramming/2024-09-24-17h53m-iteration18-mutau/out_mutau.root", "READ")

for hist in histsToCheck:
    title = f"inclusive/{hist}_bpt_deepflavour_1"
    h = myFile.Get(title)
    h.Print("all")
    