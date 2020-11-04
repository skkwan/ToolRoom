// Usage: root -l -b -q runDistributionPlots.C
// Create plots of variables from a TTree

#include "../baseCodeForPlots/singleDistribution.C"

void runDistributionPlots(TString sampleName, TString legend, TString inputDirectory)
{
  // Load the macro
  //  gROOT->ProcessLine(".L ../baseCodeForPlots/comparisonPlots.C");
 
  std::cout << sampleName << " " << legend << " " << inputDirectory << std::endl;
  TString treePath = "mutau_tree";
  //  TString inputDirectory  = "/eos/user/s/skkwan/signalNanoAOD/2018/SUSYVBFToHToAA_AToBB_AToTauTau_M-40/SUSYVBFToHToAA_AToBB_AToTauTau_M-40_BATCH_1_NANO.root";
  TString outputDirectory = "/eos/user/s/skkwan/hToAA/signalGenLevelPlots/2018/" + sampleName + "/"; 
  gSystem->Exec("mkdir " + outputDirectory);

  TString cut = "";

  int nBins = 50;
  singleDistributionPlots("pt_1", cut, legend, treePath, inputDirectory, outputDirectory, "Muon p_{T}", nBins, 15, 150);
  singleDistributionPlots("eta_1", cut, legend, treePath, inputDirectory, outputDirectory, "Muon #eta", nBins, -3, 3);
  singleDistributionPlots("phi_1", cut, legend, treePath, inputDirectory, outputDirectory, "Muon #phi", nBins, -4, 4);

  singleDistributionPlots("pt_2", cut, legend, treePath, inputDirectory, outputDirectory, "#tau_{h} p_{T}", nBins, 15, 150);
  singleDistributionPlots("eta_2", cut, legend, treePath, inputDirectory, outputDirectory, "#tau_{h} #eta", nBins, -3, 3);
  singleDistributionPlots("phi_2", cut, legend, treePath, inputDirectory, outputDirectory, "#tau_{h} #phi", nBins, -4, 4);

  

  
}
