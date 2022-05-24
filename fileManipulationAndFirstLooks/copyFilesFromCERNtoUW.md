# Copying files from CERN to UW

E.g. For skimmed n-tuples that need SVFit run on them:


On the help site (https://www.hep.wisc.edu/cms/comp/faq.html#example-of-how-to-copy) it says:

```bash
gfal-copy -p -r srm://srm-eoscms.cern.ch//eos/user/s/skkwan/hToAA/condor/May-21-2022-02h23m-DataMC2018_withGen davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018
```
 
What works is logging onto lxplus and removing the `srm://srm-eoscms.cern.ch/` portion:

```bash
 gfal-copy -p -r /eos/user/s/skkwan/hToAA/condor/May-21-2022-02h23m-DataMC2018_withGen davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018
```
