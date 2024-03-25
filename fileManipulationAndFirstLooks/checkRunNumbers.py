# checkRunNumbers.py
# Check if the listed files contain any runs with run number < 317509.


import os
import subprocess

files = [
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/00B7FFB1-3455-C941-AE3B-CF7085966A41.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/011D185E-4BBF-0E4D-8C39-EDB13AD8E7D3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/02713A49-3272-B84F-A4CC-F0E924FCAB90.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/0361FF13-A5B8-0E4A-B100-C5A9C39868A3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/045FAFBE-1A3D-F141-B864-A54197D2E352.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/04B3750E-6057-7C43-B0B0-D25A4E76E198.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/04BF0318-9B59-204A-A92E-C9DF64D8EB45.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/05692A05-250B-834B-90D1-A62043A43D1F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/06547562-FF58-E846-840A-DDDCB3CC9E18.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/06AAF640-FB06-2B4D-A80F-C548F10743CE.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/09E45B96-746E-A247-AE59-F8FD85E586FB.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/0B1BC0B6-40C8-804D-A8BA-7C53419B8C0F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/0C2EC37F-D444-D04E-82FF-4F2B0766E9B8.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/0D8C0592-DF3E-4F49-B0E9-F773FD62C0A0.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/0FE21F8F-013A-B64F-BC46-379630E884E7.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/10B01681-E0D5-D64A-8CA1-98198A3E27AF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/112929FB-F5E3-8E49-9F9B-7EBC95BF404D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/12EBB5A4-27D2-8F45-A7BA-5B22500BAA02.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/164C11CC-F7AB-7549-9DF3-F2B4EA46F081.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/16DCC63C-39BD-2E4B-A490-B8BCD9B47B2A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/17750069-D8A0-8742-A0C7-F0CE3A241646.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/195CD88F-D50A-5340-B78D-A7B6345EBBFD.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/1A9DC7C6-1C51-3A48-A8BE-45105FD7B499.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/1B914B0F-188C-7A46-BE48-F40774D53CC8.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/1C53E10C-3AD6-FC4F-BBBF-6907495452C6.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/1E368AAC-B4EB-7241-B5EB-3045F97A06E3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/1F1CCBBB-38F5-8C4A-9CBB-D69F61A7F7FB.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/1F3A94C1-1E5C-9644-B1F1-B95BC4ED19B4.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2045295A-FE10-F540-8A6E-95D33499122A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/21BE806A-E7D7-D648-A806-2B90051675BF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/22512755-FBF6-1C4E-8E37-F66AC03188BB.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/236CC70A-7B01-0240-ADF1-9ABD8AA138AF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2603D043-FC8E-3940-8CFA-58DC8AD1189F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/266850F7-3481-094B-9C9C-C1A446C51246.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/277A7295-D4CA-C049-885F-B59BCA1B1131.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2A3E24D0-1619-E940-9DD6-47F2DB72302F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2B509802-9971-B949-ACE4-2F0E0AE13120.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2B656885-20C1-4F46-A12C-F2A817F1BD9A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2B6A4845-BD88-804C-8FFB-B01E83C61689.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2D734FE3-C456-4647-8FB2-80CE5C7DDECF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/2DCF74FA-44F3-1243-8649-2550B33B0544.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/30D147BE-56E7-3A40-B425-7B49793D0F73.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/312ACA15-31BF-5649-936B-32E88A56045C.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/31CC8DE2-73BD-4741-84BE-DFFC399F1BEE.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3418AA6F-D6A1-E545-B719-441FC126C5AC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/34F0EB2C-C2F8-6647-905C-91AE9D0E25BA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/35C04270-5889-5F43-99BF-8BAB93A2193A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/35DC70FF-1879-E84E-931C-1DEE9D6F6C07.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/36B23D24-812A-1C47-8020-F848D1694D1A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/37AB1852-B48A-114E-BD6E-6508CCC42BA5.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/383BC6C3-3991-4A49-A31A-79D4452AFEB4.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3AB8FF72-A070-CD4A-9734-1F49283A25E1.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3ABE541A-987D-124E-B71A-372A345D64B8.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3AE1529F-6D83-2748-B7AE-42668D101EF3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3B419827-DD6D-044F-A98F-425BD5DD6FFF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3B5474E8-3AC3-2D43-BD13-B7CC02253663.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3CD2C6DE-0FAC-B04A-8B5F-1A40BB737D78.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3D8FE005-80E0-2E42-82FE-09D60200773D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3E023570-1DF0-C44A-B54C-82279FB91AC8.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3E58D3E3-860A-1F4B-BB12-1A6095D77A09.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3F082A26-D68C-C448-91BA-7E5614602E08.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/3FF66E38-D13C-0148-A894-428D91A0E1DD.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/42870807-245C-AC47-AFDB-0E40084EB302.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4515677B-4CA0-EA4D-A23F-1976A69643D7.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/45AA5E66-362E-6245-9588-F999ECEC5FBF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/471FF18D-E2FA-E148-9E4E-0D10347C0B1C.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/49CAFCC9-9D3E-DF43-8C55-E792DABD1382.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/49CD8DB3-034D-0E46-A156-069A57B59957.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/49EB9162-288E-014C-8FA9-135A57E9B128.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4A343FC7-46AF-7C48-B9A9-A20F683A9A8A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4B852745-9DFB-A541-9078-4812C7ABDF10.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4CA1F2AA-DE75-8C44-86E9-CF6C56F6A89A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4E3E0ABD-8EE0-5948-BF3A-6F45E6F019D0.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4EB18AFA-0429-5643-A80A-EC433D844C26.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4F4904A9-8615-7646-B861-6C09899D3A31.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/4FB71D34-209F-DE46-907C-6AAA399B46DF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/50D18A5D-64D2-5A45-A2F5-C5B8DB90514F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/51052CAD-D8FA-DF45-AFEE-20F616C072E4.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/5115AFC0-825C-E04C-9132-A31509FED701.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/51A465C0-2415-8849-B1C8-554CDEC4F125.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/52716465-962A-DB4C-905B-3D0552C94C1D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/55425803-8B51-D54E-AF07-62057715B67E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/55F1CFFE-2849-0D42-8845-FCE840668193.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/5766DB28-FC89-9B42-812F-962E1C7363B2.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/57C6DCC2-210E-3B44-BC97-20B51558CC58.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/583D6BFC-8C72-3C42-98B5-9259B8A881BA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/5898B524-E2AA-F040-9B04-DADD3B9DF93B.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/59452197-2F86-6042-88B5-45B7D93A74AF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/5945F0A0-33BB-7748-B84C-DC4532E62F97.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/5B2263B7-8094-A440-9502-47D5A79CF08D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/5B71B1E5-9570-684D-906A-EE9AD83485B1.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/5E383605-B54E-2D42-8707-1B0FFF3EFFCA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/60B31CD0-C753-874A-8EDF-604CB3F0D826.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/60CAE3A0-F0E0-4348-BBC6-1C224484C584.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/61051773-8EB6-AF4E-BA2B-CA30BDCE4A81.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/62A191CB-5D4C-034F-B519-975945698345.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/672A62C3-FACF-F54E-88AA-D0878A0C98DA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/67DA26D9-6012-B548-98AD-3886A79E040E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/67DDE133-EDAA-634C-A458-CAAD5A397FA7.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/69FE5DCF-0ED2-2045-9C80-ABA44A517A34.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/6B3B3ACE-5850-4341-B2F1-A4B93C1851DC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/6B8AB6F0-AC16-3849-A73F-93044C666B9A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/6BBA24AC-7DB5-6146-B79A-F214CA35CB5E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/6CC271DB-B5B7-644A-95AB-6F17128CC6EE.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/70B36814-AFC6-9C42-98A0-65840BAFA3E6.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/71C9D445-8B56-0F46-ADAE-4CEB4F187F9C.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7272A226-D8D6-6148-A7FD-86C009F55922.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/72DC66B9-0206-DF4B-965D-374934AC0490.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/760B6E40-EDBC-DD42-BCD9-03B6B0F2E140.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/763A3A5A-B3D5-054D-8685-53C24648846A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7ADAD437-24F4-0E4F-8FD5-52BC746562AA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7C0D99A8-63EF-E545-A568-BA3EE45CEA82.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7C979072-4792-8C4E-A2D1-D765A5908D11.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7CB260FC-48D5-1D44-9F86-CAD07DDFBA67.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7D2E5A87-03F3-AE4C-8968-7C852C287E08.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7E84CC32-3F47-DE45-9649-59798F03AD4D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/7EA5090D-CB50-3844-AA5F-065234D02506.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/802BD527-9A8C-DF40-8B0B-34821153945F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/824D54F5-1091-3C49-BF67-31E0D054803F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8317A33E-C995-F140-A54B-EA357C44DEA2.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/840C6C21-5AC1-ED4A-90AB-05ABCA0DA299.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/856F41D4-5A52-384D-BFAC-47B1A4DA750D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/86C6B751-6EBC-F045-82B9-3441CA344395.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/87F8A655-2A34-D14D-A498-E521D2FB8F4F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/89DE363B-D691-3945-BCB2-824F789D301E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8A4C4273-AFA0-E04B-81B1-02814BC45D70.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8A8859EA-6332-754A-8305-52B1864D6647.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8A9F72E4-988B-5A45-BDBF-8E24AA1DB17D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8B4C47CE-E166-544C-BFA6-6960E8E976AA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8CEB2DF9-092F-754A-B8B6-21FEF43C0744.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8D95863E-5CE5-D04C-A6A7-7B3CE9484A6F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8E2C8E49-0169-0940-A72A-F5DDC81544A3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8F217D6D-29EA-4543-8C8E-7BCFA2D7A79D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8F96C11E-463B-AE44-AF36-450A13152533.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/8FB5FED6-0D24-8F44-B7E3-25CE15D5E7E8.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/90D3669A-4148-E842-AAF8-9751EC42C0BE.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/93262701-FB34-F34D-8004-EBD238EAF571.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9483684D-D223-6045-BF6B-78B2E2671D37.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/94C69E5D-3616-C04E-9B51-84124C6C5DA7.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/95A159AA-5B87-DA42-B1C9-DCC030E5A0FE.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/965CAD39-753A-5D45-B477-CED9B3A7F41E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/98A23080-A90A-ED48-8918-8588DA55088D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/98CC8884-248C-C342-B3DB-9DEE5AE662ED.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9A5600CA-B5D6-5E48-A921-7D365BFF0E57.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9B0B6F3D-579D-5A44-837E-8A217B9CFA69.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9B52297C-90B6-D34A-9A8A-73FC7C8F12AC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9DFD7BDE-E58E-674A-B287-13B5D85F0E70.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9E45655B-3892-264C-9185-18FBA99AB965.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9ECDE3DC-DCEF-4646-BEF8-874501CA8BFE.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/9EF24C36-ED5E-904E-B2C9-6FDDD076B9A3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/A1013133-2EAD-1C4F-BE88-1789E043B1F3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/A320C345-44A8-4443-8421-3622B4E4B165.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/A32AE33D-5A49-1C4C-9E82-156DF4490A69.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/A4AA7CE5-E1BF-6947-8E5C-6BBFF8D5F076.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/A546CC92-2E39-AB42-B1BF-5528A29034EF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/A69E2486-D610-CE4C-945B-E9EFED3CDB63.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/A6D18720-B5FD-B64B-A22E-C62921D85A01.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/AA9C4283-B8FA-1045-BE27-942175E57B77.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B03BD488-583F-F444-9826-BAE26978B486.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B0BD0EC7-72C1-4949-94DC-3E44FF6B5EE5.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B113CF33-8FFB-9942-8FFA-37D9AC036CEC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B53CC902-3EF0-DC40-9207-9FC496F91056.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B5AEF519-E6A2-4843-BE58-9FE1F9B6DF21.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B5E4981A-6056-6B43-AD41-E863193CEC3B.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B763E0DB-1C48-BA40-BFD2-CB9F002D925E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B7B5E5B1-267B-2147-B72A-BFE6D334B688.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/B80B18FB-8EC3-1246-81B3-37A6AFBBCBBC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/BA442B99-B8A8-714E-9D24-88DE577C9336.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/BC5924D8-88E9-F647-8DC4-DFF790FB30AA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/BD94B8A0-AAEE-AE49-BB5C-835EFBD82252.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/BE6C9982-9237-874F-A6F9-4ACE9C7D2420.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/BF71771D-F373-5E44-A1F1-EFC6A982336E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/C22E1A4B-8222-C54D-8867-497F8CED8D9D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/C29E191E-7B92-4541-BC60-820B2D678C2C.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/C6AE7FD9-085B-984D-8F1A-5B9A017CEDC0.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/CAED6CA4-0954-6F41-AF68-DF89D6140787.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/CB198A7B-5BCD-9549-AA55-35567E456B11.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/CBB7490B-4CD9-554A-8EF5-47E530C23ACA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D0704D5E-A856-EE47-B476-DF86E848EC0E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D14FBD3D-CDC6-9B4D-A75F-ABC9923590F3.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D1F9083B-FCC4-1544-8B00-3EB00ABF89CC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D260012B-E30E-AB49-8BF8-95CF27030C16.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D293B873-D555-284A-8107-9A2489E994BC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D394A243-AEB7-BA46-B808-D1BA4BC7E8CA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D3B87FAF-C16F-F043-A48D-70F0EF3D06BF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D48FEC20-10CD-4745-8F8C-0A03376D615B.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D5113358-672A-AA4C-BC97-DF0940C4E608.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D52F814A-F451-E84F-9B52-C9C47583449F.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D6E273DF-728E-7E44-BAD3-6B28D95C3A31.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D71E9D7C-E444-8E45-8039-F5FA2FA9315A.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/D8768BA5-0664-EF43-AE2B-0C1B6D974A77.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/DA0EFC7A-2218-C04F-B27D-E7D115BE9809.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/DC9402F2-83F2-F64F-8475-71C256417133.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/DCB67998-FAE5-AA41-BC65-EAAF9A56269E.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/DD0BF239-1B17-9C49-9085-74146EBEB9DC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/DDAB94EB-8073-3D4A-91FD-D4B438ECE831.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/DDDF2D2F-5676-E649-AB6A-32D6BC786CEA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/DFD5B349-4148-0C48-85FD-9FE2F29D0998.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E16708EF-5A51-3740-9E4C-0E5501C83A15.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E17C94A6-7F8A-9444-BAC3-BDF44BF9387B.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E1F3E26D-756E-C843-8272-AF2770147AFD.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E35D2E6A-5C75-3F47-851D-53C272276106.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E6CBB287-9CB4-0D4F-8554-D8BA26F839F5.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E809AA60-5BDD-8B42-B86D-C1F8970F6856.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E850CB12-8436-064A-8985-796A1A8E429B.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/E8902CDD-0297-6342-A819-C1E41A468B71.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/EB3E1E0E-23CB-BA4A-B3D9-B458235CA13D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/EB609BEB-0BFB-854C-AEF9-3E2415518A0D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/EB703433-936F-F942-9341-635CB46ADD71.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/EB7914E6-663E-314B-ADEC-9935309678C9.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/EB7E8FB5-97BF-2D4E-8A0C-562A786D12AD.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/ECA24238-5997-B141-9004-40BED99C3D0B.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/ED557E4D-7A4D-3946-BE12-A64A11355848.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/ED5FF52A-52F6-8A44-93B9-33BEEA1BF7DF.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/ED79BA77-8887-CB47-871B-2D19FD83F9CC.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/EDD65D7B-D253-2444-9A3D-23DDDDBA4975.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/F15C65A0-EF4F-0B44-BCFB-BABE73D728C7.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/F160B5FB-7B93-4044-9C92-5A6078C7CFAD.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/F1D4F84C-D6AE-7C46-8034-E7477604F457.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/F56056E7-06FD-8C40-93F6-7BD883B536AA.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/F71086DB-A3CD-714D-85E1-A7D640030F1D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/F8F84CA2-7E90-2D45-98B0-2773BCDCEF1D.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/F92AB528-9824-C645-B255-CA624D7F0913.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/FEE1CE60-C2AB-D84B-8CEF-E6DD7D584C94.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/270000/FF0211CD-9151-8D41-9BDA-DE13EE0E3C35.root',
    '/store/data/Run2018A/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/70000/79C57B8F-B2E1-E245-9F19-D8ADF3285CF7.root'
]

filesWithoutEarlyRuns = []

for file in files:
    command="dasgoclient -query='run file={}' | tee temp.txt".format(file)
    status, output = subprocess.getstatusoutput(command)
    listOfRuns = output.split()

    hasEarlyRuns = False
    for runString in listOfRuns:
        run = int(runString)
        if (run < 317509):
            hasEarlyRuns = True
            break
    
    if not hasEarlyRuns:
        print("NO EARLY RUNS IN {}".format(file))
        filesWithoutEarlyRuns.append(file)

print(filesWithoutEarlyRuns)