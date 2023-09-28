// Usage: root -l -b -q runPlotTH1F.cpp

// Customize this file

#include "../baseCodeForPlots/plotTH1F.cpp"

int runPlotTH1Fs()
{
  

/* Read in and plot an EXISTING TH1F:
    th1fName :  the name of the TH1F inside the file (usually the name of the variable).
    xLabel   :  the x-axis label on the plot.
    paveText :  text to go in a TPave box. 
    isAU     : if True, normalize the plot so the area under the curve is 1, and set y-axis title to "A.U.".
               if False, do not normalize and set y-axis title to "Counts".
    histPath :  the path to the TH1F inside the file (usually the name of the folder in the ROOT file).
    inputDirectory : the path to the ROOT file (~/myRepo/input.root).
    outputDirectory: the directory where the output plots will be saved.
    */
 
  //  std::vector<TString> histPaths = {"", "b1_sr1", "b1_sr2", "b1_sr3", "b1_cr", "b2_sr1", "b2_sr2", "b2_cr"};
  std::vector<std::string> categories = {""};
  std::string inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/out.root";
  std::string outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/sysplots";


  std::vector<std::string> sysToPlot = {"muES_eta0to1p2", "muES_eta1p2to2p1", "muES_eta2p1to2p4",
  "tauES_dm0", "tauES_dm1", "tauES_dm10", "tauES_dm11",
  "JER", "JetAbsolute", "JetAbsoluteyear", "JetBBEC1", "JetBBEC1year", "JetEC2", "JetEC2year", "JetFlavorQCD", "JetHF", "JetHFyear", "JetRelativeBal", "JetRelativeSample",
  "met_0j_resolution", "met_1j_resolution", "met_gt1j_resolution", "met_0j_response",  "met_1j_response",  "met_gt1j_response",
  "tauideff_pt20to25", "tauideff_pt25to30", "tauideff_pt30to35", "tauideff_pt35to40", "tauideff_pt40to500", "tauideff_pt500to1000", "tauideff_ptgt1000",
  "tauideff_VSe_bar", "tauideff_VSe_end",
  "tauideff_VSmu_eta0to0p4", "tauideff_VSmu_eta0p4to0p8", "tauideff_VSmu_eta0p8to1p2", "tauideff_VSmu_eta1p2to1p7", "tauideff_VSmu_eta1p7to2p3",
  "btagsf_hf", "btagsf_lf", "btagsf_hfstats1", "btagsf_hfstats2", "btagsf_lfstats1", "btagsf_lfstats2", "btagsf_cferr1", "btagsf_cferr2",
  "jetFR_pt0to25", "jetFR_pt25to30", "jetFR_pt30to35", "jetFR_pt35to40", "jetFR_pt40to50", "jetFR_pt50to60", "jetFR_ptgt60",
  "crosstrg_fakefactor",
  "trgeff_single", "trgeff_cross"};



  for ( std::string var : {"met", "m_vis"}) {
    for (std::string updown : {"Up", "Down"}) {
      for ( std::string sys : sysToPlot ) {

        std::cout << sys << std::endl;

        // Folder name
        std::string folder;
        
        // Path to histogram in the file
        TString inputName = TString::Format("%s_CMS_%s_2018%s", var.c_str(), sys.c_str(), updown.c_str());
        std::cout << inputName.Data() << std::endl;
        // Label
        TString axisLabel = var.c_str();

        // Label text added to plot
        TString additionalLabel = TString::Format("%s %s", sys.c_str(), updown.c_str());

        // Path to output .pdf file
        TString outputName = TString::Format("%s/%s_CMS_%s_2018%s.pdf", outputDirectory.c_str(), var.c_str(), sys.c_str(), updown.c_str());
        

        std::cout << outputName << std::endl;
        plotTH1F(inputName, axisLabel, additionalLabel, false, inputDirectory, outputName, false);
      }
    }
    else {
      // Category
      folder = cat + "/";
    }
    
    // Path to histogram in the file
    TString inputName = TString::Format("%s%s_m_vis", folder.c_str(), sampleName.c_str());

    // Label
    TString axisLabel = "m_{vis}";

    // Label text added to plot
    TString additionalLabel = TString::Format("%s %s", label.c_str(), cat.c_str());

    // Path to output .pdf file
    TString outputName  = TString::Format("%s/%s_%s_m_vis.pdf", outputDirectory.c_str(), sampleName.c_str(), cat.c_str());

    // Nominal
    if (cat == "") {
      outputName = TString::Format("%s/%s_m_vis.pdf", outputDirectory.c_str(), sampleName.c_str());
    }

    std::cout << outputName << std::endl;
    plotTH1D(inputDirectory, inputName, axisLabel, additionalLabel, outputName);
  }
  return 1; 

}
