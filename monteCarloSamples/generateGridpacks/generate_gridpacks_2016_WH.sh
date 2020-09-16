masspoints=(12 15 20 25 30 35 40 45 50 55 60)

finalstate_dir="cards/production/2017/13TeV/bbtautau_final_state/"
process_dir="Wh01_M125_Toa01a01_Tobbtautau/"

for mp in "${masspoints[@]}"
do
    masspoint_str="Wh01_M125_Toa01a01_M${mp}_Tobbtautau"
    
    cmd="./gridpack_generation.sh ${masspoint_str} ${finalstate_dir}${process_dir}${masspoint_str}"
    echo ">>> Executing ${cmd}"
    eval $cmd
    
done
