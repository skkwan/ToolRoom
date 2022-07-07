# Example from Dan Marlow

from ROOT import TFile, TTree, TH1D, TLorentzVector  

inFile = TFile.Open("inFile.root")
inTree = inFile.Get("Events")
nentries = inTree.GetEntries()
print("nentries={0:d}".format(nentries))

# make a single histogram 
fOut = TFile('hist.root', 'recreate' )
hMmumu = TH1D('hMmumu','hMmumu',200,0., 200.) 

verbose = 1
nMax = nentries
nMax = 100000       # if you don't want to read the whole file 
for count, e in enumerate(inTree) :
    if count > nMax : break
    nMuon = e.nMuon
    if nMuon < 2 : continue
    if verbose > 1 or (count % 1000 == 0) : print("count={0:d} nMuon={1:d}".format(count,nMuon))

    # make a list of muons
    muListPos = []
    muListNeg = []
    for j in range(nMuon) :
        # filter list of muons
        if not e.Muon_mediumId[j] : continue
        if abs(e.Muon_dxy[j]) > 0.045 : continue
        if abs(e.Muon_dz[j]) > 0.2 : continue
        eta1, phi1 = e.Muon_eta[j], e.Muon_phi[j]
        if abs(eta1) > 2.1 : continue

        # this is a good muon.  Make a LorentzVector
        mu = TLorentzVector()
        mu.SetPtEtaPhiM(e.Muon_pt[j],e.Muon_eta[j],e.Muon_phi[j],0.105)

        # add it to the right list 
        if e.Muon_charge[j] == 1:
            muListPos.append(mu)
        else :
            muListNeg.append(mu)
            
    # get opp. sign dimuon + ditau mass pairings
    for muPos in muListPos : 
        for muNeg in muListNeg :
            mumu = muPos + muNeg
            hMmumu.Fill(mumu.M())
            
fOut.cd()
fOut.Write()
fOut.Close()        
