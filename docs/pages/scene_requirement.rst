======================
Maya scene requirement
======================

.. contents:: Overview
   :depth: 3


Setup
=====

------
Meshes
------

--------------
Configurations
--------------

- Configuration groups only contains locators
- Each locators must have a string attribute named "Variation_obj"

| **Configuration groups only contains locators :**
| It's important because otherwise, the script can not make the difference 
| between a configuration group and a blocking group
| 
| **Each locators must have a string attribute named "Variation_obj" :**
| It's important because otherwise, the script can not make the difference 
| between a configuration group and a blocking group

Purpose of the configurations
-----------------------------

Purpose of the locators
-----------------------

When to use multiple locators
-----------------------------

When to use multiple configurations
-----------------------------------



Blocking
========

- Blocking groups only contains meshes
- Blocking groups must be named with ``_grp`` at the end
- Meshes has not been freeze transformed

.. image:: images/scene_requirement/Blocking_Outline.png

| **Blocking groups only contains meshes :**
| It's important because otherwise, the script can not make the difference 
| between a blocking group and a configuration group
|
| **Meshes has not been freeze transformed :**
| The group of meshes that will be created by the script will be placed
| at the position and orientation of the blocking meshes' pivot.
| So if you want the generation to be in the right orientation,
| please don't freeze transform your blocking

