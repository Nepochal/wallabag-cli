**Notice**

This document describes the compilation of the whole project into one single file. If you only want to execute the program use the description in the [readme](https://github.com/Nepochal/wallabag-cli/blob/master/readme.md).

---

1. Install python 3.4.2 or above
2. Install missing dependencies via pip  
   `pip install -r requirements.txt`
3. Install pyinstaller  
   `pip install pyinstaller`
4. Switch to the wallabag subfolder
5. From within the main folder build the project.

   On Linux or Cygwin:
   ```
   pyinstaller -F \
     wallabag.py \
     api.py \
     conf.py \
     entry.py \
     wallabag_add.py \
     wallabag_config.py \
     wallabag_help.py \
     wallabag_list.py
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
     wallabag_help.py ^
     wallabag_list.py   
   ```

The executable will be in the dist-folder.
