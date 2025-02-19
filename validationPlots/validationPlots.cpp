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
 
  TString treePath = "gen_tree";

  gSystem->Exec("mkdir -p " + outputDirectory);

  TString cut_hasEle = "p4_gen_ele1.Pt() > 0";
  TString cut_hasMuon = "p4_gen_muon1.Pt() > 0";

  singleDistributionPlots("p4_gen_ele1.Pt()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 1 p_{T} / GeV", 40, 0, 120, sampleName + "_gen_ele_1_pt");
  singleDistributionPlots("p4_gen_ele2.Pt()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 2 p_{T} / GeV", 40, 0, 120, sampleName + "_gen_ele_2_pt");
  singleDistributionPlots("p4_gen_ele1.Eta()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 1 #eta", 40, -3.4, 3.4, sampleName + "_gen_ele_1_eta");
  singleDistributionPlots("p4_gen_ele2.Eta()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 2 #eta", 40, -3.4, 3.4, sampleName + "_gen_ele_2_eta");


  singleDistributionPlots("p4_gen_muon1.Pt()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 1 p_{T} / GeV", 40, 0, 120, sampleName + "_gen_muon_1_pt");
  singleDistributionPlots("p4_gen_muon2.Pt()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 2 p_{T} / GeV", 40, 0, 120, sampleName + "_gen_muon_2_pt");
  singleDistributionPlots("p4_gen_muon1.Eta()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 1 #eta", 40, -3.4, 3.4, sampleName + "_gen_muon_1_eta");
  singleDistributionPlots("p4_gen_muon2.Eta()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 2 #eta", 40, -3.4, 3.4, sampleName + "_gen_muon_2_eta");


  // singleDistributionPlots("jet_btagDeepFlavB_ak4_matched_leadingPair", cut, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "DeepFlavB score of nearest AK4 jet", 40, 0, 1);  
  // singleDistributionPlots("jetPt_ak4_matched_leadingPair", cut, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "p_{T} of nearest AK4 jet", 50, 0, 200);  
  // singleDistributionPlots("genPt_leadingPair", cut, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen p_{T} of close-by gen b's", 50, 0, 200);  

        
}
