import os

dict_wwwPlotDirs = {
    "2018": {
        "mutau": "/eos/user/s/skkwan/www/dataMC/2024-11-20-23h57m-benchmark-2018-mutau-iteration1-m_vis",
        "etau": "/eos/user/s/skkwan/www/dataMC/2024-12-04-11h55m-benchmark-2018-etau-iteration1p5-m_vis",
        "emu": "/eos/user/s/skkwan/www/dataMC/2024-12-04-14h39m-benchmark-2018-emu-iteration1p5-m_vis",
    },
    "2017": {
        "mutau": "/eos/user/s/skkwan/www/dataMC/2024-10-16-11h36m-year_2017-iteration0-mutau/",
        "etau":  "/eos/user/s/skkwan/www/dataMC/2024-10-16-17h19m-year_2017-iteration0-etau/",
        "emu":   "/eos/user/s/skkwan/www/dataMC/2024-10-17-14h25m-year_2017_iteration0-emu/",
    },
}

for year in ["2018"]:
    for channel in ["mutau", "etau", "emu"]:
        wwwPlotDir = dict_wwwPlotDirs[year][channel]
        plotnames = [
            f"{wwwPlotDir}/{channel}_highMassCR_m_vis_signal_4b2t_mass_100_15.pdf",
            f"{wwwPlotDir}/{channel}_lowMassSR_m_vis_signal_4b2t_mass_100_15.pdf",
            f"{wwwPlotDir}/{channel}_mediumMassSR_m_vis_signal_4b2t_mass_100_15.pdf",
            f"{wwwPlotDir}/{channel}_highMassSR_m_vis_signal_4b2t_mass_100_15.pdf",
        ]
        anPlotDir = f"/eos/user/s/skkwan/AnalysisNotes/AN-24-166/plots/{channel}_cutbased/{year}/prefit"

        for plot in plotnames:
            os.system(f"mkdir -p {anPlotDir}")
            command = f"cp {plot} {anPlotDir}"
            print(command)
            os.system(command)
