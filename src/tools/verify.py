import csv
import hashlib
import logging
import os
import time

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def verify_files(GTA_PATH: str, HASH: bool, DEBUG: bool) -> str:
    start = time.time()
    sha256 = None
    gta_files = os.walk(GTA_PATH, topdown=True)
    exclude = set(["ReadMe", "Redistributables", "update", "x64"])
    OUT_FILE = f"{os.getcwd()}/Gta_Mod_Manager/file_integrity.csv"

    try:

        if not os.path.exists("Gta_Mod_Manager"):
            os.mkdir("Gta_Mod_Manager")

        if os.path.exists(OUT_FILE):
            os.remove(OUT_FILE)

        for root, dir, files in gta_files:
            dir[:] = [d for d in dir if d not in exclude]
            for file in files:
                file_path = os.path.join(root, file)

                if file.endswith(".txt") or file.endswith(".cab"):
                    continue

                
                if HASH == "True": 
                    with open(f"{GTA_PATH}/{file}", "rb") as f:
                        bytes = f.read()
                        sha256 = hashlib.sha256(bytes).hexdigest()

                if DEBUG == "True":
                    logging.info(
                        f"File Name: {file} \nFile Hash: {sha256} \nFile Path: {file_path}\n")

                with open(OUT_FILE, "a", newline="") as csvfile:
                    fieldnames = ["File_Name", "File_Hash", "File_Path"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(
                        {"File_Name": file, "File_Hash": sha256, "File_Path": file_path})

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        if DEBUG == "True":
            end = time.time()
            logging.debug(f"Took {end - start} seconds to complete scan.\n")
