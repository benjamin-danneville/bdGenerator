============
Installation
============

This will cover how to install the bdGenerator script 
on Maya 2020 and Maya 2022 (With Python 3).

1- Rename 'bdGenerator-master' folder containing the README.md, bdGenerator.py and logo folder into 'bdGenerator'

2- You must put the 'bdGenerator' folder into you document > maya > script folder

3- Copy/paste this into your script editor, select everything and drop it into your selected shelf and select Python :

import sys
sys.path.append("C:/Users/Benjamin/Documents/maya/scripts/bdGenerator")

import bdGenerator
reload(bdGenerator)

4- Launch the script by pressing the button you've just created

--------------------
Maya 2020 (Python 2)
--------------------

--------------------
Maya 2022 (Python 3)
--------------------

For instructions on how to use it, check my video here:
https://www.benjamindanneville.com/generateur