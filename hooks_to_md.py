"""TODO
- links
- font colors / weights
- numbers or something to write down good ones
"""

# Imports
import json

# Vars
jsonFile = open('hooks.json')
data = json.load(jsonFile)
counter = 0
 
# Getting + printing values:
for category in data:
    print('\n' + category)
    for hook in data[category]:
        if "description" in hook:
            description = hook["description"]
        else:
            description = hook["name"]

        print('  * ' + hook["id"] + ' - ' + description)
        counter += 1

print('\n\nHooks: ' + str(counter))

# Closing JSON file
jsonFile.close()
