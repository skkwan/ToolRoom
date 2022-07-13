// Usage: root -l -b -q weightedHistogramsFromTTree
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/comparisonPlotsWeighted.cpp"

void weightedHistogramsFromTTree()
{
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/comparisonPlotsWeighted.cpp");
 
  TString treePath = "mutau_tree";
  // TString inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/preapprovalChecks/reco-ntuples/";
  // TString outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/preapprovalChecks/reco-plots/";

  //TString inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/preapprovalChecks/final-ntuples/Jul-12-2022-15h55m-Preapproval_check/";
  TString inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/preapprovalChecks/final-ntuples/Jul-13-2022-14h36m-Data_all/";
  TString outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/preapprovalChecks/final-plots/";

 // std::vector<TString> samples = {"TTTo2L2Nu", "DYJetsToLL_M-10to50", "DYJetsToLL", 
 //                                 "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45"};
  //std::vector<TString> samples = {"DYJetsToLL_M-10to50", "TTTo2L2Nu"};
  std::vector<TString> samples = {"SingleMuon-Run2018ABCD"};


  TString sigCut;     // selection cut on n-tuple for "signal"
  TString bkgCut;     // selection cut on n-tuple for "bkg"
  TString sigLabel;   // legend label for "signal" histogram
  TString bkgLabel;   // legend label for "bkg" histogram
  TString legTitle;   // legend title (good to include the sample name)

  TString weight = "";     // weight branch to use

  float xmax_pt, xmax_mtt, xmax_pTtt;

  float xsec, nEvents;

  float nOriginalEvents = 1.0;  // number of events in the m_{tautau} histogram with no cuts applied

  TString inputFile;

  for (unsigned int i = 0; i < samples.size(); i++) {

    // inputFile = inputDirectory + samples[i] + "_Skim.root";
    inputFile =  inputDirectory + "ntup_" + samples[i] + ".root";
    
    if (samples[i].Contains("SUSY")) inputFile = inputDirectory + samples[i] + "GenSkim.root";

    sigCut = "gen_mtt < 20";
    bkgCut = "";
    sigLabel = "m_{#tau#tau} < 20 GeV";
    bkgLabel = "No cuts on m_{#tau#tau}";

    // Special values for readability
    if (samples[i] == "TTTo2L2Nu")                { xmax_pt = 250; xmax_mtt = 200; xmax_pTtt = 300; }
    else if (samples[i] == "DYJetsToLL_M-10to50") { xmax_pt =  50; xmax_mtt =  60; xmax_pTtt = 100; }
    else                                          { xmax_pt = 250; xmax_mtt = 600; xmax_pTtt = 300;  } // default

    legTitle = samples[i] + ", full sample";


    // comparisonPlotsWeighted("genPt_tau1", "Gen p_{T} of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_tau1" + "_SHAPE", 60, 0, xmax_pt);
    // comparisonPlotsWeighted("genEta_tau1", "Gen #eta of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_tau1" + "_SHAPE", 60, -3, 3);
    // comparisonPlotsWeighted("genPhi_tau1", "Gen #phi of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_tau1" + "_SHAPE", 60, -4, 4);

    // comparisonPlotsWeighted("genPt_tau2", "Gen p_{T} of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_tau2" + "_SHAPE", 60, 0, xmax_pt);
    // comparisonPlotsWeighted("genEta_tau2", "Gen #eta of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_tau2" + "_SHAPE", 60, -3, 3);
    // comparisonPlotsWeighted("genPhi_tau2", "Gen #phi of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_tau2" + "_SHAPE", 60, -4, 4);

    // comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt" + "_SHAPE", 60, 0, xmax_mtt);
    // comparisonPlotsWeighted("gen_pTtt", "Gen p_{T} of #tau#tau", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_pTtt" + "_SHAPE", 60, 0, xmax_pTtt);




    bool doDistributionStyle = false;
    bool showBackground = false;
    sigCut = "";
    bkgCut = "";
    //sigLabel = "Reco #mu#tau pair, Embedded overlap removal, gen tautau pair";
    bkgLabel = "";

    // Special values for readability; dataset-specific cross-sections, number of events in NanoAOD
    if (samples[i] == "TTTo2L2Nu")                { xmax_pt = 250; xmax_mtt = 600; xmax_pTtt = 300; xsec = 88.29;    nEvents = 64310000.0;}
    else if (samples[i] == "DYJetsToLL_M-10to50") { xmax_pt =  50; xmax_mtt =  60; xmax_pTtt = 100; xsec = 15810.0;  nEvents = 39392062.0;}
    else if (samples[i].Contains("SUSY"))         { xmax_pt =  50; xmax_mtt =  60; xmax_pTtt = 100; xsec = 48.6;     nEvents = 199429.0; } // not quite right: only for ggH
    else if (samples[i].Contains("DYJetsToLL"))   { xmax_pt = 100; xmax_mtt = 140; xmax_pTtt = 200; xsec = 5343.0;   nEvents = 100194597.0; }
    else                                          { xmax_pt = 250; xmax_mtt =  50; xmax_pTtt = 300; xsec = 48.6;     nEvents = 199429.0;} // default


    // // Get n events with no cuts
    // // No cuts
    // treePath = "mutau_tree_HasGenTauTau";
    // // sigLabel = "No cuts on m_{#tau#tau}";
    // sigLabel = "Gen m_{#tau#tau}";
    // nOriginalEvents = 1.0;
    // nOriginalEvents = comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt_" + treePath, 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);


    // treePath = "mutau_tree";
    // comparisonPlotsWeighted("genPt_tau1", "Gen p_{T} of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_tau1", 60, 0, xmax_pt, nOriginalEvents, doDistributionStyle, showBackground);
    // comparisonPlotsWeighted("genEta_tau1", "Gen #eta of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_tau1", 60, -3, 3, nOriginalEvents, doDistributionStyle, showBackground);
    // comparisonPlotsWeighted("genPhi_tau1", "Gen #phi of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_tau1", 60, -4, 4, nOriginalEvents, doDistributionStyle, showBackground);

    // comparisonPlotsWeighted("genPt_tau2", "Gen p_{T} of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_tau2", 60, 0, xmax_pt, nOriginalEvents, doDistributionStyle, showBackground);
    // comparisonPlotsWeighted("genEta_tau2", "Gen #eta of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_tau2", 60, -3, 3, nOriginalEvents, doDistributionStyle, showBackground);
    // comparisonPlotsWeighted("genPhi_tau2", "Gen #phi of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_tau2", 60, -4, 4, nOriginalEvents, doDistributionStyle, showBackground);

    // comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt", 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);
    // comparisonPlotsWeighted("gen_pTtt", "Gen p_{T} of #tau#tau", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_pTtt", 60, 0, xmax_pTtt, nOriginalEvents, doDistributionStyle, showBackground);


    //*****************************************//
    // gen_mtt at each stage of the cutflow
    //*****************************************//

    // // Get n events with no cuts
    // // No cuts
    // treePath = "mutau_tree_HasGenTauTau";
    // sigLabel = "No cuts on m_{#tau#tau}";
    // nOriginalEvents = comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt_" + treePath, 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);


    // // Minimal reco mutau selection
    // treePath = "mutau_tree_MinimalRecoMuTauSelection";
    // sigLabel = "Has any reco #mu and #tau_{h}";
    // comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt_" + treePath, 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);

    // // Has good taus good muons (baseline analysis selection)
    // treePath = "mutau_tree_HasGoodTausGoodMuons";
    // sigLabel = "Reco #mu, #tau_{h} pass baseline selection";
    // comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt_" + treePath, 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);

    // // Has leading reco mutauh pair
    // treePath = "mutau_tree_HasMuTauPair";
    // sigLabel = "Has leading reco #mu#tau_{h} pair";
    // comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt_" + treePath, 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);

    // // Has leading b-tag jet
    // treePath = "mutau_tree_HasLeadingBTagJet";
    // sigLabel = "Has leading b-tag jet";
    // comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt_" + treePath, 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);

    // // Try adding embedded overlap removal
    // treePath = "mutau_tree";
    // sigLabel = "Remove overlap with Embed";
    // sigCut = "((gen_match_1 == 2) && (gen_match_2 != 6)) || ((gen_match_1 == 4) && (gen_match_2 < 3))";
    // comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt_withEmbedOverlapRemoval", 60, 0, xmax_mtt, nOriginalEvents, doDistributionStyle, showBackground);

    //*****************************************//
    // Plot m_sv with various requirements    //
    //*****************************************//
    // Hard code original # of events with two gen level particles

    if (samples[i] == "TTTo2L2Nu")                { nOriginalEvents = 7141448;  }
    else if (samples[i] == "DYJetsToLL_M-10to50") { nOriginalEvents = 13089253; }

    float xmax_m_sv = 800;

    // // m_sv with no cuts
   //  treePath = "mutau_tree";
   //  sigLabel = "Signal region";
   //  sigCut = "";
   //  bkgCut = "";
   //  // weight="weight_passIso";
   //  //weight = "weight_initial";
   //  if (samples[i] == "DYJetsToLL_M-10to50") { weight = "weight_initial * weight_DYJets"; }
   //  // comparisonPlotsWeighted("m_sv", "SVFit m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory,
   //  //			    samples[i] + "_" + "m_sv", 60, 0, xmax_m_sv, nOriginalEvents, weight, doDistributionStyle, showBackground);


   //  // m_sv with <= 20 GeV cut
   //  sigLabel = "Signal region, gen m_{#tau#tau} #leq 20 GeV";
   //  sigCut = "(gen_mtt <= 20)";
   //  bkgCut = "";
   //  weight = "weight_initial";
   // if (samples[i] == "DYJetsToLL_M-10to50") { weight = "weight_initial * weight_DYJets"; }
   //  comparisonPlotsWeighted("m_sv", "SVFit m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory,
   // 			    samples[i] + "_" + "m_sv_with_gen_mtt_leq_20", 60, 0, xmax_m_sv, nOriginalEvents, weight, doDistributionStyle, showBackground);
    

    sigCut = "";
    bkgCut = "";
    weight = "";
    sigLabel = "m_sv";
    comparisonPlotsWeighted("m_sv", "SVFit m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory,
			    samples[i], 60, 0, xmax_m_sv, nOriginalEvents, weight, doDistributionStyle, showBackground);

    sigCut = "m_sv <= 50";
    sigLabel = "m_sv <= 50";
    comparisonPlotsWeighted("m_sv", "SVFit m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory,
			    samples[i] + "_" + "m_sv_leq_50", 60, 0, xmax_m_sv, nOriginalEvents, weight, doDistributionStyle, showBackground);

    
  }
  
}
