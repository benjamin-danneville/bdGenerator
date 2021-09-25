======================
Maya scene requirement
======================

.. contents:: Overview
   :depth: 2

--------
Blocking
--------

A blocking is composed of several groups, containing only meshes

.. image:: images/scene_requirement/Blocking_Outline.png


Key points
----------

- Groups only contains meshes
- Groups must be named with ``_grp`` at the end
- Meshes has not been freeze transformed

| **Groups only contains meshes :**
| It's important because otherwise, the script can not make the difference 
| between a blocking group and a configuration group

-------------
Configuration
-------------


