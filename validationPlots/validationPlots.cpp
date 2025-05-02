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

  TString cut_hasEle = "(p4_gen_ele1.Pt() > 0) && (p4_gen_ele2.Pt() > 0)";
  TString cut_hasRecoEle = "(p4_reco_ele_matched_1.Pt() > 0) && (p4_reco_ele_matched_2.Pt() > 0)";

  TString cut_hasMuon = "(p4_gen_muon1.Pt() > 0) && (p4_gen_muon2.Pt() > 0)";
  TString cut_hasRecoMuon = "(p4_reco_mu_matched_1.Pt() > 0) && (p4_reco_mu_matched_2.Pt() > 0)";

  singleDistributionPlots("p4_gen_ele1.Pt()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 1, gen p_{T} / GeV", 40, 0, 120, sampleName + "_gen_ele_1_pt");
  singleDistributionPlots("p4_gen_ele2.Pt()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 2, gen p_{T} / GeV", 40, 0, 120, sampleName + "_gen_ele_2_pt");
  singleDistributionPlots("p4_gen_ele1.Eta()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 1, gen eta", 40, -4, 4, sampleName + "_gen_ele_1_eta");
  singleDistributionPlots("p4_gen_ele2.Eta()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 2, gen eta", 40, -4, 4, sampleName + "_gen_ele_2_eta");
  singleDistributionPlots("p4_gen_ele1.Phi()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 1, gen phi", 40, -4, 4, sampleName + "_gen_ele_1_phi");
  singleDistributionPlots("p4_gen_ele2.Phi()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen electron 2, gen phi", 40, -4, 4, sampleName + "_gen_ele_2_phi");


  singleDistributionPlots("p4_gen_muon1.Pt()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 1, gen p_{T} / GeV", 40, 0, 120, sampleName + "_gen_muon_1_pt");
  singleDistributionPlots("p4_gen_muon2.Pt()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 2, gen p_{T} / GeV", 40, 0, 120, sampleName + "_gen_muon_2_pt");
  singleDistributionPlots("p4_gen_muon1.Eta()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 1, gen eta", 40, -4, 4, sampleName + "_gen_muon_1_eta");
  singleDistributionPlots("p4_gen_muon2.Eta()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 2, gen eta", 40, -4, 4, sampleName + "_gen_muon_2_eta");
  singleDistributionPlots("p4_gen_muon1.Phi()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 1, gen phi", 40, -4, 4, sampleName + "_gen_muon_1_phi");
  singleDistributionPlots("p4_gen_muon2.Phi()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen muon 2, gen phi", 40, -4, 4, sampleName + "_gen_muon_2_phi");

  singleDistributionPlots("p4_gen_ee.M()", cut_hasEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen m_{ee} (vector sum) / GeV", 40, 0, 140, sampleName + "_m_ee");
  singleDistributionPlots("p4_gen_mumu.M()", cut_hasMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen m_{#mu#mu} (vector sum) / GeV", 40, 0, 140, sampleName + "_m_mumu");

  singleDistributionPlots("p4_reco_ele_matched_1.Pt()", cut_hasRecoEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco electron 1, p_{T} / GeV", 40, 0, 120, sampleName + "_reco_ele_1_pt");
  singleDistributionPlots("p4_reco_ele_matched_2.Pt()", cut_hasRecoEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco electron 2, p_{T} / GeV", 40, 0, 120, sampleName + "_reco_ele_2_pt");
  singleDistributionPlots("p4_reco_ele_matched_1.Eta()", cut_hasRecoEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco electron 1, reco eta", 40, -4, 4, sampleName + "_reco_ele_1_eta");
  singleDistributionPlots("p4_reco_ele_matched_2.Eta()", cut_hasRecoEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco electron 2, reco eta", 40, -4, 4, sampleName + "_reco_ele_2_eta");
  singleDistributionPlots("p4_reco_ele_matched_1.Phi()", cut_hasRecoEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco electron 1, reco phi", 40, -4, 4, sampleName + "_reco_ele_1_phi");
  singleDistributionPlots("p4_reco_ele_matched_2.Phi()", cut_hasRecoEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco electron 2, reco phi", 40, -4, 4, sampleName + "_reco_ele_2_phi");

  singleDistributionPlots("p4_reco_mu_matched_1.Pt()", cut_hasRecoMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco muon 1, p_{T} / GeV", 40, 0, 120, sampleName + "_reco_muon_1_pt");
  singleDistributionPlots("p4_reco_mu_matched_2.Pt()", cut_hasRecoMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco muon 2, p_{T} / GeV", 40, 0, 120, sampleName + "_reco_muon_2_pt");
  singleDistributionPlots("p4_reco_mu_matched_1.Eta()", cut_hasRecoMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco muon 1, reco eta", 40, -4, 4, sampleName + "_reco_muon_1_eta");
  singleDistributionPlots("p4_reco_mu_matched_2.Eta()", cut_hasRecoMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco muon 2, reco eta", 40, -4, 4, sampleName + "_reco_muon_2_eta");
  singleDistributionPlots("p4_reco_mu_matched_1.Phi()", cut_hasRecoMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco muon 1, reco phi", 40, -4, 4, sampleName + "_reco_muon_1_phi");
  singleDistributionPlots("p4_reco_mu_matched_2.Phi()", cut_hasRecoMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco muon 2, reco phi", 40, -4, 4, sampleName + "_reco_muon_2_phi");

  singleDistributionPlots("p4_reco_ee.M()", cut_hasRecoEle, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco m_{ee} (vector sum) / GeV", 40, 0, 140, sampleName + "_m_ee_reco");
  singleDistributionPlots("p4_reco_mumu.M()", cut_hasRecoMuon, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Reco m_{#mu#mu} (vector sum) / GeV", 40, 0, 140, sampleName + "_m_mumu_reco");

  // singleDistributionPlots("jet_btagDeepFlavB_ak4_matched_leadingPair", cut, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "DeepFlavB score of nearest AK4 jet", 40, 0, 1);  
  // singleDistributionPlots("jetPt_ak4_matched_leadingPair", cut, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "p_{T} of nearest AK4 jet", 50, 0, 200);  
  // singleDistributionPlots("genPt_leadingPair", cut, sampleName, sampleName, treePath, inputDirectory, outputDirectory, "Gen p_{T} of close-by gen b's", 50, 0, 200);  

        
}
