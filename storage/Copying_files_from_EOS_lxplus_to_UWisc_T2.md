# Copying files from EOS lxplus to UWisconsin T2

Based on [UWisc T2 instructions](https://www.hep.wisc.edu/cms/comp/faq.html#example-of-how-to-copy):

1. On UWisc `hdfs` make the directory to copy stuff to

```
# On UWisc
mkdir /hdfs/store/user/skkwan/hToAA/skims/2018/Apr-04-2022-18h26m-DataMC2018_JERsys_withTES
```

2. Log onto `lxplus`, run the gfal-copy command. See [documentation](https://www.systutorials.com/docs/linux/man/1-gfal-copy/)

```
# On lxplus
gfal-copy -p -r --timeout 999999 /eos/user/s/skkwan/hToAA/condor/Apr-04-2022-18h26m-DataMC2018_JERsys_withTES/ davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/hToAA/skims/2018/Apr-04-2022-18h26m-DataMC2018_JERsys_withTES/
```

For some reason `gfal-copy` doesn't like wildcards.