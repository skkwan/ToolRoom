// Usage: root -l -b -q runDistributionPlots.C
// Create plots of variables from a TTree

#include "../baseCodeForPlots/singleDistribution.cpp"

void runDistributionPlots(void)
{


  std::vector<TString> massPoints = {
    "Cascade_VBF_MA2-100_MA1-15",
    "Cascade_VBF_MA2-100_MA1-20",
    "Cascade_VBF_MA2-40_MA1-15",
    "Cascade_VBF_MA2-40_MA1-20",
    "Cascade_VBF_MA2-60_MA1-15",
    "Cascade_VBF_MA2-60_MA1-20",
    "Cascade_VBF_MA2-60_MA1-30",
    "Cascade_VBF_MA2-80_MA1-15",
    "Cascade_VBF_MA2-80_MA1-20",
    "Cascade_VBF_MA2-80_MA1-30",
    "Cascade_ggH_MA2-100_MA1-15",
    "Cascade_ggH_MA2-100_MA1-20",
    "Cascade_ggH_MA2-40_MA1-15",
    "Cascade_ggH_MA2-40_MA1-20",
    "Cascade_ggH_MA2-60_MA1-15",
    "Cascade_ggH_MA2-60_MA1-20",
    "Cascade_ggH_MA2-60_MA1-30",
    "Cascade_ggH_MA2-80_MA1-15",
    "Cascade_ggH_MA2-80_MA1-20",
    "Cascade_ggH_MA2-80_MA1-30"
  };

  for (auto sampleName : massPoints) {

    TString legend = sampleName;
    TString inDir = "/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/cascade_4b2tau_investigation/2023-09-25-15h48m_asymmetricSamples/" + sampleName + "/" + sampleName + "_0.root";

    std::cout << sampleName << " " << legend << " " << inDir << std::endl;
    TString treePath = "event_tree";

    TString outputBaseDirectory = "/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/cascade_4b2tau_investigation/2023-09-25-15h48m_asymmetricSamples/"; 
    gSystem->Exec("mkdir -p " + outputBaseDirectory);

    std::map<std::string, std::string> dictCut = {
      {"mutau", "(b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && (passMuTauTrigger && channel==0)"}, 
      {"etau", "(b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && (passETauTrigger && channel==1)"},
      {"emu", " (b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && (passEMuTrigger && channel==2) "},
      {"allgeq2btag", "(b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && ((passMuTauTrigger && channel==0) || (passETauTrigger && channel==1) || (passEMuTrigger && channel==2))"},
      {"allexactly1btag", "(b_flav_idx_1 != -1) && (b_flav_idx_2 == -1) && ((passMuTauTrigger && channel==0) || (passETauTrigger && channel==1) || (passEMuTrigger && channel==2))"}
    };

    std::map<std::string, TString> dictLegends = {
      {"mutau", "#mu#tau_{h} channel"},
      {"etau", "e#tau_{h} channel"},
      {"emu", "e#mu channel"},
      {"allgeq2btag", "all channels, #geq 2 b-tag jets"},
      {"allexactly1btag", "all channels, exactly 1 b-tag jet"}
    };

    std::map<std::string, TString> dictLeg1 = {
      {"mutau", "Muon"},
      {"etau", "Electron"},
      {"emu", "Electron"}
    };
    
    std::map<std::string, TString> dictLeg2 = {
      {"mutau", "#tau_{h}"},
      {"etau", "#tau_{h}"},
      {"emu", "Muon"}
    };

    std::vector<std::string> channelsToPlot = {"allgeq2btag", "allexactly1btag"};

    int nBins = 30;
    bool normOption = false;  

    for (std::string channel : channelsToPlot) {

      TString ch(channel);
      TString outDir = outputBaseDirectory;
      gSystem->Exec("mkdir -p " + outDir);

      TString description = "_" + sampleName + "_" + dictLegends[channel];
      singleDistributionPlots("m_vis", dictCut[channel], legend + ", " + dictLegends[channel], treePath, inDir, outDir, "m_{#tau#tau}^{vis}", nBins, 0, 200, normOption, description);

    }
  }
}
