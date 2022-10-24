# TODO

- Suggest that custom hooks are available?
- Fix the `directories` / `extensions` thing with the `hook_ext_pairs.json` file
- Add requirements.txt file [res1](https://www.google.com/search?q=requirements+file&oq=requirements+file&aqs=chrome..69i57.2414j0j1&sourceid=chrome&ie=UTF-8) ; [res2](https://stackoverflow.com/a/41117308/11749019)
- Implement import solution [res1](https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files) ; [res2](https://csatlas.com/python-import-file-module/)
<!-- -->
- Modes
  - Select everything by yourself mode (language / name and such)
    - Add a search function and pick by checking off a group? (this will then get printed in to an MD file to pick the exact hooks)
  - Auto select the language ones by detecting ext and than add additional ones yourself
    - Count amount of each file?
    - Check if the script really gets all extensions
    - Blacklist certain directories (like `.expo cache`) / make the user do that manually?
    - Print (in to an MD file) extensions that couldn't be paired with any hooks, the picked hooks and other available hooks (ones that are not language specific) so people can find new stuff they may like to use
    - Figure out edge cases
      - `run` / `artisan` (no ext) try getting from shebang?
      - `.env.testing` / `.add.spl` (combined ext)
      - `.gitattribute` (file names that are the ext)
<!-- -->
- Add spinner animations (Sciagi)?
- Error catching + msgs
- Prep for open source?
