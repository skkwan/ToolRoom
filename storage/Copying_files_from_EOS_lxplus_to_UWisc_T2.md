# Copying files from EOS lxplus to UWisconsin T2

Based on [UWisc T2 instructions](https://www.hep.wisc.edu/cms/comp/faq.html#example-of-how-to-copy):

1. Log onto `lxplus`, run this:

`gfal-copy -p -r /eos/user/s/skkwan/hToAA/condor/Apr-04-2022-18h26m-DataMC2018_JERsys_withTES/ davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/hToAA/skims/2018/` 

2. This will write files to the UWisc T2 hdfs storage area (note in step 1 we omitted the `/hdfs/` part)

`/hdfs/store/user/skkwan/hToAA/skims/2018`

