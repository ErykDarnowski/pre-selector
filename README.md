# pre-SELECTOR

A python program to ease picking [**pre-commit**](https://pre-commit.com/) hooks.

![image](https://user-images.githubusercontent.com/81530705/197750175-39cc431d-1daa-410b-b2fa-4f1009700f5f.png)

## TODO

- Prep for open source (GIST)
<!-- -->
- Run in path where command is called + write the MD files there?
- Make sure the path given in arg has correct format (`/`) - will be taken from where command is run
- [Building Beautiful Command Line Interfaces with Python](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)
- Don't run when `.git` isn't detected?
  - When repo is not found, shows message
  - If there is a repo in a repo, it get's the "closest" repo
  - Command can be run anywhere in a repo (it finds the root by itself)
- Ext to hook group pairing
  - Automatically add hooks related to git
  - Figure out sorting of the hook group texts?
  - Fix the `directories` / `extensions` / `files` situation in `hook_ext_pairs.json`
- `generate_output_files.py`
  - TOC generation
  - alphabetical sorting
  - remove new lines from templates (nicer code but harder to edit)
- Add diff view of updated file display?
  - <https://docs.python.org/3/library/difflib.html>
- Implement proper import solution
  - <https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files>
  - <https://csatlas.com/python-import-file-module/>
- `get_ext-git.py`
  - <https://stackoverflow.com/a/8578096/11749019>
  - <https://stackoverflow.com/a/15315667/11749019>
  - <https://stackoverflow.com/questions/67673018/how-to-execute-raw-git-commands-from-gitpython>
  - <https://python.hotexamples.com/examples/git/Git/execute/python-git-execute-method-examples.html>
<!-- -->
- Modes
  - Select everything by yourself mode (language / name and such)
    - Show detected ext to ease the process? (do so by highlighting certain hook groups?)
    - Add a search function and pick by checking off a group? (this will then get printed in to an MD file to pick the exact hooks)
  - Auto select the language ones by detecting ext and than add additional ones yourself
    - Figure out the exact process (step by step)
    - Figure out better approach to getting file extensions
      - Count amount of each file?
      - Only get files that aren't in `.gitignore`
        - `git ls-files` (BUT everything needs to be at least staged - check out command options?)
        - exclude files like `.gitignore` itself and other git files
        - <https://waylonwalker.com/python-git/>
        - <https://unix.stackexchange.com/a/358286>
        - <https://stackoverflow.com/a/51170709/11749019>
        - <https://gitpython.readthedocs.io/en/0.3.5/tutorial.html>
      - Figure out edge cases
        - `run` / `artisan` (no ext) try getting from shebang?
        - `.env.testing` / `.add.spl` (combined ext)
        - `.gitattribute` (file names that are the ext)
<!-- -->
- Check if the script really gets all extensions
- Fix up things like missing descriptions and so on in `hook_ext_pairs` (from `hooks.json`)
- Add spinner animations (Sciagi)?
- Error catching + clear messages
  - internet (update check scripts)
- Make sure it works on other OSs
- [How to build and distribute a CLI Tool with Python](https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78)
  - Add `requirements.txt` file
    - <https://www.google.com/search?q=requirements+file&oq=requirements+file&aqs=chrome..69i57.2414j0j1&sourceid=chrome&ie=UTF-8>
    - <https://stackoverflow.com/a/41117308/11749019>

## Files

| File                              | Description                                                                                                                                                                                                                                                                                                     |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `menu.py`                         | Prototype of the program's initial menu screen.                                                                                                                                                                                                                                                                 |
| `get_ext.py`                      | Prints distinct extensions in path given as argument.                                                                                                                                                                                                                                                           |
| `is_git_repo.py`                  | Checks whether path given in argument contains git repository.                                                                                                                                                                                                                                                  |
| `hooks_to_md.py`                  | Converts and prints `hooks.json` as Markdown (this way it's easier to edit when you're picking the exact hooks). Keep in mind you have to pipe it in to a file, like so: `./hooks_to_md.py >> markdown.md`.                                                                                                     |
| `convert_to_one_line.py`          | Converts a multi line piece of text (given in variable) describing a hook group (taken from a Markdown file generated by `hooks_to_md.py`) in to one line required by JSON in `hook_ext_pairs.json`.                                                                                                            |
| `generate_output_files.py`        | Writes the output files containing information such as auto picked hook groups, other available ones and so on.                                                                                                                                                                                                 |
| `find_hook_group_for_ext.py`      | Print the right text (hook group) from `hook_ext_pairs.json` for extension given as argument.                                                                                                                                                                                                                   |
| `updates/were_hooks_added.py`     | Check line number difference in local `hooks.json` file and the one hosted on the **pre-commit** website: <https://pre-commit.com/all-hooks.json> to determine whether a hook was added (the approach is supposed to not allow for things like version number bumps to trigger an update alert).                |
| `updates/are_hooks_up_to_date.py` | Check for any difference between the local `hooks.json` file and the one hosted on the **pre-commit** website: <https://pre-commit.com/all-hooks.json> to determine whether anything was changed (this approach is supposed to allow for things like version number bumps and such to trigger an update alert). |
