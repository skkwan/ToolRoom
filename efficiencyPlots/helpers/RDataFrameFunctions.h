// RDataFrameFunctions.h

#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"

#ifndef RDATAFRAME_FUNCTIONS_H
#define RDATAFRAME_FUNCTIONS_H


/*******************************************************************/
// Returns dataframe df if extraCut is empty, otherwise apply the                                        
// cut and return the filtered dataframe (filter is called filterName).

// Useful for applying non-compile cuts to numerator dataframes.

template <typename T>
auto applyExtraCut(T &df, std::string extraCut, std::string filterName) {

  // If there is an extra cut string, filter the given dataframe                                         
  if (!extraCut.empty()) {
    std::cout << ">>> RDataFrameFunctions.h: Apply extra numerator cut to specified dataframe: "
              << extraCut << std::endl;
    auto df2 = df.Filter(extraCut, filterName);
    return df2;
  }
  else {
    std::cout << ">>> RDataFrameFunctions.h: NO additional numerator cut applied to specified dataframe" << std::endl;
    return df;
  }
}
/*******************************************************************/

#endif
