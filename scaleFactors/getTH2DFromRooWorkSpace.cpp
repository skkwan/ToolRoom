/* 
 * Usage: root -l getTH2DFromRooWorkSpace.cpp
 */

#include "RooWorkspace.h"


/*
 * Set plot style, title and axis labels of a TH2D. 
 */
void setPlotStyle(TH2D*& myHist, TString title, TString xLabel, TString yLabel, double plot_ymin, double plot_ymax) {
    myHist->GetXaxis()->SetTitle(xLabel);
    myHist->GetYaxis()->SetTitle(yLabel);
    myHist->SetTitle(title);

    myHist->GetXaxis()->SetTitleSize(0.04); // default is 0.03                                                                    
    myHist->GetYaxis()->SetTitleSize(0.04); // default is 0.03 

    myHist->GetYaxis()->SetRangeUser(plot_ymin, plot_ymax);
}

/*
 * Set title and axis labels of a TGraph.
 */
void setPlotStyleTGraph(TGraph*& myGraph, TString title, TString xLabel, TString yLabel) {
    if (myGraph != NULL) {
        myGraph->GetXaxis()->SetTitle(xLabel);
        myGraph->GetYaxis()->SetTitle(yLabel);
        myGraph->SetTitle(title);

        myGraph->GetXaxis()->SetTitleSize(0.04); // default is 0.03                                                                    
        myGraph->GetYaxis()->SetTitleSize(0.04); // default is 0.03 
    }
}

/*
 * Make canvas larger so side label won't run off the side.
 */

void setPadMargins(TPad*& myPad) {

    myPad->SetRightMargin(0.15);
    myPad->SetLeftMargin(0.15);
}

/*
 * Draw and save the provided h2 to the output name. If h2Cutoff (TH2D) is provided, also draw it.
 */

void drawAndSaveTH2D(TH2D* h2, TString title, TString xLabel, TString yLabel, TString outputName, double plot_ymin, double plot_ymax, TGraph* tGraph = NULL) {

    TCanvas *c1 = new TCanvas("c1", "c1", 1900, 1900);
    TPad *pad1 = new TPad("pad1", "The pad", 0, 0, 1, 1);
    setPadMargins(pad1);
    
    gStyle->SetOptStat(0);

    pad1->Draw();
    pad1->cd();
    
    h2->Draw("COLZ 1 SAME");

    setPlotStyle(h2, title, xLabel, yLabel, plot_ymin, plot_ymax);
    setPlotStyleTGraph(tGraph, title, xLabel, yLabel);
    c1->SaveAs(outputName);

    delete pad1;
    delete c1;
}

/* 
 *
 */

float getSF_E12(RooWorkspace *wmc, float ele_pt, float ele_eta) {


    wmc->var("e_pt")->setVal(ele_pt);
    wmc->var("e_eta")->setVal(ele_eta);
    float sf_e_trg_12_ic_data = wmc->function("e_trg_12_ic_data")->getVal();
    float sf_e_trg_12_ic_mc = wmc->function("e_trg_12_ic_mc")->getVal();

    // FIXME: 
    // float trgsf_Mu23E12only_num = sf_m_trg_23_ic_data * sf_e_trg_12_ic_data; 
    // float trgsf_Mu23E12only_den = sf_m_trg_23_ic_mc * sf_e_trg_12_ic_mc;

    // float trgsf = (trgsf_Mu23E12only_num / trgsf_Mu23E12only_den);

    // return trgsf;
    return (sf_e_trg_12_ic_data/sf_e_trg_12_ic_mc);
}


float getSF_electron_HLT_Mu8Ele23(RooWorkspace *wmc, float ele_pt, float ele_eta) {


    wmc->var("e_pt")->setVal(ele_pt);
    wmc->var("e_eta")->setVal(ele_eta);
    float sf_data = wmc->function("e_trg_23_ic_data")->getVal();
    float sf_mc = wmc->function("e_trg_23_ic_mc")->getVal();

    // return trgsf;
    return (sf_data/sf_mc);
}


float getSF_muon_HLT_Mu8Ele23(RooWorkspace *wmc, float mu_pt, float mu_eta) {


    wmc->var("m_pt")->setVal(mu_pt);
    wmc->var("m_eta")->setVal(mu_eta);
    float sf_data = wmc->function("m_trg_23_ic_data")->getVal();
    float sf_mc = wmc->function("m_trg_23_ic_mc")->getVal();

    // return trgsf;
    return (sf_data/sf_mc);
}


/*
 * Main function: Create TH2D of the isolation and et2x5/et5x5 vs. the cluster pT for a given TTree.
 * Also finds and overlays the cut-off points (one per x-axis bin) where 95% of the events fall above (or below) the cut-off point.
 * Saves the plots as pdfs.
 */

int getTH2DFromRooWorkSpace(void) {

    TString pathToNewHisto_electron = "/eos/user/s/skkwan/www/sfFromAshling/sf_el_2018_HLTMu8Ele23.root";
    TString pathToNewHisto_muon = "/eos/user/s/skkwan/www/sfFromAshling/sf_mu_2018_HLTMu8Ele23.root";

    TFile *newFile_electron = new TFile(pathToNewHisto_electron);
    if (!newFile_electron->IsOpen() || newFile_electron==0 ) {
        std::cout<<"ERROR: FILE "<< pathToNewHisto_electron <<" NOT FOUND; EXITING" << std::endl;
        return 0;
    }
    TFile *newFile_muon = new TFile(pathToNewHisto_muon);
    if (!newFile_muon->IsOpen() || newFile_muon==0 ) {
        std::cout<<"ERROR: FILE "<< pathToNewHisto_muon <<" NOT FOUND; EXITING" << std::endl;
        return 0;
    }
    TH2F* newSF_electron = (TH2F*) newFile_electron->Get("SF2D");
    newSF_electron->SetName("electron_SF2D");
    TH2F* newSF_muon = (TH2F*) newFile_muon->Get("SF2D");
    newSF_muon->SetName("muon_SF2D");

    if ((newSF_electron == 0) || (newSF_muon == 0)) {
        std::cout << "ERROR: SF2D not found in one of the two files; EXITING" << std::endl;
        return 0;
    }

    TString wsFileName = "/afs/cern.ch/work/s/skkwan/public/hToA1A2/CMSSW_13_2_6_patch2/src/lunaFramework/commonFiles/htt_scalefactors_legacy_2018.root";
    TFile fwmc(wsFileName);
    RooWorkspace *wmc;
    fwmc.GetObject("w", wmc);
    if (wmc == 0) {
        std::cout << "[ERROR:] RooWorkspace not retrievable from " << wsFileName << "!" << std::endl;
        return 0;
    }

    TH2F* oldSF_electron = (TH2F*) newSF_electron->Clone("old_electron_SF2D");
    TH2F *oldSF_muon = (TH2F*) newSF_muon->Clone("old_muon_SF2D");

    // Loop through bin contents for electron
    for (int i = 0; i < newSF_electron->GetNbinsX(); i++) {
        for (int j = 0; j < newSF_electron->GetNbinsY(); j++) {
            int iBin = newSF_electron->GetBin(i, j);
            float ele_pt = newSF_electron->GetXaxis()->GetBinCenter(i);
            float ele_eta = newSF_electron->GetYaxis()->GetBinCenter(j);

            // Evaluate the RooWorkSpace at this point
            float newValue = getSF_electron_HLT_Mu8Ele23(wmc, ele_pt, ele_eta);
            if (newValue > 2.0) {
                newValue = 2.0;
            }
            oldSF_electron->SetBinContent(iBin, newValue);

            std::cout << "Electron: " << ele_pt << ", " << ele_eta << ", " << newSF_electron->GetBinContent(iBin) << ", compared to old SF " << oldSF_electron->GetBinContent(iBin) << std::endl;

        }
    }
    // Loop through bin contents for muon leg
    for (int i = 0; i < newSF_muon->GetNbinsX(); i++) {
        for (int j = 0; j < newSF_muon->GetNbinsY(); j++) {
            int iBin = newSF_muon->GetBin(i, j);
            float mu_pt = newSF_muon->GetXaxis()->GetBinCenter(i);
            float mu_eta = newSF_muon->GetYaxis()->GetBinCenter(j);

            // Evaluate the RooWorkSpace at this point
            float newValue = getSF_muon_HLT_Mu8Ele23(wmc, mu_pt, mu_eta);
            if (newValue > 2.0) {
                newValue = 2.0;
            }
            oldSF_muon->SetBinContent(iBin, newValue);

            std::cout << "Muon: " << mu_pt << ", " << mu_eta << ", " << newSF_muon->GetBinContent(iBin) << ", compared to old SF " << oldSF_muon->GetBinContent(iBin) << std::endl;

        }
    }



    TFile fOldSF_electron("out_HLT_Mu8Ele23.root", "RECREATE");
    fOldSF_electron.cd();
    oldSF_electron->Write();
    oldSF_muon->Write();
    newSF_electron->Write();
    newSF_muon->Write();
    fOldSF_electron.Close();

    newFile_electron->Close();
    newFile_muon->Close();


    return 1;
}