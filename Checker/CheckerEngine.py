#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.getcwd() )
from ObjectInfo import DatabaseClass
from ObjectInfo import AdministratorClass
from ObjectInfo import Server
import time, datetime
from System import Logger

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 18
# @Last at      Aprl. 18
# @Music        
# @Information  This class is made for checking the system. You can check the system to use this class.
#           But if you want to make server checker, server checker must has server class,
#           And define some modules.
#            Database checker may need Database class. That's all.

class CheckerEngine (object) :
    def __init__(self, LocalServer=None, LocalDatabase=None, LocalAdmin=None) :
        # Checker must has local settings.
        self.LocalServer = LocalServer
        self.LocalDatabase = LocalDatabase
        self.db = self.LocalDatabase # for Logger
        self.LocalAdmin = LocalAdmin
        self.Logger = Logger.Logger(self)
        self.EngineName = "CHECKERENGINE"
        

    def CheckerConditionCheck(self) :
        # Server check.
        isOkay, Msg = self.LocalServer.isTryConnect()
        if( isOkay != True ) :
            self.SendLog_ServerConnectionBad(self.Logger, Msg)
            return False, "Program can not make a link with local server. Check the log."
            # Send Log
        isOkay, Msg = self.LocalDatabase.isTryConnect()
        if( isOkay != True ) :
            return False, "Program can not link with local database. check the log."
            self.SendLog_DatabaseConnectionBad(self.Logger, Msg)
            # Send Log
        if( str(self.LocalAdmin) != "ADMINISTRATORCLASS" ) :
            return False, "Program can not make a link with local administrator. Check the admin."
            # 여기 하면 됨
        return True, "Good"
            # Send Log

    def SendLog_ServerConnectionBad (self, Logger, ExceptionMsg) :
        # Log structure :
        ##   [ADMIN.ID] tried to connect [ServerID] by [ServerRole]@[Host] at [Date.time]
        ##   Server was [Server.isOkay]. And program tried to connect, but server connection is BAD.
        ##   specific report which pssh says is here : [Exception E]
        strLogMsg = str(self.LocalAdmin.ID) + " tried to connect " + str(self.LocalServer.ID) + " by " + str(self.LocalServer.CONNECTION_USERNAME)+"@" + str(self.LocalServer.CONNECTION_IPADDRESS)  + " at " + str(datetime.datetime.now()) + "\n" + \
                    "Server was " + self.LocalServer.IS_ERROR + ". And program tried to connect, but server connection is BAD." + "\n" + \
                    "specific report which pssh says is here : " + str(ExceptionMsg)
        Logger.SetOrigin('KNOWN_LOG')
        RK = Logger.MakeReport( 'SERVICE_STATUS_CHECK', self.LocalAdmin.PATH, self.LocalAdmin.NAME, strLogMsg)
        Logger.push_log( self.EngineName, self.LocalServer.ID, RK, 'KNOWN_LOG', 'BAD', 'CheckerEngine.SendLog_ConnectionBad', 'SERVER')

    
    def SendLog_DatabaseConnectionBad (self, Logger, ExceptionMsg) :
        # Log structure :
        ##   [ADMIN.ID] tried to connect Database ID : [DB_ID]
        ##   Database Setting is : 
        ##   SORTS, HOSTS, NAME, PW, USER, DB_KEY, IS_CONNECTED, OBJECT, SERVER_KEY :
        ##   Values;
        strLogMsg = str(self.LocalAdmin.ID) + " tried to connect Database ID : " + str(self.LocalDatabase.DB_KEY) + "\n" + \
                    "Database setting is : " + "\n" + \
                    "SORTS, HOSTS, NAME, PW, USER, DB_KEY, IS_CONNECTED, OBJECT, SERVER_KEY : " + "\n" + \
                    self.LocalDatabase.getInfo() + "\n" + \
                    "Exception Msg : " + ExceptionMsg + "\n"
        Logger.SetOrigin('KNOWN_LOG')
        RK = Logger.MakeReport( 'SERVICE_STATUS_CHECK', self.LocalAdmin.PATH, self.LocalAdmin.NAME, strLogMsg)
        Logger.push_log( self.EngineName, self.LocalAdmin.SERVER_KEY, RK, 'KNOWN_LOG', 'BAD', 'CheckerEngine.SendLog_ConnectionBad', 'SERVER')

    def __str__(self) :
        return "CHECKERENGINE"