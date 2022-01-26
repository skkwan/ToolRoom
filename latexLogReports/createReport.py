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
                    help="Path to the postprocess log files (typically in intermediateTuples)", required=True)
parser.add_argument("--plotdir",
                    help="Path to the plot log files (typically in stackPlots)", required=False, 
                    default="")
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

def getFileContent(f):
    '''
    Helper function to return the contents of file f as a string, with LaTeX 
    special characters escaped.
    '''
    with open(f) as myfile:
        content = myfile.readlines() 
        content = '\n'.join(content)      # collapse the list back into one string             
        content = escape_latex(content)
    return content

def main():
    '''
    Compile postprocess.cxx log files (all files titled logRun_*) in a directory
    and write them to a LaTeX file. Also make note of datasets that do not say 'SUCCESS' in the logRun.

    Builds the LaTeX file and writes the PDF to the intermediateTuples/ directory with the logRun_*.

    If the yields directory is specified, also write yields to an output LaTeX file, builds it, aand
    writes the PDF to the stackPlots/ directory.
    '''
    descriptor=os.path.basename(args.rootdir)
    sectionsWithSummaries = ''
    postprocessSummaries = ''
    samplesThatDidNotFinish = ''
    samplesWithWarnings = ''

    #########################################################    
    # Loop through log files in the postprocess.cxx directory
    #########################################################    
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
                    cutFlow = logfile.readlines()[5:]    # use readlines to get a list
                    skimCutFlow = []

                    # Ignore any line in the log file thta contains one of these strings:
                    # (alternate solution: in future log files, put "%%" in front of 
                    #  std::cout print statements)
                    ignore = ["1 b-tag jet:", "2 b-tag jet:", "%%"]

                    # Loop over the lines in the logfile
                    for i in range(len(cutFlow)):
                        if any(x in cutFlow[i] for x in ignore):
                            continue
                        # print("line", i, ":", cutFlow[i])
                        skimCutFlow.append(cutFlow[i])
                    skimCutFlow = '\n'.join(skimCutFlow)      # collapse the list back into one string
                    skimCutFlow = escape_latex(skimCutFlow)
                    
                    # Build the section in LaTeX
                    header = '\section{%s}' % escape_latex(sample)
                    # print(header)
                    
                    sectionsWithSummaries += header + '\n'
                    if 'SUCCESS' not in skimCutFlow:
                        sectionsWithSummaries += '[ERROR:] Run did not finish! Printing cutflow anyway... \n'
                        sectionsWithSummaries += skimCutFlow
                        samplesThatDidNotFinish += escape_latex(sample) + ', '
                    elif ('WARNING' in skimCutFlow) or ('ERROR' in skimCutFlow):
                        samplesWithWarnings     += escape_latex(sample) + ', '
                        sectionsWithSummaries += skimCutFlow 
                        sectionsWithSummaries += '\n'
                    else:
                        sectionsWithSummaries += skimCutFlow 
                        sectionsWithSummaries += '\n'
    # end of loop over postprocess.cxx logRun_* files

    ######################################################### 
    # Print yields if args.plotdir was specified
    #########################################################   
    yieldReport = ''
    varsToPrint = ['pt_1', 'pt_2', 'm_vis']
    if (args.plotdir != ""):
        for subdir, dirs, files in os.walk(args.plotdir):
            for f in files:
                
                for var in varsToPrint:
                    if (('%s_yields' % var) == f):
                        logname = os.path.basename(f)
                        print(">>> " + logname)
                        # Get the contents of the file                              
                        content = getFileContent(os.path.join(subdir, f))
                        header = '\section{%s}' % escape_latex(logname)
                        # print(header)
                        # print(content)
                        # print(f)
                        yieldReport += header
                        yieldReport += content
    
    # [!!!] Add the yield report to the top of the cutflow report
    sectionsWithSummaries = (yieldReport + sectionsWithSummaries)
    # print(sectionsWithSummaries)
    
    ##########################################################
    # Open the template and replace placeholders with reports
    ##########################################################
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
    
    ##########################################################
    # Build the report and copy it to the relevant places
    ##########################################################
    # Build the PDF
    command = 'pdflatex report.tex' 
    os.system(command)
    
    # If args.plotdir was specified, copy the report there
    if (args.plotdir != ""):
        command = 'cp report.pdf %s' % (args.plotdir)
        os.system(command)
        print('Report.pdf copied to %s' % (args.plotdir))

    # Copy the report to the postprocess.cxx dir
    command = 'mv report.pdf %s' % (args.rootdir)
    os.system(command)
    print('Report.pdf copied to %s' % (args.rootdir))

if __name__ == "__main__":
    main()
