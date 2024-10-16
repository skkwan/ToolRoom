import os

dict_wwwPlotDirs = {
    "2018": {
        "mutau": "/eos/user/s/skkwan/www/dataMC/2024-10-12-16h58m-iteration18-mutau",
        "etau": "/eos/user/s/skkwan/www/dataMC/2024-10-12-17h03m-iteration18-etau",
        "emu": "/eos/user/s/skkwan/www/dataMC/2024-10-11-11h12m-iteration18-emu"
    },
}

for year in ["2018"]:
    for channel in ["mutau", "etau", "emu"]:
        wwwPlotDir = dict_wwwPlotDirs[year][channel]
        plotnames = [
            f"{wwwPlotDir}/{channel}_inclusive_bpt_deepflavour_1_signal_cascade_mass_100_15.pdf",
            f"{wwwPlotDir}/{channel}_inclusive_bpt_deepflavour_2_signal_cascade_mass_100_15.pdf",
            f"{wwwPlotDir}/{channel}_inclusive_pt_1_signal_cascade_mass_100_15.pdf",
            f"{wwwPlotDir}/{channel}_inclusive_pt_2_signal_cascade_mass_100_15.pdf",
            f"{wwwPlotDir}/{channel}_inclusive_m_vis_signal_cascade_mass_100_15.pdf",
        ]
        anPlotDir = f"/eos/user/s/skkwan/AnalysisNotes/AN-24-166/plots/{channel}_control/{year}/prefit"

        for plot in plotnames:
            command = f"cp {plot} {anPlotDir}"
            print(command)
            os.system(command)
