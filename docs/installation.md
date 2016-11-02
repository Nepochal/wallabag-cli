# Installation

There are two ways to install wallabag-cli. You can either use a prebuild file or the sources.<br>
The prebuild file is easier to use. The sources can be used on every operating system and architecture.<br>
We suggest using the prebuild file if you are technically not skilled.

--------------------------------------------------------------------------------

## Prebuild binaries

- Download the latest binaries from our [release-page](https://github.com/Nepochal/wallabag-cli/releases) for your operating system
- Unzip them
- Done :)

On Linux you can make the program globally executable for each user by running the following commands:

```bash
sudo chown root:root wallabag
sudo chmod 755 wallabag
sudo mv wallabag /usr/local/bin
```

--------------------------------------------------------------------------------

## Sources

- Download the sources via git or from our [release-page](https://github.com/Nepochal/wallabag-cli/releases)
- Probably unzip them
- Install all missing python modules by executing<br>
  `pip install -r requirements.txt`<br>
  in the main folder
- The program can be executed by running the file wallabag.py in the wallabag-subfolder
