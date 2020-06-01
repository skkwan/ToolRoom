// Usage: root -l -b -q runValidationPlots.C
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/comparisonPlots.C"

void runValidationPlots()
{
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/comparisonPlots.C");
 
  TString treePath = "l1NtupleProducer/Stage2/efficiencyTree";
  TString inputDirectory  = "/scratch/skkwan/Run2Ntuplizer/2020-Apr-27_Run2_ggHtautau.root";
  TString outputDirectory = "test_";

  TString sigCut = "recoTauPt>10 && genTauPt>10 && genTauDM>9 && l1TauPt>0";
  TString bkgCut = "genTauPt<5";

  comparisonPlots("l1TauPt", sigCut, bkgCut, treePath, inputDirectory, outputDirectory, "l1TauPt", 60, 0, 120);
  comparisonPlots("l1TauEta", sigCut, bkgCut, treePath, inputDirectory, outputDirectory, "l1TauEta", 60, -3, 3);
  comparisonPlots("l1TauPhi", sigCut, bkgCut, treePath, inputDirectory, outputDirectory, "l1TauPhi", 60, -4, 4);

}
