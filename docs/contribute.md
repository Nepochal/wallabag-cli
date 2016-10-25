# Obtain and run the source code

1. Obtain the source code via git<br>
  `git clone https://github.com/Nepochal/wallabag-cli.git`
2. Install python 3.4.2 or above
3. Install all missing dependencies via pip<br>
  `pip install -r requirements.txt`

The program can now be used by executing wallabag.py.

_Next steps_

- Create a config<br>
  `wallabag.py config`
- See the help<br>
  `wallabag.py --help`

--------------------------------------------------------------------------------

# About the project management and contribution

This project uses [semantic versioning](http://semver.org/).

All releases have a tag with the scheme "x.y.z-identifier". Identifiers can be alpha, beta, rc1, rc2... Final releases have no identifier.

The master-branch always heads on the latest release.<br>
The hotfix-branch includes bugfixes for the next hotfix-patch.<br>
The develop-branch consists of changes for the next feature-update.<br>
Every other branch is a temporary branch for a single purpose.

Feel free to send me issues or pull requests. If you wish to contribute than use a different new branch for the pull request.<br>
Pull requests on the master-, hotfix- or develop-branches will be rejected unseen!
