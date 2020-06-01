// Usage: root -l -b -q runSingleVariablePlots.C

// Draw nicely formatted histograms for a single variable
#include "../baseCodeForPlots/singleVariablePlots.C"

void runSingleVariablePlots()
{
 
  TString treePath = "mutau_slimmed";
  TString inputDirectory  = "/afs/hep.wisc.edu/user/skkwan/public/exoticHiggs/May2020/CMSSW_9_4_0/src/AABBTT/hists.root";
  TString outputDirectory = "myPlots/";

  TString myCut = "";

  singleVariablePlots("muPt", myCut, treePath, inputDirectory, outputDirectory, "muPt", 60, 0, 100);
  /*
  singleVariablePlots("muEta", myCut, treePath, inputDirectory, outputDirectory, "muEta", 30, -2.7, 2.7);
  singleVariablePlots("tauPt", myCut, treePath, inputDirectory, outputDirectory, "tauPt", 60, 0, 140);
  singleVariablePlots("tauEta", myCut, treePath, inputDirectory, outputDirectory, "tauEta", 30, -2.7, 2.7);
  */
}
