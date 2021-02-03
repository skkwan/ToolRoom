/*******************************************************************/
/* makeEfficienciesPlot.cpp                                        */
/* ROOT macro                                                      */
/* Usage: root -l -b -q makeEfficienciesPlot.cpp                   */
/*******************************************************************/

#include "efficiencyHist.cpp"
#include "calculateEfficiency.cpp"

#include <string>
/*********************************************************************/

/* Plots L1 tau efficiency for different BDT discriminant working
   points. */

void makeEfficienciesPlot(void)
{
  gROOT->ProcessLine(".L calculateEfficiency.cpp");

  /* Load the TTree. */
  TString treePath = "l1NtupleProducer/efficiencyTree";
  //  TString rootFileDirectory = "../test/analyzer.root";
  TString rootFileDirectory = "/afs/cern.ch/work/s/skkwan/public/tauBoostedTrigger/CMSSW_10_6_20/src/L1Trigger/Run3Ntuplizer/test/l1TNtuple-ggHtautau.root";
  TString outputDirectory = "/eos/user/s/skkwan/boostedTauTrigger/efficiencyPlots/2021_Feb_3/";
  gSystem->Exec("mkdir -p " + outputDirectory);
  float xMin, xMax;
  int nCurves;

  /*******************************************************/
  /* efficiency as a function of recoPt                  */
  /*******************************************************/
  xMin = 200;
  xMax = 500;
  std::vector<TGraphAsymmErrors*> vGraphs;
  std::vector<std::string> vLabels = {"L1 p_{T} > 100 GeV", 
				      "L1 p_{T} > 200 GeV",    
				      "L1 p_{T} > 300 GeV",
				      "L1 p_{T} > 400 GeV"};
  std::vector<int> vColors = {kBlue-3, kViolet-5,
			      kPink+6, kAzure+1};

  for (std::string l1PtCut : {"100", "200", "300", "400"}) {
    
    TGraphAsymmErrors* eff = calculateEfficiency("recoPt_1", treePath, rootFileDirectory,
						 xMin, xMax, false,
						 "1.2 * l1Pt_1 > " + l1PtCut);
    vGraphs.push_back(eff);

  }

  // Send the vectors to a plotting function
  plotNEfficiencies(vGraphs, vLabels, vColors,
		    "Jet reco p_{T} [GeV]",
		    "ggHtautau",                                                                
		    "eff_jet_recoPt",        
		    outputDirectory);    
  
  // Don't forget to clear the vectors if adding another set of graphs

}
/*********************************************************************/
