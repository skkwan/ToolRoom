'''
getTotalEventsInDirectory.py

'''

import ROOT
import sys
import os

def main(argv=None):

    rootdir = "/eos/user/s/skkwan/hToAA/condor/Jun-03-2021-23h04m/Embedded-Run2017E-MuTau/"

    nEntriesTotal = 0


    for myFile in os.listdir(rootdir):
        if myFile.endswith(".root"):
            fpath = str(os.path.join(rootdir, myFile))
            print(fpath)

            f = ROOT.TFile.Open(fpath, "READ")
            if (f.GetListOfKeys().Contains("mutau_tree")):
                t = f.Get("mutau_tree")
                data = t.AsMatrix(["nEntries"])
                nEntriesTotal += data[0][0]
                print("Found %i entries" % (int(data[0])))
            f.Close()


    print(nEntriesTotal)

    return




if __name__ == '__main__':
    main()
