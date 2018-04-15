#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 5
# @Last at      Aprl. 13
# @Music        Castle of magic by MC Sniper
# @Information  This class is only for server each of being managed.
#               Unfortunately, now, if your DB is not 'postgreSQl', you can't control it.


from pexpect import pxssh       # Added at Aprl 15
from DatabaseClass import DB
from AdministratorClass import Administrator

class Server (object) :

    def __init__(self, i=None, p=None, s=None, ip=None, pa=None, u=None, n=None, id=None, os=None, Na=None, IE=None, LST_DATE=None) :
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


    def isTryConnect(self) :
        try :
            shell = pxssh.pxssh()
            shell.login( self.CONNECTION_IPADDRESS, self.CONNECTION_USERNAME, self.CONNECTION_PASSWORD)
            shell.sendline('ls -al')
            shell.prompt()
            print( "before\n" + shell.before)

            shell.logout()
        
        except pxssh.ExceptionPxssh as e :
            return False, e

        return True, 'GOOD'


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


    def __str__ (self) :
        return "Server"



#
#       Test if server can have Administrator and Database
#
if __name__ == "__main__" :
    S = Server()
    S.DB = DB()
    S.Admin = Administrator()


#
#   Develop Log ( Aprl 15 )
#

# Aprl 15
#  Desginer Wonseok. J
#
#  I think server has to have connector's function named 'Connect_Servers)
#  So I copied that function to Server.py