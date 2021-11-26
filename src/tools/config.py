

from tools.FileChecker import file_Checker
from tools.path import find_path


class commands(object):

    "Commands to run"

    def __init__(self):

        self.command_list = ["help", "gta_path", "check_files"]

        self.command_dict = {"help": self.help,
                             "gta_path": find_path, "check_files": file_Checker}

    def help(self):
        print("\n".join(self.command_list[1:]), sep="\n")


commands = commands()
