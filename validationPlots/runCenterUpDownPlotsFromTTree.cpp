// Usage: root -l -b -q runValidationPlotsFromTTree.C
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/updownShiftsPlotsFromBranches.cpp"


/*********************************************************************/

/*
 *  Helper function which churns out plots given a vector of systematics and a vector of variables.
 *  "process" is the name of the physics process (all histograms should start with the process name).
 *  "year" is used as a suffix for the output .png and .pdf.
 */

void makeShiftedPlotsFromBranches(TString process, std::vector<std::string> vSystematics, std::vector<std::string> vVariables, std::string year,
                      TString treename, TString inputDirectory, TString outputDirectory) {

  for (unsigned int i = 0; i < vSystematics.size(); i++) {
    for (unsigned int j = 0; j < vVariables.size(); j++ ) {
      updownShiftsPlotsFromBranches(process, vVariables[j], + "_" + vSystematics[i], treename, inputDirectory, outputDirectory);
    }   
  }

}

/*********************************************************************/

/*
 *  Main function. Generates comparison plots of the nominal/ up/ down histograms for a specific file.
 *  Assumes that the inputFile name is histograms_{PROCESSNAME}.root.
 */

void runCenterUpDownPlotsFromTTree()
{
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/updownShiftsPlotsFromBranches.cpp");
 
  // std::vector<std::string> vProcesses = {"DYJetsToLL_M-50", "DYJetsToLL_M-10to50", 
  //                                        "DY1JetsToLL", "DY2JetsToLL", "DY3JetsToLL", "DY4JetsToLL",
  //                                        "TTTo2L2Nu", "TTToHadronic", "TTToSemiLeptonic", 
  //                                        "ST_t-channel_top", "ST_t-channel_antitop", 
  //                                        "ST_tW_top", "ST_tW_antitop", 
  //                                        "VVTo2L2Nu", "WZTo3LNu", "WZTo2L2Q", "ZZTo2L2Q", "ZZTo4L",
  //                                        "WJetsToLNu", "W1JetsToLNu", "W2JetsToLNu", "W3JetsToLNu", "W4JetsToLNu",
  //                                        "GluGluHToTauTau", "GluGluHToWWTo2L2Nu", "GluGluZH_HToWW",
  //                                        "HWminusJ_HToWW", "HWplusJ_HToWW", "HZJ_HToWW",
  //                                        "VBFHToTauTau", "VBFHToWWTo2L2Nu",
  //                                        "WminusHToTauTau", "WplusHToTauTau",
  //                                        "ZHToTauTau",
  //                                        "ggZH_HToTauTau_ZToLL", "ggZH_HToTauTau_ZToNuNu", "ggZH_HToTauTau_ZToQQ",
  //                                        "ttHToNonbb", "ttHTobb", 
  //                                        "SUSYVBFToHToAA_AToBB_AToTauTau_M-45", "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45"};


  //   std::vector<std::string> vProcesses = {"VBFHToTauTau"}; // , "GluGluHToTauTau"};
  std::vector<std::string> vProcesses = {"TTTo2L2Nu"};

  for (unsigned int i = 0; i < vProcesses.size(); i++) {
  
    std::string process = vProcesses[i];

    TString treePath = "mutau_tree";
    // TString inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/Systematics/04_25_22_test_mvis_with_current_sys/histograms_" + process + ".root";
    // TString outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/Systematics/plots/04_25_22_test_mvis_with_current_sys/" + process + "/";

    TString inputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/SVFit/mt_2018_TTTo2L2Nu-TTTo2L2Nu_0.root";
    TString outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/Systematics/plots/05_10_22_svfit_test/" + process + "/";

    gSystem->Exec("mkdir -p " + outputDirectory);

    // Muon Energy Scale
    std::vector<std::string> vSystematicsMES_ = {"CMS_muES_eta0to1p2", "CMS_muES_eta1p2to2p1", "CMS_muES_eta2p1to2p4"};
    
    std::vector<std::string> vVariablesMES_   = {"m_vis", "met"};
      // {"pt_1", "mtMET_1", "m_vis"};
    makeShiftedPlotsFromBranches(process, vSystematicsMES_, vVariablesMES_, "2018", treePath, inputDirectory, outputDirectory);


    // Tau Energy Scale
    // std::vector<std::string> vSystematicsTauES_ = {"CMS_TES_dm0", "CMS_TES_dm1", "CMS_TES_dm10", "CMS_TES_dm11",
    //                                               "CMS_eleTES_dm0", "CMS_eleTES_dm1",
    //                                               "CMS_muTES_dm0",  "CMS_muTES_dm1"};
    // std::vector<std::string> vVariablesTauES_   = {"pt_2", "eta_2", "met", "metphi", "mtMET_2", "m_vis"};
    // makeShiftedPlotsFromBranches(process, vSystematicsTauES_, vVariablesTauES_, "2018", treePath inputDirectory, outputDirectory);

    // JER
    // std::vector<std::string> vSystematicsJER_ = {"CMS_JER", "CMS_JetAbsolute", "CMS_JetBBEC1", "CMS_JetEC2", "CMS_JetFlavorQCD", "CMS_JetHF", 
    //     "CMS_JetRelativeBal",
    //     "CMS_JetAbsoluteyear", "CMS_JetBBEC1year", "CMS_JetEC2year", "CMS_JetHFyear", "CMS_JetRelativeSample"};

    std::vector<std::string> vSystematicsJER_ = {"JER", "JetAbsolute", "JetBBEC1", "JetEC2", "JetFlavorQCD", "JetHF", 
        "JetRelativeBal",
        "JetAbsoluteyear", "JetBBEC1year", "JetEC2year", "JetHFyear", "JetRelativeSample"};
    // std::vector<std::string> vVariablesJER_   = {"bpt_deepflavour_1", "beta_deepflavour_1", "met", "metphi",
    //                                            "bpt_deepflavour_2", "beta_deepflavour_2"};
    std::vector<std::string> vVariablesJER_   = {"m_sv"};
    makeShiftedPlotsFromBranches(process, vSystematicsJER_, vVariablesJER_, "2018", treePath, inputDirectory, outputDirectory);
  }

}


/*********************************************************************/
