# Imports
import os
import sys

# Vars
workdir = sys.argv[-1] # "./" # dir to work in
extensions = set()

# Check if any path has been given:
if len(sys.argv) == 1:
    sys.exit("You need to give path to dir!!!")
    
# Get distinct extensions:
for root, dirs, files in os.walk(workdir):
    if ".git" not in root:
        for file in files:
            pathname, exten = os.path.splitext(file)
            if (exten != ""):
                extensions.add(exten[1:])
                #                    ^ removing the first char (`.`)
            else:
                extensions.add(pathname[1:])
                #                       ^ removing the first char (`.`)

# Sort extensions alphabetical:
extensions = sorted(extensions)

# Print extensions:
os.system('cls' if os.name == 'nt' else 'clear')
for ext in extensions:
    print(ext)

exit()
