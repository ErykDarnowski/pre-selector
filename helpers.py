#!/usr/bin/env python3

# Imports:
import os

# Funcs:

# Clears the terminal:
def clear_term():
    os.system("cls" if os.name == "nt" else "clear")
