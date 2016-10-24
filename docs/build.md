**Notice**

This document describes the compilation of the whole project into one single file. If you only want to execute the program use the description in the [readme](https://github.com/Nepochal/wallabag-cli/blob/master/readme.md).

---

1. Install python 3.4.2 or above
2. Install missing dependencies via pip  
   `pip install -r requirements.txt`
3. Install pyinstaller  
   `pip install pyinstaller`
4. From within the main folder build the project.

   On Linux or Cygwin:
   ```
   pyinstaller -F \
     wallabag/wallabag.py \
     wallabag/api.py \
     wallabag/conf.py \
     wallabag/wallabag_add.py \
     wallabag/wallabag_config.py \
     wallabag/wallabag_help.py
   ```

   On Windows:
   ```
   pyinstaller -F ^
     wallabag/wallabag.py ^
     wallabag/api.py ^
     wallabag/conf.py ^
     wallabag/wallabag_add.py ^
     wallabag/wallabag_config.py ^
     wallabag/wallabag_help.py   
   ```

The executable will be in the dist-folder.
