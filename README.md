# ToolRoom 

For boilerplate code.


## Draw existing TH1F in ROOT file

In `validationPlots/`, edit `runPlotTH1Fs.cpp`, and run it as a ROOT macro:

   ```
   root -l -b -q runPlotTH1Fs.cpp
   ```


## Make histogram from existing n-tuple

In `makeHistogramsFromNtuples/`, edit `makeHistsFromNtuples.cc`, and compile it:

   ```
   ./Make.sh makeHistsFromNtuples.cc
   ```

and run the executable:

   ```
   makeHistsFromNtuples.exe input.root output.root
   ```


## Make efficiency plots

In `efficiencyPlots/`, edit `makeEfficienciesPlot.cpp`, and run it as a ROOT macro:

   ```
   root -l -b -q makeEfficiencyPlots.cpp
   ```

## Make rates plots

   To be added.

## MC Sample generation
   Augments the GenProductions GitHub.
   ### Datacard creation
   See my GenProductions Github.

   ### Gridpack generation and validation 
   Currently I run them from the directory `genproductions/bin/MadGraph5_aMCatNLO`. Scripts for looping over mass points to generate and validate gridpacks are in `monteCarloSamples` (they won't run out of the box, but I'm saving them for reference.)

## Synchronization: compare two n-tuples
   Code is copied from [2015 Higgs to Tau Tau GitHub](https://github.com/CMS-HTT/2015-sync/blob/master/compare.py). See documentation inside `compare.py` for how to call it (CMSSW release not necessary).