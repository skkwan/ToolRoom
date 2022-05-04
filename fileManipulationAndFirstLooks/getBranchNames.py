###########################################################################################
# getBranchNames.py                                      
#
# Stand-alone to print branch names of n-tuple to a text file.
#
# Usage: python3 getBranchNames.py <path to ntuple> <path to tree> <output text file name>
# E.g.: python3 getBranchNames.py /afs/cern.ch/user/s/skkwan/tree_1.root Events list.txt
###########################################################################################

import argparse
import ROOT as r


# Main function
def main(filepath, treepath, output):
    print(">>> Accessing {} in file {}, writing to {}".format(treepath, filepath, output))
    infile = r.TFile.Open(filepath)
    tree = infile.Get(treepath)

    # Create output text file                                                                   
    f = open(output, "w+")

    print(">>> Only writing branches with Jet or MET:")
    for branch in tree.GetListOfBranches():
        if (("Jet_" in str(branch)) or "MET_" in str(branch)):
            f.write(branch.GetName()+"\n")
        

    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="Full path to ntuple")
    parser.add_argument("treepath", type=str, help="Tree path/name")
    parser.add_argument("output", type=str, help="Output text file with branch names")
    args = parser.parse_args()
    main(args.filepath, args.treepath, args.output)

