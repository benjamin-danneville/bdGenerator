##############################################################
## BENJAMIN DANNEVILLE                                      ##
## bdGenerator                                              ##
##                                                          ##
## Version : 0.1.6                                          ##
## Date : Septembre 2021                                    ##
## Website : https://www.benjamindanneville.com/generateur  ##
##############################################################

#########
## LIB ##
#########

import maya.cmds as cmds
import maya.mel as mel
import random

import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

#############
## GLOBALS ##
#############

#Stock latest groups created from last generation
geoDuplicatedObj_grp_list =[]
#Stock selected objects from last generation
selection_list = []

###############
## FUNCTIONS ##
###############

def Generator(reset):
    ## Handling both buttons ##
    ###########################
    
    #Reset selection list only if we "Gsenerate"
    if reset == 1:
        selection_list[:] = []
        selection = cmds.ls(sl=True)
        for i in range(len(selection)):
            selection_list.append(selection[i])
    else:
        selection = selection_list

    ## Variable ##
    ##############

    #Lists appended with the blocking's and configuration's groups
    config_grp_list = []
    geo_grp_list = []
    
    ## SORTING GROUPS ##
    ####################

    for i in range(len(selection)):
        #If first shape under selected groups' first object correspond to a locator, it's a configuration group 
        if (cmds.nodeType(cmds.listRelatives(cmds.listRelatives(selection[i])[0])[0]) == "locator"):
            config_grp_list.append(selection[i])
        #If first shape under selected groups' first object correspond to a locator, it's a blocking group
        elif (cmds.nodeType(cmds.listRelatives(cmds.listRelatives(selection[i])[0])[0]) == "mesh"):
            geo_grp_list.append(selection[i])

    ## Assembling ##
    ################

    geoDuplicatedObj_grp_list[:] = []

    for geo_grp in geo_grp_list:

        iteration = 0
        
        #Creating group and appending my list to be able to regenerate it with "Random" button
        geoDuplicatedObj_grp = cmds.group( em=True, name=geo_grp[0:-3] + "All_grp")
        geoDuplicatedObj_grp_list.append(geoDuplicatedObj_grp)

        for geo in cmds.listRelatives(geo_grp):
            iteration += 1

            #Creating group containing the assembly of objects
            obj_grp = cmds.group( em=True, name=geo_grp[0:-3] + str(iteration) + "_grp")

            #Choosing one configurations from the list
            random_config = random.choice(config_grp_list)

            for locator in cmds.listRelatives(random_config):
                #We have to exclude the shape of our configuration group, so that only the locators are left
                if not cmds.nodeType(locator) == "locator" :
                    variationObj_input = cmds.getAttr(locator + ".Variation_obj")
                    variationObj_output = variationObj_input.split(",")
                    #Choosing one of the possible meshes
                    randomObj_variation = random.choice(variationObj_output)   
                    duplicated = cmds.duplicate(randomObj_variation, n=randomObj_variation[0:-3] + "DUPLICATED_" + str(iteration) + "_geo")
                    #Moving it to our locator
                    cmds.parentConstraint(locator, duplicated, mo=False)
                    cmds.delete(duplicated[0] + "_parentConstraint1")

                    #Moving the object under the assembly group
                    cmds.parent(duplicated, obj_grp)
            #Center pivot the assembly group so that it correspond to the center of all objects inside.        
            cmds.select(obj_grp)
            mel.eval("CenterPivot;")
            #Moving the assembly group to an object from the blocking group
            cmds.parentConstraint(geo, obj_grp)
            cmds.delete(obj_grp + "_parentConstraint1")
            #Parenting it under a group containing all assembled groups
            cmds.parent(obj_grp, geoDuplicatedObj_grp)

############
## Button ##
############

def GeneratorButton(_):
    Generator(1)

def RandomButton(_):
    cmds.delete(geoDuplicatedObj_grp_list)
    Generator(0)

########
## UI ##
########

#Return maya main window as QWidget
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

#Extended QDialog Widget
class bdGeneratorWindow(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(bdGeneratorWindow, self).__init__(parent)

        #Window title and minimum width
        self.setWindowTitle("bdGenerator")
        self.setMinimumWidth(320)

        #Remove Question Mark
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        #Method Calling
        self.create_widgets()
        self.create_layouts()
    
    def create_widgets(self):
        self.textInstruction = QtWidgets.QLabel("Select all the blocking groups that you want to generate\nSelect all the config groups containing the locators\nClick the Generate button !", alignment=QtCore.Qt.AlignCenter)
        self.textRandom = QtWidgets.QLabel("You can generate new seeds by clicking on Random\n", alignment=QtCore.Qt.AlignCenter)
        self.creditName = QtWidgets.QLabel("copyright Benjamin Danneville", alignment=QtCore.Qt.AlignLeft)
        self.creditLicense = QtWidgets.QLabel("licence GNU GPL", alignment=QtCore.Qt.AlignRight)
        self.buttonGen = QtWidgets.QPushButton("Generate")
        self.buttonGen.clicked.connect(GeneratorButton)
        self.buttonRan = QtWidgets.QPushButton("Random")
        self.buttonRan.clicked.connect(RandomButton)

    def create_layouts(self):
        #Creating main vertical layout containg a vertical layout and a horizontal one
        main_layout = QtWidgets.QVBoxLayout(self)
        content_layout = QtWidgets.QVBoxLayout(self)
        credit_layout = QtWidgets.QHBoxLayout(self)

        content_layout.addWidget(self.textInstruction)
        content_layout.addWidget(self.textRandom)
        content_layout.addWidget(self.buttonGen)
        content_layout.addWidget(self.buttonRan)
        
        credit_layout.addWidget(self.creditName)
        credit_layout.addWidget(self.creditLicense)

        main_layout.addLayout(content_layout)
        main_layout.addLayout(credit_layout)

#If Dialog exists, it deletes it
try:
    Dialog.close()
except NameError:
    pass

#Show extend QDialog
Dialog = bdGeneratorWindow()
Dialog.show()