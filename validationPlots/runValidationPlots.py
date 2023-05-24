# runValidationPlots.py
# Usage: python runValidationPlots.py
# If this is running slowly, deactivate the venv

import argparse
import os

if __name__ == "__main__":
    output_file_name = "Cascade_VBFH125ToA1A2To3A1_A1ToBBorTauTau_MA2-100_MA1-15"
    legend = "Cascade VBF a_{3} #rightarrow a_{1} a_{2} #rightarrow 3a_{1} (m_{a2} = 100 GeV), m_{a1} = 15 GeV)"
    path = "/afs/cern.ch/work/s/skkwan/public/hToA1A2/CMSSW_13_1_0_pre4/src/lunaFramework/syncNanoAOD/"
    input_root_file = "Cascade_VBFH125ToA1A2To3A1_A1ToBBorTauTau_MA2-100_MA1-15GenSkim.root"

    command = "root -l -b -q 'validationPlots.cpp(\"{}\", \"{}\", \"{}\")'".format(output_file_name, legend, path + input_root_file) 

    print(command)
    os.system(command)