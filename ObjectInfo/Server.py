#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 5
# @Last at      Aprl. 15
# @Music        Castle of magic by MC Sniper
# @Information  This class is only for server each of being managed.
#               Unfortunately, now, if your DB is not 'postgreSQl', you can't control it.


from pexpect import pxssh       # Added at Aprl 15
import psycopg2
from DatabaseClass import DB
from AdministratorClass import Administrator
import time, datetime

import os, sys
sys.path.insert(0, os.getcwd())
from System import Logger
class Server (object) :

    def __init__(self, i=None, p=None, s=None, ip=None, pa=None, u=None, n=None, id=None, os=None, Na=None, IE=None, LST_DATE=None, db_key=None, obj_key=None) :
        self.ID = i                     # Primary Key for Serv
        self.CONNECTION_PORT = p        # Connection port ( ssh = 22 )
        self.CONNECTION_SORT = s        # ssh or ftp ...
        self.CONNECTION_IPADDRESS = ip  # 192.168.10.1 ..
        self.CONNECTION_PASSWORD = pa   # Wonseok...
        self.CONNECTION_USERNAME = u    # root
        self.OWNER_NAME = n             # Wonseok
        self.OWNER_ID = id              # key of wonseok. Primary key of Administrator will be a good point for understanding.
        self.SERVER_OS = os             # Ubuntu 16.04 ..
        self.SERVER_NAME = Na           # WonseokServer..
        self.IS_ERROR = IE              # True? False? or something
        self.CONNECTION_LASTDATE = LST_DATE
        self.DB_KEY = db_key
        self.OBJECT_KEY = obj_key

        self.DB= None
        self.Admin= None

        # Local is server's owner.
        self.local_db = None
        self.local_admin = None

    # Try connecting if server is okay
    # okay -> self.iserror= true, No -> self.iserror= false
    def isTryConnect(self) :
        try :
            shell = pxssh.pxssh()
            shell.login( self.CONNECTION_IPADDRESS, self.CONNECTION_USERNAME, self.CONNECTION_PASSWORD)
            shell.sendline('ls -al')
            shell.prompt()
            print( "before\n" + shell.before)

            shell.logout()
        
        except pxssh.ExceptionPxssh as e :
            self.IS_ERROR = "YES"   # Error occur
            return False, e

        self.IS_ERROR = None        # No error
        return True, 'GOOD'


    # Using this function makes you easier to throw command.
    def ThrowCommand(self, comd) :
        try : 
            shell = pxssh.pxssh()
            shell.login( self.CONNECTION_IPADDRESS, self.CONNECTION_USERNAME, self.CONNECTION_PASSWORD)
            shell.sendline(comd)
            shell.prompt()
            print("command : " + shell.before)

            shell.logout()

        except pxssh.ExceptionPxssh as e :
            ServerLogger = Logger.Logger(Server)                # Because, Logger is in other directory.
            self.SendLog_ThrowMsgError(ServerLogger, comd, e)
            return False, e
        
        return True, 'GOOD'


    # Using this function, you can get server's owner easy
    def GetServerOwner(self) :
        # @Return   True -> get admin information successfully, False -> No
        # @Befroe   You have to make sure that this server class has 'local_db'
        # Algo : Connect DB -> Using Foreinn key -> Get Admin's information -> put it in admin class
        if self.DB.IS_CONNECTED == False :
            print("This server doesn't have local database!\n \
                   You hae to execute db.Connect_DB first!")
            return False, "Not connected local_db"
        else :
            try :
                cur = self.DB.conn.cursor()
                cur.execute("SELECT * FROM administrator WHERE admin_key=" + str(self.OWNER_ID) )
                owner_info = cur.fetchall()     # administrator call succeed
            
            except psycopg2.Error as e :
                # send log
                print(e)
                return False, e
            
            except Exception as e :
                print('error:', e)
                ServerLogger = Logger.Logger(self)
                ServerLogger.PushLog_UnknownError(self.Admin, 'Server.GetServerOwner', e)
                return False, e
            
            # Make admin class
            if len(owner_info) != 1 :
                # Because of primary key, it won't happen.
                print('Owner is wrong! The system must have just one owner!')
            owner_info = owner_info[0]
            tmpAdmin = Administrator(owner_info[0], owner_info[1], owner_info[2], owner_info[3], owner_info[4])
            tmpAdmin.printInfo()

            # Initialize
            self.local_admin = tmpAdmin

            # Return success
            return True, "Success"

    #       Created at Aprl 17. with Say you love me please - red cheek puberty
    #       Below functions are loger.
    #       Written by Wonseok. J

    # This function is copied from Scheduler.SendLog_ThrowMsgError
    def SendLog_ThrowMsgError (self, Logger, command, ExceptionMsg) :
        # Log structure :
        ##   [ADMIN.ID] tried to throw [command] to [ServerID] by [ServerRole]@[Host] at [Date.time]
        ##   Server was [Server.isOkay]. And program tried to connect, but server connection is BAD.
        ##   specific report which pssh says is here : [Exception E]
        strLogMsg = str(self.Admin.ID) + " tried to throw " + str(command) + " to " + str(self.ID) + " by " + str(self.CONNECTION_USERNAME)+"@" + str(self.CONNECTION_IPADDRESS)  + " at " + str(datetime.datetime.now()) + "\n" + \
                    "Server was " + self.IS_ERROR + ". And program tried to connect, but server connection is BAD." + "\n" + \
                    "specific report which pssh says is here : " + str(ExceptionMsg)
        Logger.SetOrigin('KNOWN_LOG')
        RK = Logger.MakeReport( 'SERVICE_STATUS_CHECK', self.Admin.PATH, self.Admin.NAME, strLogMsg)
        Logger.push_log('REQ_COMMAND', self.ID, RK, 'KNOWN_LOG', 'BAD', 'Server.SendLog_ThrowMsgError', 'SERVER')

    def SendLog_ConnectionBad (self, Logger, ExceptionMsg) :
        # Log structure :
        ##   [ADMIN.ID] tried to connect [ServerID] by [ServerRole]@[Host] at [Date.time]
        ##   Server was [Server.isOkay]. And program tried to connect, but server connection is BAD.
        ##   specific report which pssh says is here : [Exception E]
        strLogMsg = str(self.Admin.ID) + " tried to connect " + str(self.ID) + " by " + str(self.CONNECTION_USERNAME)+"@" + str(self.CONNECTION_IPADDRESS)  + " at " + str(datetime.datetime.now()) + "\n" + \
                    "Server was " + self.IS_ERROR + ". And program tried to connect, but server connection is BAD." + "\n" + \
                    "specific report which pssh says is here : " + str(ExceptionMsg)
        Logger.SetOrigin('KNOWN_LOG')
        RK = Logger.MakeReport( 'SERVICE_STATUS_CHECK', self.Admin.PATH, self.Admin.NAME, strLogMsg)
        Logger.push_log( 'CONNECT', self.ID, RK, 'KNOWN_LOG', 'BAD', 'Server.SendLog_ConnectionBad', 'SERVER')


    def __str__ (self) :
        # upper only
        return "SERVER"

    def getInfo(self) :
        # CAUTION : DO NOT RETURN OTHER CLASS.
        # IF YOU DO THAT, THIS FUNCTION WILL MAKE FULL STACK RECURSIVE FUNCTION, AND MAKE 
        # STACK OVERFLOW ERROR. 
        strMsg = "ID = " + str(self.ID) + \
                "\nConnection_port = " + str(self.CONNECTION_PORT) + \
                "\nCONNECTION_SORT = " + str(self.CONNECTION_SORT) + \
                "\nCONNECTION_IPADDRESS = " + str(self.CONNECTION_IPADDRESS) + \
                "\nCONNECTION_PASSWORD = " + str(self.CONNECTION_PASSWORD) + \
                "\nCONNECTION_USERNAME = " + str(self.CONNECTION_USERNAME) + \
                "\nOWNER_NAME = " + str(self.OWNER_NAME) + \
                "\nOWNER_ID = " + str(self.OWNER_ID) + \
                "\nSERVER_OS = " + str(self.SERVER_OS) + \
                "\nSERVER_NAME = " + str(self.SERVER_NAME) + \
                "\nIS_ERROR = " + str(self.IS_ERROR) + \
                "\nCONNECTION_LASTDATE = " + str(self.CONNECTION_LASTDATE) + \
                "\nDB_KEY = " + str(self.DB_KEY) + \
                "\nOBJECT_KEY = " + str(self.OBJECT_KEY)
        return strMsg

#
#       Test if server can have Administrator and Database
#

if __name__ == "__main__" :
    S = Server(1, 22, 'ssh', '45.32.249.71', 'makeitpopwebuzzz!1', 'root', 'Wonseok.J', 1230, 'ubuntu', 'wonseokbuntu', None, '2018-03-02', None, None)
    S.DB = DB("psql", "'localhost'", "'5432'", "'testdb'", "'1234'", "'test'")
    S.DB.Connect_DB()
    S.Admin = Administrator('Wonseok', '/root/바탕화면/ServerPlayer/Report/', 'root', 'Admin', 'root')
    S.GetServerOwner()
    S.local_db = S.DB.AdminToDatabaseConnect( S.local_admin )


#
#   Develop Log ( Aprl 15 )
#

# Aprl 15
#   Desginer Wonseok. J
#
#  I think server has to have connector's function named 'Connect_Servers)
#  So I copied that function to Server.py
#
# Aprl 17
#   Designer Wonseok.J
#
#  I added some functions named GetServerOwner in this class. Just using this class, 
# You can get server's owner. And once you call this function, automatically server makes admin
# class. It will initialize that with server.
#  