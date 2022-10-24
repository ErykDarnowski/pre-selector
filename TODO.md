# TODO

- Prep for open source?
<!-- -->
- Error catching + msgs
- Add spinner animations (Sciagi)?
- Suggest the possibility of custom hooks?
- Create a JSON with ext to hook text pairs and from it get the hooks based on found ext
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
