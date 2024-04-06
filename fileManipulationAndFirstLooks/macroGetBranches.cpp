#include <stdlib.h>
#include <iostream>
#include <cmath>


int macroGetBranches(TString file) {
    TFile *fInput = TFile::Open(file.Data());
    TTree *t = (TTree*)fInput->Get("Events");
    t->Print("all");
    return 0;
}