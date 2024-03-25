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
  // std::string inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G6/TauIDSFs/data/TauID_SF_eta_DeepTau2017v2p1VSmu_2018ReReco.root";
  std::string inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G6/TauIDSFs/data/TauID_SF_eta_DeepTau2017v2p1VSe_2018ReReco.root";

  std::string outputDirectory = "/Users/stephaniekwan/Dropbox/Thesis/figures/ch-8-scale-factors-and-corrections/";





  TString inputName = "Tight";

  // Label
  TString axisLabel = "|#eta| of electron faking tau";

  // Label text added to plot
  TString additionalLabel = "DeepTau vs. electron, Tight WP";

  // Path to output .pdf file
  TString outputName = outputDirectory + "efficiency_misID_deeptau_vs_e_TightWP.pdf";
  

  plotTH1F(inputName, axisLabel, additionalLabel, false, inputDirectory, outputName, false);

  return 1; 

}
