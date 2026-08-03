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

cut = "LHE_HT < 70"

files = [    
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_1.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_10.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_11.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_12.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_13.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_14.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_15.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_16.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_17.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_18.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_19.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_2.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_20.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_21.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_22.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_23.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_24.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_25.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_26.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_27.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_28.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_29.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_3.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_30.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_31.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_32.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_33.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_34.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_35.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_36.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_37.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_38.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_39.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_4.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_40.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_41.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_42.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_43.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_44.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_45.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_46.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_47.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_48.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_49.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_5.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_50.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_51.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_52.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_53.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_54.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_55.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_56.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_57.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_58.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_59.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_6.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_60.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_61.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_62.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_63.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_64.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_65.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_66.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_67.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_68.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_69.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_7.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_70.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_71.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_8.root",
    "root://cmsxrootd.fnal.gov//store/user/skkwan/HiggsinoSkim/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skimTest_DYJetsToLL_M-50_RunIISummer20UL18NanoAODv9/250218_205201/0000/tree_9.root",
]

def getNumberOfEventsPassingCut(cut: str) -> float:
    """
    Get the number of events in a dataset passing a cut.
    """

    print("Building TChain...")

    # Add the input files to a TChain
    ch = ROOT.TChain("Events")

    for file in files:
        print(f"Adding {file}")
        ch.Add(file)

    # Create dataframe from TChain
    df = ROOT.RDataFrame(ch)
    # df = df.DefaultValueFor("GenModel_TChiZH_700_1", False)

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
    with open("out.csv", "w") as out:
        out.write(f"{eventCount}")
