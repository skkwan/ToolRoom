# Usage
# First do cmsenv from some CMSSW environment, and get voms proxy, and come back to this script
# python3 getEventsInDatasets.py
#
# This script looks up a dataset 

from json import dumps
import json

import os

import sys
import ROOT
import re

datasets = [    
    "2018,WWTo2L2Nu,/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/skkwan-skimTest_WWTo2L2Nu_RunIISummer20UL18NanoAODv9-1ea93bf7cfbb24e247bd0f4bd1955225/USER,1",
    "2018,WZTo2Q2L,/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/skkwan-skimTest_WZTo2Q2L_RunIISummer20UL18NanoAODv9-1ea93bf7cfbb24e247bd0f4bd1955225/USER,1",
    "2018,WZTo3LNu,/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/skkwan-skimTest_WZTo3LNu_RunIISummer20UL18NanoAODv9-1ea93bf7cfbb24e247bd0f4bd1955225/USER,1",
    "2018,ZH_HToBB_ZToLL_M-125,/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/skkwan-skimTest_ZH_HToBB_ZToLL_M-125_RunIISummer20UL18NanoAODv9-1ea93bf7cfbb24e247bd0f4bd1955225/USER,1",
]

def getNumberOfEvents(dataset_name):
    """
    Get the number of events in a dataset
    """
    command = f'dasgoclient -query="file dataset={dataset_name} instance=prod/phys03" > allfiles.csv'
    os.system(command)

    nEntriesTotal = 0

    with open("allfiles.csv", "r") as allfiles:
        for line in allfiles:
            df = ROOT.RDataFrame("Events", f"root://cms-xrd-global.cern.ch//{line}")
            nEntries = df.Count().GetValue()
            nEntriesTotal += nEntries
            print(f"Found {nEntries} events, so far I have {nEntriesTotal} events")
    print(nEntriesTotal)
    return nEntriesTotal



if __name__ == '__main__':
    os.system("rm out.csv")
    os.system("touch out.csv")
    for line in datasets:
        x = line.split(",")
        dataset_name = x[1]
        dataset_path = x[2]
        eventCount = getNumberOfEvents(dataset_path)
        eventCountAsString = str(eventCount)
        # Use regex to get the simple name
        with open("out.csv", "a") as out:
            out.write("    {" + dataset_name + ", " + eventCountAsString + ".0},")
