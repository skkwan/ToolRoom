'''
Usage: python haddHistograms.py --dir [directory]
where [directory] is some timestamped directory.

Add --recreate (FALSE by default) to force re-creation of existing hists_{sample}.root
Add --execute to execute all the bash commands.

Hadds files in [dir]/[sample]/*.root into [dir]/sample.root.
'''

import argparse
import os
import sys


parser = argparse.ArgumentParser(description='Hadd files from a directory with sub-directories')
#parser.add_argument('--year',    dest='year',    help='Year of dataset', required=True)
parser.add_argument('--dir', dest='rootdir', help='Path to directory', required=True)
parser.add_argument('--recreate',  dest='recreate',  action='store_true')
parser.add_argument('--execute', dest='execute', action='store_true')
parser.set_defaults(recreate=False)
parser.set_defaults(execute=False)

args = parser.parse_args()

if not args.rootdir.endswith("/"):
    args.rootdir += "/"

print("Directory to use: " + args.rootdir)

for subdir, dirs, files in os.walk(args.rootdir):
    sampleName = os.path.basename(os.path.normpath(subdir))
    outputFile = args.rootdir + "hists_" + sampleName + ".root"
    
    targetFile = args.rootdir + sampleName + "/*.root"
    if (os.path.exists(outputFile) and not args.recreate):
        print(outputFile + " exists, do not recreate")
        continue
    command = "hadd -f " + outputFile + " " + targetFile
    if (args.execute):
        print(command)
        os.system(command)


# for subdir, dirs, files in os.walk(args.rootdir): 
#     sampleName = os.path.basename(os.path.normpath(subdir))  
#    print(subdir + sampleName + "_Skim.root")

if (not args.execute):
    print("--execute flag was not set: did not execute any commands")
