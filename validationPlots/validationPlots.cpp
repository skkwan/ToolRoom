// Usage:
//    Example (note the parentheses): root -l -b -q 'runDistributionPlots.C("SUSYVBFHToAA_AToBB_AToTauTau_M-40", \
                                      "VBF h #rightarrow aa #rightarrow bb#tau#tau (m_{a} = 40 GeV)",\
                                      "/eos/user/s/skkwan/hToAA/genSkims/Nov-03-2020-20h40m/SUSYVBFToHToAA_AToBB_AToTauTau_M-40GenSkim.root")'
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/singleDistribution.cpp"

void validationPlots(TString sampleName, TString legend, TString inputDirectory) {
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/singleDistribution.cpp");
 
  TString treePath = "mutau_tree";
  TString outputDirectory = "/eos/user/s/skkwan/hToA1A2/genStudies/plots/";

  TString cut = "";

  // All the legs
  for (int i = 0; i < 6; i++) {
    singleDistributionPlots(TString::Format("genPt_%i", i), cut, sampleName, treePath, inputDirectory, outputDirectory, TString::Format("genPt_%i [GeV]", i), 60, 0, 120);
  }

  for (int i = 1; i <= 2; i++) {
    singleDistributionPlots(TString::Format("genPt_tau%i", i), cut, sampleName, treePath, inputDirectory, outputDirectory, TString::Format("genPt of #tau %i [GeV]", i), 60, 0, 120);  
    singleDistributionPlots(TString::Format("genPt_b%i", i), cut, sampleName, treePath, inputDirectory, outputDirectory, TString::Format("genPt of b jet %i [GeV]", i), 60, 0, 120);  

    // Trailing bottom quarks for 4b2tau events
    singleDistributionPlots(TString::Format("genPt_trailing%i", i), "(n_gen_bb_pairs == 2)", sampleName, treePath, inputDirectory, outputDirectory, TString::Format("genPt of trailing b jet %i [GeV]", i), 60, 0, 120,
                            TString::Format("genPt_trailing_bjet_%i", i));  

    // Trailing taus, for 2b4tau events
    singleDistributionPlots(TString::Format("genPt_trailing%i", i), "(n_gen_bb_pairs == 1)", sampleName, treePath, inputDirectory, outputDirectory, TString::Format("genPt of trailing #tau %i [GeV]", i), 60, 0, 120,
                            TString::Format("genPt_trailing_tau_%i", i));  
  }

  // Distribution of number of gen bb pairs
  singleDistributionPlots("n_gen_bb_pairs", cut, sampleName, treePath, inputDirectory, outputDirectory, "Number of gen bb pairs (either 1 or 2)", 3, 0, 3);

}
