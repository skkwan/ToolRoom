#include "TFile.h"
#include "TH1F.h"
#include "TTreeReader.h"
#include "TTreeReaderValue.h"

void printRunLumiEventFromTTree() {
    
   // Create a histogram for the values we read.
   auto myHist = new TH1F("h1","ntuple",100,-4,4);
   // Open the file containing the tree.
   auto myFile = TFile::Open("/eos/user/s/skkwan/hToAA/skims/Aug-17-2023-02h47m/VBFHToTauTau-pre-UL-mini_Skim.root");
   if (!myFile || myFile->IsZombie()) {
      return;
   }
   // Create a TTreeReader for the tree, for instance by passing the
   // TTree's name and the TDirectory / TFile it is in.
   TTreeReader myReader("event_tree", myFile);

   TTreeReaderValue<unsigned int> myRun(myReader, "run");
   TTreeReaderValue<unsigned int> myLumi(myReader, "lumi");
   TTreeReaderValue<unsigned int> myEvent(myReader, "evt");
   TTreeReaderValue<int> myChannel(myReader, "channel");

    ofstream myfile;
    myfile.open("/eos/user/s/skkwan/hToAA/comparisonWithAnagha/VBFHToTauTau_2018_mini.txt");

   // TTreeReaderValue<unsigne int > my(myReader, "py");
   // Loop over all entries of the TTree or TChain.
   while (myReader.Next()) {
      if (*myChannel == 0) {
         std::cout << *myChannel << std::endl;
         myfile << *myRun << ":" << *myLumi << ":" << *myEvent << "\n";
      }
   }
   myfile.close();
   // myHist->Draw();
}
