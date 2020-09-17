#!/bin/bash

# Start with DM 0 
root -l -b -q makeTGraphAsymmErrorsPlot.cpp

# Do DM 10
FILE="makeTGraphAsymmErrorsPlot_DM10.cpp"
cp makeTGraphAsymmErrorsPlot.cpp ${FILE}
grep -rl 'DM0' ${FILE} | xargs sed -i 's/DM0/DM10/g'
grep -rl 'dm0' ${FILE} | xargs sed -i 's/dm0/dm10/g' 
grep -rl 'ErrorsPlot(' ${FILE} | xargs sed -i 's/ErrorsPlot(/ErrorsPlot_DM10(/g'

root -l -b -q ${FILE}
rm ${FILE}

# Do DM 11
FILE="makeTGraphAsymmErrorsPlot_DM11.cpp"
cp makeTGraphAsymmErrorsPlot.cpp ${FILE}
grep -rl 'DM0' ${FILE} | xargs sed -i 's/DM0/DM11/g'
grep -rl 'dm0' ${FILE} | xargs sed -i 's/dm0/dm11/g'
grep -rl 'ErrorsPlot(' ${FILE} | xargs sed -i 's/ErrorsPlot(/ErrorsPlot_DM11(/g'

root -l -b -q ${FILE}

rm ${FILE}
