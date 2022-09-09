/*
 * comparisonPlotsWeighted.cpp
 * Same as comparisonPlots.C but doesn't do log scale, uses realistic weights 
 */

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

#ifndef COMPARISON_PLOTS_WEIGHTED_INCL
#define COMPARISON_PLOTS_WEIGHTED_INCL
 
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
  // leg->SetHeader("");
  leg->SetShadowColor(0);
  leg->SetTextSize(0.05);   // make it larger than default
  leg->SetTextFont(42);     // un-bold (62 is bold helvetica, the default)
}
 
/* Generate a comparison plot of "variable", using the gen-level sigCut, and selecting fakes using bkgCut. treePath specifies the tree in the ROOT file to use.
   The ROOT file is located at inputDirectory. The resulting plots are written to outputDirectory, with filename including "name". The histogram has (bins)
   number of bins and ranges from integers low to high. 
   If totalnEvents != 1.0, also print the % of the yield in the histogram
   weight:  reweight the histogram by that branch
   If doDistributionStyle is true, plot the histogram(s) as distributions
   If showBackground is true, plot the background histogram
   Returns the yield of the signal histogram. */
float comparisonPlotsWeighted(TString variable, TString xLabel, TString sigCut, TString bkgCut,
			      TString sigLabel, TString bkgLabel,
			      TString legTitle,
			      TString treePath,
			      TString inputDirectory, TString outputDirectory, TString name, int bins, int low, int high,
			      int totalNEvents = 1.0,
			      TString weight = "",
			      bool doDistributionStyle = true,
			      bool showBackground = true){ 

  std::cout << "sig  cut: " << sigCut << std::endl;
  if (sigCut != "") { std::cout << "found a sig cut " << std::endl; }
  //gROOT->LoadMacro("CMS_lumi.C");
  //gROOT->ProcessLine(".L ~/Documents/work/Analysis/PhaseIIStudies/2018/tdrstyle.C");
  setTDRStyle();
 
  //int bins = 30;
  //int low = 0; 
  //int high = 15;
 
  //  TFile* tauFile = new TFile("dummy");
  TCanvas* Tcan = new TCanvas("Tcan","", 100, 20, 800, 600);
  Tcan->cd();     /* Set current canvas */
  Tcan->SetFillColor(0);
  //TPad* pad1 = new TPad("pad1","The pad",0,0.0,0.98,1);
  //applyPadStyle(pad1);
 
  TLegend *leg = new TLegend(0.30,0.65,0.95,0.9);
  applyLegStyle(leg);
 
  TFile *file = new TFile(inputDirectory);
 
  if(!file->IsOpen()||file==0){
    std::cout<<"ERROR FILE "<< inputDirectory + name<<" NOT FOUND; EXITING"<<std::endl;
    return 0;
  }
 
  //gStyle->SetOptFit(0);
  //gStyle->SetOptStat(0);
  //gStyle->SetEndErrorSize(0);
  //gStyle->SetErrorX(0.5);
 
  TTree* tree = (TTree*)file->Get(treePath);
  if(tree == 0){
    std::cout<<"ERROR Tau Tree is "<< tree<<" NOT FOUND; EXITING"<<std::endl;
    return 0;
  } 

  TString sigWeight;
  TString bkgWeight;

  if ((weight != "") && (sigCut != "")) { sigWeight = weight + "*" + sigCut; }
  else if (weight != "")                {std::cout << "2" << std::endl; sigWeight = weight; }
  else if (sigCut != "")                { sigWeight = sigCut; }

  if ((weight != "") && (bkgCut != "")) { bkgWeight = weight + "*" + bkgCut; }
  else if (weight != "")                {std::cout << "2" << std::endl; bkgWeight = weight; }
  else if (bkgCut != "")                { bkgWeight = bkgCut; }

  std::cout << "Sig weight: " << sigWeight << std::endl;
  std::cout << "Bkg weight: " << bkgWeight << std::endl;
  TH1F *True = new TH1F("True","True",bins,low,high);
  float sigEvents = tree->Draw(variable+">>+True", sigWeight);
  
  // Add the overflow bin
  std::cout << "nbins: " << True->GetNbinsX() << std::endl;
  float overflow = True->GetBinContent(True->GetNbinsX() + 1);
  std::cout << "adding overflow to sigEvents: " << overflow << std::endl;
  sigEvents += overflow;
  
  TH1F *Fake = new TH1F("Fake","Fake",bins,low,high);
  float bkgEvents = tree->Draw(variable+">>+Fake", bkgWeight); 
 
  /* Compute the ratio by cloning the True histogram, subtracting the Fake values,
     and dividing it by the Fake value. */
  /*
  TH1F *ratio = (TH1F*)True->Clone();
  ratio->Add(Fake,-1);
  ratio->Divide(Fake);
  */

  True->SetMarkerColor(0);
  True->SetFillStyle(1001);
  True->SetFillColorAlpha(kBlue+2, 0.1);
  True->SetLineWidth(1);
  True->SetLineColor(kBlue+2);

  Fake->SetMarkerColor(0);
  Fake->SetFillStyle(1001);
  Fake->SetFillColorAlpha(kRed+2, 0.1);
  Fake->SetLineWidth(1);
  Fake->SetLineColor(kRed+2);

  // if we're doing the distribution style, normalize the histograms to get their shape
  if (doDistributionStyle) {

    Fake->Scale(1/Fake->Integral());

    True->Scale(1/True->Integral());
    Tcan->SetLogy();
  }

  
  True->Draw("HIST");

  if (showBackground) {
    Fake->Draw("HIST same");  
  }
  
  True->GetXaxis()->SetTitle(xLabel);

  if (doDistributionStyle) {
    True->GetYaxis()->SetTitle("A.U.");
  }
  else {
    True->GetYaxis()->SetTitle("Yield");

  }

  /*
  float max = 10;
  if(Fake->GetXaxis()->GetBinCenter( Fake->GetMaximumBin() ) > True->GetXaxis()->GetBinCenter( True->GetMaximumBin() ) )
    max = Fake->GetXaxis()->GetBinCenter(Fake->GetMaximumBin());
  else
    max = True->GetXaxis()->GetBinCenter(True->GetMaximumBin());
   
    std::cout<<"max: "<<max<<std::endl;
  Fake->SetMaximum(max/60);
  */


  float max = True->GetMaximum(); 
  True->SetMaximum(max * 1.5);  

  if (doDistributionStyle) {
    True->SetMaximum(max * 2);  
  }
  

  //leg->AddEntry(NoIso,"No Isolation","l");
  //  leg->AddEntry(True,"#tau_{h} Gen-Vis p_{T}>20 GeV","l");
  //  leg->AddEntry(Fake,"Fake Background","l");

  leg->SetHeader(legTitle);
  leg->AddEntry(True, sigLabel, "l");
  // Also show the yield as int, and yield as an integral
  TString sigEventsLabel = "nEvents (incl. overflow): " + TString::Format("%i", (int) sigEvents);
  TString sigYieldLabel  = "Yield shown: " + TString::Format("%.2f", True->Integral());
  leg->AddEntry((TObject*)0, sigEventsLabel, "");
  leg->AddEntry((TObject*)0, sigYieldLabel, "");

  // Also show % of original events
  if (totalNEvents != 1.0) {
    float percentage = (sigEvents/totalNEvents) * 100;
    std::cout << ">>> Out of " << totalNEvents << " events with gen #tau#tau, " << sigEvents << " make the cut" << std::endl;
    // TString percLabel = TString::Format("%.2f%% of events with gen #tau#tau", percentage);  // X% of original events
    // leg->AddEntry((TObject*)0, percLabel, "");
  }

  if (showBackground) {
    leg->AddEntry(Fake, bkgLabel, "l");
    // Also show the yield as int
    // std::string bkgYieldLabel = "No. of events: " + std::to_string((int) bkgYield);
    // leg->AddEntry((TObject*)0, bkgYieldLabel.c_str(), "");

  } 



  applyLegStyle(leg);

  leg->Draw();
 
  Tcan->cd();

  //TPad* pad2 = new TPad("pad2","The lower pad",0,0,0.98,0.25);
  //applyPadStyle(pad2);
  //pad2->cd();
  //pad2->SetGrid(0,0); 
 
  //ratio->Draw("p");

 
  Tcan->cd();
  // Tcan->SetLogy();
  Tcan->SaveAs(outputDirectory+name+".pdf");
  // Tcan->SaveAs(outputDirectory+name+".png");
 
  delete Tcan;

  return sigEvents;

}

#endif
