background_samples = {
    "DYJets": [
            "DYJetsToLL_M-50",
            "DYJetsToLL_M-50_HT-70to100",
            "DYJetsToLL_M-50_HT-100to200",
            "DYJetsToLL_M-50_HT-200to400",
            "DYJetsToLL_M-50_HT-400to600",
            "DYJetsToLL_M-50_HT-600to800",
            "DYJetsToLL_M-50_HT-800to1200",
            "DYJetsToLL_M-50_HT-1200to2500",
            "DYJetsToLL_M-50_HT-2500toInf",
        ],
        "WJets": [
            "WJetsToLNu",
        ],
        "ttbar": [
            "TTTo2L2Nu",
            ],
		"TTZ_peak": [
			"TTZToLLNuNu_M-10_peak_mll",
		],
		"TTZ_nonpeak": [
			"TTZToLLNuNu_M-10_nonpeak_mll",
		],
		"TTW": [
			"TTWJetsToLNu",
		],
        "WH": [
            "WminusH_HToBB_WToLNu_M-125",
            "WplusH_HToBB_WToLNu_M-125",
		],
		"ZH": [
            "ZH_HToBB_ZToLL_M-125",
        ], 
        "WZ": [
            "WZTo3LNu",
            "WZTo2Q2L",
			"WZTo2Q2Nu",
		],
		"WW": [
            "WWTo2L2Nu",
        ],
        "ZZ": [
            "ZZTo2L2Nu",
            "ZZTo2Q2L",
            "ZZTo2Q2Nu",
			"ZZTo4L", 
        ]
}

# List comprehension: .values() gives a list of lists
# https://www.geeksforgeeks.org/python/nested-list-comprehensions-in-python/
# Loop through each list and then get each element in the list
cats = [sample for category in background_samples.values() for sample in category]
print(cats)
print( background_samples.values())

m = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flat = []
for s in m:
    for r in s:
        flat.append(r)

print(flat)

# equivalent to: get all the r's, for ALL the s's in m. But what is the relation with r and s? r is in s
compact = [r for s in m for r in s]
# 
print(compact)