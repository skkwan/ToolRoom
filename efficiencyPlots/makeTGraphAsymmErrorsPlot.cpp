/*******************************************************************/
/* makeTGraphAsymmErrorsPlot.cpp                                   */
/* ROOT macro                                                      */
/* Usage: root -l -b -q makeTGraphAsymmErrorsPlot.cpp              */
/*******************************************************************/

#include "../baseCodeForPlots/CMS_lumi.h"
#include "../baseCodeForPlots/tdrstyle.C"
#include "../baseCodeForPlots/comparisonPlots.C"

#include <string>


/*******************************************************************/

void plotTGraphAsymmErrors(std::vector<TGraphAsymmErrors*> graphs, 
			   std::vector<TString> labels,
			   std::vector<int> colors,
			   TString xAxisLabel,
			   TString yAxisLabel,
			   TString legendName,
			   TString outputName,
			   TString outputDir
		       )
{
  assert((graphs.size() == labels.size()) && (graphs.size() == colors.size()));

  setTDRStyle();
  TCanvas* Tcan = new TCanvas("Tcan","", 100, 20, 1000, 800);
  TLegend* leg = new TLegend(0.50,0.50,0.95,0.90);

  Tcan->SetGrid();

  Tcan->cd();     /* Set current canvas */
  Tcan->SetFillColor(0);
  applyLegStyle(leg);

  
  gStyle->SetOptFit(0);
  std::vector<TGraphAsymmErrors*>::iterator itGraph;
  std::vector<TString>::iterator itLabel;
  std::vector<int>::iterator itColor;
  
  TGraphAsymmErrors* histDummy;
  for (itGraph = graphs.begin(), itLabel = labels.begin(), itColor = colors.begin();
       itGraph != graphs.end();
       itGraph++, itLabel++, itColor++)
    {
      if (itGraph == graphs.begin()) // only do this once 
	{
	  histDummy = new TGraphAsymmErrors(**itGraph);
	}
      
      // De-reference the iterator to get the TGraphAsymmErrors*
      (*itGraph)->SetMarkerColor(*itColor);
      (*itGraph)->SetMarkerStyle(kFullCircle);
      (*itGraph)->SetLineWidth(2);
      (*itGraph)->SetLineColor(*itColor);
      (*itGraph)->SetMarkerSize(2);
    }

  histDummy->SetMarkerColor(0);
  histDummy->SetLineColor(0);

  histDummy->Draw("");

  for (itGraph = graphs.begin(); itGraph != graphs.end(); itGraph++)
    {
      (*itGraph)->Draw("P");
    }

  histDummy->GetXaxis()->SetTitle(xAxisLabel);
  histDummy->GetYaxis()->SetTitle(yAxisLabel);
  histDummy->GetXaxis()->SetTitleSize(0.06); // default is 0.03                                                                    
  histDummy->GetYaxis()->SetTitleSize(0.06); // default is 0.03
  /* Set y-axis limits */
  histDummy->GetYaxis()->SetRangeUser(0.0, 1.1);

  /* Customize legend */
  for (itGraph = graphs.begin(), itLabel = labels.begin();
       itGraph != graphs.end();
       itGraph++, itLabel++)
    {
      leg->AddEntry(*itGraph, *itLabel,  "P");
    }
  // Set legend title
  leg->SetHeader(legendName);
  gStyle->SetLegendFont(30);

  leg->Draw();

  Tcan->cd();
  Tcan->SaveAs(outputDir+outputName+".pdf");
  Tcan->SaveAs(outputDir+outputName+".png");
}

/*********************************************************************/

/* Plots L1 tau efficiency for different BDT discriminant working
   points. */

void makeTGraphAsymmErrorsPlot(void)
{
  gROOT->ProcessLine(".L calculateEfficiency.cpp");

  /* Load the TTree. */
  //TString treePath = "l1NtupleProducer/Stage2/efficiencyTree";
  TString treePath = "";
  //  TString rootFileDirectory = "../test/analyzer.root";
  TString rootFileDirectory = "/eos/user/s/skkwan/hToAA/tauFRfromCecile/FitHistograms_tauFR_2018.root";
  TString outputDirectory = "/eos/user/s/skkwan/hToAA/tauFRfromCecile/plots/";

  TFile f(rootFileDirectory);

  std::vector<TGraphAsymmErrors*> vGraphs;
  std::vector<TString> vLabels;
  std::vector<int> vColors;

  /*******************************************************/
  /* Fake rate f as a function of pT: DM 0               */
  /*******************************************************/
  
  // Load the TGraphAsymmErrors
  TGraphAsymmErrors *temp;

  f.GetObject("hpt_dm0_deeploose_hpt_dm0_deepveryveryveryloose", temp);
  TGraphAsymmErrors* dm0_loose = (TGraphAsymmErrors*)temp->Clone(0);
  vGraphs.push_back(dm0_loose);
  vLabels.push_back("Loose/VVVLoose");
  vColors.push_back(kAzure+1);

  f.GetObject("hpt_dm0_deepmedium_hpt_dm0_deepveryveryveryloose", temp);
  TGraphAsymmErrors* dm0_medium = (TGraphAsymmErrors*)temp->Clone(0);
  vGraphs.push_back(dm0_medium);
  vLabels.push_back("Medium/VVVLoose");
  vColors.push_back(kPink+6);
  
  f.GetObject("hpt_dm0_deeptight_hpt_dm0_deepveryveryveryloose", temp);
  TGraphAsymmErrors* dm0_tight = (TGraphAsymmErrors*)temp->Clone(0);
  vGraphs.push_back(dm0_tight);
  vLabels.push_back("Tight/VVVLoose");
  vColors.push_back(kViolet-5);

  f.GetObject("hpt_dm0_deepverytight_hpt_dm0_deepveryveryveryloose", temp);
  TGraphAsymmErrors* dm0_vtight = (TGraphAsymmErrors*)temp->Clone(0);
  vGraphs.push_back(dm0_vtight);
  vLabels.push_back("VTight/VVVLoose");
  vColors.push_back(kBlue-3);

  plotTGraphAsymmErrors(vGraphs, vLabels, vColors,
  			"Reco #tau_{H} p_{T} [GeV]",
  			"Fake rate f",
  			"Tau Fake Rate 2018 DM0",        
  			"dm0_tauFR_2018",        
  			outputDirectory);    
   vGraphs.clear();  vLabels.clear();  vColors.clear();
}
/*********************************************************************/
