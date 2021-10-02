# lookForErrorFiles.py

import os
import re

rootdir='.'

proofstring='Valid tau in selected pair' 

# Loop through log files in the directory
for subdir, dirs, files in os.walk(rootdir):
    sample = os.path.basename(subdir)   
    print(">>> " + sample)
    
    for filename in files:
        path = os.path.join(subdir, filename)

        # In .out files, check for the proofstring
        if ('.out' in path):
            with open(path) as f:
                
                if proofstring not in f.read():
                    print("    " + filename + ': proofstring not found')
                    num = re.findall("\d+(?=\.\w+$)", filename)
                    
                    # Make sure we unequivocably know the batch number
                    if (len(num) > 1):
                        sys.exit("Could not find batch number in " + filename)
                    batchnum = num[0]
                    print("    " + batchnum)

                    # Want to submit one Condor job for each failed job
                    # Need condorSkim.sh but have nInstances = 1,
                    # INPUT_LIST says the batchnum instead of \$(Process)
                    
                    # Add flag arguments to condorSubmit.sh
                    # https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script

                    # https://linuxize.com/post/bash-check-if-file-exists/
                    # If there is a rescue_[sample].csv file, loop through it
                    # and create a new sub file etc.
                    
