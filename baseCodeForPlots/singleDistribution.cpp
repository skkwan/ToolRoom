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

#ifndef SINGLE_DISTRIBUTION_C_INCL
#define SINGLE_DISTRIBUTION_C_INCL 
 
/* Apply template style to a TPad* pad1. */
void applyPadStyle(TPad* pad1){
  pad1->SetFillColor(0);
  pad1->Draw();  pad1->cd();  pad1->SetLeftMargin(0.2);  pad1->SetBottomMargin(0.2); pad1->SetRightMargin(0.3); pad1->SetTopMargin(0.2);
  //pad1->SetGrid(); 
  pad1->SetGrid(10,10); 
}

/* Apply legend style to a TLegend *leg. */
void applyLegStyle(TLegend *leg){
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetTextSize(0.05);
  leg->SetTextFont(42);
  leg->SetHeader("");
  leg->SetShadowColor(0);
}
 
/* Generate a single distribution plot.
   treePath specifies the tree in the ROOT file to use.
   The ROOT file is located at inputDirectory. The resulting plots are written to outputDirectory, with filename including "variable". The histogram has (bins)
   number of bins and ranges from integers low to high.
   "legend" is the legend label, "xLabel" is the x-axis label. */
int singleDistributionPlots(TString variable, TString cut, TString title, TString legend, TString treePath, TString inputDirectory, TString outputDirectory,
			    TString xLabel, int bins, double low, double high, TString plotname = ""){ 
 
  setTDRStyle();
 
  TCanvas* Tcan = new TCanvas("Tcan","", 100, 20, 800, 600);
  Tcan->cd();     /* Set current canvas */
  Tcan->SetFillColor(0);
  Tcan->SetRightMargin(0.07);
 
  TLegend *leg = new TLegend(0.20,0.85,0.9,0.95);
  applyLegStyle(leg);
 
  TLatex *latex = new TLatex(); 
  latex->SetNDC();
  latex->SetTextFont(42);
  latex->SetTextColor(kBlack);

  TFile *file = new TFile(inputDirectory);
 
  if(!file->IsOpen()||file==0){
    std::cout<<"ERROR FILE "<< inputDirectory <<" NOT FOUND; EXITING"<<std::endl;
    return 0;
  }
 
  TTree* tree = (TTree*)file->Get(treePath);
  if(tree == 0){
    std::cout<<"ERROR: " << treePath <<" NOT FOUND; EXITING"<<std::endl;
    return 0;
  }
 
  TH1F *hist = new TH1F("hist","hist", bins, low, high);
  int yield = tree->Draw(variable+">>+hist", cut);

  hist->SetMarkerColor(0);
  hist->SetFillStyle(1001);
  hist->SetFillColorAlpha(kBlue+2, 0.1);
  hist->SetLineWidth(1);
  hist->SetLineColor(kBlue+2);

  hist->Draw("HIST"); 
  
  hist->GetXaxis()->SetTitle(xLabel);
  hist->GetYaxis()->SetTitle("Count");

  // leg->AddEntry(hist, legend + ": " + yield + " events","l");
  // leg->Draw();

  latex->DrawLatex(0.16, 0.960, "#scale[0.7]{" + title + "}"); 
 
  Tcan->cd();

  if (plotname == "") {
    Tcan->SaveAs(outputDirectory+variable+".pdf");
    Tcan->SaveAs(outputDirectory+variable+".png");
  }
  else {
    Tcan->SaveAs(outputDirectory+plotname+".pdf");
    Tcan->SaveAs(outputDirectory+plotname+".png");
  }


  //TPad* pad2 = new TPad("pad2","The lower pad",0,0,0.98,0.25);
  //applyPadStyle(pad2);
  //pad2->cd();
  //pad2->SetGrid(0,0); 
 
  //ratio->Draw("p");



  delete Tcan;
  return 1;

}

#endif