// Usage: root -l -b -q runDistributionPlots.C
// Create plots of variables from a TTree

#include "../baseCodeForPlots/singleDistribution.cpp"

void runDistributionPlots(void)
{


  std::vector<TString> massPoints = {
    "Cascade_VBF_MA2-100_MA1-15",
    // "Cascade_VBF_MA2-100_MA1-20",
    // "Cascade_VBF_MA2-40_MA1-15",
    // "Cascade_VBF_MA2-40_MA1-20",
    // "Cascade_VBF_MA2-60_MA1-15",
    // "Cascade_VBF_MA2-60_MA1-20",
    // "Cascade_VBF_MA2-60_MA1-30",
    // "Cascade_VBF_MA2-80_MA1-15",
    // "Cascade_VBF_MA2-80_MA1-20",
    // "Cascade_VBF_MA2-80_MA1-30",
    // "Cascade_ggH_MA2-100_MA1-15",
    // "Cascade_ggH_MA2-100_MA1-20",
    // "Cascade_ggH_MA2-40_MA1-15",
    // "Cascade_ggH_MA2-40_MA1-20",
    // "Cascade_ggH_MA2-60_MA1-15",
    // "Cascade_ggH_MA2-60_MA1-20",
    // "Cascade_ggH_MA2-60_MA1-30",
    // "Cascade_ggH_MA2-80_MA1-15",
    // "Cascade_ggH_MA2-80_MA1-20",
    // "Cascade_ggH_MA2-80_MA1-30"
  };

  for (auto sampleName : massPoints) {

    TString inDir = "/eos/user/s/skkwan/hToAA/condorSkim/2023-10-03-17h02m/" + sampleName + "/" + sampleName + "_0.root";

    std::cout << sampleName << " " << inDir << std::endl;
    TString treePath = "event_tree";

    TString outputBaseDirectory = "/eos/user/s/skkwan/hToAA/condorSkim/2023-10-03-17h02m/plots/"; 
    gSystem->Exec("mkdir -p " + outputBaseDirectory);

    std::map<std::string, std::string> dictCut = {
      {"mutau", "(b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && (passMuTauTrigger && channel==0)"}, 
      {"etau", "(b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && (passETauTrigger && channel==1)"},
      {"emu", " (b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && (passEMuTrigger && channel==2) "},
      {"geq1btag", "(b_flav_idx_1 != -1) && ((passMuTauTrigger && channel==0) || (passETauTrigger && channel==1) || (passEMuTrigger && channel==2))"},
      {"geq2btag", "(b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && ((passMuTauTrigger && channel==0) || (passETauTrigger && channel==1) || (passEMuTrigger && channel==2))"},
      {"geq3btag", "(b_flav_idx_1 != -1) && (b_flav_idx_2 != -1) && (b_flav_idx_3 != -1) && ((passMuTauTrigger && channel==0) || (passETauTrigger && channel==1) || (passEMuTrigger && channel==2))"}

    };
    

    std::map<std::string, TString> dictLegends = {
      {"mutau", "#mu#tau_{h} channel"},
      {"etau", "e#tau_{h} channel"},
      {"emu", "e#mu channel"},
      {"geq1btag", "all #tau#tau channels, #geq 1 b-tag jets"},
      {"geq2btag", "all #tau#tau channels, #geq 2 b-tag jets"},
      {"geq3btag", "all #tau#tau channels, #geq 3 b-tag jets"}
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

    std::vector<std::string> channelsToPlot = {"geq1btag", "geq2btag", "geq3btag"};

    int nBins = 30;

    for (std::string channel : channelsToPlot) {

      TString ch(channel);
      TString outDir = outputBaseDirectory;
      gSystem->Exec("mkdir -p " + outDir);

      TString plotname = sampleName + "_" + channel;
      TString title = sampleName + ", with loosened deepFlav for sub-leading jet";

      singleDistributionPlots("m_vis", dictCut[channel], title, dictLegends[channel], treePath, inDir, outDir, "m_{#tau#tau}^{vis}", nBins, 0, 200, plotname);

    }
  }
}
