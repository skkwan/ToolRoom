# Usage:
# Do voms proxy, make sure you are in ROOT version > 6.34 (for DefaultValueFor to work)
# python3 aggregateSignalMassPointBranchNames.py
#
# M

from json import dumps
import json

import os

import sys
import ROOT
import re

cut = ""

files = [    

#### FULLSIM 2022EE
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/017025d4-45f2-4a44-ae75-a0b8725ca882.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/05a0facd-0093-4714-a4d4-05ef4e0b313f.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/08f12a0e-4d81-4f91-8445-192773fb4114.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/0912cfb4-212a-4646-a54f-650c83cbe869.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/09ecd6ba-c56b-45e2-8c3a-314201c6e3f8.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/0ca2fff9-5d83-43ec-bb76-27daada8107a.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/11bba33c-fbe8-4ca0-b5bf-dad35c487cbf.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/1634ae29-bfe0-474b-b984-a6f01bd62d9e.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/22a90930-1eac-4dee-a281-ed216547aff0.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/275b113d-15c8-4f71-ab52-af0acf08b52b.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/297a558b-6f78-47f6-858a-ab468348f0c2.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/2e32269e-8aef-4605-9487-1d93ff041b5c.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/351df64f-4d45-4a45-a01b-3199dbe8197c.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/35bf9097-891a-444e-9f90-7854c84b9507.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/3c5983a4-2a5e-4072-a3fe-a5be4430ffdf.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/3eedab0a-cd32-49ce-ac48-8f576feef622.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/4b0c690d-491d-4281-8e70-8e84e24f0216.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/4c3d375d-427f-43d4-aef2-48842ec0e325.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/4fc4122e-1a93-4289-ba19-9d32282edbce.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/5058f989-c36d-46dd-9f25-a5502498c84b.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/5444d3bb-359b-4abc-a692-a4b903599e88.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/5870377f-580d-4bfe-ab65-cc3ac72c3d03.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/5b3c71ab-d6bf-4557-8a5a-d1dd30e22962.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/5bfc5acf-fc89-476c-9349-a858c87ad2d3.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/5e96d057-283d-4858-a39a-9cbb3f659bbb.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/5febee25-baa9-424a-be46-0c4bf38ee2df.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/61808b89-cdf2-4b45-aaf7-f70987cb838b.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/62aa7ca2-8fc7-4c83-a97c-5bab2f5a9bd4.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/64d8f741-9b22-4406-b77a-5d7c522766dd.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/68772ed1-38fe-458a-9797-aab15b15d855.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/6d3e5d8e-0042-4d2d-9cbb-9c240a4dc7cd.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/71b59d6c-5304-4c48-80ce-983c9a9888ab.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/72e048d1-8f38-43c4-b26b-c328c3960061.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/752e95c2-7255-4ddd-8112-53ce828f436b.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/76d0cd6a-c0d4-4022-ab90-61d7577b07cd.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/77a46cfb-62a1-4530-bbda-fc31fe996f28.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/781f245a-0fe4-463a-9306-7d0a56ac31fd.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/798f3ea2-ab10-4033-bfb1-dd887c9e5d2e.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/7da1af7e-c211-4234-ae25-dfc0241dd33f.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/7e875fbc-41cb-4f71-ae5d-9c9d00c9b5b4.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/84259b4e-06ea-41ac-9e25-8ed4412e68c6.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/86ae7f4b-1fe2-4f1f-acc5-f1d2ebc3b8c3.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/88641558-c5fe-4dea-a08e-bde132fbf1ae.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/8898f1a7-14c2-4a03-a143-8b180b69597f.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/8e46b988-3e7f-45b7-8915-5d71643986f3.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/970d9866-8c7f-4144-b2d1-02f505cc562c.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/9d3d3649-dd8a-4044-acd6-e46eff5ef256.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/a1026e3d-c035-4f21-a7ac-b44fea791934.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/a30a3b87-8c80-4ae1-a4e0-a283cb42cfc5.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/a88459b8-1a51-4d8d-975c-bbc130446421.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/aee360c5-97f9-476a-aaaa-a317c08c3bf8.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/afa2d35e-116e-46ac-a28e-afd476c33245.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/b2fde9c0-8825-4d03-abfb-8cfe15d5b532.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/b410f268-719e-4158-b462-d5f84d2d3208.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/b4c4097d-ec21-4711-893d-41747b93eb87.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/b8a3e6fd-434a-47d8-b1fa-e6149e3d0bb0.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/bf3a9b70-723f-4fb4-844e-8117ceebd5b1.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/c0f615f3-7c51-46dc-821d-d7d561f2cae7.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/cd91fec3-21d0-4c36-8a4d-453869784ec3.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/d7e4817f-ebb1-470d-927e-a9cbeae5a83c.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/d903417b-cabe-40d0-862b-539176d67a0d.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/daba8264-9cb2-4f70-8e6c-f447c092eeb8.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/db14054a-61f7-4ab3-91f6-ff7fbc86f0eb.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/ddd4eb1e-bb95-46a2-9023-54e0c2c10d25.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/dfca154c-5f22-4a96-9b92-6bc7e03f6183.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/e3d7fb1b-0737-49a9-ac7c-a8648e25e6e4.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/e82dc84d-46c7-4821-9518-6312b06ee00c.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/ec0f4877-be6f-4040-8cac-d479fa479779.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/f375024d-eb78-4126-8ea9-7111bbd60888.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/f452dfa1-9953-41d2-b27c-c94976e3d3ea.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/f5f9b34a-8ebe-4f87-94f5-13f83581d16b.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/f9427fea-1706-4ca4-bc50-386fa6c89904.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/f9b02d10-7a23-4d38-b094-10eb78f00909.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/f9b383d5-f694-4bc8-9e62-765919cd77fb.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/facc1406-e188-4568-b38a-beb6e30b8eba.root",
	"root://cms-xrd-global.cern.ch//store/mc/Run3Summer22EENanoAODv12/SMS-TChiZH-Zto2L_mNLSP200To1500_mLSP0To600_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_postEE_v6-v2/2810000/feee2691-a00a-4473-841f-9a37d3b5dba3.root",
  
   # Note: if this first file (0051C0B9*.root) gets added to the TChain, the resulting df.GetColumnNames() will fail to find GenModel_TChiZH_600_300. We don't know why this happens

##### FASTSIM
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/0051C0B9-4639-C04E-A548-55EB7C33CD89.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A78401FF-A506-ED4C-A7D8-E1DB40FE7609.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/430B5C71-0DF5-5E4E-81DC-15840D2AB4CF.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/B15411C9-6150-834C-AAC9-5AC1883971FE.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/4E7F2D48-33E7-564D-BE3E-9251DD9BCC7E.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/BAA99EDF-91CE-534E-90F8-192F3C012181.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A9F6D499-D1A6-4C48-8105-89262B7E54B1.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A2BAAB7E-BC95-8F40-B8F1-9BC663EC0039.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/18EB0057-F784-E64C-9F31-883E4E536CF0.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/514247BE-9B35-5E43-8729-AC6507271FD7.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A9B4AE16-3CF5-0E42-A55A-27842389BA34.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/106F18D9-C493-3849-9BD4-81283F0696D3.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/2D0A3A96-E351-A64A-95B3-F97B69A78BA5.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/BEAB0832-FD6A-F546-BAF5-A21E3CAA65F6.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/A8CBD5A0-4B16-0546-9557-2CC503D462BB.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/4AF1EAFA-2F5E-8C45-8380-86CAA5EEF423.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/5E51979D-20C8-4F4A-9E5A-887086A05BC9.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/1A78966B-61E3-0D4E-9823-945B03E47617.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/5A67165A-7C99-8248-A021-7C42B7E14973.root",
    # "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/SMS-TChiZH-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/FSUL18_FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1/60000/F9E29EFC-D3E9-5540-A3A8-A6F4181B1389.root",
]

def aggregateBranchNames() -> None:
    """
    Get the number of events in a dataset passing a cut.
    """

    dictModelNames = {}

    for file in files:
        # print(f"Adding {file}")
        # Add the input files to a TChain
        ch = ROOT.TChain("Events")
        ch.Add(file)

        # Create dataframe from TChain
        df = ROOT.RDataFrame(ch)
        
        colNames = df.GetColumnNames()
        for thisColName in colNames:
            # need to cast this strange object into a string
            colName = str(thisColName)
            if "GenModel_TChiZH" in colName:
                # print(colName)
                if colName not in dictModelNames:
                    dictModelNames[colName] = "1"

    for key in dictModelNames:
        modelname = key.replace("GenModel_", "")
        print(f"{modelname}")



if __name__ == '__main__':
    aggregateBranchNames()
