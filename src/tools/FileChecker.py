import csv
import logging
import os

from tools.FilePathChecker import check_modded_path

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

clean_files = ["bink2w64.dll", "common.rpf", "d3dcompiler_46.dll", "d3dcsx_46.dll", "GFSDK_ShadowLib.win64.dll", "GFSDK_TXAA.win64.dll", "GFSDK_TXAA_AlphaResolve.win64.dll", "GPUPerfAPIDX11-x64.dll", "GTA5.exe", "GTAVLanguageSelect.exe", "GTAVLauncher.exe", "index.bin", "NvPmApi.Core.win64.dll",
               "PlayGTAV.exe", "uninstall.exe", "x64a.rpf", "x64b.rpf", "x64c.rpf", "x64d.rpf", "x64e.rpf", "x64f.rpf", "x64g.rpf", "x64h.rpf", "x64i.rpf", "x64j.rpf", "x64k.rpf", "x64l.rpf", "x64m.rpf", "x64n.rpf", "x64o.rpf", "x64p.rpf", "x64q.rpf", "x64r.rpf", "x64s.rpf", "x64t.rpf", "x64u.rpf", "x64v.rpf", "x64w.rpf"]


def file_Checker():
    """Compares files"""
    with open(f"{os.getcwd()}/Gta_Mod_Manager/file_integrity.csv") as csv_file:
        files = []
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        
        for row in csv_reader:
            files.append(row["File_Name"])
    
    try:
        for i in files:
            files.remove("File_Name")
    except:
        pass
    
    vanilla = 0
    modded_files = []
    
    for file in files:
        if file in clean_files:
            pass
        
        else:
            modded_files.append(file)
            vanilla += 1
            
    
    
    if vanilla > 0:
        logging.info(f"Game is modded, found: {len(modded_files)} modded file(s):\n{modded_files}\n")
        check_modded_path(modded_files)
    
    else:
        logging.info(f"Game is not modded, found: {len(modded_files)} modded file(s)\n")
    