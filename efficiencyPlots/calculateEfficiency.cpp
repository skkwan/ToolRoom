/*******************************************************************/
/* calculateEfficiency.cpp                                         */
/* Helper function                                                 */
/* Author: Stephanie Kwan                                          */
/*******************************************************************/

#include "../baseCodeForPlots/CMS_lumi.h"
#include "../baseCodeForPlots/tdrstyle.C"

#include "efficiencyHist.cpp"

#include "TAxis.h"
#include "TChain.h"
#include "TF1.h"
#include "TFile.h"
#include "TGaxis.h"
#include "TGraphAsymmErrors.h"
#include "TH1.h"
#include "TH1F.h"

#include "THStack.h"
#include "TLegend.h"
#include "TPad.h"
#include "TPaveText.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TTree.h"

#include <cmath>
#include <iostream>
#include <math.h>
#include <string>
#include <TMath.h>
#include <vector>

#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "helpers/boostedTau.h"
#include "helpers/RDataFrameFunctions.h"

#ifndef CALCULATE_EFFICIENCY_CPP_INCL
#define CALCULATE_EFFICIENCY_CPP_INCL

/*******************************************************************/

/* Helper function declarations */

void setMaxErrorTo1(TGraphAsymmErrors *graph);

/*******************************************************************/

/* Calculates and returns the efficiency and statistical uncertainty
   for variable, using the n-tuple specified by rootFileDirectory
   and treePath.

   ** n.b.: The exact cut applied depends on the helper file included above! 
      The helper file must contain a function GetNumDenom which Defines 
      passNumCut and passDenomCut ** 
      An optional argument numExtraCut can be passed, which is helpful when
      the efficiency plot has multiple curves where we tweak something in the
      numerator.
   
   Returns a TGraphAsymmErrors with x-axis range [low, high]).
   If variableBin = true, uses the bins specified in the function.
*/
   
TGraphAsymmErrors* calculateEfficiency(TString variable,
				       TString treePath, TString rootFileDirectory,
				       double low,
				       double high,
				       bool variableBin = false,
				       std::string numExtraCut = "")
{
  // Check if file/tree exists (also loads it, but later we use RDataFrame)
  TFile *file = new TFile(rootFileDirectory);
  if (!file->IsOpen() || file==0 )
    {
      std::cout<<"ERROR: FILE "<< rootFileDirectory <<" NOT FOUND; EXITING"<<std::endl;
      return NULL;
    }

  TTree* tree = (TTree*)file->Get(treePath);
  if (tree == 0)
    {
      std::cout<<"ERROR: Tree is "<< tree<<" NOT FOUND; EXITING"<<std::endl;
      return NULL;
    }

  // Load file into RDataFrame
  ROOT::RDataFrame dfBase((std::string) treePath, (std::string) rootFileDirectory);

  
  auto df = GetNumDenom(dfBase);

  auto dfNum   = df.Filter("passNumCompiledCut > 0", "Pass numerator cut (compiled component ONLY)");
  auto dfDenom = df.Filter("passDenomCut > 0", "Pass denominator cut");

  // If there was an extra num cut, add an extra filter and update dfNumFinal
  auto dfNumFinal = applyExtraCut(dfNum, numExtraCut, "Pass extra numerator cut " + numExtraCut);
  
  // Print cutflow reports
  auto reportNum = dfNumFinal.Report();
  auto reportDenom = dfDenom.Report();
  reportNum->Print();
  reportDenom->Print();
  
  // Initialize histograms and bins
  ROOT::RDF::RResultPtr<TH1D> denom, num;
  int bins = 10;
  // Float_t xbins[10] = {0, 5, 10, 20, 25, 30, 50, 70, 100, 200};
  Float_t xbins[11] = {20, 25, 30, 35, 40, 45, 50, 60, 70, 90, 110};
  int nVarBins = (int) sizeof(xbins)/sizeof(xbins[0]) - 1;
  std::string var = (std::string) variable;

  // Fill the histograms
  if(variableBin)
    {
      num   = dfNumFinal.Histo1D({"num", "num", nVarBins, xbins}, var);
      denom = dfDenom.Histo1D({"denom", "denom", nVarBins, xbins}, var);
    }
  else
    {
      num   = dfNumFinal.Histo1D({"num", "num", bins, low, high}, var);
      denom = dfDenom.Histo1D({"denom", "denom", bins, low, high}, var);
    }
  
  num->Sumw2();
  denom->Sumw2();

  num.GetPtr()->Divide(denom.GetPtr());

  // Check:
  printf("Printing first ten bin contents (before restricting max/min to 1.0 and 0.0)\n");
  for (int i = 0; i < 10; i++)
    {
      printf("num bin %d content is %f, with error %f\n", i,
	     num->GetBinContent(i),
             num->GetBinError(i));

    }

  // Efficiencies cannot be less than 0 or greater than 1
  TGraphAsymmErrors* effAsym = new TGraphAsymmErrors(num.GetPtr());
  setMaxErrorTo1(effAsym);

  return effAsym;
}

/*******************************************************************/

/* Sets the maximum and minimum error of graph to be 1.0 and 0.0 
   respectively. */

void setMaxErrorTo1(TGraphAsymmErrors *graph)
{
  for (int i = 0; i < graph->GetN(); i++)
    {
      Double_t errorY = graph->GetErrorY(i);
      Double_t pointX, pointY;

      if (graph->GetPoint(i, pointX, pointY) < 0)
        printf("Error getting point\n");

      Double_t errorUp = pointY + errorY;
      Double_t errorLow = pointY - errorY;

      if (errorUp > 1)
        graph->SetPointEYhigh(i, 1 - pointY);
      else if (errorLow < 0)
        graph->SetPointEYlow(i, pointY);

    }
}



/*******************************************************************/

#endif
