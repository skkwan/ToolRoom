'''
Usage: python gfalCopyDirectoriesIntelligently.py
'''

import argparse
import os
import sys

parser = argparse.ArgumentParser(description='From the below listed origin and existing destination folders (e.g. on lxplus and UW Tier 2 respectively, gfal-copy the missing directories as background processes.')
parser.add_argument('--execute', dest='execute', action='store_true')
parser.set_defaults(execute=False)

args = parser.parse_args()


# List all directories in this folder with "" and commas 
# Better: for i in $(ls -d */); do echo \"${i%%/}\"\,; done

#originFolders=["DY1JetsToLL","DY2JetsToLL","DY3JetsToLL","DY4JetsToLL","DYJetsToLL","DYJetsToLL_M-10to50","Embedded-Run2018A-MuTau","Embedded-Run2018B-MuTau","Embedded-Run2018C-MuTau","Embedded-Run2018D-MuTau","ggZH_HToTauTau_ZToLL","ggZH_HToTauTau_ZToNuNu","ggZH_HToTauTau_ZToQQ","GluGluHToTauTau","GluGluHToWWTo2L2Nu","GluGluZH_HToWW","HWminusJ_HToWW","HWplusJ_HToWW","HZJ_HToWW","README.md","SingleMuon-Run2018A","SingleMuon-Run2018B","SingleMuon-Run2018C","SingleMuon-Run2018D","ST_t-channel_antitop","ST_t-channel_top","ST_tW_antitop","ST_tW_top","SUSYGluGluToHToAA_AToBB_AToTauTau_M-45","SUSYVBFHToAA_AToBB_AToTauTau_M-45","ttHTobb","ttHToNonbb","TTTo2L2Nu","TTTo2L2Nu_Skim.root","TTToHadronic","TTToHadronic-ext2","TTToSemiLeptonic","TTToSemiLeptonic-ext3","VBFHToTauTau","VBFHToTauTau_Skim.root","VBFHToWWTo2L2Nu","VVTo2L2Nu","W1JetsToLNu","W2JetsToLNu","W3JetsToLNu","W4JetsToLNu","WJetsToLNu","WminusHToTauTau","WplusHToTauTau","WZTo2L2Q","WZTo3LNu","ZHToTauTau","ZZTo2L2Q","ZZTo4L"]

#existingDestinationFolders=["DY1JetsToLL","DY2JetsToLL","DY3JetsToLL","DY4JetsToLL","DYJetsToLL","DYJetsToLL_M-10to50","Embedded-Run2018A-MuTau","Embedded-Run2018B-MuTau","Embedded-Run2018C-MuTau","Embedded-Run2018D-MuTau","GluGluHToTauTau","GluGluHToWWTo2L2Nu","GluGluZH_HToWW","HWminusJ_HToWW","HWplusJ_HToWW","HZJ_HToWW","README.md","SingleMuon-Run2018A","SingleMuon-Run2018B","SingleMuon-Run2018C","SingleMuon-Run2018D","ST_t-channel_antitop","ST_t-channel_top","ST_tW_antitop","ST_tW_top","SUSYGluGluToHToAA_AToBB_AToTauTau_M-45","SUSYVBFHToAA_AToBB_AToTauTau_M-45"]


# Need to copy these files
# originFolders=["DY1JetsToLL",
# "DY2JetsToLL",
# "DY3JetsToLL",
# "DY4JetsToLL",
# "DYJetsToLL",
# "DYJetsToLL_M-10to50",
# "GluGluHToTauTau",
# "GluGluHToWWTo2L2Nu",
# "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45",
# "SUSYVBFHToAA_AToBB_AToTauTau_M-45",
# "VBFHToTauTau",
# "VBFHToWWTo2L2Nu",
# "W1JetsToLNu",
# "W2JetsToLNu",
# "W3JetsToLNu",
# "W4JetsToLNu",
# "WJetsToLNu"]

#originFolders=["DYJetsToLL_M-10to50", "TTTo2L2Nu"]
originFolders=["SingleMuon-Run2018A","SingleMuon-Run2018B","SingleMuon-Run2018C","SingleMuon-Run2018D"]

existingDestinationFolders=[]

for originFolder in originFolders:
    if (originFolder not in existingDestinationFolders):
        print(originFolder + " not found at destination")
        # command = "nohup gfal-copy -p -r -t 999999999 /eos/user/s/skkwan/hToAA/condor/Jul-11-2022-14h25m-PreApprovalChecks_test/%s davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018_preapprovalChecks/%s > logRun_%s &" % (originFolder, originFolder, originFolder)

        command = "nohup gfal-copy -p -r -t 999999999 davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018_svfitted/%s /eos/user/s/skkwan/hToAA/svfitted/%s > logRun_%s &" % (originFolder, originFolder, originFolder)
        if (args.execute):
            print(">>> Executing " + command)
            os.system(command)
        else:
            print(">>> Execute flag not set, command is " + command)
        
        
        
