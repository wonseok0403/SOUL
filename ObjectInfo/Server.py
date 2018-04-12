#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 5
# @Last at      Aprl. 12
# @Music        주인공
# @Information  This class is only for server each of being managed.
#               Unfortunately, now, if your DB is not 'postgreSQl', you can't control it.


from DatabaseClass import DB
from AdministratorClass import Administrator

class Server (object) :

    def __init__(slef, i, p, s, ip, pa, u, n, id, os, Na, IE) :
        self.ID = i
        self.CONNECTION_PORT = p
        self.CONNECTION_SORT = s
        self.CONNECTION_IPADDRESS = ip
        self.CONNECTION_PASSWORD = pa
        self.CONNECTION_USERNAME = u
        self.OWNER_NAME = n
        self.OWNER_ID = id
        self.SERVER_OS = os
        self.SERVER_NAME = Na
        self.IS_ERROR = IE


    def __init__ (self) :
        self.ID = ""
        self.CONNECTION_PORT = ""
        self.CONNECTION_SORT = ""
        self.CONNECTION_IPADDRESS = ""
        self.CONNECTION_PASSWORD = ""
        self.CONNECTION_USERNAME = ""
        self.OWNER_NAME = ""
        self.OWNER_ID = ""
        self.SERVER_OS = ""
        self.SERVER_NAME = ""
        self.IS_ERROR = ""

    def __str__ (self) :
        return "Server"



#
#       Test if server can have Administrator and Database
#
if __name__ == "__main__" :
    S = Server()
    S.DB = DB()
    S.Admin = Administrator()
