# copyFiles.py

# xrdcp all files in a list defined below, to the current directory

import os

list = [# '/store/relval/CMSSW_10_6_0_patch2/RelValElectronGunPt2To100/GEN-SIM-DIGI-RAW/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/190EDE9F-770B-174A-8BA6-F7814FC67FD4.root',
        '/store/relval/CMSSW_10_6_0_patch2/RelValElectronGunPt2To100/GEN-SIM-DIGI-RAW/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/283255C6-1E20-6F48-8B8B-31E6A62BD48D.root',
        '/store/relval/CMSSW_10_6_0_patch2/RelValElectronGunPt2To100/GEN-SIM-DIGI-RAW/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/71C02E39-ED72-054B-871F-6B1FD1A1C14A.root',
        '/store/relval/CMSSW_10_6_0_patch2/RelValElectronGunPt2To100/GEN-SIM-DIGI-RAW/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/8B75BCAF-FF0C-094C-AB40-08F104148BC0.root',
        '/store/relval/CMSSW_10_6_0_patch2/RelValElectronGunPt2To100/GEN-SIM-DIGI-RAW/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/A22AA5DB-ACEE-1140-B081-104F634079A1.root']

for file in list:
    command = "xrdcp root://cmsxrootd.fnal.gov//" + file + " RelValElectronGunPt2To100_" + os.path.basename(file) 
    print(command)
    os.system(command)
