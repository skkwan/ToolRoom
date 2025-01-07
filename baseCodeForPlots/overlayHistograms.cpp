/*******************************************************************/
/* plotRates.cpp                                                   */
/* Author: Stephanie Kwan                                          */
/*******************************************************************/

#include "TGraphAsymmErrors.h"
#include "TH1.h"
#include "TH1F.h"

#include "TAxis.h"
#include "TChain.h"

#include "THStack.h"
#include "TLegend.h"
#include "TPad.h"
#include "TPaveText.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TTree.h"

#include <assert.h>
#include <cmath>
#include <iostream>
#include <math.h>
#include <string>
#include <TMath.h>
#include <vector>

#include "../baseCodeForPlots/tdrstyle.C"

#ifndef OVERLAY_HISTOGRAMS_CPP_INCL
#define OVERLAY_HISTOGRAMS_CPP_INCL

/*******************************************************************/

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

/*******************************************************************/

void plotNHistograms(std::vector<TH1F*> hists, 
                std::vector<TString> labels,
                std::vector<int> colors,
                TString legendName,
                TString xAxisLabel,
                TString outputName,
                TString outputDir,
                bool useLogy
                ) {
    assert((hists.size() == labels.size()) && (hists.size() == colors.size()));

    setTDRStyle();
    TCanvas* Tcan = new TCanvas("Tcan","", 100, 20, 1000, 1000);
    //  TLegend* leg = new TLegend(0.55,0.15,0.90,0.45); // bottom right corner
    TLegend* leg = new TLegend(0.40,0.65,0.90,0.95);
    applyLegStyle(leg);

    Tcan->SetGrid();

    TLatex *latex = new TLatex(); 
    latex->SetNDC();
    latex->SetTextFont(42);
    latex->SetTextColor(kBlack);

    Tcan->cd();     /* Set current canvas */
    Tcan->SetFillColor(0);

    if (useLogy) gPad->SetLogy();


    // Make canvas larger so y-axis label won't run off the side
    Tcan->SetLeftMargin(0.18);
    Tcan->SetTopMargin(0.05);

    std::vector<TH1F*>::iterator itHist;
    std::vector<TString>::iterator itLabel;
    std::vector<int>::iterator itColor;
    
    float maximumVal = 0.0;
    
    // Get the maximum value 
    for (itHist = hists.begin(); itHist != hists.end(); itHist++) {
        if ((*itHist)->GetMaximum() > maximumVal) {
            maximumVal = (*itHist)->GetMaximum();
        }
    }

    TH1F* histDummy;
    for (itHist = hists.begin(), itLabel = labels.begin(), itColor = colors.begin();
        itHist != hists.end();
        itHist++, itLabel++, itColor++)
        {
        if (itHist == hists.begin()) // only do this once 
        {
            histDummy = new TH1F(**itHist);
        }
        
        // De-reference the iterator to get the TH1F*
        (*itHist)->SetMarkerColor(0);
        (*itHist)->SetLineWidth(2);
        (*itHist)->SetLineColor(*itColor);
        }
    histDummy->Draw("HIST");

    for (itHist = hists.begin(); itHist != hists.end(); itHist++) {
        (*itHist)->Draw("HIST SAME");
    }


    // histDummy->GetXaxis()->SetRangeUser(xMin, xMax);
    histDummy->GetYaxis()->SetRangeUser(0, maximumVal * 1.4);
    histDummy->GetXaxis()->SetTitle(xAxisLabel);
    histDummy->GetYaxis()->SetTitle("Yield");
    histDummy->GetXaxis()->SetTitleSize(0.05); // default is 0.03                                                                    
    histDummy->GetYaxis()->SetTitleSize(0.05); // default is 0.03 

    /* Customize legend */
    leg->SetHeader("#scale[0.6]{" + legendName + "}"); 
    for (itHist = hists.begin(), itLabel = labels.begin();
        itHist != hists.end();
        itHist++, itLabel++) {
        leg->AddEntry(*itHist,"#scale[0.6]{" + *itLabel + "}", "l");
    }
    leg->Draw();



    latex->DrawLatex(0.18, 0.96, "#scale[1.0]{#bf{CMS}} #it{Preliminary}");

    float commentaryXpos = 0.41;
    // latex->DrawLatex(commentaryXpos, 0.9, "#scale[0.7]{Phase-2 L1EG (Crystal, Barrel)}");

    Tcan->Update();


    Tcan->cd();
    Tcan->SaveAs(outputDir+outputName+".pdf");
    Tcan->SaveAs(outputDir+outputName+".png");

}
             

/*******************************************************************/

#endif