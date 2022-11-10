# pre-SELECTOR

A python CLI tool to make setting up [**pre-commit**](https://pre-commit.com/) (picking hook groups) in projects simpler and faster (+ somewhat automated too)!

![image](https://user-images.githubusercontent.com/81530705/197750175-39cc431d-1daa-410b-b2fa-4f1009700f5f.png)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 orderedList=false} -->

<!-- code_chunk_output -->

- [pre-SELECTOR](#pre-selector)
  - [Development setup](#development-setup)
    - [Virtual environment](#virtual-environment)
      - [Initial commands](#initial-commands)
      - [Additional commands](#additional-commands)
  - [Files](#files)
  - [To flesh out](#to-flesh-out)

<!-- /code_chunk_output -->

<!-- FOR THE FUTURE:
## Table of Contents

[ TOC ]

## Instruction

1. Install by running: `pip install X`.
2. `cd` in to repo you'd like to add [**pre-commit**]() to.
3. Temporarily stage all your changes, like so: `git add -A`.
3. Run: `X`.
  - This command can be run anywhere in a repo (it finds the root dir by itself).
  - If there are 'recursive' repos (repos in repos), it get's the "closest" repo (meaning the first root dir it finds going up the dir tree).

## Development setup

### pre-commit
-->

---

## Development setup

### Virtual environment

The use of a virtual environment while working on python projects is strongly encouraged, as this approach has many benefits (which you can read up on [here](https://towardsdatascience.com/why-you-should-use-a-virtual-environment-for-every-python-project-c17dab3b0fd0))!

#### Initial commands

```bash
# 1. Create virtual env:
python3 -m venv venv

# 2. Activate virtual env:
source venv/bin/activate 

# 3. Install required pkgs:
pip install -r requirements.txt 
```

#### Additional commands

- To check whether the virtual environment is **activated** / **deactivated** you can run either of these two commands:

  *(if the command throws an error, the virtual environment isn't **activated**)*

  - ```bash
    pip -V | grep $PWD
    ```

  - ```bash
    echo $VIRTUAL_ENV | grep $PWD
    ```

- To **deactivate** and delete the virtual environment run:

  ```bash
  deactivate
  rm -rf venv # (optional)
  ```

- To update `pip` in the virtual environment, run:

  ```bash
  pip install --upgrade pip
  ```

- To use a `pip` package in the virtual environment, run:

  ```bash
  python3 -m <pkg_name>
  ```

- To install / uninstall `pip` packages in the virtual environment, run either:

  - ```bash
    pip install <pkg_name>
    ```

  - ```bash
    pip uninstall <pkg_name>
    ```

## Files

| File                              | Description                                                                                                                                                                                                                                                                                                     |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `menu.py`                         | Prototype of the program's initial menu screen.                                                                                                                                                                                                                                                                 |
| `get_ext.py`                      | Prints distinct extensions in path given as argument.                                                                                                                                                                                                                                                           |
| `is_git_repo.py`                  | Checks whether path given in argument contains git repository.                                                                                                                                                                                                                                                  |
| `get_ext-git.py`                  | Prints table of files and their extensions (meant to be a better approach than current one in `get_ext.py` as it uses `git ls-files` to only get the files 'important' for the repo).                                                                                                                           |
| `hooks_to_md.py`                  | Converts and prints `hooks.json` as Markdown (this way it's easier to edit when you're picking the exact hooks). Keep in mind you have to pipe it in to a file, like so: `./hooks_to_md.py >> markdown.md`.                                                                                                     |
| `convert_to_one_line.py`          | Converts a multi line piece of text (given in variable) describing a hook group (taken from a Markdown file generated by `hooks_to_md.py`) in to one line required by JSON in `hook_ext_pairs.json`.                                                                                                            |
| `generate_output_files.py`        | Writes the output files containing information such as auto picked hook groups, other available ones and so on.                                                                                                                                                                                                 |
| `find_hook_group_for_ext.py`      | Print the right text (hook group) from `hook_ext_pairs.json` for extension given as argument.                                                                                                                                                                                                                   |
| `updates/were_hooks_added.py`     | Check line number difference in local `hooks.json` file and the one hosted on the **pre-commit** website: <https://pre-commit.com/all-hooks.json> to determine whether a hook was added (the approach is supposed to not allow for things like version number bumps to trigger an update alert).                |
| `updates/are_hooks_up_to_date.py` | Check for any difference between the local `hooks.json` file and the one hosted on the **pre-commit** website: <https://pre-commit.com/all-hooks.json> to determine whether anything was changed (this approach is supposed to allow for things like version number bumps and such to trigger an update alert). |

## To flesh out

Things to test (find edge cases) / flesh out over time.

- `get_ext.py` (`git ls-files` behavior getting all files)
- `hook_ext_pairs.json` (hook group to ext matching)
- `detect_from_shebang.py` (matching to ext / variations of being able to write the same shebang)
