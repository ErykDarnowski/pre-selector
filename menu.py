#!/usr/bin/env python3

# Imports
from simple_term_menu import TerminalMenu

# Vars
options = [
    "Automatic (suggests hooks groups based on file extensions and let's you pick the rest)",
    "Manual (you manually pick every hook group)",
    "exit"
]
terminal_menu = TerminalMenu(options)

# Funcs
def main():

    # CLEAR SCREEN (get func from a helper sort of file?)

    print("""                       ____  _____ _     _____ ____ _____ ___  ____  
   _ __  _ __ ___     / ___|| ____| |   | ____/ ___|_   _/ _ \|  _ \ 
  | '_ \| '__/ _ \____\___ \|  _| | |   |  _|| |     | || | | | |_) |
  | |_) | | |  __/_____|__) | |___| |___| |__| |___  | || |_| |  _ < 
  | .__/|_|  \___|    |____/|_____|_____|_____\____| |_| \___/|_| \_\\
  |_|                                                                
""")

    # https://github.com/IngoMeyer441/simple-term-menu # <- styling options and so on
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


if __name__ == "__main__":
    main()
