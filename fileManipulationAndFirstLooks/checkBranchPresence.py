# checkRunNumbers.py
# Check if the listed files contain any runs with run number < 317509.


import os
import subprocess

files = [
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_1.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_10.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_11.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_12.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_13.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_14.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_15.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_16.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_17.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_18.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_19.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_2.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_20.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_21.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_22.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_23.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_24.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_25.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_26.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_27.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_28.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_29.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_3.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_30.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_31.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_32.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_33.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_34.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_35.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_36.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_37.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_38.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_39.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_4.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_40.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_41.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_42.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_43.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_44.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_45.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_46.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_47.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_48.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_49.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_5.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_50.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_51.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_6.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_7.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_8.root',
	'/store/user/skkwan/NanoPost/SingleMuon/NanoPost_SingleMuon-Run2018B_UL2018_MiniAODv2_NanoAODv9/230828_104608/0000/tree_9.root',
    ]

# files = [
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_1.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_10.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_11.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_12.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_13.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_14.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_15.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_16.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_17.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_18.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_19.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_2.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_20.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_21.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_22.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_23.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_24.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_25.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_26.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_27.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_28.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_29.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_3.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_30.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_31.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_32.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_33.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_34.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_35.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_36.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_37.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_38.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_39.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_4.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_40.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_41.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_42.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_43.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_44.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_45.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_46.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_47.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_48.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_49.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_5.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_50.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_51.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_52.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_53.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_54.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_55.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_56.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_57.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_58.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_59.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_6.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_60.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_61.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_62.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_63.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_64.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_65.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_66.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_67.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_68.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_69.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_7.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_70.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_71.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_72.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_73.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_74.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_8.root',
# '/store/user/skkwan/NanoPost/EGamma/NanoPost_EGamma-Run2018A_UL2018_MiniAODv2_NanoAODv9/230828_105438/0000/tree_9.root'
# ]



fHPS = []
fNone = []

for file in files:
    cmdOpen="root -b -q 'macroGetBranches.cpp(\"root://cmsxrootd.fnal.gov/{}\")' | tee temp.txt".format(file)
    print(cmdOpen)
    os.system(cmdOpen)
    cmdFindHPS='grep "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1" temp.txt'
    cmdFindNon='grep "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1" temp.txt'
    statusHPS, outputHPS = subprocess.getstatusoutput(cmdFindHPS)
    statusNon, outputNon = subprocess.getstatusoutput(cmdFindNon)


    if ((outputHPS != "") and (outputNon == "")):
        print("Couldn't find non-HPS, has HPS")
        with open("hasHPSOnly.txt", "a+") as f:
            f.write("root://cmsxrootd.hep.wisc.edu/{}\n".format(file))
    elif ((outputHPS != "") and (outputNon != "")):
        print("Found HPS and non-HPS!")
        with open("hasBoth.txt", "a+") as f:
            f.write("root://cmsxrootd.hep.wisc.edu/{}\n".format(file))