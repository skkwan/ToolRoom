import json
import os
import sys

BASE = "/cvmfs/cms-griddata.cern.ch/cat/metadata"
DEFAULT_OUT_PATH = "meta_corrections.json"

# era key (matches skim.cxx sConfig.era()) -> {POG: cvmfs era directory name}
ERA_MAP = {
    "2016preVFP": {
        "LUM": "Run2-2016preVFP-UL-NanoAODv9",
        "MUO": "Run2-2016preVFP-UL-NanoAODv9",
        "EGM": "Run2-2016preVFP-UL-NanoAODv15",
        "JME": "Run2-2016preVFP-UL-NanoAODv9",
        "TAU": "Run2-2016preVFP-UL-NanoAODv9",
        "BTV": "Run2-2016preVFP-UL-NanoAODv9",
    },
    "2016postVFP": {
        "LUM": "Run2-2016postVFP-UL-NanoAODv9",
        "MUO": "Run2-2016postVFP-UL-NanoAODv9",
        "EGM": "Run2-2016postVFP-UL-NanoAODv15",
        "JME": "Run2-2016postVFP-UL-NanoAODv9",
        "TAU": "Run2-2016postVFP-UL-NanoAODv9",
        "BTV": "Run2-2016postVFP-UL-NanoAODv9",
    },
    "2017": {
        "LUM": "Run2-2017-UL-NanoAODv9",
        "MUO": "Run2-2017-UL-NanoAODv9",
        "EGM": "Run2-2017-UL-NanoAODv15",
        "JME": "Run2-2017-UL-NanoAODv9",
        "TAU": "Run2-2017-UL-NanoAODv9",
        "BTV": "Run2-2017-UL-NanoAODv9",
    },
    "2018": {
        "LUM": "Run2-2018-UL-NanoAODv9",
        "MUO": "Run2-2018-UL-NanoAODv9",
        "EGM": "Run2-2018-UL-NanoAODv15",
        "JME": "Run2-2018-UL-NanoAODv9",
        "TAU": "Run2-2018-UL-NanoAODv9",
        "BTV": "Run2-2018-UL-NanoAODv9",
    },
    "2022": {pog: "Run3-22CDSep23-Summer22-NanoAODv12" for pog in
             ("LUM", "MUO", "EGM", "JME", "TAU", "BTV")},
    "2022postEE": {pog: "Run3-22EFGSep23-Summer22EE-NanoAODv12" for pog in
                   ("LUM", "MUO", "EGM", "JME", "TAU", "BTV")},
    "2023": {pog: "Run3-23CSep23-Summer23-NanoAODv12" for pog in
             ("LUM", "MUO", "EGM", "JME", "TAU", "BTV")},
    "2023postBPix": {pog: "Run3-23DSep23-Summer23BPix-NanoAODv12" for pog in
                      ("LUM", "MUO", "EGM", "JME", "TAU", "BTV")},
    "2024": {pog: "Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15" for pog in
             ("LUM", "MUO", "EGM", "JME", "TAU", "BTV")},
    "2025": {
        "LUM": "Run3-25Prompt-Summer24-NanoAODv15",
        "MUO": "Run3-25Prompt-Summer24-NanoAODv15",
        "EGM": "Run3-25Prompt-Summer24-NanoAODv15",
        "JME": "Run3-25Prompt-Winter25-NanoAODv15",
        "BTV": "Run3-25Prompt-Summer24-NanoAODv15",
        # TAU: no dated snapshot published yet -> omitted
    },
}


def latest_dated_subdir(era_dir_path):
    if not os.path.isdir(era_dir_path):
        return None
    dated = [
        d for d in os.listdir(era_dir_path)
        if d != "latest" and len(d) == 10 and d[4] == "-" and d[7] == "-"
    ]
    if not dated:
        return None
    return sorted(dated)[-1]


result = {}
for era, pog_map in ERA_MAP.items():
    result[era] = {}
    for pog, era_dir in pog_map.items():
        era_dir_path = os.path.join(BASE, pog, era_dir)
        date = latest_dated_subdir(era_dir_path)
        if date is None:
            continue
        snapshot_path = os.path.join(era_dir_path, date)
        corrections = {}
        for fname in sorted(os.listdir(snapshot_path)):
            if fname.endswith(".json.gz"):
                name = fname[: -len(".json.gz")]
                corrections[name] = os.path.join(snapshot_path, fname)
        if corrections:
            result[era][pog] = corrections

out_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT_PATH
with open(out_path, "w") as f:
    json.dump(result, f, indent=2, sort_keys=False)
    f.write("\n")

print(f"Wrote {out_path}")
print(f"Eras: {list(result.keys())}")
for era, pogs in result.items():
    print(f"  {era}: {list(pogs.keys())}")
