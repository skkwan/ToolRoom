int getData() {
    std::unique_ptr<TFile> file1(TFile::Open("/eos/user/s/skkwan/hToAA/condorHistogramming/2024-07-04-10h25m-iteration10-etau/histograms.root", "READ"));
    std::unique_ptr<TFile> file2(TFile::Open("/eos/user/s/skkwan/hToAA/condorHistogramming/2024-07-30-14h03m-iteration12-etau/histograms.root", "READ"));

    std::unique_ptr<TH1D> ha1(file1->Get<TH1D>("etau/inclusive/EGamma-Run2018A_m_vis"));
    std::unique_ptr<TH1D> ha2(file2->Get<TH1D>("etau/inclusive/EGamma-Run2018A_m_vis"));

    std::unique_ptr<TH1D> hb1(file1->Get<TH1D>("etau/inclusive/EGamma-Run2018B_m_vis"));
    std::unique_ptr<TH1D> hb2(file2->Get<TH1D>("etau/inclusive/EGamma-Run2018B_m_vis"));

    std::unique_ptr<TH1D> hc1(file1->Get<TH1D>("etau/inclusive/EGamma-Run2018C_m_vis"));
    std::unique_ptr<TH1D> hc2(file2->Get<TH1D>("etau/inclusive/EGamma-Run2018C_m_vis"));

    std::unique_ptr<TH1D> hd1(file1->Get<TH1D>("etau/inclusive/EGamma-Run2018D_m_vis"));
    std::unique_ptr<TH1D> hd2(file2->Get<TH1D>("etau/inclusive/EGamma-Run2018D_m_vis"));
    std::cout <<  ha1->Integral() << ", " << ha2->Integral() << std::endl;
    std::cout <<  hb1->Integral() << ", " << hb2->Integral() << std::endl;
    std::cout <<  hc1->Integral() << ", " << hc2->Integral() << std::endl;
    std::cout <<  hd1->Integral() << ", " << hd2->Integral() << std::endl;

    std::cout << "First total: " <<  ha1->Integral() + hb1->Integral() + hc1->Integral() + hd1->Integral()  << std::endl;
    std::cout << "Second total: " <<  ha2->Integral() + hb2->Integral() + hc2->Integral() + hd2->Integral()  << std::endl;


    std::unique_ptr<TFile> f1(TFile::Open("/eos/user/s/skkwan/hToAA/condorHistogramming/2024-07-04-10h25m-iteration10-etau/out_etau.root", "READ"));
    std::unique_ptr<TFile> f2(TFile::Open("/eos/user/s/skkwan/hToAA/condorHistogramming/2024-07-30-14h03m-iteration12-etau/out_etau.root", "READ"));

    std::unique_ptr<TH1D> d1(f1->Get<TH1D>("inclusive/data_obs_m_vis"));
    std::unique_ptr<TH1D> d2(f2->Get<TH1D>("inclusive/data_obs_m_vis"));
    std::cout <<  d1->Integral() << ", " << d2->Integral() << std::endl;
    return 0;
}