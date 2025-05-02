import os
import re


oldnames = [

"info_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90.root"

]

for oldname in oldnames:
    x = re.findall("(Cascade_.*)_(MA1-\d+)_(MA2-\d+).root", oldname)
    myArray = x[0]
    newname = f"{myArray[0]}_{myArray[2]}_{myArray[1]}.root"
    # command=f"git mv {oldname} {newname}"