import os

dict_wwwPlotDirs = {
    "2018": {
        "mutau": "/eos/user/s/skkwan/www/limits/limits_2018_mutau",
        "etau": "/eos/user/s/skkwan/www/limits/limits_2018_etau",
        "emu": "/eos/user/s/skkwan/www/limits/limits_2018_emu",
    },
    "2017": {
        # "mutau": "/eos/user/s/skkwan/www/dataMC/2024-10-16-11h36m-year_2017-iteration0-mutau/",
        # "etau":  "/eos/user/s/skkwan/www/dataMC/2024-10-16-17h19m-year_2017-iteration0-etau/",
        # "emu":   "/eos/user/s/skkwan/www/dataMC/2024-10-17-14h25m-year_2017_iteration0-emu/",
    },
}

for year in ["2018"]:
    for channel in ["mutau", "etau", "emu"]:
        wwwPlotDir = dict_wwwPlotDirs[year][channel]
        plotnames = [
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_2b2t_m1_15_{channel}.pdf",
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_2b2t_m1_20_{channel}.pdf",
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_2b2t_m1_30_{channel}.pdf",
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_2b2t_m1_40_{channel}.pdf",
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_2b2t_m1_50_{channel}.pdf",
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_4b2t_m1_15_{channel}.pdf",
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_4b2t_m1_20_{channel}.pdf",
            f"{wwwPlotDir}/plotLimit_{year}_a1a2_4b2t_m1_30_{channel}.pdf",
        ]
        anPlotDir = f"/eos/user/s/skkwan/AnalysisNotes/AN-24-166/plots/{channel}_cutbased/{year}/limits"

        for plot in plotnames:
            os.system(f"mkdir -p {anPlotDir}")
            command = f"cp {plot} {anPlotDir}"
            print(command)
            os.system(command)
