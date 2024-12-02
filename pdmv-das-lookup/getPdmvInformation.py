# Usage
# First do cmsenv from some CMSSW environment, and get voms proxy, and come back to this script
# python3 getPdmvInformation.py
#
# This script looks up a set of prepIDs (the LHEGEN level ones) in a range in "requests_query". Note
# that the command-line interface gives a URL to click on to verify your login, then go back to the
# command line and hit "Enter" per the prompt.
# This gives a .json and in it we look up the filter efficiency. The entry to check is "4" (hardcoded in filter_efficiency).
# Next, the script looks up the number of events in the associated AOD dataset from dasgoclient, with the --json flag
# so it outputs to a temp.json, and we look for the entry with "nevents" in it.
# Lastly, all of this is piped to a report.txt file.

from json import dumps
import json

import os

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM

mcm = McM(id=McM.OIDC, dev=True, debug=False)

# https://its.cern.ch/jira/browse/HIGHPRIOREQ-760 

# 2018 Cascade
    # SUS-RunIISummer20UL18wmLHEGEN-00934 -> SUS-RunIISummer20UL18wmLHEGEN-00953
    # SUS-RunIISummer20UL18wmLHEGEN-01071 -> SUS-RunIISummer20UL18wmLHEGEN-01090

# 2018 Non-Cascade
    # SUS-RunIISummer20UL18wmLHEGEN-00913 -> SUS-RunIISummer20UL18wmLHEGEN-00925
    # SUS-RunIISummer20UL18wmLHEGEN-00968  
    # SUS-RunIISummer20UL18wmLHEGEN-01058  
    # SUS-RunIISummer20UL18wmLHEGEN-01060 -> SUS-RunIISummer20UL18wmLHEGEN-01070

# 2017 Cascade
    # SUS-RunIISummer20UL17wmLHEGEN-00900
    # SUS-RunIISummer20UL17wmLHEGEN-01004 -> SUS-RunIISummer20UL17wmLHEGEN-01018
    # SUS-RunIISummer20UL17wmLHEGEN-01020 -> SUS-RunIISummer20UL17wmLHEGEN-01023
    # SUS-RunIISummer20UL17wmLHEGEN-00864 -> SUS-RunIISummer20UL17wmLHEGEN-00883
#2017 Non-Cascade
    # SUS-RunIISummer20UL17wmLHEGEN-00847 -> SUS-RunIISummer20UL17wmLHEGEN-00859
    # SUS-RunIISummer20UL17wmLHEGEN-00901  
    # SUS-RunIISummer20UL17wmLHEGEN-00992 -> SUS-RunIISummer20UL17wmLHEGEN-01003

# 2016 Cascade preVFP
    # SUS-RunIISummer20UL16wmLHEGENAPV-00890 -> SUS-RunIISummer20UL16wmLHEGENAPV-00909
    # SUS-RunIISummer20UL16wmLHEGENAPV-01031 -> SUS-RunIISummer20UL16wmLHEGENAPV-01050

# 2016 Non-Cascade preVFP
    # SUS-RunIISummer20UL16wmLHEGENAPV-00873 -> SUS-RunIISummer20UL16wmLHEGENAPV-00885
    # SUS-RunIISummer20UL16wmLHEGENAPV-00924  
    # SUS-RunIISummer20UL16wmLHEGENAPV-01018 -> SUS-RunIISummer20UL16wmLHEGENAPV-01029


# 2016 Cascade postVFP
    # SUS-RunIISummer20UL16wmLHEGEN-00987 -> SUS-RunIISummer20UL16wmLHEGEN-01006
    # SUS-RunIISummer20UL16wmLHEGEN-01112 -> SUS-RunIISummer20UL16wmLHEGEN-01131

# 2016 Non-Cascade postVFP
    # SUS-RunIISummer20UL16wmLHEGEN-00943 -> SUS-RunIISummer20UL16wmLHEGEN-00955
    # SUS-RunIISummer20UL16wmLHEGEN-01099 -> SUS-RunIISummer20UL16wmLHEGEN-01111

requests_query = """
    SUS-RunIISummer20UL16wmLHEGEN-00987 -> SUS-RunIISummer20UL16wmLHEGEN-01006
    SUS-RunIISummer20UL16wmLHEGEN-01112 -> SUS-RunIISummer20UL16wmLHEGEN-01131
    SUS-RunIISummer20UL16wmLHEGEN-00943 -> SUS-RunIISummer20UL16wmLHEGEN-00955
    SUS-RunIISummer20UL16wmLHEGEN-01099 -> SUS-RunIISummer20UL16wmLHEGEN-01111
"""

range_of_requests = mcm.get_range_of_requests(requests_query)
print("Found %s requests" % (len(range_of_requests)))
for request in range_of_requests:

    # "request" is a dictionary. We need to loop through the dictionary to get the dataset name stored in "pdmv_dataset_name", because this is inconsistently in different locations
    arrayOfDictsToCheck = request["reqmgr_name"]
    for dictToCheck in arrayOfDictsToCheck: # e.g. request["reqmgr_name"][2]
        if "content" in dictToCheck:
            d = dictToCheck["content"] # it will always be in "content"
            if "pdmv_dataset_name" in d:
                dataset_name=d["pdmv_dataset_name"]
                print(f">>> Found {dataset_name}")

    # Note: "4" is hardcoded
    filter_efficiency=request["validation"]["results"]["4"][0]["filter_efficiency"]

    # Now look up by the dataset name 
    campaign_requests = mcm.get(
        "requests", query=f"produce={dataset_name}"
    )

    
    command=f'dasgoclient -query="dataset={dataset_name}" --json > temp.json'
    os.system(command)
    with open("temp.json", "r") as json_file:
        data = json.load(json_file)
        # This is really specific, if in doubt inspect the .json file 
        for d1 in data:
            for d2 in d1["dataset"]:
                if "nevents" in d2.keys():
                    nevents = d2["nevents"]
                    nEventsAsMillion = nevents/1000000

    with open("report.txt", "a") as report:
        dataset_name_abbrev = dataset_name[:dataset_name.find('_TuneCP5')]
        dataset_name_abbrev = dataset_name_abbrev.replace(" ", "_")
        report.write(f'{dataset_name_abbrev}  & {nEventsAsMillion:.2f}M & {filter_efficiency:.6f} \\\\ \n')

    with open("pythonConfig.py", "a") as report:
        report.write(f'"{dataset_name_abbrev}": {filter_efficiency:.6f},\n')