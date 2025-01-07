#include "TColor.h"

#include "../baseCodeForPlots/overlayHistograms.cpp"

int makeOverlayHistograms(void) {

    TString year = "2018";

    TString inputDirectory = "/eos/cms/store/group/phys_susy/AN-24-166/skkwan/condorHistogramming/2024-11-20-23h57m-benchmark-2018-mutau-iteration1-m_vis/";
    TString outputBaseDirectory = "/eos/user/s/skkwan/www/signalStudies/";
    gSystem->Exec("mkdir -p " + outputBaseDirectory);

    TFile *f = new TFile(inputDirectory + "histograms.root");
    if (!f->IsOpen() || f==0){
        std::cout << "[ERROR:] File "<< inputDirectory << " NOT FOUND; EXITING"<<std::endl;
        return 0;
    }

    std::vector<TString> massPoints = {
        "Cascade_ggH_MA1-15_MA2-100",
        "Cascade_ggH_MA1-15_MA2-90",
        "Cascade_ggH_MA1-20_MA2-90",
        "Cascade_ggH_MA1-20_MA2-100",
        "Cascade_ggH_MA1-30_MA2-90",

    };

    std::vector<TString> categories = {
        "lowMassSR",
        "mediumMassSR",
        "highMassSR",
        "highMassCR",
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
        };

    for (auto category : categories) {
        TString legendName = category + " " + year + " #mu#tau_{h}, signal yield x100";

        // index for getting colors
        int idx = 0;
        for (auto sampleName : massPoints) {
            // Get the histograms
            TString hName = channel + "/" + category + "/" + sampleName + "_m_vis";
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
            vColors.push_back(TColor::GetColor(palette[idx]));

            // increment index
            idx++;
        }

        bool doLog = false;

        plotNHistograms(vHists, vLabels, vColors, 
                        legendName,
                        "Visible di-tau mass",
                        channel + "_" + year + "_" + category,
                        outputBaseDirectory,
                        doLog);

        vHists.clear();
        vLabels.clear();
        vColors.clear();
    }
    
    std::cout << "Check https://skkwan.web.cern.ch/signalStudies/" << std::endl;

    return 0;
}