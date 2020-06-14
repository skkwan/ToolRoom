# Usage: (e.g. on lxplus)
# First make sure your grid certificate is created (voms proxy init etc.)
# Edit the following variables and run with: ./getFiles.sh 

INPUT="filepaths.txt"
REDIRECTOR="root://cmsxrootd.fnal.gov/"
DESTINATION="."

while IFS= read -r FILE
do 
  echo "Executing: xrdcp ${REDIRECTOR}${FILE} ${DESTINATION}";
  eval "xrdcp ${REDIRECTOR}${FILE} ${DESTINATION}";
done < "${INPUT}"
