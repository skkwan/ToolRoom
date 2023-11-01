scp 'skkwan@lxplus9.cern.ch:/afs/cern.ch/work/s/skkwan/public/hToA1A2/CMSSW_13_2_6_patch2/src/lunaFramework/postProcessing/out.root' '/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp'

rm /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/mutau/*.png
rm /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/mutau/*.pdf
rm /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/etau/*.png
rm /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/etau/*.pdf
rm /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/emu/*.png
rm /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/emu/*.pdf


root -l -b -q runCenterUpDownPlotsFromHistograms.cpp

scp -r /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/emu/* 'skkwan@lxplus9.cern.ch:/eos/user/s/skkwan/www/sysPlots/emu/'
scp -r /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/etau/* 'skkwan@lxplus9.cern.ch:/eos/user/s/skkwan/www/sysPlots/etau/'
scp -r /Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysPlots/mutau/* 'skkwan@lxplus9.cern.ch:/eos/user/s/skkwan/www/sysPlots/mutau/'

echo "Visit https://skkwan.web.cern.ch/sysPlots/"