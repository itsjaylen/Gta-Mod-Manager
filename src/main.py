import ctypes
import hashlib
import json
import logging
import os
import time
import sys

from tools.config import commands

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def terminal():
    while True:
        try:
            cmd = input("Type the command you want to run: ")
            if cmd not in commands.command_list:
                logging.error("Command not found")

            if cmd in commands.command_list:
                try:
                    commands.command_dict[cmd]()
                except KeyError:
                    logging.warning(f"Command: {cmd} not implemented.")
        except KeyboardInterrupt:
            print("\n")
            break


if __name__ == "__main__":
    terminal()
