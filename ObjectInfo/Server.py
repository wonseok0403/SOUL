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

class Server (object) :

    def __init__(self, i=None, p=None, s=None, ip=None, pa=None, u=None, n=None, id=None, os=None, Na=None, IE=None, LST_DATE=None, db_key=None, obj_key=None) :
        self.ID = i                     # Primary Key for DB
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
                owner_info = cur.fetchall()
            
            except psycopg2.Error as e :
                print(e)
        
    def __str__ (self) :
        # upper only
        return "SERVER"


#
#       Test if server can have Administrator and Database
#
if __name__ == "__main__" :
    S = Server(1, 22, 'ssh', '45.77.177.76', '3@mHze=5K{1wj){}', 'root', 'Wonseok.J', 970403, 'ubuntu', 'wonseokbuntu', None, '2018-03-02', None, None)
    S.DB = DB("psql", "'localhost'", "'5432'", "'testdb'", "'1234'", "'test'")
    S.DB.Connect_DB()
    S.Admin = Administrator()
    S.local_admin = S.GetServerOwner()


#
#   Develop Log ( Aprl 15 )
#

# Aprl 15
#  Desginer Wonseok. J
#
#  I think server has to have connector's function named 'Connect_Servers)
#  So I copied that function to Server.py