import logging
import os
import subprocess

from tools.path import get_path

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def check_modded_path(modded_files):
    mf = os.walk(get_path(), topdown=True)

    for root, dir, files in mf:
        for file in files:
            file_path = os.path.join(root, file)
            for mod in modded_files:
                if file.endswith(mod):
                    with open(f"{os.getcwd()}/Gta_Mod_Manager/modded_files.txt", "w", newline="") as f:
                        f.write(file_path)

    logging.info("All modded files written to text file.")
    
    delete = input("Delete modded files (Y/N): ")
    
    if delete.upper() == "Y":
        with open(f"{os.getcwd()}/Gta_Mod_Manager/modded_files.txt", "r", newline="") as f:
            while True:
                mod = f.readline()
                if not mod:
                    break
                
                try:
                    subprocess.call(["runas", "/user:Administrator", f"DEL {mod.strip()}"])
                except Exception as e:
                    print(e)
    
    if delete.upper() == "N":
        pass
