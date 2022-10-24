#!/usr/bin/env python3

# Imports
import os
import sys
import json

# Vars
json_file = open("hook_ext_pairs.json")
hook_list = json.load(json_file)

# Check if extension arg was given:
if len(sys.argv) != 1:
    extension = sys.argv[-1]
else:
    sys.exit("Specify extension!")

# Clear screen (get this from a helper file):
os.system("cls" if os.name == "nt" else "clear")

# Loop through all groups
for group in hook_list:
    if "directories" in hook_list[group]:
        final = hook_list[group]["directories"]
    else:
        final = hook_list[group]["extensions"]

    # Checking if ext given in arg is in extensions / directories list (THIS NEEDS TO BE FIXED):
    if extension in final:
        print(hook_list[group]["text"])
