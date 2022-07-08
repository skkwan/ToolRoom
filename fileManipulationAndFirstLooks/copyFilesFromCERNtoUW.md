# Copying files between CERN and UW Tier 2 storage

## From CERN to UW Tier 2

E.g. For skimmed n-tuples that need SVFit run on them:


On the help site (https://www.hep.wisc.edu/cms/comp/faq.html#example-of-how-to-copy) it says:

```bash
# voms-proxy-init
gfal-copy -p -r srm://srm-eoscms.cern.ch//eos/user/s/skkwan/hToAA/condor/May-21-2022-02h23m-DataMC2018_withGen davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018
```
 
Log onto lxplus and removing the `srm://srm-eoscms.cern.ch/` portion: make sure to also set a
maximum time or it will time out very quickly:

```bash
# voms-proxy-init
 gfal-copy -p -r -t 999999999 /eos/user/s/skkwan/hToAA/condor/May-21-2022-02h23m-DataMC2018_withGen davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018
```

## From UW Tier 2 to CERN lxplus

```bash
# voms-proxy-init
gfal-copy -p -r davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018_preapprovalChecks_svfitted .
```