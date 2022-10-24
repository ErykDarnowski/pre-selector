# Imports
import os
import sys

# Vars
workdir = sys.argv[-1] # "./" # dir to work in
file_blacklist = [".spl"]
extensions = set()

# Check if any path has been given:
if len(sys.argv) == 1:
    sys.exit("You need to give path to dir!!!")
    
# Get distinct extensions:
for root, dirs, files in os.walk(workdir):
    if ".git" not in root:
        for file in files:
            pathname, exten = os.path.splitext(file)

            # Checking if extension is missing (for files like: `.gitignore`) for example:
            if (exten != ""):
                final = exten#[1:]) # ^ removing the first char (`.`)
            else:
                final = pathname#[1:]) # < removing the first char (`.`)

            # Not adding blacklisted extensions:
            if final not in file_blacklist:
                extensions.add(final)

# Sort extensions alphabetical:
extensions = sorted(extensions)

# Print extensions:
os.system('cls' if os.name == 'nt' else 'clear')
for ext in extensions:
    print(ext)

exit()
