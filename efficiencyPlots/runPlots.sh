
# We need this to set the C++14 compiler (other methods of setting the C compiler to C++14
# instead of C++11 should work), otherwise the auto return type in helpers/boostedTau.h won't work

source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_94python3 x86_64-centos7-gcc8-opt

# See makeEfficienciesPlot.cpp to set the output directory
root -l -b -q 'makeEfficienciesPlot.cpp'
