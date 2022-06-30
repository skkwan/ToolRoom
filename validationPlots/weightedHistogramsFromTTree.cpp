// Usage: root -l -b -q weightedHistogramsFromTTree
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/comparisonPlotsWeighted.cpp"

void weightedHistogramsFromTTree()
{
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/comparisonPlotsWeighted.cpp");
 
  TString treePath = "mutau_tree";
  TString inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/preapprovalChecks/ntuples/";
  TString outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/preapprovalChecks/plots/";

  std::vector<TString> samples = {"TTTo2L2Nu", "DYJetsToLL_M-10to50", "DYJetsToLL", 
                                  "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45"};



  TString sigCut;     // selection cut on n-tuple for "signal"
  TString bkgCut;     // selection cut on n-tuple for "bkg"
  TString sigLabel;   // legend label for "signal" histogram
  TString bkgLabel;   // legend label for "bkg" histogram
  TString legTitle;   // legend title (good to include the sample name)

  float xmax_pt, xmax_mtt, xmax_pTtt;


  for (unsigned int i = 0; i < samples.size(); i++) {

    TString inputFile = inputDirectory + samples[i] + "-miniGenSkim.root";
    if (samples[i].Contains("SUSY")) inputFile = inputDirectory + samples[i] + "GenSkim.root";

    sigCut = "gen_mtt < 25";
    bkgCut = "";
    sigLabel = "m_{#tau#tau} < 25 GeV";
    bkgLabel = "No cuts on m_{#tau#tau}";

    // Special values for readability
    if (samples[i] == "TTTo2L2Nu")                { xmax_pt = 250; xmax_mtt = 200; xmax_pTtt = 300; }
    else if (samples[i] == "DYJetsToLL_M-10to50") { xmax_pt =  50; xmax_mtt =  60; xmax_pTtt = 100; }
    else                                          { xmax_pt = 250; xmax_mtt = 600; xmax_pTtt = 300;  } // default

    legTitle = samples[i] + ", one file";


    comparisonPlotsWeighted("genPt_tau1", "Gen p_{T} of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_1" + "_SHAPE", 60, 0, xmax_pt);
    comparisonPlotsWeighted("genEta_tau1", "Gen #eta of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_1" + "_SHAPE", 60, -3, 3);
    comparisonPlotsWeighted("genPhi_tau1", "Gen #phi of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_1" + "_SHAPE", 60, -4, 4);

    comparisonPlotsWeighted("genPt_tau2", "Gen p_{T} of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_2" + "_SHAPE", 60, 0, xmax_pt);
    comparisonPlotsWeighted("genEta_tau2", "Gen #eta of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_2" + "_SHAPE", 60, -3, 3);
    comparisonPlotsWeighted("genPhi_tau2", "Gen #phi of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_2" + "_SHAPE", 60, -4, 4);

    comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt" + "_SHAPE", 60, 0, xmax_mtt);
    comparisonPlotsWeighted("gen_pTtt", "Gen p_{T} of #tau#tau", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_pTtt" + "_SHAPE", 60, 0, xmax_pTtt);




    bool doDistributionStyle = false;
    bool showBackground = false;
    sigCut = "";
    bkgCut = "";
    sigLabel = "No cuts on m_{#tau#tau}";
    bkgLabel = "";

    // Special values for readability
    if (samples[i] == "TTTo2L2Nu")                { xmax_pt = 250; xmax_mtt = 600; xmax_pTtt = 300; }
    else if (samples[i] == "DYJetsToLL_M-10to50") { xmax_pt =  50; xmax_mtt =  60; xmax_pTtt = 100; }
    else if (samples[i].Contains("SUSY"))         { xmax_pt =  50; xmax_mtt =  60; xmax_pTtt = 100; }
    else if (samples[i].Contains("DYJetsToLL"))   { xmax_pt = 100; xmax_mtt = 140; xmax_pTtt = 200; }
    else                                          { xmax_pt = 250; xmax_mtt =  50; xmax_pTtt = 300;  } // default



    comparisonPlotsWeighted("genPt_tau1", "Gen p_{T} of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_1", 60, 0, xmax_pt, doDistributionStyle, showBackground);
    comparisonPlotsWeighted("genEta_tau1", "Gen #eta of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_1", 60, -3, 3, doDistributionStyle, showBackground);
    comparisonPlotsWeighted("genPhi_tau1", "Gen #phi of gen tau 1", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_1", 60, -4, 4, doDistributionStyle, showBackground);

    comparisonPlotsWeighted("genPt_tau2", "Gen p_{T} of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "pt_2", 60, 0, xmax_pt, doDistributionStyle, showBackground);
    comparisonPlotsWeighted("genEta_tau2", "Gen #eta of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "eta_2", 60, -3, 3, doDistributionStyle, showBackground);
    comparisonPlotsWeighted("genPhi_tau2", "Gen #phi of gen tau 2", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "phi_2", 60, -4, 4, doDistributionStyle, showBackground);

    comparisonPlotsWeighted("gen_mtt", "Gen m_{#tau#tau}", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_mtt", 60, 0, xmax_mtt, doDistributionStyle, showBackground);
    comparisonPlotsWeighted("gen_pTtt", "Gen p_{T} of #tau#tau", sigCut, bkgCut, sigLabel, bkgLabel, legTitle, treePath, inputFile, outputDirectory, samples[i] + "_" + "gen_pTtt", 60, 0, xmax_pTtt, doDistributionStyle, showBackground);

  }
  
}
