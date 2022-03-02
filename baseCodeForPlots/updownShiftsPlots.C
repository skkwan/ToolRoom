#include "TAxis.h"
#include "TCanvas.h"
#include "TChain.h"
#include "TEfficiency.h"
#include "TFile.h"
#include "TFormula.h"
#include "TGaxis.h"
#include "TH1.h"
#include "TH1.h"
#include "TF1.h"
#include "TH2.h"
#include "TLegend.h"
#include "THStack.h"
#include "TMath.h"
#include "TPad.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TTree.h"

#include <cmath>
#include <iostream>
#include <math.h>
#include <string>

#include "tdrstyle.C"
#include "CMS_lumi.h"

#ifndef UP_DOWN_SHIFTS_PLOTS_INCL
#define UP_DOWN_SHIFTS_PLOTS_INCL
 
/* Apply template style to a TPad* pad1. */
void applyPadStyle(TPad* pad1){
  pad1->SetFillColor(0);
  pad1->Draw();  pad1->cd();  pad1->SetLeftMargin(0.2);  pad1->SetBottomMargin(0.13); pad1->SetRightMargin(0.1);
  //pad1->SetGrid(); 
  pad1->SetGrid(10,10); 
}

/* Apply legend style to a TLegend *leg. */
void applyLegStyle(TLegend *leg){
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetHeader("");
  leg->SetShadowColor(0);
}
 
/* Generate a comparison plot of variable with systematics varUp and varDown. Assumes that these histograms already exist in the
   input file. 
   The ROOT file is located at inputDirectory. The resulting plots are written to outputDirectory, with filename including "name". The histogram has (bins)
   number of bins and ranges from integers low to high. */
int updownShiftsPlots(TString process, TString baseVariable, TString systematic, TString inputDirectory, TString outputDirectory){ 
 
  //gROOT->LoadMacro("CMS_lumi.C");
  //gROOT->ProcessLine(".L ~/Documents/work/Analysis/PhaseIIStudies/2018/tdrstyle.C");
  setTDRStyle();
 

  TString variable = process + baseVariable;
    TString varUp    = process + baseVariable + systematic + "Up";
   TString varDown  = process + baseVariable + systematic + "Down";

  // TString variable = baseVariable;
  // TString varUp    = baseVariable + systematic + "Up";
  // TString varDown  = baseVariable + systematic + "Down";
 
  //  TFile* tauFile = new TFile("dummy");
  TCanvas* Tcan = new TCanvas("Tcan","", 100, 20, 800, 600);
  Tcan->cd();     /* Set current canvas */
  Tcan->SetFillColor(0);
  //TPad* pad1 = new TPad("pad1","The pad",0,0.0,0.98,1);
  //applyPadStyle(pad1);
 
  TLegend *leg = new TLegend(0.60,0.75,0.85,0.9);
  applyLegStyle(leg);
 
  TFile *file = new TFile(inputDirectory);
 
  if(!file->IsOpen()||file==0){
    std::cout<<"[ERROR:] File "<< inputDirectory << " NOT FOUND; EXITING"<<std::endl;
    return 0;
  }

  TH1D *hCenter = 0;
  file->GetObject(variable, hCenter);


  TH1D *hUp = 0;
  file->GetObject(varUp, hUp);

  TH1D *hDown = 0;
  file->GetObject(varDown, hDown);

  if (hCenter == 0) {
    std::cout << "[ERROR:] Failed to histogram called " 
              << variable << ", " << varUp << ",  and " << varDown << " exist in the input file, exiting" << std::endl;
    return 0;
  }
  if (hUp == 0) {
    std::cout << "[ERROR:] Failed to histogram called " 
              << varUp << " exist in the input file, exiting" << std::endl;
    return 0;

  }
  if (hDown == 0) {
    std::cout << "[ERROR:] Failed to histogram called " 
              << varDown << " exist in the input file, exiting" << std::endl;
    return 0;

  }
  hCenter->SetMarkerColor(0);
//  hCenter->SetFillStyle(1001);
//  hCenter->SetFillColorAlpha(kBlack, 0.1);
  hCenter->SetLineWidth(1);
  hCenter->SetLineColor(kBlack);

  hDown->SetMarkerColor(0);
//  hDown->SetFillStyle(1001);
//  hDown->SetFillColorAlpha(kBlue+2, 0.1);
  hDown->SetLineWidth(1);
  hDown->SetLineColor(kGreen);

  hUp->SetMarkerColor(0);
//  hUp->SetFillStyle(1001);
//  hUp->SetFillColorAlpha(kRed+2, 0.1);
  hUp->SetLineWidth(1);
  hUp->SetLineColor(kRed+2);

  //   hUp->Scale(1/hUp->Integral());
  //   hCenter->Scale(1/hCenter->Integral());
  //   Tcan->SetLogy();

  hCenter->Draw("HIST");  
  hUp->Draw("HIST same"); 
  hDown->Draw("HIST same");
  
  hCenter->GetXaxis()->SetTitle(baseVariable+systematic);
  hCenter->GetYaxis()->SetTitle("Yield");
hCenter->GetXaxis()->SetTitleSize(0.06); // default is 0.03     
hCenter->GetYaxis()->SetTitleSize(0.06); // default is 0.03     
  /*
  float max = 10;
  if(Fake->GetXaxis()->GetBinCenter( Fake->GetMaximumBin() ) > hCenter->GetXaxis()->GetBinCenter( hCenter->GetMaximumBin() ) )
    max = Fake->GetXaxis()->GetBinCenter(Fake->GetMaximumBin());
  else
    max = hCenter->GetXaxis()->GetBinCenter(hCenter->GetMaximumBin());
   
    std::cout<<"max: "<<max<<std::endl;
  Fake->SetMaximum(max/60);
  */

  //leg->AddEntry(NoIso,"No Isolation","l");
  //  leg->AddEntry(hCenter,"#tau_{h} Gen-Vis p_{T}>20 GeV","l");
  //  leg->AddEntry(Fake,"Fake Background","l");
  leg->AddEntry(hCenter, "Central value", "l");
  leg->AddEntry(hUp,     "Up",            "l");
  leg->AddEntry(hDown,   "Down",          "l");
  leg->Draw();
 
  Tcan->cd();

  //TPad* pad2 = new TPad("pad2","The lower pad",0,0,0.98,0.25);
  //applyPadStyle(pad2);
  //pad2->cd();
  //pad2->SetGrid(0,0); 
 
  //ratio->Draw("p");

 
  Tcan->cd();
  Tcan->SetLogy();
  Tcan->SaveAs(outputDirectory+baseVariable+systematic+".pdf");
  Tcan->SaveAs(outputDirectory+baseVariable+systematic+".png");
 
  delete Tcan;

  return 1;

}

#endif
