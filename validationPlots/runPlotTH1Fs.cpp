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
  std::string inputDirectory  = "/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/2023-09-21_histograms.root";
  std::string outputDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/temp/plots/";


  std::vector<std::string> channels = {"mutau", "etau", "emu"};
  std::vector<std::string> sampleNames = {
    "TTToSemiLeptonic",
    "DY1JetsToLL",
    "DYJetsToLL_M-10to50",
    "ST_t-channel_top",
    "ST_t-channel_antitop",
    "VVTo2L2Nu",
    "DY4JetsToLL",
    "W2JetsToLNu",
    "W3JetsToLNu",
    "W4JetsToLNu",
    "GluGluHToTauTau",
    "WZTo3LNu",
    "GluGluHToWWTo2L2Nu",
    "DYJetsToLL_M-50",
    "DY2JetsToLL",
    "TTToHadronic",
    "ZZTo4L",
    "HWplusJ_HToWW",
    "HZJ_HToWW",
    "GluGluZH_HToWW_ZTo2L",
    "ZHToTauTau",
    "EGamma-Run2018A",
    "ttHToNonbb",
    "ttHTobb",
    "EGamma-Run2018B",
    "WZTo2L2Q",
    "VBFHToWWTo2L2Nu",
    "MuonEG-Run2018D",
    "Embedded-Run2018A-MuTau",
    "VBFHToTauTau",
    "MuonEG-Run2018C",
    "Embedded-Run2018B-ElTau",
    "ZZTo2L2Q",
    "W1JetsToLNu",
    "WminusHToTauTau",
    "WJetsToLNu",
    "DY3JetsToLL",
    "ST_tW_antitop",
    "ST_tW_top",
    "GluGluZH_HToWWTo2L2Nu",
    "SingleMuon-Run2018D",
    "HWminusJ_HToWW",
    "MuonEG-Run2018B",
    "SingleMuon-Run2018C",
    "SingleMuon-Run2018B",
    "Embedded-Run2018C-ElTau",
    "WplusHToTauTau",
    "SingleMuon-Run2018A",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-45",
    "EGamma-Run2018C",
    "Embedded-Run2018A-ElTau",
    "MuonEG-Run2018A",
    "Embedded-Run2018C-MuTau",
    "Embedded-Run2018B-MuTau",
    "EGamma-Run2018D",
    "Embedded-Run2018D-MuTau",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45",
    "Embedded-Run2018D-ElTau",
    "TTTo2L2Nu"
    };

  for ( std::string ch : channels ) {
    for ( std::string sampleName : sampleNames ) {
      std::cout << sampleName << std::endl;

      // Folder name
      std::string folder = ch + "/";

      // Path to histogram in the file
      TString inputName = TString::Format("%s/%s_m_vis", ch.c_str(), sampleName.c_str());

      // Label
      TString axisLabel = "m_{vis} [GeV]";

      // Label text added to plot
      TString additionalLabel = TString::Format("%s %s", sampleName.c_str(), ch.c_str());

      // Path to output .pdf file
      TString outputName  = TString::Format("%s%s_%s_m_vis.pdf", outputDirectory.c_str(), sampleName.c_str(), ch.c_str());

      std::cout << outputName << std::endl;
      bool isAU = false;
      bool useLogy = false;
      plotTH1F(inputName, axisLabel, additionalLabel, isAU, inputDirectory, outputName, useLogy);
    }

  }

  return 1; 

}
