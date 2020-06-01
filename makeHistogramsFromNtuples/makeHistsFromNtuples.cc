/*****************************************************************/
/* makeHistsFromNtuples.cc                                       */
/* Usage: To build, run ./Make.sh [path to this file]            */
/*        Then makeHistsFromNtuples.cc input.root output.root    */
/*****************************************************************/


#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <utility>
#include <map>
#include <string>
#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include "TTree.h"
#include "TChain.h"
#include "TFile.h"
#include "TMath.h"
#include "TSystem.h"
#include "TLorentzVector.h"

using namespace std;

pair<float,float> makeHistogram(string variable, string name, string cut,
                                TTree* tree, TFile *fout, string folder,
                                int bins, float min, float max, float scaleFactor);

int main(int argc, char** argv) {
  
  string in = argv[1];
  string inname = in;
  cout << "Reading input " << inname << "..." << endl;
  TFile *fIn = TFile::Open(inname.c_str());
  TTree* treePtr = (TTree*) fIn->Get("mutau_tree"); 

  string out = argv[2];
  string outname = out;
  cout << "Opening output file" << outname << "..." << endl;
  TFile *fout = TFile::Open(outname.c_str(), "RECREATE");

  cout << "Drawing histograms..." << endl;

  //CUSTOMIZE
  string folderName = "mutau_slimmed";    
  makeHistogram("pt_1",  "muPt",   "", treePtr, fout, folderName, 100, 0, 200, 1.);
  makeHistogram("eta_1", "muEta",  "", treePtr, fout, folderName, 100, -2.7, 2.7, 1.);
  makeHistogram("pt_2",  "tauPt",  "", treePtr, fout, folderName, 100, 0, 200, 1.);
  makeHistogram("eta_2", "tauEta", "", treePtr, fout, folderName, 100, -2.7, 2.7, 1.);
  
}

pair<float,float> makeHistogram(string variable, string name, string cut,
				TTree* tree, TFile *fout, string folder,
				int bins, float min, float max, float scaleFactor = 1.){

  if(fout->Get(folder.c_str())==0)
    fout->mkdir(folder.c_str());

  TH1F *h = 0;
  h = new TH1F(name.c_str(), name.c_str(), bins, min, max);

  h->Sumw2();

  tree->Draw((variable+">>"+name).c_str(), cut.c_str());

  h->Scale(scaleFactor);

  fout->cd(folder.c_str());

  Double_t error = 0.0;
  float yield = h->IntegralAndError(1, h->GetNbinsX(), error, "");
  if(yield == 0){
    h->SetBinContent(1, 0.00001);
  }
    
  h->Write(h->GetName(), TObject::kOverwrite);

  cout << name << ": " << h->Integral() << ", entries: " << h->GetEntries() <<endl;
  
  return make_pair(yield,error);
}
