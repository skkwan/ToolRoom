// Usage:
//    Example (note the parentheses): root -l -b -q 'runDistributionPlots.C("SUSYVBFHToAA_AToBB_AToTauTau_M-40", \
                                      "VBF h #rightarrow aa #rightarrow bb#tau#tau (m_{a} = 40 GeV)",\
                                      "/eos/user/s/skkwan/hToAA/genSkims/Nov-03-2020-20h40m/SUSYVBFToHToAA_AToBB_AToTauTau_M-40GenSkim.root")'
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/overlayDistributions.cpp"
#include "../baseCodeForPlots/singleDistribution.cpp"

void validationPlots(TString sampleName, TString legend, TString inputDirectory, TString outputDirectory) {
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/singleDistribution.cpp");
 
  TString treePath = "event_tree";

  gSystem->Exec("mkdir -p " + outputDirectory);

  TString cut = "";

  singleDistributionPlots("deltaR_ak4_leadingPair", cut, sampleName, treePath, inputDirectory, outputDirectory, "#DeltaR(close-by gen b's, nearest AK4 jet)", 40, 0, 1);
  singleDistributionPlots("pt_resolution_ak4_leadingPair", cut, sampleName, treePath, inputDirectory, outputDirectory, "pT resolution of close-by gen b's and nearest AK4 jet", 40, -2, 3);  
  singleDistributionPlots("jet_btagDeepFlavB_ak4_matched_leadingPair", cut, sampleName, treePath, inputDirectory, outputDirectory, "DeepFlavB score of nearest AK4 jet", 40, 0, 1);  
  singleDistributionPlots("jetPt_ak4_matched_leadingPair", cut, sampleName, treePath, inputDirectory, outputDirectory, "p_{T} of nearest AK4 jet", 50, 0, 200);  
  singleDistributionPlots("genPt_leadingPair", cut, sampleName, treePath, inputDirectory, outputDirectory, "Gen p_{T} of close-by gen b's", 50, 0, 200);  


  singleDistributionPlots("closest_idx2", cut, sampleName, treePath, inputDirectory, outputDirectory, "Index of third b, if within #DeltaR < 0.4", 5, -1, 3);
  singleDistributionPlots("closest_idx3", cut, sampleName, treePath, inputDirectory, outputDirectory, "Index of fourth nearby b, if within #DeltaR < 0.4", 5, -1, 3);


  // overlayDistributions("genPt_b0", "genPt_b1", "genPt_b2", "genPt_b3",
  //                      "leading", "sub-leading", "sub-sub-leading", "sub-sub-sub-leading", 
  //                      cut, treePath, inputDirectory, outputDirectory,
  //                      "genPt of b jet [GeV]",
  //                      60, 0, 150,
  //                      sampleName,
  //                      sampleName + "_overlay");
        
}
