# Quick start guide

*Notice:*
This is a very basic quick start guide. It will be improved once the program is feature-complete.

Please make sure that you meet the [requirements](requirements.md) and [installed](installation.md) the tool properly.

The command `wallabag` has always to be replaces with `wallabag.py` if you installed wallabag-cli from sources.

---

## Configuration

Wallabag-cli needs some information. You can run `wallabag config` to run an interactive configuration wizard.

Use `wallabag config --help` to see a list of possible parameters.

---

## Usage

Wallabag-cli is entirely used via command line inputs. The syntax is always  
`wallabag <command> <parameters>`

For example:  
`wallabag list --read --count=50`  
This lists the last 50 read articles.

Use `wallabag --help` to see a list of all valid commands.  
To see all parameters for a command you can type `wallabag <command> --help`
