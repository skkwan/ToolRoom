
#include "../baseCodeForPlots/plotTH1F.cpp"

// inputName :  the name of the TH1F inside the file (usually the name of the variable).
// xLabel   :  the x-axis label on the plot.
// paveText :  text to go in a TPave box. 
// isAU     : if True, normalize the plot so the area under the curve is 1, and set y-axis title to "A.U.".
//            if False, do not normalize and set y-axis title to "Counts".
// histFolder :  the folder the TH1F is in
// inputDirectory : the path to the ROOT file (~/myRepo/input.root).
// outputDirectory: the directory where the output plots will be saved.
// useLogy:  if True, use log y-axis.

int plotTH1F(void) {
    plotTH1F("m_dimuon", "m(#mu#mu)", "Double Muon", false, "/afs/cern.ch/work/s/skkwan/public/higgsino/higgsino-plotting/rdf-solution/histograms/hists_DoubleMuon_skimmed.root", "/eos/user/s/skkwan/www/higgsino/skim-test/", false);

}