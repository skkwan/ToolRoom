import ROOT

thisDf = ROOT.RDataFrame("mutau/event_tree", "/eos/user/s/skkwan/hToAA/condorPostProcessing/2024-01-22-11h39m-no-btag-cut-accept-all-Embedded/SingleMuon-Run2018B/postprocessed_ntuple_SingleMuon-Run2018B_1.root")

thisDf.Filter("evt == 186648436").Snapshot("mutau/event_tree", "oneEvent.root")

report = thisDf.Report()
report.Print()