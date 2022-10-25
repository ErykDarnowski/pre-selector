# pre-SELECTOR

A python program to ease picking [**pre-commit**](https://pre-commit.com/) hooks.

![image](https://user-images.githubusercontent.com/81530705/197750175-39cc431d-1daa-410b-b2fa-4f1009700f5f.png)

## TODO

- Prep for open source
- Start using the `from` imports?
- Figure out sorting of the hook group texts?
- Add diff view of updated file display?
- Make sure the path given in arg has correct format (`/`)
- Run in path where command is called + write the MD files there?
- Fix the `directories` / `extensions` / `files` situation in the `hook_ext_pairs.json` file
- [Building Beautiful Command Line Interfaces with Python](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)
- `generate_output_files.py`
  - TOC generation
  - alphabetical sorting
  - remove new lines from templates (nicer code but harder to edit)
- Implement proper import solution
  - <https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files>
  - <https://csatlas.com/python-import-file-module/>
<!-- -->
- Modes
  - Select everything by yourself mode (language / name and such)
    - Add a search function and pick by checking off a group? (this will then get printed in to an MD file to pick the exact hooks)
  - Auto select the language ones by detecting ext and than add additional ones yourself
    - Figure out better solution for getting file extensions
      - Check if the script really gets all extensions
      - Count amount of each file?
      - Blacklist certain directories (like `.expo cache`) / make the user do that manually? - ONLY CHECK FILES THAT AREN'T IN GITIGNORE!!!
      - Figure out edge cases
        - `run` / `artisan` (no ext) try getting from shebang?
        - `.env.testing` / `.add.spl` (combined ext)
        - `.gitattribute` (file names that are the ext)
<!-- -->
- Fix up things like missing descriptions and so on in `hook_ext_pairs` (from `hooks.json`)
- Add spinner animations (Sciagi)?
- Error catching + clear messages
- Make sure it works on other OSs
- [How to build and distribute a CLI Tool with Python](https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78)
  - Add `requirements.txt` file
    - <https://www.google.com/search?q=requirements+file&oq=requirements+file&aqs=chrome..69i57.2414j0j1&sourceid=chrome&ie=UTF-8>
    - <https://stackoverflow.com/a/41117308/11749019>

## Files

| File                            | Description                                                                                                                                                                                                                                                                                                     |
| :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `menu.py`                       | Prototype of the program's initial menu screen.                                                                                                                                                                                                                                                                 |
| `get_ext.py`                    | Prints distinct extensions in path given as argument.                                                                                                                                                                                                                                                           |
| `hooks_to_md.py`                | Converts and prints `hooks.json` as Markdown (this way it's easier to edit when you're picking the exact hooks). Keep in mind you have to pipe it in to a file, like so: `./hooks_to_md.py >> markdown.md`.                                                                                                     |
| `convert_to_one_line.py`        | Converts a multi line piece of text (given in variable) describing a hook group (taken from a Markdown file generated by `hooks_to_md.py`) in to one line required by JSON in `hook_ext_pairs.json`.                                                                                                            |
| `generate_output_files.py`      | Writes the output files containing information such as auto picked hook groups, other available ones and so on.                                                                                                                                                                                                 |
| `find_hook_group_for_ext.py`    | Print the right text (hook group) from `hook_ext_pairs.json` for extension given as argument.                                                                                                                                                                                                                   |
| `updates/was_hook_added.py`     | Check line number difference in local `hooks.json` file and the one hosted on the **pre-commit** website: <https://pre-commit.com/all-hooks.json> to determine whether a hook was added (the approach is supposed to not allow for things like version number bumps to trigger an update alert).                |
| `updates/were_hooks_updated.py` | Check for any difference between the local `hooks.json` file and the one hosted on the **pre-commit** website: <https://pre-commit.com/all-hooks.json> to determine whether anything was changed (this approach is supposed to allow for things like version number bumps and such to trigger an update alert). |
