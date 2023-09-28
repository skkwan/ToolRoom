# runValidationPlots.py
# Usage: python runValidationPlots.py
# If this is running slowly, deactivate the venv

import argparse
import os

if __name__ == "__main__":
    samples = [ 
        "Cascade_VBF_MA2-40_MA1-15"
    ]

    for sample in samples:
        legend = sample
        path = "/eos/user/s/skkwan/hToAA/condorSkim/2023-09-28-15h50m"
        input_root_file = "{}/{}/{}_0.root".format(path, sample, sample)

        command = "root -l -b -q 'validationPlots.cpp(\"{}\", \"{}\", \"{}\")'".format(sample, legend, input_root_file) 

        print(command)
        os.system(command)