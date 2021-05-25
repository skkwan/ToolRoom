'''
Simple script to go into a directory and search .out files for a successfulString (defined below) and report which
datasets' jobs succeeded and which didn't.
'''

import os
import sys

rootdir = str(sys.argv[1])
print("Directory to search: " + rootdir)

# The string indicated that the job completed
successfulString = 'Valid muon in selected pair'

successReports=[]
failedReports=[]

for subdir, dirs, files in os.walk(rootdir):
    for filename in files:
        # print(os.path.join(subdir, filename))
        relPath    = os.path.join(subdir, filename)
        sampleName = os.path.basename(os.path.normpath(subdir))
        # Search all files ending with .out
        if (filename.endswith('.out')):
            # print(relPath)
            with open(relPath) as myfile:
                if successfulString in myfile.read():
                    successReports.append(sampleName + ': Job completed normally')
                else:
                    failedReports.append("[WARNING:] " + sampleName + ': Job did not complete normally!' + '(' + filename + ')')
        
# Print the reports, doing the failed jobs last
for reports in [successReports, failedReports]:
    for r in reports:
        print(r)

print("Report of " + rootdir + " complete, using " + successfulString + " as the searched substring")
