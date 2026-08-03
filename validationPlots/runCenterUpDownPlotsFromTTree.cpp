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
      updownShiftsPlotsFromBranches(process, vVariables[j], + "_" + vSystematics[i], treename, inputDirectory, outputDirectory, year);
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

  std::vector<std::string> vProcesses = {"DYJetsToLL_MLL-50-mini"};

  std::string year = "2022";

  for (unsigned int i = 0; i < vProcesses.size(); i++) {
  
    std::string process = vProcesses[i];

    TString treePath = "event_tree";

    TString inputDirectory = "/afs/cern.ch/work/s/skkwan/public/zhmet/CMSSW_14_0_21/src/luna-zhmet/skim/DYJetsToLL_MLL-50-mini.root";
    TString outputDirectory = "/eos/user/s/skkwan/www/higgsino/sys-Checks/" + year + "/";

    gSystem->Exec("mkdir -p " + outputDirectory);

    // Muon energy scale
    std::vector<std::string> vSystematicsMES_ = {"CMS_scale_m", "CMS_res_m"};
    
    std::vector<std::string> vVariablesMES_   = {"pt_1", "pt_2"};
    makeShiftedPlotsFromBranches(process, vSystematicsMES_, vVariablesMES_, year, treePath, inputDirectory, outputDirectory);

    // JER and JES
    std::vector<std::string> vSystematicsJER_ = {"CMS_scale_j", "CMS_res_j"};
    std::vector<std::string> vVariablesJER_   = {"bpt_ak4_1", "bpt_ak4_2", "met", "metphi"};
    makeShiftedPlotsFromBranches(process, vSystematicsJER_, vVariablesJER_, year, treePath, inputDirectory, outputDirectory);
  }

}


/*********************************************************************/
