/**********************************************************/
// ranges.h
/**********************************************************/

#ifndef RANGES_H_INCL
#define RANGES_H_INCL

#include <map>
#include <string>
#include <vector>

typedef std::map<std::string, std::vector<float>> ranges_t;

/**********************************************************/

const int default_nbins = 40;

// for these variables, control region and inclusive plots will have a different range than the signal region ones. The control region ranges
// are specified with _control_region
std::vector<std::string> varsWithSpecialRanges = {"pt_1", "pt_2", "mt2", "mt2_lb", "zeromass_mt2", "mt2_crz",
                                                  "bpt_ak4_1", "bpt_ak4_2",
                                                  "bmass_ak4_1", "bmass_ak4_2", "bmass_ak8_1",
                                                  "m_ll", "pt_ll", "m_bb"};
std::vector<std::string> varsWithHyperSpecificRanges = {"m_ll", "pt_ll", "m_bb"};
std::vector<std::string> categoriesWithHyperSpecificRanges = {"CRZ", "CRTT", "CRA", "minimal", "baselineSR", "SR_mll_MET_fit_scheme", "SR_mbb_MET_fit_scheme"};

ranges_t ranges {

    {"pt_1", {default_nbins, 0, 200}},
    {"pt_1_control_region", {default_nbins, 0, 200}},
    {"pt_2", {default_nbins, 0, 120}},
    {"pt_2_control_region", {default_nbins, 0, 200}},
    {"eta_1", {default_nbins, -3, 3}},
    {"eta_2", {default_nbins, -3, 3}},
    {"phi_1", {default_nbins, -3.14, 3.14}},
    {"phi_2", {default_nbins, -3.14, 3.14}},
    {"m_1", {default_nbins, 0, 2.0}},
    {"m_2", {default_nbins, 0, 2.0}},

    {"m_ll", {60, 60, 120}}, // 60-180 spans 120 GeV, in bins of (120/60) = 2 GeV
    {"m_ll_control_region", {default_nbins, 40, 440}},
    {"m_ll_minimal", {default_nbins, 40, 440}},
    {"m_ll_baselineSR", {60, 60, 120}}, // 60 GeV in bins of 1 GeV
    {"m_ll_CRZ", {default_nbins, 60, 140}}, // 80 GeV in bins of 2 GeV
    {"m_ll_CRTT", {default_nbins, 40, 440}},  // 400 GeV in bins of 10 GeV
    {"m_ll_CRA", {default_nbins, 60, 140}}, // same as CRZ and SR bins
    {"m_ll_SR_mll_MET_fit_scheme", {60, 60., 120.}}, // If fitting to m_ll, show m_ll sidebands: 1 GeV bins
    {"m_ll_SR_mbb_MET_fit_scheme", {60, 60., 120.}}, // If fitting to m_bb, cut tighter on m_ll: 87 to 95 GeV spans 12 GeV, 1 GeV bin width

    {"pt_ll", {default_nbins, 0, 200}},
    {"pt_ll_baselineSR", {default_nbins, 0, 200}},
    {"pt_ll_control_region", {default_nbins, 0, 200}},
    {"pt_ll_CRZ", {default_nbins, 0, 800}},
    {"pt_ll_CRTT", {default_nbins, 0, 800}},

    {"eta_ll", {default_nbins, -3, 3}},
    {"phi_ll", {default_nbins, -3.14, 3.14}},

    {"deltaPhi_between_ll", {default_nbins, 0, 3.14}},
    {"abs_deltaEta_between_ll", {default_nbins, 0, 3}},

    {"nJets", {7, 0.5, 7.5}},
    {"nFatJets", {5, 0.5, 5.5}},
    {"nBTagJets", {6, -0.5, 5.5}},
    {"nBTagFatJets", {3, -0.5, 2.5}},
    {"bpt_ak4_1", {default_nbins, 0, 400}},
    {"bpt_ak4_1_control_region", {default_nbins, 0, 1600}},
    {"beta_ak4_1", {default_nbins, -3, 3}},
    {"bphi_ak4_1", {default_nbins, -3.14, 3.14}},
    {"bmass_ak4_1", {default_nbins, 0, 80}},
    {"bmass_ak4_1_control_region", {default_nbins, 0, 600}},
    {"btagScore_ak4_1", {default_nbins, 0, 1.5}},

    {"bpt_ak4_2", {default_nbins, 0, 400}},
    {"bpt_ak4_2_control_region", {default_nbins, 0, 1620}},
    {"beta_ak4_2", {default_nbins, -3, 3}},
    {"bphi_ak4_2", {default_nbins, -3.14, 3.14}},
    {"bmass_ak4_2", {default_nbins, 0, 80}},
    {"bmass_ak4_2_control_region", {default_nbins, 0, 600}},
    {"btagScore_ak4_2", {default_nbins, 0, 1.5}},

    // {"bpt_ak4_3",{default_nbins, 20, 1620}},
    // {"beta_ak4_3", {default_nbins, -3, 3}},
    // {"bphi_ak4_3", {default_nbins, -3.14, 3.14}},
    // {"bmass_ak4_3", {default_nbins, 0, 600}},
    // {"btagScore_ak4_3", {default_nbins, 0, 1}},

    {"m_bb", {60, 60., 180.}},  // 60 + 60*2 = 180
    {"m_bb_minimal", {60., 60., 360.}},
    {"m_bb_control_region", {60, 60., 200.}}, // 50 GeV per bin
    {"m_bb_SR_mll_MET_fit_scheme", {25, 60., 185.}}, // 60 + 25*5 = 185
    {"m_bb_SR_mbb_MET_fit_scheme", {25, 60., 185.}}, // 60 + 25*5 = 185

    {"pt_bb", {default_nbins, 0, 1200}},

    {"bpt_ak8_1",{default_nbins, 100, 2100}},
    {"beta_ak8_1", {default_nbins, -3, 3}},
    {"bphi_ak8_1", {default_nbins, -3.14, 3.14}},
    {"bmass_ak8_1", {default_nbins, 0, 800}},
    {"bmass_ak8_1_control_region", {default_nbins, 0, 800}},
    {"btagScore_ak8_1", {default_nbins, 0, 1.5}},

    // {"bpt_ak8_2",{default_nbins, 100, 2100}},
    // {"beta_ak8_2", {default_nbins, -3, 3}},
    // {"bphi_ak8_2", {default_nbins, -3.14, 3.14}},
    // {"bmass_ak8_2", {default_nbins, 0, 500}},
    // {"btagScore_ak8_2", {default_nbins, 0, 1.5}},

    // {"bpt_ak8_3",{default_nbins, 100, 2100}},
    // {"beta_ak8_3", {default_nbins, -3, 3}},
    // {"bphi_ak8_3", {default_nbins, -3.14, 3.14}},
    // {"bmass_ak8_3", {default_nbins, 0, 500}},
    // {"btagScore_ak8_3", {default_nbins, 0, 1.5}},

    {"met",    {60, 50, 650}}, // bins of 10 GeV each
    {"metphi", {default_nbins, -3.14, 3.14}},
    {"recoHT", {default_nbins, 0, 800}},

    {"mt2_lb", {default_nbins, 0, 200}},
    {"mt2_lb_control_region", {default_nbins, 0, 200}},
    {"mt2", {default_nbins, 0, 400}},
    {"mt2_control_region", {default_nbins, 40, 440}},
    {"zeromass_mt2", {default_nbins, 0, 400}},
    {"zeromass_mt2_control_region", {default_nbins, 0, 200}},
    {"mt2_crz", {default_nbins, 0, 200}},
    {"mt2_crz_control_region", {default_nbins, 0, 200}},

    {"m_jj", {default_nbins, 0, 400}},
    {"pt_jj", {default_nbins, 0, 400}},


};


#endif
