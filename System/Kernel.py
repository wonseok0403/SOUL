# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 13
# @Last at      Aprl. 13
# @Music        Parallax, U-Won-Jae
# @Information


import os, sys
from SystemLoader import SystemLoader
from Connector import Connector
from Configurator import Configurator
sys.path.insert( 0, os.getcwd() )
from ObjectInfo import DatabaseClass
from ObjectInfo import Server
# if you want to use server class in server, you have to write Server.Server( ...  ) - interesting issue

class Kernel(object) :
    # SystemLoader which kernel has provide information to connector,
    # and check if connection is successful. If not, kernel will load logger
    # to save logs for programmer.

    def serverToServer(self, server) :
        # the server is just element in list.
        # Server is a element which is class named 'server'
        print(server)
        _Server = Server.Server( server[0], server[1], server[2], server[3], server[4], server[5], server[6], server[7], server[8], server[9], server[10] )
        _Server.db = self.Conn.db
        _Server.admin = self.Conn.admin
        return _Server


    # def __init__(self):
    #     print('Log : Kernel Initilizer is loaded!')
    #     self.Conn = Connector()


    def __init__(self, object = None) :
        # Initializer check
        if( object == None ) :
            print('Kernel error. You must define kerenel with System Loader!')
            return

        self.SystemLoader = object
        self.SystemLoader.printInfo()
        self.GoodServerList = []
        self.BadServerList = []

        self.Conn = Connector(self.SystemLoader) # Conn has logger DB
        self.GoodServerList = self.Conn.GoodServerList
        self.BadServerList = self.Conn.BadServerList

        Configurators_Badguys = []
        for i in self.BadServerList :
            print("Bad guys will have more connection!")
            serv = self.serverToServer(i)
            Conf = Configurator(serv, self.Conn.admin)
            Conf.ConnectSSH()
            Configurators_Badguys.append(Conf)



    def __str__ (self):
        return "KERNEL"
