#!/usr/bin/env python3

text = """
- <https://github.com/pre-commit/pre-commit-hooks>
  - check-json = checks json files for parseable syntax.
  - pretty-format-json = sets a standard for formatting json files.

- <https://github.com/pre-commit/mirrors-fixmyjs>
  - fixmyjs = fixmyjs

- <https://github.com/pre-commit/mirrors-jshint>
  - jshint = 

- <https://github.com/elidupuis/mirrors-jscs>
  - jscs = jscs

- <https://github.com/Lucas-C/pre-commit-hooks-nodejs>
  - htmlhint = NodeJS HTML syntax linter (htmlhint)
  - htmllint = NodeJS HTML syntax linter (htmllint)
"""
counter = 0
final = ""

# Go through every line:
for line in text.split("\n"):
    # Checking if line is empty
    if line != "":
        # Checking if 0 level point or an inner one:
        if line[:1] == "-":
            # Not adding the 2 new lines if it's the first group
            if counter != 0:
                final += "\\n\\n" + line
            else:
                final += line
        else:
            final += "\\n" + line

        counter += 1

print(final)
