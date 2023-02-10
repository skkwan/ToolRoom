# mergeLocalPdfFiles.sh

# Source: https://www.baeldung.com/linux/merge-pdf-files

# -q: quiet mode
# -dBATCH: instructs to exit after processing all files
# -dNOPAUSE: disables prompting after processing each file
# -sDEVICE: selects the output device for saving to a pdf file
# -sOutputFile: pass the name for the final output file

export dir="/Users/stephaniekwan/Dropbox/Princeton_G5/Phase2EGamma/debugIsolation/minbias1000events/"
gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=${dir}merged_newIsoFlagTrue.pdf ${dir}newIsoFlagTrue/*.pdf
gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=${dir}merged_newIsoFlagFalse.pdf ${dir}newIsoFlagFalse/*.pdf
