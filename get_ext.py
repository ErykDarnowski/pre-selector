# Imports
import os
import sys

# Vars
workdir = sys.argv[-1] # "./" # dir to work in
extensions = set()

# Get the distinct extensions:
for root, dirs, files in os.walk(workdir):
    for file in files:
        pathname, exten = os.path.splitext(file)
        if (exten != ""):
            extensions.add(exten)

# Print them:
for ext in extensions:
    print(ext)
