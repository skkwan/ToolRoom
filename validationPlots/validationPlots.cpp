// Usage:
//    Example (note the parentheses): root -l -b -q 'runDistributionPlots.C("SUSYVBFHToAA_AToBB_AToTauTau_M-40", \
                                      "VBF h #rightarrow aa #rightarrow bb#tau#tau (m_{a} = 40 GeV)",\
                                      "/eos/user/s/skkwan/hToAA/genSkims/Nov-03-2020-20h40m/SUSYVBFToHToAA_AToBB_AToTauTau_M-40GenSkim.root")'
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/singleDistribution.cpp"

void validationPlots(TString sampleName, TString legend, TString inputDirectory) {
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/singleDistribution.cpp");
 
  TString treePath = "event_tree";
  TString outputDirectory = inputDirectory + "/plots/" + sampleName + "/";

  gSystem->Exec("mkdir -p " + outputDirectory);

  TString cut = "";

  for (int i = 0; i < 4; i++) {
    singleDistributionPlots(TString::Format("genPt_b%i", i), cut, sampleName, treePath, inputDirectory, outputDirectory, TString::Format("genPt of b jet %i [GeV]", i), 60, 0, 120);
  }

  for (int i = 0; i < 2; i++) {
    singleDistributionPlots(TString::Format("genPt_tau%i", i), cut, sampleName, treePath, inputDirectory, outputDirectory, TString::Format("genPt of tau %i [GeV]", i), 60, 0, 120);  
  }

}
