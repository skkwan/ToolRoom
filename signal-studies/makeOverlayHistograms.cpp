#include "TColor.h"

#include "../baseCodeForPlots/overlayHistograms.cpp"

int makeOverlayHistograms(void) {

    TString year = "2018";

    TString inputDirectory = "/eos/cms/store/group/phys_susy/AN-24-166/skkwan/condorHistogramming/2025-01-07-16h58m-year-2018-mutau-iteration0/";
    TString outputBaseDirectory = "/eos/user/s/skkwan/www/signalStudies/variableScans/";
    gSystem->Exec("mkdir -p " + outputBaseDirectory);

    TFile *f = new TFile(inputDirectory + "histograms.root");
    if (!f->IsOpen() || f==0){
        std::cout << "[ERROR:] File "<< inputDirectory << " NOT FOUND; EXITING"<<std::endl;
        return 0;
    }

    std::vector<TString> massPoints = {
        // "Cascade_ggH_MA1-15_MA2-100",
        // "Cascade_ggH_MA1-15_MA2-90",
        // "Cascade_ggH_MA1-20_MA2-90",
        // "Cascade_ggH_MA1-20_MA2-100",
        // "Cascade_ggH_MA1-30_MA2-90",

        "Cascade_ggH_MA1-20_MA2-40",
        "Cascade_ggH_MA1-20_MA2-50",
        "Cascade_ggH_MA1-20_MA2-60",
        "Cascade_ggH_MA1-20_MA2-70",
        "Cascade_ggH_MA1-20_MA2-80",
        "Cascade_ggH_MA1-20_MA2-90",
        "Cascade_ggH_MA1-20_MA2-100",

        // "NonCascade_ggH_MA2-50-MA1-40",
        // "NonCascade_ggH_MA2-60-MA1-40",
        // "NonCascade_ggH_MA2-70-MA1-40",
        // "NonCascade_ggH_MA2-80-MA1-40",

        // "TTToSemiLeptonic",
    };

    std::vector<TString> categories = {
        "inclusive",
        // "lowMassSR",
        // "mediumMassSR",
        // "highMassSR",
        // "highMassCR",
    };

    TString channel = "mutau";
    TString inFile = "histograms.root";


    std::vector<TH1F*> vHists;
    std::vector<TString> vLabels;
    std::vector<int> vColors;

    std::vector<const char*> palette = {
        "#5790fc",		
        "#f89c20",		
        "#e42536",		
        "#964a8b",		
        "#9c9ca1",		
        "#7a21dd",
        "#92dadd",
        };

    std::vector<std::vector<std::string>> variables = {
        {"m_tt", "m_{#tau#tau} / GeV"},
        {"pt_1", "Leading muon p_{T} / GeV"},
        {"pt_2", "Leading #tau_{h} p_{T} / GeV"},
        {"D_zeta", "D_{#zeta}"},
        {"m_btautau", "m_{b#tau#tau} / GeV"},
        {"mtMET_1", "m_{T}(#mu, MET) / GeV"},
        {"mtMET_2", "m_{T}(#tau_{h}, MET) / GeV"},
    };

    for (auto category : categories) {
        for (auto variableInfo : variables) {
            std::string variableName = variableInfo[0];
            std::string labelName = variableInfo[1];

            TString legendName = category + " " + year + " #mu#tau_{h}, signal yield x100";

            // index for getting colors
            int idx = 0;
            for (auto sampleName : massPoints) {
                // Get the histograms
                TString hName = channel + "/" + category + "/" + sampleName + "_" + variableName;
                TH1F *h = (TH1F*) f->Get(hName);

                if (h == 0) {
                    std::cout << "[ERROR:] Failed to find histogram called " << hName << " in the input file " << inFile << ", exiting" << std::endl;
                    return 0;
                }
                else {
                    std::cout << "Got " << hName << std::endl;
                }

                vHists.push_back(h);
                vLabels.push_back(sampleName);

                if (sampleName == "TTToSemiLeptonic") {
                    // black
                    vColors.push_back(1);
                }   
                else {
                    vColors.push_back(TColor::GetColor(palette[idx]));
                    // increment index
                    idx++;
                }

            }

            bool doLog = false;

            plotNHistograms(vHists, vLabels, vColors, 
                            legendName,
                            labelName,
                            channel + "_" + year + "_" + category + + "_" + variableName,
                            outputBaseDirectory,
                            doLog);

            vHists.clear();
            vLabels.clear();
            vColors.clear();
        }
    }
    
    std::cout << "Check https://skkwan.web.cern.ch/signalStudies/" << std::endl;

    return 0;
}