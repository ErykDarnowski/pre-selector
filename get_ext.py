# Imports
import os
import sys

# Vars
workdir = sys.argv[-1] # "./" # dir to work in
extensions = set()

# Check if any path has been given:
if len(sys.argv) == 1:
    print("You need to give path to dir!!!")
    exit()

# Get distinct extensions:
for root, dirs, files in os.walk(workdir):
    if ".git" not in root:
        for file in files:
            pathname, exten = os.path.splitext(file)
            if (exten != ""):
                extensions.add(exten)
            else:
                extensions.add(pathname)

# Print distinct extensions:
for ext in extensions:
    print(ext)

exit()
