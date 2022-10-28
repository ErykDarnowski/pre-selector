#!/usr/bin/env python3

# Imports
import os
import sys
import git
import pathlib
from prettytable import PrettyTable

# Vars
path = sys.argv[-1]  # dir to work in (scan)
g = git.Git(path)

# Check if any path has been given:
if len(sys.argv) == 1:
    sys.exit("You need to give path to dir!!!")


files = g.execute(["git", "ls-files"]).split("\n")

# GET THIS FROM HELPER FILE!
os.system("cls" if os.name == "nt" else "clear")

t = PrettyTable(["Num", "Path", "Ext (suffix)", "Ext (suffixes)", "Ext (splitext)"])
t.align = "l"
for i in range(0, len(files)):
    # print(f"{i + 1}. {files[i]} = {pathlib.Path(files[i]).suffix} / {pathlib.Path(files[i]).suffixes} / {os.path.splitext(files[i])[1]}") # <- joing the suffixes? / use suffix?
    t.add_row(
        [
            i + 1,
            files[i],
            pathlib.Path(files[i]).suffix,
            pathlib.Path(files[i]).suffixes,
            os.path.splitext(files[i])[1],
        ]
    )

print(t)
