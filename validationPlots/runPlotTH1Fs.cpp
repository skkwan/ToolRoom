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
  std::vector<std::string> categories = {"", "b1_sr1"};
  std::string inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/Systematics/plots/10_03_22_Categories_syncOnly_check/histograms_VBFHToTauTau.root";
  std::string outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G5/hToAA/Systematics/plots/10_03_22_Categories_syncOnly_check/";

  std::string sampleName = "VBFHToTauTau";
  std::string label = "VBF H to #tau#tau, 2018 #mu#tau_{H}";

  for ( std::string cat : categories ) {
    std::cout << cat << std::endl;

    // Folder name
    std::string folder;
    if (cat == "") {
      // Nominal
      folder = "";
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
