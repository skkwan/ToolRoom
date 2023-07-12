

int testTChainBehavior(void) {

    TChain *ch = new TChain("Events");

    ch->Add("root://cmsxrootd.fnal.gov//store/data/Run2018B/EGamma/NANOAOD/02Apr2020-v1/40000/19F02981-E639-274D-ADF9-069A4C7ECC48.root");
    ch->Add("root://cmsxrootd.fnal.gov//store/data/Run2018B/EGamma/NANOAOD/02Apr2020-v1/240000/3878DDCD-721D-F740-B24C-534C8098B143.root");
    ch->Add("root://cmsxrootd.fnal.gov//store/data/Run2018B/EGamma/NANOAOD/02Apr2020-v1/20000/39BBAE9D-B748-8B4F-B6E8-BC4F66A5AEBC.root");

    std::string problem = "/store/data/Run2018B/EGamma/NANOAOD/02Apr2020-v1/40000/19F02981-E639-274D-ADF9-069A4C7ECC48.root";

    TObjArray* listOfFiles = ch->GetListOfFiles();
    TIter next(listOfFiles);
    TChainElement *chEl = 0;
    while ((chEl = (TChainElement*) next() )) {   
        std::string chTitle = chEl->GetTitle();
        std::cout << chTitle << std::endl;

        if (chTitle.find(problem) != std::string::npos) {
            std::cout << "problem found!" << std::endl;
        }
    }

    return 0;
}