#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 17
# @Last at      Aprl. 17
# @Music        ANTI - ZICO( feat.. )
# @Information  This class is parent class for backup system. This will need some class.
# @details
#           First, This class need server class. For example, if you want to back-up your
#        postgreSQL data to server, you have to regist master server and slave server.
#        (master = server which is backed up. slave = server which back up.)
#         -> slave will take data from master to save in itself.
#           (If you want to make database backup system) Second, you need DataBase.
#         If you want to make copy-database, just copy it and put it in your database.

import os, sys
sys.path.insert(0, os.getcwd())

from ObjectInfo import Server
from ObjectInfo import AdministratorClass
from ObjectInfo import DatabaseClass
from System import Logger
import time, datetime
class BackupEngine(object) :

    def __init__(self, Master, Slave, Admin) :
        self.IS_INITIALIZE = False

        if( (str(Master) is not "SERVER") or
            (str(Slave) is not "SERVER") or
            (str(Admin) is not "ADMINISTRATORCLASS")) :
            print(str(Master), str(Slave), str(Admin))
            print('Backup initialize fail!')
            return

        # Engine will back up from master to slave.
        self.Master = Master
        self.Slave = Slave
        self.Admin = Admin

        # Server connection test.
        if( self.ConnectionTest_toServer() ) :
            print('Test accepted!')
        else :
            print('BackupEngine tried to connect master & server. But it failed.')

    # Connection test needs to be accepted. If not, Backup Engine failed to initialize.
    def ConnectionTest_toServer(self) :
        IS_OKAY_MASTER, Msg_MASTER = self.Master.isTryConnect()
        IS_OKAY_SLAVE, Msg_SLAVE = self.Slave.isTryConnect()

        if( (IS_OKAY_MASTER and IS_OKAY_SLAVE ) == False ) :
            self.SendLog_ConnectionWrong(IS_OKAY_MASTER, IS_OKAY_SLAVE, Msg_MASTER, Msg_SLAVE)
            self.Master = None
            self.Slave = None
            return False

        return True

    def SendLog_ConnectionWrong(self, ConnMaster, ConnSlave, Msg_MASTER, Msg_SLAVE ) :
        # LogStructure :
        ##  [Admin.ID] tried to connect these at [Date.time] : 
        ##  Master : [Master.ID], [Master.Role]@[MAST.Host] / Slave : [Slave.ID], [Slave.Role]@[Slav.Host]
        ##  But server Connection is BAD. 
        ##  Master connection status : [ConnMaster], Slave connection status : [ConnSlave]
        ##  Here is the Msg from master : [Msg_Master]
        ##  Here is the Msg from slave  : [Msg_Slave]

        StrLogMsg = str(self.Admin.ID) + " tried to connect these at " + str(datetime.datetime.now()) + " : \n" + \
                    "Master : " + str(self.Master.ID) + ", " + str(self.Master.ROLE) + "@" + str(self.Master.HOST) + \
                     " / Slve : " + str(self.Slave.ID) + ", " + str(self.Slave.ROLE) + "@" + str(self.Slave.HOST) + "\n" + \
                     "But server Connection is BAD." + \
                     "Master connection status : " + str(ConnMaster) + ", Slave connection status : " + str(ConnSlave) + "\n" + \
                     "Here is the Msg from master : " + str(Msg_MASTER) + "\n" + \
                     "Here is the Msg from slave  : " + str(Msg_SLAVE) + "\n"
        BackupLogger = Logger.Logger(self)
        BackupLogger.SetOrigin('KNOWN_LOG')
        RK = BackupLogger.MakeReport('SERVICE_STATUS_CHECK', self.Admin.PATH, self.Admin.NAME, StrLogMsg)

        if( ConnMaster ) :
            ConnMaster = "BAD"
        else :
            ConnMaster = "GOOD"
        if( ConnSlave ) :
            ConnSlave = "BAD"
        else :
            ConnSlave = "GOOD"

        # Push master log and slave log.
        BackupLogger.push_log('CONNECT', self.Master.ID, RK, 'KNOWN_LOG', ConnMaster, 'BackupEngine.SendLog_ConnectionBad', 'BACKUPENGINE')
        BackupLogger.push_log('CONNECT', self.Slave.ID, RK, 'KNOWN_LOG', ConnMaster, 'BackupEngine.SendLog_ConnectionBad', 'BACKUPENGINE')
        


#
#       Test if BackupEngine's status is good.
#

if __name__ == "__main__" :
    S = Server.Server(1, 22, 'ssh', '45.77.177.76', '3@mHze=5K{1wj){}', 'root', 'Wonseok.J', 970403, 'ubuntu', 'wonseokbuntu', None, '2018-03-02', None, None)
    S.db = DatabaseClass.DB("psql", "'localhost'", "'5432'", "'testdb'", "'12345'", "'test'")
    S.db.Connect_DB()
    S.DB=S.db
    S.Admin = AdministratorClass.Administrator('Wonseok', '/root/바탕화면/ServerPlayer/Report/', 'root', 'Admin', 'root')
    S.local_admin = S.GetServerOwner()

    BE = BackupEngine(S, S, S.Admin)