#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 12
# @Last at      Aprl. 13
# @Music        Do you heare the people sing? (Les miserables), To X-Girlfriend (san-E)
# @Information  This class is only for server each of being managed.
#               Unfortunately, now, if your DB is not 'postgreSQl', you can't control it.
from Logger import Logger
from pexpect import pxssh

sys.path.insert(0, os.getcwd() )
from ObjectInfo import DatabaseClass
from ObjectInfo import AdministratorClass
import time, datetime

class Configurator(object) :
    # Configurator supports functions which are about 'connect', 'back-up scheduling' ..
    # You can write some special functions in here to expand your own servers
    def Shell_login(self, Shell, Hostname, Username, Password) :
        # as same as Connector function named 'Shell_login'
        Shell.login( Hostname, Username, Password )
        Shell.prompt()
        print("Log 24 at Configurator" + Shell.before)


    def Shell_logout(self, Shell) :
        s.logout()


    def SendLog_NotConnecting(self, ExceptionClass) :
        ServerLogger = Logger( self.Server )
        # ReportType, Path, Name, Content
        s = str(datetime.datetime.now())
        CONTENT = "The server host (" + str(self.Server.ID) +") has some issue to connect. \
                    here is the log from server host." + str(ExceptionClass) + " This log \
                    is written at Configurator-SendLog_Notconnecting. Today date is " + \
                    s + " Log end. "

        RK = ServerLogger.MakeReport( 'WARNING_SERVICE_REPORT', self.Admin.PATH, self.Admin.NAME, CONTENT)
        ServerLogger.push_log('CONNECT', str(self.Server.ID), RK, 'KNOWN_LOG', 'BAD', 'PXSSHEXCEPTION', 'SERVERCLASS')

    def ConnectSSH(self) :
        # as similar as Connector's Connect_Servers

        try :
            sh = pxssh.pxssh()
            hostname = self.Server.CONNECTION_IPADDRESS
            username = self.Server.CONNECTION_USERNAME
            password = self.Server.CONNECTION_PASSWORD

            self.Shell_login(sh, hostname, username, password)

        except pxssh.ExceptionPxssh as e :
            self.SendLog_NotConnecting(e)


    def __init__(self) :
        self.Logger = Logger( Configurator )


    def __init__(self, object, adminObject) :
        # Configurator must control server only < at Aprl 13 >
        # If configurator becomes bigger and has to support more functions,
        # code it on here.
        print("asdf", str(object))
        if( str(object) == "Server" ) :
            self.master = "Server"
            self.Server = object
            self.Admin = adminObject


    def __str__(self) :
        return 'Configurator'





def ParseDataList_FromPath(FilePath) :
    # returns file contents in 'FilePath'
    # You can check your dir by using'print(os.getcwd())'
    File = open(str(FilePath), "r")
    return File.readlines()




#
#       The codes below over here are for test.
#       Last updated at Aprl 13. < Tough cookie - Zico (feat. Don.mills) >

def ParseSortCont_FromString(List_forParse):
    # It only returns two data which are Sort and Content of string in listself.
    # EX) NAME:Wonseok
    # Sort = Name, Content = Wonseok
    ParsedStr = List_forParse.split('=')
    Sort = str(ParsedStr[0])
    Content = str(ParsedStr[1]).strip()
    return Sort, Content


class testClass(object):

    def __init__ (self) :
        # logger SETTINGS
        print("DB class is made")
        self.db = DatabaseClass.DB()
        self.LoadDBFiles()


    def __str__(self) :
        return "Server"


    def LoadDBFiles(self):
        # ParseDataFromPath returns list in file contents
        # This function returns nothing
        print("load is complete")
        DatabaseData = ParseDataList_FromPath("./ProgramSettings/DataBaseSettings.txt")
        for i in range(0, len(DatabaseData)) :
            Sort, Content = ParseSortCont_FromString( DatabaseData[i] )
            if Sort == 'SORTS' :
                self.db.SORTS = Content
            elif Sort == 'USER' :
                self.db.USER = Content
            elif Sort == 'HOST' :
                self.db.HOST = Content
            elif Sort == 'PORT' :
                self.db.PORT = Content
            elif Sort == 'NAME' :
                self.db.NAME = Content
            elif Sort == 'PW' :
                self.db.PW = Content
            else : # For catch the error
                print (' INPUT ERROR AT DB SETTINGS.TXT ' )
                print (' (Input) Sort : ', Sort, ' Content : ', Content)
        # # END LOOP & for check
        # self.DB.printInfo()N

if __name__ == "__main__" :
    TestClass = testClass()
    Conf1 = Configurator(TestClass)
