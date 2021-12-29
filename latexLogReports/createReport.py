# createReport.py

import argparse
import os
import re
import shutil

parser = argparse.ArgumentParser(description='Create a cutflow report.')

parser.add_argument("--build",
                    help="Build the resulting .tex",
                    dest='execute', action = 'store_true')
parser.add_argument("--rootdir",
                    help="Path to the log files", required=True)
parser.set_defaults(execute=True)

args = parser.parse_args()


def escape_latex(value):
    '''
    Helper function to escape special characters in LaTeX.
    '''
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

def main():

    descriptor=os.path.basename(args.rootdir)
    sectionsWithSummaries = ''
    samplesThatDidNotFinish = ''
    samplesWithWarnings = ''

    # Loop through log files in the directory
    for subdir, dirs, files in os.walk(args.rootdir):
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
                    if 'SUCCESS' not in skimCutFlow:
                        sectionsWithSummaries += '[ERROR:] Run did not finish!'
                        samplesThatDidNotFinish += escape_latex(sample) + ', '
                    if 'WARNING' in skimCutFlow:
                        samplesWithWarnings     += escape_latex(sample) + ', '
                    sectionsWithSummaries += skimCutFlow 
                    sectionsWithSummaries += '\n'
                    
    print(sectionsWithSummaries)

    # Replace the dummy section in the template
    template = open("templateCutflowReport.tex", "rt")
    report   = open("report.tex",         "wt")
                    
    for line in template:
        # Modify the title
        dummy = 'Directory'
        if dummy in line: 
            report.write(line.replace(dummy, escape_latex(descriptor)))
            continue

        # Print the samples that did not finish                                                  
        dummy = 'samples that did not finish'
        if dummy in line:
            report.write(line.replace(dummy, samplesThatDidNotFinish))
            continue

        # Print the samples that had warnings
        dummy = 'samples that threw warnings'
        if dummy in line:
            report.write(line.replace(dummy, samplesWithWarnings))
            continue

        # Print the log files
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
    command = 'mv report.pdf %s' % (args.rootdir)
    os.system(command)

if __name__ == "__main__":
    main()
