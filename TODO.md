# TODO

- Prep for open source?
<!-- -->
- What about possibility of custom hooks?
- Print final result in to MD file and let user pick and choose final hooks
- Create a JSON with ext to hook text pairs and from it get the hooks based on found ext
<!-- -->
- Modes
  - Select everything by yourself mode (language / name and such)
  - Auto select the language ones by detecting ext and than add additional ones yourself
    - Count amount of each file?
    - Check if the script really gets all extensions
    - Blacklist certain directories (like `.expo cache`) / make the user do that manually?
    - Print ext that couldn't be paired with any hooks and print other available hooks (ones that are not language specific) so people can find new stuff
    - Figure out edge cases
      - `run` / `artisan` (no ext)
      - `.env.testing` / `.add.spl` (combined ext)
