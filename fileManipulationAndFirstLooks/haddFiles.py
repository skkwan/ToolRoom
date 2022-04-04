'''
Usage: python haddFiles.py --year [year] --rootdir [directory]
where [directory] is some timestamped directory.

Add --recreate (FALSE by default) to force re-creation of existing _Skim.root
Add --execute to execute all the bash commands.

Hadds files in [dir]/[sample]/*.root into [dir]/sample.root.
Hadds extensions into one file, moving the original dataset to _ext0.
'''

import argparse
import os
import sys


parser = argparse.ArgumentParser(description='Hadd files from a directory with sub-directories')
parser.add_argument('--year',    dest='year',    help='Year of dataset', required=True)
parser.add_argument('--rootdir', dest='rootdir', help='Path to directory', required=True)
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
    outputFile = args.rootdir + sampleName + "_Skim.root"
    
    targetFile = args.rootdir + sampleName + "/*.root"
    if (os.path.exists(outputFile) and not args.recreate):
        print(outputFile + " exists, do not recreate")
        continue
    command = "hadd -f " + outputFile + " " + targetFile
    if (args.execute):
        print(command)
        os.system(command)


# Args.Year-specific
datasetsWithExtensions = { "2017": [["DYJetsToLL", "DYJetsToLL-ext1"],
                                    ["DY2JetsToLL", "DY2JetsToLL-ext1"],
                                    ["DY3JetsToLL", "DY3JetsToLL-ext1"],
                                    ["WJetsToLNu", "WJetsToLNu-ext1"]] ,
                           "2018": [["TTToHadronic",     "TTToHadronic-ext2"],
                                    ["TTToSemiLeptonic", "TTToSemiLeptonic-ext3"]]
                       }

# for subdir, dirs, files in os.walk(args.rootdir): 
#     sampleName = os.path.basename(os.path.normpath(subdir))  
#    print(subdir + sampleName + "_Skim.root")

# Merge extensions; only do this if the rootdir doesn't have "Embed" in its name
if ("Embed" not in args.rootdir):
    for pair in datasetsWithExtensions[args.year]:
        originalname = args.rootdir + pair[0] + "_Skim.root"
        temp_name    = args.rootdir + pair[0] + "-ext0_Skim.root"
        extname      = args.rootdir + pair[1] + "_Skim.root"
        command = "mv " + originalname + " " + temp_name
        if (args.execute):
            print(command)
            os.system(command)
            
            command = "hadd -f " + originalname + " " + temp_name + " " + extname
            if (args.execute):
                print(command)
                os.system(command)

if (not args.execute):
    print("--execute flag was not set: did not execute any commands")
