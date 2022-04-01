/*
 * Macro to print the contents of a single file.
 */

#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>

#include "TChain.h"
#include "TROOT.h"

int main(int argc, char **argv) {

  std::string input = argv[1];
  std::cout << ">>> Input: " << input << std::endl;
  
  std::cout << "[ROOT version:] " << gROOT->GetVersion() << std::endl;

  std::ifstream file;
  std::string line;
  file.open(input, std::ifstream::in);  

  std::getline(file, line);

  TChain *ch = new TChain("Events");
  TChain *chRuns = new TChain("Runs");

  const char *filename = line.c_str();
  int result = ch->Add(filename); 
  int result2 = chRuns->Add(filename);
  

  std::cout << ">>> Input " << input << " read successfully:" << line << ", results: " << result << " " << result2 << std::endl;      
  std::cout << ">>> Done" << std::endl;
  
  // TChain ch("Events");

}
