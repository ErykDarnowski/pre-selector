#!/usr/bin/env python3

# Imports
import requests

# Vars
url = "https://pre-commit.com/all-hooks.json"
local_file = "hooks.json"
website_lines = 0

# Funcs
def main():
    # Get JSON from url (updated from website):
    response = requests.get(url)

    # GET LINES IN A BETTER WAY!!!
    website_lines = response.text.split('\n')

    # Read local `hooks.json` file:
    with open(local_file) as f:
        local_lines = f.read().split('\n')

        # Checking if they're the same length (avoids reacting to version changes) [TO MAKE SURE THEY ARE YOU CAN USE: `curl https://pre-commit.com/all-hooks.json >> hooks.json`]
        print("Could a new hook been added: " + str(website_lines != local_lines))
    f.close()


if __name__ == "__main__":
    main()
