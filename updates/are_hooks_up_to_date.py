#!/usr/bin/env python3

# Imports
from requests import get

# Vars
url = "https://pre-commit.com/all-hooks.json"
local_file = r"../hooks.json"

# Funcs
def main():
    # Get JSON from url (updated from website):
    response = get(url)

    # Read local `hooks.json` file:
    with open(local_file) as f:
        contents = f.read()

        # Checking if they're the same (TO MAKE SURE THEY ARE YOU CAN USE: `curl https://pre-commit.com/all-hooks.json >> hooks.json`)
        print("Are hooks up to date: " + str(response.text == contents))

    f.close()


if __name__ == "__main__":
    main()
