
int plotTH2Ds(void) {

    TString thisHLTPath = "HLTMu8Ele23";
    // TString thisHLTPath = "HLTMu23Ele12";
    TString path = "out_HLT_" + thisHLTPath + ".root";

    TFile *newFile = new TFile(path);
    if (!newFile->IsOpen() || newFile==0 ) {
        std::cout<<"ERROR: FILE "<< path <<" NOT FOUND; EXITING" << std::endl;
        return 0;
    }
    TH2F* newSF_ele = (TH2F*) newFile->Get("electron_SF2D");
    if (newSF_ele == 0) {
        std::cout << "ERROR: electron_SF2D not found in file; EXITING" << std::endl;
        return 0;
    }
    TH2F* oldSF_ele = (TH2F*) newFile->Get("old_electron_SF2D");
    if (oldSF_ele == 0) {
        std::cout << "ERROR: old_electron_SF2D not found in file; EXITING" << std::endl;
        return 0;
    }
    newSF_ele->SetMaximum(2.0);
    oldSF_ele->SetMaximum(2.0);
    newSF_ele->SetMinimum(0.0);
    oldSF_ele->SetMinimum(0.0);

    // Get the muons
    TH2F* newSF_muon = (TH2F*) newFile->Get("muon_SF2D");
    if (newSF_muon == 0) {
        std::cout << "ERROR: muon_SF2D;1 not found in file; EXITING" << std::endl;
        return 0;
    }

    TH2F* oldSF_muon = (TH2F*) newFile->Get("old_muon_SF2D");
    if (oldSF_muon == 0) {
        std::cout << "ERROR: old_muon_SF2D not found in file; EXITING" << std::endl;
        return 0;
    }
    newSF_muon->SetMaximum(2.0);
    oldSF_muon->SetMaximum(2.0);
    newSF_muon->SetMinimum(0.0);
    oldSF_muon->SetMinimum(0.0);

    TCanvas* c1 = new TCanvas("Tcan","", 100, 20, 1000, 800);
    TLegend* leg = new TLegend(0.60,0.75,0.85,0.9);

    // Draw the electrons
    newSF_ele->SetTitle("UL electron SF");
    newSF_ele->Draw("");
    newSF_ele->Draw("TEXT45 SAME");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/electron_HLT_" + thisHLTPath + "_UL.pdf");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/electron_HLT_" + thisHLTPath + "_UL.png");

    oldSF_ele->SetTitle("Pre-UL electron SF");
    oldSF_ele->Draw("");
    oldSF_ele->Draw("TEXT45 SAME");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/electron_HLT_" + thisHLTPath + "_preUL.pdf");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/electron_HLT_" + thisHLTPath + "_preUL.png");

    // Draw the muons
    newSF_muon->SetTitle("UL muon SF");
    newSF_muon->Draw("");
    newSF_muon->Draw("TEXT45 SAME");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/muon_HLT_" + thisHLTPath + "_UL.pdf");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/muon_HLT_" + thisHLTPath + "_UL.png");

    oldSF_muon->SetTitle("Pre-UL muon SF");
    oldSF_muon->Draw("");
    oldSF_muon->Draw("TEXT45 SAME");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/muon_HLT_" + thisHLTPath + "_preUL.pdf");
    c1->SaveAs("/eos/user/s/skkwan/www/sfComparisons/muon_HLT_" + thisHLTPath + "_preUL.png");

    return 1;
}