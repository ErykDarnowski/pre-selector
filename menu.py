#!/usr/bin/env python3

# Imports
import os
from colorama import Fore
from colorama import Style
from simple_term_menu import TerminalMenu

# Vars
options = [
    "Automatic (suggests hooks groups based on file extensions and let's you pick the rest)",
    "Manual (you manually pick every hook group)",
    "exit",
]
terminal_menu = TerminalMenu(options)

# Funcs
def clear():  # CLEAR SCREEN (get func from a helper sort of file?)
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear()

    print(
        f"""{Fore.YELLOW}                       {Fore.RED}____  _____ _     _____ ____ _____ ___  ____  
{Fore.YELLOW}   _ __  _ __ ___     {Fore.RED}/ ___|| ____| |   | ____/ ___|_   _/ _ \|  _ \ 
{Fore.YELLOW}  | '_ \| '__/ _ \____{Fore.RED}\___ \|  _| | |   |  _|| |     | || | | | |_) |
{Fore.YELLOW}  | |_) | | |  __/_____{Fore.RED}|__) | |___| |___| |__| |___  | || |_| |  _ < 
{Fore.YELLOW}  | .__/|_|  \___|    {Fore.RED}|____/|_____|_____|_____\____| |_| \___/|_| \_\\
{Fore.YELLOW}  |_|
"""
    )

    # https://github.com/IngoMeyer441/simple-term-menu # <- styling options and so on
    menu_entry_index = terminal_menu.show()

    clear()

    # print(f"You have selected {options[menu_entry_index]}!")
    if menu_entry_index == 0:
        print("Automatic")
    elif menu_entry_index == 1:
        print("Manual")
    else:
        exit()


if __name__ == "__main__":
    main()
