# Usage:
# In genproductions/bin/MadGraph5_aMCatNLO, make the cards, first, and then use this Python to make the gridpacks in a loop.
# e.g. this file would be located in, and run in, /afs/cern.ch/work/s/skkwan/public/gridpacks_hToAA/genproductions/bin/MadGraph5_aMCatNLO
# python makeGridPacks.py
#
# This makes a bunch of tar files


import os



# /afs/cern.ch/work/s/skkwan/public/gridpacks_hToAA/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/bbtautau_final_state/ggh01_M125_Toa01a01_Tobbtautau/ggh01_M125_Toa01a01_M11_Tobbtautau



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


for scenario in all_scenarios:
    for name in scenario["names"]:

        command="./gridpack_generation.sh {} {}{}".format(name, scenario["path"], name)
        print(command)