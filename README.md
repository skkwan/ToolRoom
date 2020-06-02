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