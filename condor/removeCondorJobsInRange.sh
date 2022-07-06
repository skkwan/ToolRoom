# removeCondorJobsInRange.sh

# condor_rm more intelligently, since
# https://htcondor.readthedocs.io/en/latest/man-pages/condor_rm.html doesn't give many examples

# For instance if we see this in condor_q

# -- Schedd: bigbird08.cern.ch : <188.185.72.155:9618?... @ 07/06/22 11:23:34
# OWNER  BATCH_NAME      SUBMITTED   DONE   RUN    IDLE   HOLD  TOTAL JOB_IDS
# skkwan ID: 12426768   7/5  17:36     18      _      _      9     27 12426768.3-26

# and we want to remove ALL of them,

condor_rm -constraint 'ClusterId == 12426768 && ProcId <= 26'


# The ClassAd attribute arguments are detailed here:
# https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html

