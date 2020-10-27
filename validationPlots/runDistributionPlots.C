// Usage: root -l -b -q runDistributionPlots.C
// Create plots of variables from a TTree

#include "../baseCodeForPlots/singleDistribution.C"

void runDistributionPlots(TString sampleName, TString legend, TString inputDirectory)
{
  // Load the macro
  //  gROOT->ProcessLine(".L ../baseCodeForPlots/comparisonPlots.C");
 
  std::cout << sampleName << " " << legend << " " << inputDirectory << std::endl;
  TString treePath = "Events";
  //  TString inputDirectory  = "/eos/user/s/skkwan/signalNanoAOD/2018/SUSYVBFToHToAA_AToBB_AToTauTau_M-40/SUSYVBFToHToAA_AToBB_AToTauTau_M-40_BATCH_1_NANO.root";
  TString outputDirectory = "/eos/user/s/skkwan/hToAA/signalGenLevelPlots/2018/" + sampleName + "/"; 
  gSystem->Exec("mkdir " + outputDirectory);

  TString cut = "";

  int nBins = 50;
  singleDistributionPlots("Muon_pt", cut, legend, treePath, inputDirectory, outputDirectory, "Muon p_{T}", nBins, 15, 150);
  singleDistributionPlots("Muon_eta", cut, legend, treePath, inputDirectory, outputDirectory, "Muon #eta", nBins, -3, 3);
  singleDistributionPlots("Muon_phi", cut, legend, treePath, inputDirectory, outputDirectory, "Muon #phi", nBins, -4, 4);

  singleDistributionPlots("Tau_pt", cut, legend, treePath, inputDirectory, outputDirectory, "Tau p_{T}", nBins, 15, 150);
  singleDistributionPlots("Tau_eta", cut, legend, treePath, inputDirectory, outputDirectory, "Tau #eta", nBins, -3, 3);
  singleDistributionPlots("Tau_phi", cut, legend, treePath, inputDirectory, outputDirectory, "Tau #phi", nBins, -4, 4);

  

  
}
