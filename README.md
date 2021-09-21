######################################################
## BENJAMIN DANNEVILLE                              ##
## bdGenerator                                      ##
##                                                  ##
## Version : 0.1.5                                  ##
## Date : Septembre 2021                            ##
## Website : https://www.benjamindanneville.com/    ##
######################################################

1- Rename 'bdGenerator-master' folder containing the README.md, bdGenerator.py and logo folder into 'bdGenerator'

2- You must put the 'bdGenerator' folder into you document > maya > script folder

3- Copy/paste this into your script editor, select everything and drop it into your selected shelf and select Python :

import sys
sys.path.append("C:/Users/Benjamin/Documents/maya/scripts/bdGenerator")

import bdGenerator
reload(bdGenerator)

4- Launch the script by pressing the button you've just created

For instructions on how to use it, check my video here:
https://www.benjamindanneville.com/generateur