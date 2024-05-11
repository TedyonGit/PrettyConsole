import shutil
import os
import sys

# Colorama
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


class Main:
    terminal = ""
    X = "" # COLUMNS
    Y = "" # ROWS

    class Types:
        Success = 1
        Error = 2
        Warning = 3
        Info = "None"

    # Further customizations

    OutputTypes = {
            1: f"[{Fore.GREEN}+{Fore.WHITE}]", 
            2: f"[{Fore.RED}/{Fore.WHITE}]", 
            3: f"[{Fore.YELLOW}!{Fore.WHITE}]",
            "None": f"[{Fore.CYAN}?{Fore.WHITE}]"
            }


    logo = """
__   __                 _                      
\ \ / /__  _   _ _ __  | |    ___   __ _  ___  
 \ V / _ \| | | | '__| | |   / _ \ / _` |/ _ \ 
  | | (_) | |_| | |    | |__| (_) | (_| | (_) |
  |_|\___/ \__,_|_|    |_____\___/ \__, |\___/ 
                                   |___/       
    """
    

    def __init__(self):
        self.terminal = shutil.get_terminal_size()
        self.X = self.terminal[0]
        self.Y = self.terminal[1]
        os.system("cls")
        return

    def showLogo(self):
        temp = ""
        for line in self.logo.splitlines():
            temp += str(f"{line}\n").center(25 + int(self.X / 2))
        print(temp)

    def output(self, type, text):
        try:
            self.centerText(f"{self.OutputTypes[type]} {text}")
        except:
            self.centerText(f"{self.OutputTypes['None']} {text}")

    def centerText(self, text):
        print(str(f"{text}").center(12 + int(self.X)))
