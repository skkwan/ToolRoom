#  python unzipGridPackTarballs.py
#  Usage:
#    In a directory in afs, e.g. /afs/hep.wisc.edu/home/skkwan/public/gridpacks-UL/genproductions/bin/MadGraph5_aMCatNLO/validation
#    run this Python script to unzip the tarballs in /hdfs/, test creation of ten events, and copy the resulting .lhe file back to /hdfs/.
#    Then it is up to the user to check whether the .lhe files make sense.

import os


ggH_symmetric = {
    "path": "cards/production/2017/13TeV/bbtautau_final_state/ggh01_M125_Toa01a01_Tobbtautau/",
    "names": [
        'ggh01_M125_Toa01a01_M11_Tobbtautau',
        'ggh01_M125_Toa01a01_M12_Tobbtautau',
        'ggh01_M125_Toa01a01_M13_Tobbtautau',
        'ggh01_M125_Toa01a01_M14_Tobbtautau',
        'ggh01_M125_Toa01a01_M15_Tobbtautau',
        'ggh01_M125_Toa01a01_M20_Tobbtautau',
        'ggh01_M125_Toa01a01_M25_Tobbtautau',
        'ggh01_M125_Toa01a01_M30_Tobbtautau',
        'ggh01_M125_Toa01a01_M35_Tobbtautau',
        'ggh01_M125_Toa01a01_M40_Tobbtautau',
        'ggh01_M125_Toa01a01_M45_Tobbtautau',
        'ggh01_M125_Toa01a01_M50_Tobbtautau',
        'ggh01_M125_Toa01a01_M55_Tobbtautau',
        'ggh01_M125_Toa01a01_M60_Tobbtautau'
    ]
}

vbf_symmetric = {
    "path": "cards/production/2017/13TeV/bbtautau_final_state/vbfh01_M125_Toa01a01_Tobbtautau/",
    "names": [
        'vbfh01_M125_Toa01a01_M11_Tobbtautau',
         'vbfh01_M125_Toa01a01_M12_Tobbtautau',
         'vbfh01_M125_Toa01a01_M13_Tobbtautau',
         'vbfh01_M125_Toa01a01_M14_Tobbtautau',
         'vbfh01_M125_Toa01a01_M15_Tobbtautau',
         'vbfh01_M125_Toa01a01_M20_Tobbtautau',
         'vbfh01_M125_Toa01a01_M25_Tobbtautau',
         'vbfh01_M125_Toa01a01_M30_Tobbtautau',
         'vbfh01_M125_Toa01a01_M35_Tobbtautau',
         'vbfh01_M125_Toa01a01_M40_Tobbtautau',
         'vbfh01_M125_Toa01a01_M45_Tobbtautau',
         'vbfh01_M125_Toa01a01_M50_Tobbtautau',
         'vbfh01_M125_Toa01a01_M55_Tobbtautau',
         'vbfh01_M125_Toa01a01_M60_Tobbtautau'
    ]
}

ggH_cascade = {
    "path": "cards/production/2017/13TeV/bbtautau_final_state/ggh3_M125_Toh1h2/cascade/",
    "names": [
         'ggh3_M125_Toh1h2_M15_M100_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M110_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M30_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M40_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M50_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M60_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M70_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M80_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M15_M90_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M20_M100_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M20_M40_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M20_M50_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M20_M60_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M20_M70_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M20_M80_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M20_M90_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M30_M60_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M30_M70_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M30_M80_h2_Toh1h1',
         'ggh3_M125_Toh1h2_M30_M90_h2_Toh1h1'
    ]
}

ggH_non_cascade = {
    "path": "cards/production/2017/13TeV/bbtautau_final_state/ggh3_M125_Toh1h2/non_cascade/",
    "names": [
         'ggh3_M125_Toh1h2_M15_M30',
         'ggh3_M125_Toh1h2_M15_M20',
         'ggh3_M125_Toh1h2_M30_M60',
         'ggh3_M125_Toh1h2_M30_M50',
         'ggh3_M125_Toh1h2_M30_M40',
         'ggh3_M125_Toh1h2_M20_M40',
         'ggh3_M125_Toh1h2_M20_M30',
         'ggh3_M125_Toh1h2_M40_M70',
         'ggh3_M125_Toh1h2_M40_M60',
         'ggh3_M125_Toh1h2_M40_M50',
         'ggh3_M125_Toh1h2_M50_M70',
         'ggh3_M125_Toh1h2_M50_M60',
         'ggh3_M125_Toh1h2_M40_M80'
    ]
}

vbf_cascade = {
    "path": "cards/production/2017/13TeV/bbtautau_final_state/vbfh3_M125_Toh1h2/cascade/",
    "names": [
         'vbfh3_M125_Toh1h2_M15_M100_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M110_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M30_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M40_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M50_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M60_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M70_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M80_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M15_M90_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M20_M100_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M20_M40_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M20_M50_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M20_M60_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M20_M70_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M20_M80_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M20_M90_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M30_M60_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M30_M70_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M30_M80_h2_Toh1h1',
         'vbfh3_M125_Toh1h2_M30_M90_h2_Toh1h1'
    ]
}

vbf_non_cascade = {
    "path": "cards/production/2017/13TeV/bbtautau_final_state/vbfh3_M125_Toh1h2/non_cascade/",
    "names": [
         'vbfh3_M125_Toh1h2_M15_M20',
         'vbfh3_M125_Toh1h2_M15_M30',
         'vbfh3_M125_Toh1h2_M20_M30',
         'vbfh3_M125_Toh1h2_M20_M40',
         'vbfh3_M125_Toh1h2_M30_M40',
         'vbfh3_M125_Toh1h2_M30_M50',
         'vbfh3_M125_Toh1h2_M30_M60',
         'vbfh3_M125_Toh1h2_M40_M50',
         'vbfh3_M125_Toh1h2_M40_M60',
         'vbfh3_M125_Toh1h2_M40_M70',
         'vbfh3_M125_Toh1h2_M40_M80',
         'vbfh3_M125_Toh1h2_M50_M60',
         'vbfh3_M125_Toh1h2_M50_M70'
    ]
}


all_scenarios = [ggH_symmetric, vbf_symmetric, ggH_cascade, ggH_non_cascade, vbf_cascade, vbf_non_cascade]

hdfs_dir = "/hdfs/store/user/skkwan/gridpacks-UL-hdfs/"
cmsgrid_dir = "/hdfs/store/user/skkwan/gridpacks-UL-hdfs/cmsgrid_files/"
for scenario in all_scenarios:
    for name in scenario["names"]:
        unzip_command="tar -xavf {}{}_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz".format(hdfs_dir, name)
        print(">>> Executing {}".format(unzip_command))
        os.system(unzip_command)

        rungrid_command="bash ./runcmsgrid.sh 10 1 4"
        print(">>> Executing {}".format(rungrid_command))
        os.system(rungrid_command)

        getfile_command = "cp cmsgrid_final.lhe {}cmsgrid_final_{}.lhe".format(cmsgrid_dir, name)
        print(">>> Executing {}".format(getfile_command))
        os.system(getfile_command)

        
