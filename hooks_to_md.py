#!/usr/bin/env python3

# Imports
import json

# Vars
jsonFile = open("hooks.json")
data = json.load(jsonFile)
counter = 0

# Getting + printing values:
for group in data:
    # Printing header / new line after each group
    if counter != 0:
        print()
    else:
        print("# Hooks\n")

    print("- <" + group + ">")
    for hook in data[group]:
        if "description" in hook:
            description = hook["description"]
        else:
            description = hook["name"]

        print("  - " + hook["id"] + " = " + description)
        counter += 1

print("\n<p>Hook count:" + str(counter) + "</p>")

# Closing JSON file
jsonFile.close()
