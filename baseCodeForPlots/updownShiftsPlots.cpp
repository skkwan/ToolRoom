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
  leg->SetTextSize(0.05);   // make it larger than default
  leg->SetTextFont(42);     // un-bold (62 is bold helvetica, the default)
}
 
/* Generate a comparison plot of variable with systematics varUp and varDown. Assumes that these histograms already exist in the
   input file. 
   The ROOT file is located at inputDirectory. The resulting plots are written to outputDirectory, with filename including "name". The histogram has (bins)
   number of bins and ranges from integers low to high. */
int updownShiftsPlots(TString process, TString baseVariable, TString channelFolder, TString systematic, TString inputDirectory, TString outputDirectory, TString optional = ""){ 
 
  //gROOT->LoadMacro("CMS_lumi.C");
  //gROOT->ProcessLine(".L ~/Documents/work/Analysis/PhaseIIStudies/2018/tdrstyle.C");
  setTDRStyle();
 

  TString variable = baseVariable + optional;
  TString varUp    = baseVariable + systematic + "Up" + optional;
  TString varDown  = baseVariable + systematic + "Down" + optional;

  TCanvas* Tcan = new TCanvas("Tcan","", 100, 20, 800, 600);
  Tcan->cd();     /* Set current canvas */
  Tcan->SetFillColor(0);
  //TPad* pad1 = new TPad("pad1","The pad",0,0.0,0.98,1);
  //applyPadStyle(pad1);
 
  TLegend *leg = new TLegend(0.50,0.62,0.9,0.92);
  applyLegStyle(leg);
 
  TFile *f = new TFile(inputDirectory);
 
  if(!f->IsOpen() || f==0){
    std::cout << "[ERROR:] File "<< inputDirectory << " NOT FOUND; EXITING"<<std::endl;
    return 0;
  }

  TString nameCenter = channelFolder + "/" + process + "_" + variable;
  TString nameUp     = channelFolder + "/" + process + "_" + varUp;
  TString nameDown   = channelFolder + "/" + process + "_" + varDown;
  TH1D *hCenter = (TH1D*) f->Get(nameCenter);
  TH1D *hUp     = (TH1D*) f->Get(nameUp);
  TH1D *hDown   = (TH1D*) f->Get(nameDown);

  if (hCenter == 0) {
    std::cout << "[ERROR:] Failed to find histogram called " << nameCenter << " in the input file " << inputDirectory << ", exiting" << std::endl;
    return 0;
  }
  else {
    std::cout << "Got " << nameCenter << std::endl;
  }
  if (hUp == 0) {
    std::cout << "[ERROR:] Failed to find histogram called " << nameUp << " in the input file " << inputDirectory << ", exiting" << std::endl;
    return 0;
  }
  else {
     std::cout << "Got " << nameUp << std::endl;
  }
  if (hDown == 0) {
    std::cout << "[ERROR:] Failed to find histogram called " << nameDown << " in the input file " << inputDirectory << ", exiting" << std::endl;
    return 0;
  }
  else {
     std::cout << "Got " << nameDown << std::endl;
  }
  float yieldCenter = hCenter->Integral();
  float yieldUp     = hUp->Integral();
  float yieldDown   = hDown->Integral();

  hCenter->SetMarkerColor(0);
//  hCenter->SetFillStyle(1001);
//  hCenter->SetFillColorAlpha(kBlack, 0.1);
  hCenter->SetLineWidth(1);
  hCenter->SetLineColor(kBlack);

  hDown->SetMarkerColor(0);
//  hDown->SetFillStyle(1001);
//  hDown->SetFillColorAlpha(kBlue+2, 0.1);
  hDown->SetLineWidth(2);
  hDown->SetLineColor(kGreen+1);

  hUp->SetMarkerColor(0);
//  hUp->SetFillStyle(1001);
//  hUp->SetFillColorAlpha(kRed+2, 0.1);
  hUp->SetLineWidth(2);
  hUp->SetLineColor(kRed+2);

  //   hUp->Scale(1/hUp->Integral());
  //   hCenter->Scale(1/hCenter->Integral());
  //   Tcan->SetLogy();

  
  hUp->Draw("HIST"); 
  hDown->Draw("HIST same");
  hCenter->Draw("HIST same");  

  
  // This has to be the first histogram we declare above or the x- and y-axes labels will not show up
  hUp->GetXaxis()->SetTitle(baseVariable+systematic);
  hUp->GetYaxis()->SetTitle("Yield");
  hUp->GetXaxis()->SetTitleSize(0.06); // default is 0.03     
  hUp->GetYaxis()->SetTitleSize(0.06); // default is 0.03     

  // Make more room at the top for the legend
  float max = hUp->GetMaximum(); 
  hUp->SetMaximum(max * 1.45);  

  leg->SetHeader(TString::Format("%s, %s", process.Data(), channelFolder.Data()));
  leg->AddEntry(hUp,     TString::Format("Up:        yield: %0.2f", yieldUp),     "l");
  leg->AddEntry(hCenter, TString::Format("Central: yield: %0.2f", yieldCenter), "l");
  leg->AddEntry(hDown,   TString::Format("Down:   yield: %0.2f", yieldDown),   "l");

  leg->Draw();

  Tcan->Update();
  Tcan->cd();

  //TPad* pad2 = new TPad("pad2","The lower pad",0,0,0.98,0.25);
  //applyPadStyle(pad2);
  //pad2->cd();
  //pad2->SetGrid(0,0); 
 
  //ratio->Draw("p");

 
  Tcan->cd();
  //Tcan->SetLogy();
  Tcan->SaveAs(outputDirectory+"/sys-"+process+"-"+baseVariable+systematic+optional+".pdf");
  Tcan->SaveAs(outputDirectory+"/sys-"+process+"-"+baseVariable+systematic+optional+".png");

  delete Tcan;

  f->Close();
  return 1;

}

#endif
