
#include "ROOT/RDataFrame.hxx"

int addFriend() {

    std::string sampleDir_="davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_mt2018_svfitted/VBFHToTauTau_Skim_svfitted.root";
    std::string dnnDir_="davs://cmsxrootd.hep.wisc.edu:1094/store/user/skkwan/haabbtt_neural_network/mt18_outputs_store/VBFHToTauTau_Skim_svfitted.root";
    TFile *fInput = TFile::Open(sampleDir_.c_str());
    TFile *fDNN   = TFile::Open(dnnDir_.c_str());

    TTree *tMain = (TTree*)fInput->Get("mutau_tree");
    TTree *tDNN = (TTree*)fDNN->Get("mutau_tree_NN");

    tMain->AddFriend(tDNN, "dnn");

    if (tMain == 0 || tDNN == 0) {
        std::cerr << "[ERROR!] Tree not found" << std::endl;
        return 1;
    }

    ROOT::RDataFrame df(*tMain);
    auto df2 = df.Filter("NN1b>0");
    df2.Snapshot("mutau_tree_slimmed", "out.root", {"m_sv", "NN1b"});

    auto cutReport = df2.Report();
    cutReport->Print();


    return 0;

}