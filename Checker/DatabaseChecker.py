#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.getcwd() )
from ObjectInfo import DatabaseClass
from ObjectInfo import AdministratorClass
from ObjectInfo import Server
from CheckerEngine import CheckerEngine
import time, datetime
from System import Logger

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 18
# @Last at      Aprl. 18
# @Music        Sing a song at TV program - Shin Yong Jae.
# @Information  This class is made for checking the database system. This system is a child class of Checker Engine.
#           You must add some functions and values in this functions. that's all.

class DatabaseChecker( CheckerEngine) :
    def __init__(self, LocalServer=None, LocalDatabase=None, LocalAdmin=None ) :
        CheckerEngine.__init__(self, LocalServer, LocalDatabase, LocalAdmin)
        self.Logger = Logger.Logger(self)
        self.EngineName = "DATABASECHECKER"

    def CheckerConditionCheck(self) :
        isOkay, msg = self.CheckerConditionCheck()
        if( isOkay ) : 
            return True, "Good"
        else :
            return False, msg
        
    