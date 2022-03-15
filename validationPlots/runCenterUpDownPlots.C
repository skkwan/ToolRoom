// Usage: root -l -b -q runValidationPlots.C
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/updownShiftsPlots.C"


/*********************************************************************/

/*
 *  Helper function which churns out plots given a vector of systematics and a vector of variables.
 *  "process" is the name of the physics process (all histograms should start with the process name).
 *  "year" is used as a suffix for the output .png and .pdf.
 */

void makeShiftedPlots(TString process, std::vector<std::string> vSystematics, std::vector<std::string> vVariables, std::string year,
                      TString inputDirectory, TString outputDirectory) {

  for (unsigned int i = 0; i < vSystematics.size(); i++) {
    for (unsigned int j = 0; j < vVariables.size(); j++ ) {
      updownShiftsPlots(process, vVariables[j], "_" + vSystematics[i] + "_" + year, inputDirectory, outputDirectory);
    }   
  }

}

/*********************************************************************/

/*
 *  Main function. Generates comparison plots of the nominal/ up/ down histograms for a specific file.
 */

void runCenterUpDownPlots()
{
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/updownShiftsPlots.C");
 
  TString treePath = "mutau_tree";
  TString inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/Systematics/temp/histograms_VBFHToTauTau-mini.root";
  TString outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/Systematics/plots/";


  TString process = "VBFHToTauTau-mini_";

  // Muon Energy Scale
  std::vector<std::string> vSystematicsMES_ = {"CMS_muES_eta0to1p2", "CMS_muES_eta1p2to2p1", "CMS_muES_eta2p1to2p4"};
  std::vector<std::string> vVariablesMES_   = {"pt_1", "mtMET_1"};
  makeShiftedPlots(process, vSystematicsMES_, vVariablesMES_, "2018", inputDirectory, outputDirectory);


  // Tau Energy Scale
  std::vector<std::string> vSystematicsTauES_ = {"CMS_TES_dm0", "CMS_TES_dm1", "CMS_TES_dm10", "CMS_TES_dm11",
                                                 "CMS_eleTES_dm0", "CMS_eleTES_dm1",
                                                 "CMS_muTES_dm0",  "CMS_muTES_dm1"};
  std::vector<std::string> vVariablesTauES_   = {"pt_2", "mtMET_2"};
  makeShiftedPlots(process, vSystematicsTauES_, vVariablesTauES_, "2018", inputDirectory, outputDirectory);

}


/*********************************************************************/
