# Requirements

- [an account on a wallabag instance](#server)
- [a valid wallabag api client credentials (client/secret)](#oauth2)
- [python 3.4.7 or above](#python)

If you want to run wallabag-cli directly from source you also need the following python modules:

- requests 2.11.1 or above

--------------------------------------------------------------------------------

# []()wallabag instance

Wallabag-cli only works with wallabag version 2.1.1 or above. To find the version number log into your wallabag-account and click on "about".

To host your own instance please read [the official documentation](http://doc.wallabag.org/en/master/user/installation.html).

Unfortunately the free instance [framabag](https://framabag.org/) is not usable until they switch to wallabag version 2.

--------------------------------------------------------------------------------

# []()wallabag api client credentials

If you have no api client credentials, you can create them on the web interface.<br>
Log in and click on "developer". Click on "Create a new client". Use a reasonable name (e.g. wallabag-cli). The value "Redirect URIs" can be ignored.<br>
After creation you can find your client ID and client secret under "Existing clients".

--------------------------------------------------------------------------------

# []()python

Please look on the [official site](https://www.python.org/) in order to install python on your system.
