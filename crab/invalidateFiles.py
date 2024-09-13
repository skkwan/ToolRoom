# invalidateFiles.py
# Loop through a given list of LFNs in DAS prod/phys03 and invalidate them, so they do not show
# up in DAS. Useful for when DAS is showing a bunch of outdated/non-existant file paths. 
# Use this after checking what files actually exist in UWisc T2 /hdfs storage.

# More details: https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Changing_a_dataset_or_file_statu

# Usage:
#    cmsenv
#    voms-proxy-init -voms cms -rfc -valid 192:00
#    source /cvmfs/cms.cern.ch/common/crab-setup.sh
#    ls $DBS3_CLIENT_ROOT/examples/DataOpsScripts/
#    python invalidateFiles.py --[execute or dryrun] --list=path_to_LFN.txt

import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description='Script for invalidating multiple files in DAS')

parser.add_argument("--execute",
                    help="Execute the crab submit commands.",
                    dest='execute', action = 'store_true')
parser.add_argument("--dryrun", 
                    help="Dryrun only.",
                    dest='execute', action = 'store_false')
parser.set_defaults(execute=False)

parser.add_argument("--list",
                    help="Path to .txt file of LFN to invalidate.",
                    dest='list_of_lfn', required=True)

args = parser.parse_args()


invalidateCommand="crab setfilestatus --status INVALID --file "

with open(args.list_of_lfn) as infile:
    for line in infile:
        print(invalidateCommand + line)
        if (args.execute):
            os.system(invalidateCommand + line)