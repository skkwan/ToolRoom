# validate_gridpacks_2016_WH.sh

masspoints=(12 15 20 25 30 35 40 45 50 55 60)

# Path to folder with all the .log and tar.xz files
gridpacks_dir="gridpacks/Wh01_M125_Toa01a01_Tobbtautau/"

# Create log file
log_file_name="validate_gridpacks_2016_WH.log"
rm ${log_file_name}
touch ${log_file_name}

# Remove old .lhe file
rm ${lhe_file_name}

lhe_file_name="cmsgrid_final.lhe"
events_string="#  Number of Events        :       10"

for mp in "${masspoints[@]}"
do
    
    masspoint_str="Wh01_M125_Toa01a01_M${mp}_Tobbtautau"
    tar_suffix_str="_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
    
    # Unzip the tar 
    cmd_unzip="tar -xavf ${gridpacks_dir}${masspoint_str}${tar_suffix_str}"
    echo ">>> Executing ${cmd_unzip}" | tee -a ${log_file_name}
    eval $cmd_unzip

    # Run the validation script
    cmd_run="bash ./runcmsgrid.sh 10 12 4"
    echo ">>> Executing ${cmd_run}" | tee -a ${log_file_name}
    eval $cmd_run

    # Check if the .lhe file exists, write error message if not
    if test -f "$lhe_file_name"; then
	echo "     (Passed check): .lhe file exists" | tee -a ${log_file_name}
	
	# Check if the .lhe file reports the desired number of events, write error message if not
	if grep -q "${events_string}" "${lhe_file_name}"; then
	    echo "     (Passed check): Number of events matches expected value" | tee -a ${log_file_name}
	else
	    echo "     [ERROR] Number of events does not match expected value" | tee -a ${log_file_name}
	fi
    else
	echo "     [ERROR] could not find .lhe file" | tee -a ${log_file_name}
    fi

    
done

