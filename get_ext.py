#!/usr/bin/env python3

# Imports
import os
import sys

# Vars
extensions = set()
workdir = sys.argv[-1]  # dir to work in (scan)
dir_blacklist = [".git", "DEV"]
ext_blacklist = [".spl"]


# Check if any path has been given:
if len(sys.argv) == 1:
    sys.exit("You need to give path to dir!!!")

# Get distinct extensions:
for root, dirs, files in os.walk(workdir):
    # Not looking through blacklisted dirs:
    print(root.replace(workdir, ""))
    # if any(dir in root for dir in dir_blacklist):
    if ".git" not in root:
        for file in files:
            pathname, exten = os.path.splitext(file)

            # Checking if extension is missing (for files like: `.gitignore`) for example:
            if exten != "":
                final = exten  # .replace(".", "")
            else:
                final = pathname  # .replace(".", "")

            # Not adding blacklisted extensions:
            if final not in ext_blacklist:
                extensions.add(final)

# Sort extensions alphabetical:
extensions = sorted(extensions)

# Print extensions:
os.system("cls" if os.name == "nt" else "clear")
for ext in extensions:
    print(ext)

exit()
