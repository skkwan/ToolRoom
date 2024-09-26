# Usage
# First do cmsenv from some CMSSW environment, and get voms proxy, and come back to this script
# python3 getPdmvInformation.py

from json import dumps
import json

import os

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM

mcm = McM(id=McM.OIDC, dev=True, debug=True)

# Cascade VBF
requests_query = """
    SUS-RunIISummer20UL18wmLHEGEN-01071 -> SUS-RunIISummer20UL18wmLHEGEN-01090
    SUS-RunIISummer20UL18wmLHEGEN-00934 -> SUS-RunIISummer20UL18wmLHEGEN-00953
"""

range_of_requests = mcm.get_range_of_requests(requests_query)
print("Found %s requests" % (len(range_of_requests)))
for request in range_of_requests:

    dataset_name=request["reqmgr_name"][1]["content"]["pdmv_dataset_name"]

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

    with open("report.txt", "a") as report:
        dataset_name_abbrev = dataset_name[:dataset_name.find('_TuneCP5')]
        dataset_name_abbrev = dataset_name_abbrev.replace(" ", "_")
        report.write(f'{dataset_name_abbrev}  & {nevents:,} & {filter_efficiency:.6f} \\\\ \n')
