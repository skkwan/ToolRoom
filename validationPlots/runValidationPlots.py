# runValidationPlots.py
# Usage: python runValidationPlots.py
# If this is running slowly, deactivate the venv

import argparse
import os

if __name__ == "__main__":
    samples = [ 
        'Cascade_ggH_MA2-80_MA1-30',
        'Cascade_VBF_MA2-100_MA1-20',
        'Cascade_VBF_MA2-100_MA1-15',
        'Cascade_VBF_MA2-80_MA1-15',
        'Cascade_VBF_MA2-40_MA1-15',
        'Cascade_VBF_MA2-40_MA1-20',
        'Cascade_VBF_MA2-60_MA1-15',
        'Cascade_ggH_MA2-60_MA1-15',
        'Cascade_VBF_MA2-80_MA1-20',
        'Cascade_VBF_MA2-60_MA1-30',
        'Cascade_ggH_MA2-60_MA1-20',
        'Cascade_VBF_MA2-80_MA1-30',
        'Cascade_ggH_MA2-100_MA1-15',
        'Cascade_ggH_MA2-60_MA1-30',
        'Cascade_ggH_MA2-40_MA1-20',
        'Cascade_ggH_MA2-100_MA1-20',
        'Cascade_ggH_MA2-40_MA1-15',
        'Cascade_VBF_MA2-60_MA1-20',
        'Cascade_ggH_MA2-80_MA1-15',
        'Cascade_ggH_MA2-80_MA1-20'
    ]

    for sample in samples:
        legend = sample
        path = "/eos/user/s/skkwan/hToAA/condorSkim/2023-10-02-17h53m"
        plot_path = "{}/plots/{}/".format(path, sample)

        input_root_file = "{}/{}/{}_0.root".format(path, sample, sample)

        command = "root -l -b -q 'validationPlots.cpp(\"{}\", \"{}\", \"{}\", \"{}\")'".format(sample, legend, input_root_file, plot_path) 

        print(command)
        os.system(command)