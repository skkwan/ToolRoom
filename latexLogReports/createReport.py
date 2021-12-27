# createReport.py

import argparse
import os
import re
import shutil

parser = argparse.ArgumentParser(description='Create a cutflow report.')

parser.add_argument("--build",
                    help="Build the resulting .tex",
                    dest='execute', action = 'store_true')
parser.set_defaults(execute=True)

args = parser.parse_args()

rootdir='/eos/user/s/skkwan/hToAA/dataMC/intermediateTuples/2018/Nov-17-2021-02h02m-intermediate-DataMC2018_JEC_JER'

# Escape latex
def escape_latex(value):
    return value.replace(
        '&', '\&').replace(
        '%', '\%').replace(
        '_', '\_').replace(
        '$', '\$').replace(
        '#', '\#').replace(
        '{', '\{').replace(
        '}', '\}').replace(
        '>>>', '').replace(
        # '\\', '\\textbackslash ').replace(
        '~', '\\textasciitilde ').replace(
        '^', '\\textasciicircum ') 


# Replace function
sectionsWithSummaries = ''

# Loop through log files in the directory
for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        
        # Only check logRun_ files
        if 'logRun' in f:
            logname = os.path.basename(f)   
            # Get the sample name using regex
            p = re.compile('logRun_(.*)')
            sample = p.search(logname).group(1)
            print(">>> " + sample)

            # Get the contents of the file
            with open(os.path.join(subdir, f)) as logfile:
                # print(logfile.read())
                # Skip the first five lines (RooFit header)
                skimCutFlow = logfile.readlines()[5:]    # use readlines to get a list
                skimCutFlow = '\n'.join(skimCutFlow)      # collapse the list back into one string
                skimCutFlow = escape_latex(skimCutFlow)

                # Build the section in LaTeX
                header = '\section{%s}' % escape_latex(sample)
                # print(header)


                sectionsWithSummaries += header + '\n'
                sectionsWithSummaries += skimCutFlow 
                sectionsWithSummaries += '\n'
                
print(sectionsWithSummaries)

# Replace the dummy section in the template
template = open("templateCutflowReport.tex", "rt")
report   = open("report.tex",         "wt")

for line in template:
    dummySection = '\section{Example}'
    if dummySection in line:
        report.write(line.replace(dummySection, sectionsWithSummaries))
    else:
        report.write(line)

template.close()
report.close()

# Build the report
command = 'pdflatex report.tex'
os.system(command)
