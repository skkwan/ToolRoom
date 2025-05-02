# Usage:
# Do voms proxy, make sure you are in ROOT version > 6.34 (for DefaultValueFor to work)
# python3 countEventsInDataset.py
#
# M

from json import dumps
import json

import os

import sys
import ROOT
import re

cut = "GenModel_TChiZH_700_1"

files = [    
    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/0051C0B9-4639-C04E-A548-55EB7C33CD89.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A78401FF-A506-ED4C-A7D8-E1DB40FE7609.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/430B5C71-0DF5-5E4E-81DC-15840D2AB4CF.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/B15411C9-6150-834C-AAC9-5AC1883971FE.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/4E7F2D48-33E7-564D-BE3E-9251DD9BCC7E.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/BAA99EDF-91CE-534E-90F8-192F3C012181.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A9F6D499-D1A6-4C48-8105-89262B7E54B1.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A2BAAB7E-BC95-8F40-B8F1-9BC663EC0039.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/18EB0057-F784-E64C-9F31-883E4E536CF0.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/514247BE-9B35-5E43-8729-AC6507271FD7.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A9B4AE16-3CF5-0E42-A55A-27842389BA34.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/106F18D9-C493-3849-9BD4-81283F0696D3.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/2D0A3A96-E351-A64A-95B3-F97B69A78BA5.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/BEAB0832-FD6A-F546-BAF5-A21E3CAA65F6.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A8CBD5A0-4B16-0546-9557-2CC503D462BB.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/4AF1EAFA-2F5E-8C45-8380-86CAA5EEF423.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/5E51979D-20C8-4F4A-9E5A-887086A05BC9.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/1A78966B-61E3-0D4E-9823-945B03E47617.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/5A67165A-7C99-8248-A021-7C42B7E14973.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/F9E29EFC-D3E9-5540-A3A8-A6F4181B1389.root",
]

def getNumberOfEventsPassingCut(cut: str) -> float:
    """
    Get the number of events in a dataset passing a cut.
    """

    # Add the input files to a TChain
    ch = ROOT.TChain("Events")

    for file in files:
        ch.Add(file)

    # Create dataframe from TChain
    df = ROOT.RDataFrame(ch)
    df = df.DefaultValueFor("GenModel_TChiZH_700_1", False)

    print(f"Will apply this cut: {cut}")
    dfWithCut = df.Filter(cut, f"Applying cut: {cut}")
    nEntries = dfWithCut.Count().GetValue()

    # Example of how to query the report programatically 
    fullreport = dfWithCut.Report()
    for report in fullreport.GetValue():
        print("This is how you print one cut: ")
        print(f"name: {report.GetName()}, eff: {report.GetEff()}, all events: {report.GetAll()}, passing events: {report.GetPass()}")
    
    # Normal way of printing the report
    print("Printing report with .Print()...")
    fullreport.Print()

    print(nEntries)
    return nEntries



if __name__ == '__main__':
    # Count number of events in the whole dataset that pass this cut 
    eventCount = getNumberOfEventsPassingCut(cut)
    # Use regex to get the simple name
    with open("out.csv", "a") as out:
        out.write(f"{eventCount}")
