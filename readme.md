wallabag-cli
==========
Wallabag-cli is a command line client for the self hosted read-it-later app wallabag.
Unlike to other services, wallabag is free and open source.

---
Warning
------

Wallabag-cli is in a very early stage of development and not suitable for productive use!

------

**How to use:**
- Install python 3.4.2 or above
- Install all missing dependencies via pip  
  `pip install -r requirements.txt`
- Create a config file  
  `wallabag.py config`
- Run the help to see how to get started  
  `wallabag.py --help`
- Run wallabag.py

For a description on how to compile the whole project into a single binary look into the [build documentation](https://github.com/Nepochal/wallabag-cli/blob/master/docs/build.md).


------

**Already implemented features**

- Add new entries

**Missing features**

- Delete entries
- Mark existing entries as read
- Mark existing entries as starred
- List entries (read, unread, starred, all)
- Show entry
- Curses interface for interactive use
