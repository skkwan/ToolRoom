// Usage: root -l -b -q runValidationPlots.C
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/updownShiftsPlots.C"

void runCenterUpDownPlots()
{
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/updownShiftsPlots.C");
 
  TString treePath = "mutau_tree";
  TString inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/Systematics/temp/histograms_VBFHToTauTau-mini.root";
  TString outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G4/hToAA/Systematics/plots/";


  TString process = "VBFHToTauTau-mini_";

  updownShiftsPlots(process, "pt_1", "_CMS_muES_eta0to1p2_2018", inputDirectory, outputDirectory);
  

  std::vector<std::string> vSystematicsTauES_ = {"CMS_TES_dm0", "CMS_TES_dm1", "CMS_TES_dm10", "CMS_TES_dm11",
                            "CMS_eleTES_dm0", "CMS_eleTES_dm1",
                            "CMS_muTES_dm0",  "CMS_muTES_dm1"};
  for (unsigned int i = 0; i < vSystematicsTauES_.size(); i++) {
    updownShiftsPlots(process, "pt_2", "_" + vSystematicsTauES_[i] + "_2018", inputDirectory, outputDirectory);
  }

}
