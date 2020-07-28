masspoints=(12 15 20 25 30 35 40 45 50 55 60)

finalstate_dir="cards/production/2017/13TeV/bbtautau_final_state/"


###############
# Non-cascade #
###############
process_dir_noncascade="Wh3_M125_Toh1h2/non_cascade/"
masspoints_non_cascade="cards/production/2017/13TeV/bbtautau_final_state/non_cascade_masspoints.txt"

while IFS=", " read H1MASS H2MASS;
do
    masspoint_str="Wh3_M125_Toh1h2_M${H1MASS}_M${H2MASS}"
    cmd="./gridpack_generation.sh ${masspoint_str} ${finalstate_dir}${process_dir_noncascade}${masspoint_str}"
    echo ">>> Executing ${cmd}"
    eval $cmd
done < "$masspoints_non_cascade"


###########
# Cascade #
###########
process_dir_cascade="Wh3_M125_Toh1h2/cascade/"
masspoints_cascade="cards/production/2017/13TeV/bbtautau_final_state/cascade_masspoints.txt"

while IFS=", " read H1MASS H2MASS;
do
    masspoint_str="Wh3_M125_Toh1h2_M${H1MASS}_M${H2MASS}_h2_Toh1h1"
    cmd="./gridpack_generation.sh ${masspoint_str} ${finalstate_dir}${process_dir_cascade}${masspoint_str}"
    echo ">>> Executing ${cmd}"
    eval $cmd
done < "$masspoints_cascade"
