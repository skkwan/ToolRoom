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

#include "singleDistribution.cpp"

#ifndef OVERLAY_DISTRIBUTIONS_CPP_INCL
#define OVERLAY_DISTRIBUTIONS_CPP_INCL 
 

 
/* Generate a single distribution plot.
   treePath specifies the tree in the ROOT file to use.
   The ROOT file is located at inputDirectory. The resulting plots are written to outputDirectory, with filename including "variable". The histogram has (bins)
   number of bins and ranges from integers low to high.
   "legend" is the legend label, "xLabel" is the x-axis label. */
int overlayDistributions(TString var0, TString var1, TString var2, TString var3, TString legend0, TString legend1, TString legend2, TString legend3, TString cut, TString treePath, TString inputDirectory, TString outputDirectory,
			    TString xLabel, int bins, int low, int high, TString title = "", TString plotname = ""){ 
 
  setTDRStyle();
 
  TCanvas* Tcan = new TCanvas("Tcan","", 100, 20, 800, 600);
  Tcan->cd();     /* Set current canvas */
  Tcan->SetFillColor(0);
 
  TLegend *leg = new TLegend(0.5,0.60,0.9,0.95);
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
 
  TH1F *h0 = new TH1F("h0", "h0", bins, low, high);
  TH1F *h1 = new TH1F("h1", "h1", bins, low, high);
  TH1F *h2 = new TH1F("h2", "h2", bins, low, high);
  TH1F *h3 = new TH1F("h3", "h3", bins, low, high);


  int yield0 = tree->Draw(var0+">>+h0", cut);
  int yield1 = tree->Draw(var1+">>+h1", cut);
  int yield2 = tree->Draw(var2+">>+h2", cut);
  int yield3 = tree->Draw(var3+">>+h3", cut);


  h0->SetMarkerColor(0);
  h0->SetLineWidth(2);
  h0->SetLineColor(kBlack);

  h1->SetMarkerColor(0);
  h1->SetLineColor(kRed);
  h1->SetLineWidth(2);
  // hist->Scale(1/hist->Integral());
  // Tcan->SetLogy();

  h2->SetMarkerColor(0);
  h2->SetLineColor(kBlue);
  h2->SetLineWidth(2);

  h3->SetMarkerColor(0);
  h3->SetLineColor(kGreen);
  h3->SetLineWidth(2);

  h0->SetMaximum(h3->GetMaximum() + 1000);

  h0->Draw("HIST");
  h1->Draw("HIST SAME");
  h2->Draw("HIST SAME");
  h3->Draw("HIST SAME");
  h0->GetXaxis()->SetTitle(xLabel);
  h0->GetYaxis()->SetTitle("Count");

  leg->SetHeader(title);
  leg->AddEntry(h0, legend0 + ": " + yield0 + " events","l");
  leg->AddEntry(h1, legend1 + ": " + yield1 + " events","l");
  leg->AddEntry(h2, legend2 + ": " + yield2 + " events","l");
  leg->AddEntry(h3, legend3 + ": " + yield3 + " events","l");


  leg->Draw();

  latex->DrawLatex(0.16, 0.960, "#scale[0.7]{" + title + "}"); 
 
  Tcan->cd();

  if (plotname == "") {
    Tcan->SaveAs(outputDirectory+var0+".pdf");
  }
  else {
    Tcan->SaveAs(outputDirectory+plotname+".pdf");
  }
 
  delete Tcan;
  return 1;

}

#endif
