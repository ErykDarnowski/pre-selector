#!/usr/bin/env python3

# Imports
import json

# Vars
json_file = open("hook_ext_pairs.json")
data = json.load(json_file)

print(data)
