# pickEventFromLocalFileInCMSSW.sh

# Must be run in a CMSSW environment: do cmsenv
# Command from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookPickEvents#Run_edm_PickEvents_py_Interactiv

# To find which file the lumi is in, you can do `file,lumi dataset=/RelValElectronGunPt2To100/CMSSW_10_6_0_patch2-106X_upgrade2023_realistic_v3_2023D41noPU-v1/GEN-SIM-DIGI-RAW` and try to Ctrl+F
# Or use the command-line interface and Ctrl+F the output file

cmsenv

edmCopyPickMerge outputFile=myEvent.root \
                 eventsToProcess=1:32:3102 \
                 inputFiles=/afs/cern.ch/work/s/skkwan/public/phase2RCT/RelValElectronGunPt2To100_71C02E39-ED72-054B-871F-6B1FD1A1C14A.root
