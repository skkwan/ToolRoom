'''
Usage: python haddFiles.py [directory]
where [directory] is some timestamped directory (include the trailing slash)

Hadds files in [dir]/[sample]/*.root into [dir]/sample.root.
'''

import os
import sys

rootdir = str(sys.argv[1])
if not rootdir.endswith("/"):
    rootdir += "/"

print("Directory to use: " + rootdir)

outBaseDir = "/eos/user/s/skkwan/hToAA/skims/"
print("Output base directory: " + outBaseDir)

for subdir, dirs, files in os.walk(rootdir):
    # The files to hadd
    sampleName = os.path.basename(os.path.normpath(subdir))
    targetFile = rootdir + sampleName + "/*.root"

    # Output directory and file name
    newDir = outBaseDir + rootdir 
    outputFile = newDir + sampleName + "Skim.root"

    # Construct the command-line commands
    command =  "mkdir -p " + newDir + "; "
    command += "hadd -f " + outputFile + " " + targetFile

    # os.walk also returns the current directory; avoid that
    if ( sampleName in rootdir ):
        continue

    # print(command)
    os.system(command)


