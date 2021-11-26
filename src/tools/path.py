import json

from tools.verify import verify_files


def find_path():
    config = json.load(open("config.json"))
    GTA_PATH = config["GTAV_PATH"]
    DEBUG = config["DEBUG_MODE"]
    HASH = config["CHECK_HASH"]

    if GTA_PATH:
        verify_files(GTA_PATH, HASH, DEBUG)

    else:
        print("Please put gta path in json file.")

def get_path():
    config = json.load(open("config.json"))
    GTA_PATH = config["GTAV_PATH"]
    return GTA_PATH
        