# runValidationPlots.py
# Usage: python runValidationPlots.py
# If this is running slowly, deactivate the venv

import argparse
import os

if __name__ == "__main__":
    samples = [ 
        "raw_DYJetsToLL_M-50-mini_GenSkim"
    ]

    for sample in samples:
        legend = sample
        path = "/eos/user/s/skkwan/zhmet/genLevelChecks"
        plot_path = "/eos/user/s/skkwan/www/higgsino/skim-test/drell-yan-check/"

        input_root_file = f"{path}/{sample}.root"

        command = "root -l -b -q 'validationPlots.cpp(\"{}\", \"{}\", \"{}\", \"{}\")'".format(sample, legend, input_root_file, plot_path) 

        print(command)
        os.system(command)