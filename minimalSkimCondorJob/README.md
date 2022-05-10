# Minimal skim Condor job

For testing Condor jobs. Usage:

```
voms-proxy-init --voms cms --valid 194:00
condor_submit job.sub
```

Will generate `.out` and `.log` and `.err` files in the same directory.