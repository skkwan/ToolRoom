// Usage:
//     # first edit inputFile to point to the file with the histograms (e.g. [path to EOS]/out_mutau.root)
//     root -l -b -q runCenterUpDownPlotsFromHistograms.cpp
// Create plots of variables from a TTree, overlaying histograms from two cuts

#include "../baseCodeForPlots/updownShiftsPlots.cpp"


/*********************************************************************/

/*
 *  Helper function which churns out plots given a vector of systematics and a vector of variables.
 *  "process" is the name of the physics process (all histograms should start with the process name).
 *  "year" is used as a suffix for the output .png and .pdf.
 */

void makeShiftedPlots(TString process, TString category, std::vector<std::string> systematics, std::vector<std::string> channelsAffected, std::vector<std::string> variables, std::string year,
                      TString inputFile, TString outputDirectory, TString optional = "") {

  for (std::string sys : systematics) {
    for (std::string var : variables) {
      for (std::string channel : channelsAffected) {
        updownShiftsPlots(process, var, category, "_" + sys + "_" + year, inputFile, outputDirectory, optional);
      }
    }   
  }
}

/*********************************************************************/

// Returns whether a substring is in a string.
bool containsSubstring(std::string string, std::string substring) {
    return (string.find(substring) != std::string::npos);
}

/*********************************************************************/

// Is MC not Higgs sample
bool isMCnonHiggs(std::string sample) {
  return !(containsSubstring(sample, "GluGluHToTauTau"))
          && !(containsSubstring(sample, "GluGluHToWW"))
          && !(containsSubstring(sample, "VBFHToTauTau"))
          && !(containsSubstring(sample, "VBFHToWW"))
          && !(containsSubstring(sample, "ZHToTauTau"))
          && !(containsSubstring(sample, "GluGluZH_HToWW"))
          && !(containsSubstring(sample, "HWplusJ_HToWW"))
          && !(containsSubstring(sample, "HWminusJ_HToWW"))
          && !(containsSubstring(sample, "WminusHToTauTau"))
          && !(containsSubstring(sample, "WplusHToTauTau"))
          && !(containsSubstring(sample, "ttHToNonbb"))
          && !(containsSubstring(sample, "ttHTobb"))
          && !(containsSubstring(sample, "HZJ_HToWW"));
}

bool isDY(std::string sample) {
    return containsSubstring(sample, "DY");
}

bool isWJets(std::string sample) {
    return (containsSubstring(sample, "W") && containsSubstring(sample, "JetsToLNu"));
}

bool isHiggsRecoil(std::string sample) {
  return (containsSubstring(sample, "GluGluH")
       || containsSubstring(sample, "VBFH")
       || containsSubstring(sample, "SUSY"));
}

bool doRecoil(std::string sample) {
    return (isDY(sample) ||  isWJets(sample) || isHiggsRecoil(sample));

}
/*********************************************************************/

/*
 *  Main function. Generates comparison plots of the nominal/ up/ down histograms for a specific file.
 */

void runCenterUpDownPlotsFromHistograms()
{
  // Load the macro
  gROOT->ProcessLine(".L ../baseCodeForPlots/updownShiftsPlots.cpp");
 
  std::vector<std::string> vProcesses = {"ZJ", "ttbar", "ST", "VV", "WJ", "fake",
                                         "ggh_htt", "ggh_hww", "qqh_htt", "qqh_hww", "Zh_htt", "Zh_hww", "Wh_htt", "Wh_hww",
                                         "tth", "embedded", "ggh2b2t-40-30", "vbf2b2t-40-30"};

  for (unsigned int i = 0; i < vProcesses.size(); i++) {
  
    std::string process = vProcesses[i];

    // Make sure all of these agree!
    TString channelToDo = "mutau";
    TString inputFile  = "/eos/cms/store/group/phys_susy/AN-24-166/skkwan/condorHistogramming/2024-11-20-23h57m-benchmark-2018-mutau-iteration1-m_vis/out_mutau.root";
    TString outputDirectory = "/eos/user/s/skkwan/www/sysPlots-combineChecks/" + channelToDo;

    // run mkdir and copy the index.php file needed to correctly display the folders and plots in website view
    gSystem->Exec("mkdir -p " + outputDirectory);
    gSystem->Exec("cp /eos/user/s/skkwan/www/index.php " + outputDirectory);

    std::vector<TString> categories = {"inclusive"}; // lowMassSR", "mediumMassSR", "highMassSR", "highMassCR"}; 
    std::vector<std::string> defaultVars = {"m_vis", "met"};


    for (TString category : categories) {

      // run mkdir and copy the index.php file needed to correctly display the plots in website view
      TString outputDirectoryWithCategory = outputDirectory + "/" + category;
      gSystem->Exec("mkdir -p " + outputDirectoryWithCategory);
      gSystem->Exec("cp " + outputDirectory + "/index.php " + outputDirectoryWithCategory);

      // Common to embed and MC    
      // makeShiftedPlots(process, category, {"CMS_crosstrg_fakefactor"}, {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory, "_antiIso");

      // makeShiftedPlots(process, category, {"CMS_trgeff_Mu8E23_em", "CMS_trgeff_Mu23E12_em", "CMS_trgeff_both_em"},
      //                           {"emu"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);

      // makeShiftedPlots(process, category, {"CMS_tauidWP_et"},  {"etau"},          {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);
      // // note m_vis_ss here
      // makeShiftedPlots(process, category, {"CMS_SScorrection", "CMS_SSclosure", "sCMS_SSboth2D", "CMS_osss"}, {"emu"}, {"m_vis_ss"}, "2018", inputFile, outputDirectoryWithCategory);


      // EMB-specific differences
      if (containsSubstring(process, "Embedded")) {
        // makeShiftedPlots(process, category, {"CMS_EMB_muES_eta0to1p2", "CMS_EMB_muES_eta1p2to2p1", "CMS_EMB_muES_eta2p1to2p4"}, {"mutau", "emu"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);
        // makeShiftedPlots(process, category, {"CMS_EMB_tauES_dm0", "CMS_EMB_tauES_dm1", "CMS_EMB_tauES_dm10", "CMS_EMB_tauES_dm11"}, {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);
        // makeShiftedPlots(process, category, {"CMS_EMB_trgeff_single", "CMS_EMB_trgeff_cross"}, {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory); 
        // makeShiftedPlots(process, category, {"CMS_EMB_tauideff_pt20to25", "CMS_EMB_tauideff_pt25to30", "CMS_EMB_tauideff_pt30to35", "CMS_EMB_tauideff_pt35to40", "CMS_EMB_tauideff_pt40to500", "CMS_EMB_tauideff_pt500to1000", "CMS_EMB_tauideff_ptgt1000"},
        //                         {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);  
        // makeShiftedPlots(process, category, {"CMS_EMB_tautrack_dm0dm10", "CMS_EMB_tautrack_dm1", "CMS_EMB_tautrack_dm11"}, {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);  
      }
      else {
        // MC
        // makeShiftedPlots(process, category, {"CMS_muES_eta0to1p2", "CMS_muES_eta1p2to2p1", "CMS_muES_eta2p1to2p4"}, {"mutau", "emu"}, defaultVars, "2018", inputFile, outputDirectoryWithCategory);
        // // makeShiftedPlots(process, category, {"CMS_tauES_dm0", "CMS_tauES_dm1", "CMS_tauES_dm10", "CMS_tauES_dm11"}, {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);
        // makeShiftedPlots(process, category, {"CMS_eleES_bar", "CMS_eleES_end"}, {"etau", "emu"},  defaultVars, "2018", inputFile, outputDirectoryWithCategory);
        // makeShiftedPlots(process, category, {"CMS_JER", "CMS_JetAbsolute", "CMS_JetBBEC1", "CMS_JetEC2", "CMS_JetFlavorQCD", "CMS_JetHF", "CMS_JetRelativeBal", \
        //                         "CMS_JetAbsoluteyear", "CMS_JetBBEC1year", "CMS_JetEC2year", "CMS_JetHFyear", "CMS_JetRelativeSample"}, \
        //                        {"mutau", "etau", "emu"}, defaultVars, "2018", inputFile, outputDirectoryWithCategory);

        // makeShiftedPlots(process, category, {"CMS_trgeff_single", "CMS_trgeff_cross"}, {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory); 
        // makeShiftedPlots(process, category, {"CMS_tauideff_pt20to25", "CMS_tauideff_pt25to30", "CMS_tauideff_pt30to35", "CMS_tauideff_pt35to40", "CMS_tauideff_pt40to500", "CMS_tauideff_pt500to1000", "CMS_tauideff_ptgt1000"}, \
                                {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);        
        // makeShiftedPlots(process, category, {"CMS_tauideff_VSe_bar", "CMS_tauideff_VSe_end"},
        //                         {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);      
        // makeShiftedPlots(process, category, {"CMS_tauideff_VSmu_eta0to0p4", "CMS_tauideff_VSmu_eta0p4to0p8", "CMS_tauideff_VSmu_eta0p8to1p2", "CMS_tauideff_VSmu_eta1p2to1p7", "CMS_tauideff_VSmu_eta1p7to2p3"},
        //                           {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);  
        makeShiftedPlots(process, category, {"CMS_btagsf_hf", "CMS_btagsf_lf", "CMS_btagsf_hfstats1", "CMS_btagsf_hfstats2", "CMS_btagsf_lfstats1", "CMS_btagsf_lfstats2", "CMS_btagsf_cferr1", "CMS_btagsf_cferr2"},
                                {"mutau", "etau", "emu"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory); 
        // // use optional argument to indicate antiIso
        // makeShiftedPlots(process, category, {"CMS_jetFR_pt0to25", "CMS_jetFR_pt25to30", "CMS_jetFR_pt30to35", "CMS_jetFR_pt35to40", "CMS_jetFR_pt40to50", "CMS_jetFR_pt50to60", "CMS_jetFR_ptgt60"},
        //                         {"mutau", "etau"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory, "_antiIso");
    

      //   // Still MC, but process-specific shifts
      //   if (isMCnonHiggs(process) && !isDY(process)) {
      //     makeShiftedPlots(process, category, {"CMS_nonDY"}, {"mutau", "etau", "emu"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);
      //   }
      //   if (containsSubstring(process, "TTTo")) {
      //     makeShiftedPlots(process, category, {"CMS_toppt"}, {"mutau", "etau", "emu"}, {"m_vis"}, "2018", inputFile, outputDirectoryWithCategory);
      //   }

      //   // Recoil
      //   if (doRecoil(process)) {
      //     makeShiftedPlots(process, category, {"CMS_met_0j_resolution", "CMS_met_1j_resolution", "CMS_met_gt1j_resolution", "CMS_met_0j_response",  "CMS_met_1j_response",  "CMS_met_gt1j_response"},
      //                           {"mutau", "etau", "emu"}, {"met"}, "2018", inputFile, outputDirectoryWithCategory);
      //   }
      //   else {
      //     makeShiftedPlots(process, category, {"CMS_UES"}, {"mutau", "etau", "emu"}, {"met"}, "2018", inputFile, outputDirectoryWithCategory);
      //   }
      }
    }
  }
}


/*********************************************************************/
