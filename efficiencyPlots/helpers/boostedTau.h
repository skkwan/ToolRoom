#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"

#ifndef BOOSTEDTAU_H
#define BOOSTEDTAU_H

using namespace ROOT::VecOps;

/**********************************************************/

// Returns whether the jet (with l1Matched_1 index i) passes the eta/phi bit patterns
// (numerator compiled cut).
int passNumCompiledCut(int genId, int genMother,
		       double genDR, double l1Pt, double l1Eta, double recoPt,
		       RVec<string>& regionEta,
		       RVec<string>& regionPhi,
		       int i) {
  
  return ((genId == 25 || genMother == 25) && genDR < 0.4) &&
    abs(l1Eta) < 2.5 &&
    (recoPt >= 200) &&
    (regionEta[i] == "010" || regionPhi[i] == "010" ||
     regionEta[i] == "110" || regionEta[i] == "011" ||
     regionPhi[i] == "110" || regionPhi[i] == "011");
  
  // TEMP: test if gen cuts are the reason why eff's don't peak at 100%
  /* return abs(l1Eta) < 2.5 && (recoPt >= 200) && */
  /*   (regionEta[i] == "010" || regionPhi[i] == "010" || */
  /*    regionEta[i] == "110" || regionEta[i] == "011" || */
  /*    regionPhi[i] == "110" || regionPhi[i] == "011"); */
  
}

/**********************************************************/

// Returns whether the jet (with l1Matched_1 index i) passes the denominator cut.
int passDenomCut(double recoPt) {
  
  return (recoPt >= 200);
}

/**********************************************************/

// This must be at the bottom of every .h: the two branches
// passNumCompiledCut AND passDenomCut must be well-defined

// Returns a new dataframe with passNumCompiledCut and passDenomCut

template <typename T>
auto GetNumDenom(T &df) {
  using namespace ROOT::VecOps;

  std::cout << ">>> Using helpers/boostedTau.h... " << std::endl;
  
  auto df2 = df.Define("passNumCompiledCut", passNumCompiledCut, {"genId", "genMother", "genDR",
	"l1Pt_1", "l1Eta_1", "recoPt_1",
	"regionEta", "regionPhi", "l1Matched_1"})
    .Define("passDenomCut", passDenomCut, {"recoPt_1"});

  return df2;
}

/**********************************************************/

#endif
