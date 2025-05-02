import re
import os

oldnames = [
    "weightFile_Cascade_ggH_MA2-100_MA1-15.root",
    "weightFile_Cascade_VBF_MA2-100_MA1-15.root",
    "weightFile_Cascade_ggH_MA2-100_MA1-20.root",
    "weightFile_Cascade_VBF_MA2-100_MA1-20.root",
    "weightFile_Cascade_ggH_MA2-40_MA1-15.root",
    "weightFile_Cascade_VBF_MA2-40_MA1-15.root",
    "weightFile_Cascade_ggH_MA2-40_MA1-20.root",
    "weightFile_Cascade_VBF_MA2-40_MA1-20.root",
    "weightFile_Cascade_ggH_MA2-60_MA1-15.root",
    "weightFile_Cascade_VBF_MA2-60_MA1-15.root",
    "weightFile_Cascade_ggH_MA2-60_MA1-20.root",
    "weightFile_Cascade_VBF_MA2-60_MA1-20.root",
    "weightFile_Cascade_ggH_MA2-60_MA1-30.root",
    "weightFile_Cascade_VBF_MA2-60_MA1-30.root",
    "weightFile_Cascade_ggH_MA2-80_MA1-15.root",
    "weightFile_Cascade_VBF_MA2-80_MA1-15.root",
    "weightFile_Cascade_ggH_MA2-80_MA1-20.root",
    "weightFile_Cascade_VBF_MA2-80_MA1-20.root",
    "weightFile_Cascade_ggH_MA2-80_MA1-30.root",
    "weightFile_Cascade_VBF_MA2-80_MA1-30.root",
]

for oldname in oldnames:
    x = re.findall("(weightFile_.*)_(MA2-\d+)_(MA1-\d+)", oldname)
    myArray = x[0]
    newname = f"{myArray[0]}_{myArray[2]}_{myArray[1]}.root"
    command=f'git mv {oldname} {newname}'
    print(command)
    os.system(command)
