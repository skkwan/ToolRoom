import ROOT

files = [
    "root://cms-xrd-global.cern.ch//store/data/Run2018A/DoubleMuon/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/714E37D3-27F4-E144-80F7-B7B19F7EFD9F.root",
]

for file in files:
    print(f">>> Opening {file}")
    df = ROOT.RDataFrame("Events", file)
    df2 = df.Filter("event == 501715073", f"Getting event 501715073 from {file}")
    df2.Snapshot("Events", "event_501715073.root")
    report = df2.Report()
    report.Print()
