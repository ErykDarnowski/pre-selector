#!/usr/bin/env python3

# Imports
import os
import sys
from shutil import rmtree

# Vars
workdir = sys.argv[-1]  # dir to work in (scan)
md_folder_name = "/pre-SELECTOR"

unmatched_extensions = ["run", "artisan", ".sh"]
other_groups = ["Terraform", "GO"]
picked_texts = [
    [
        "Git",
        "- <https://github.com/milin/gitown>\n  - gitown = Keep your CODEOWNERS file up to date to streamline code review process.\n\n- <https://github.com/homebysix/pre-commit-macadmin>\n  - check-git-config-email = This hook checks to ensure the Git config email matches one of the specified domains.\n",
    ],
    [
        "Swift",
        "- <https://github.com/nicklockwood/SwiftFormat>\n  - swiftformat = Check swift files for formating issues with SwiftFormat\n\n- <https://github.com/realm/SwiftLint>\n  - swiftlint = Check Swift files for issues with SwiftLint",
    ],
]
other_texts = [
    [
        "Git",
        "- <https://github.com/milin/gitown>\n  - gitown = Keep your CODEOWNERS file up to date to streamline code review process.\n\n- <https://github.com/homebysix/pre-commit-macadmin>\n  - check-git-config-email = This hook checks to ensure the Git config email matches one of the specified domains.\n",
    ],
    [
        "Swift",
        "- <https://github.com/nicklockwood/SwiftFormat>\n  - swiftformat = Check swift files for formating issues with SwiftFormat\n\n- <https://github.com/realm/SwiftLint>\n  - swiftlint = Check Swift files for issues with SwiftLint",
    ],
]


# Check if any path has been given:
if len(sys.argv) == 1:
    sys.exit("You need to give path to dir!!!")

# Check if the output folder already exists and ask to overwrite?
if os.path.isdir(workdir + md_folder_name):
    response = input(
        "Output files already exist, would you like to overwrite them? [y/N]: "
    )
    if response == "y" or response == "Y":
        # Remove output dir:
        rmtree(workdir + md_folder_name)
    else:
        exit()


# Create dir for the md files:
os.mkdir(workdir + md_folder_name)

# Write `final.md` (main) file:
file = open(workdir + md_folder_name + "/final.md", "a")
file.write(
    """# Final

## Table of contents

[TOC]

## Unmatched extensions

These are extensions that couldn't be matched to any text pair in `hook_ext_pairs.json` file:

"""
)

# Print unmatched extensions:
for ext in unmatched_extensions:
    file.write("- " + ext + "\n")

file.write(
    """
## Other available hook groups

These are the hook groups that are not language specific and are available (you might like to check out what you may want to use):

"""
)

# Print other available hook groups (not language based):
for group in other_groups:
    file.write(f"- {group}\n")

file.write(
    """
You can view them in: `other.md`

## Suggestion (custom hooks)

You of course can find / write your own custom hooks and don't have to soley relly on **pre-commit** ones. (you can expand)

## Picked hook groups

"""
)

file.write(f"These are the auto picked hook groups based on extensions found in: `{workdir}`:\n\n")

# Print matched hook groups:
for group in picked_texts:
    file.write(f"### {group[0]}\n\n")
    file.write(group[1] + "\n")

file.close()

# Generate table of contents in `final.md` file:

# Write `other.md` (secondary) file:
file = open(workdir + md_folder_name + "/other.md", "a")
file.write(
    """# Other

## Table of contents

[TOC]

## Other hook groups

"""
)

# Print other hook groups:
for group in other_texts:
    file.write(f"### {group[0]}\n\n")
    file.write(group[1] + "\n")

file.close()
