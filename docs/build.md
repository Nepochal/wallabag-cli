# Compile a binary

1. Install python 3.4.2 or above
2. Install missing dependencies via pip<br>
  `pip install -r requirements.txt`
3. Install pyinstaller<br>
  `pip install pyinstaller`
4. Switch to the wallabag subfolder
5. Build the project

  On Linux or Cygwin:

  ```
  pyinstaller -F \
    wallabag.py \
    api.py \
    conf.py \
    entry.py \
    wallabag_add.py \
    wallabag_config.py \
    wallabag_delete.py \
    wallabag_export.py \
    wallabag_help.py \
    wallabag_list.py \
    wallabag_show.py \
    wallabag_update.py
  ```

  On Windows:

  ```
  pyinstaller -F ^
    wallabag.py ^
    api.py ^
    conf.py ^
    entry.py ^
    wallabag_add.py ^
    wallabag_config.py ^
    wallabag_delete.py ^
    wallabag_export.py ^
    wallabag_help.py ^
    wallabag_list.py ^
    wallabag_show.py ^
    wallabag_update.py
  ```

The executable will be in the dist-folder. It needs a working python 3 installation. The pip-modules listed in requirements.txt are not necessary.
