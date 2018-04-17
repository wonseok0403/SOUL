#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 17
# @Last at      Aprl. 18
# @Music        The tear of PPIERO - Outsider(Moo-oong) ( feat Bae-Chi-Gi )
# @Information  This class is child class of BackupEngine.
# @details
#               DBE(Database Backup Engine) is only for doing backup service. 
#           You have to connect master and slave server, and connect local database in parent initalizer.
#           This is a previous work for using this class. After this work, you have to connect local database.
#           Obviously this work is held in this class. It is easy but may take some time to do this work.
import os, sys
sys.path.insert(0, os.getcwd())
from BackupEngine import BackupEngine 
from ObjectInfo import Server
from ObjectInfo import AdministratorClass
from ObjectInfo import DatabaseClass
from System import Logger
class DatabaseBackupEngine ( BackupEngine ) :
    def __init__(self, Master=None, Slave=None, Admin=None) :
        BackupEngine.__init__(self, Master, Slave, Admin)




#
#      Test if DBE status is good
#
if __name__ == "__main__" :
    # Test Configuration :
    # Master server is server id (1)
    # Slave server is server id (4)
    # Admin is me
    #
    # Test algorithm
    # 1. Server connection test
    #   - Master server connect [ Parent class done ]
    #   - Slave server connect  [ Parent class done ]
    # 
    # 2. Get master's local db_key from local database.
    #   - Using master server's owner_key to get DB_key     -> will be written in DatabaseClass
    #   - Using master server's db_key, get the db_data from local db.
    #      
    # 3. Database connection test 
    #   The database which is gotton from task number 2, connect test it.
    #
    # 4. Send the command which back-up database.
    #   Make the command ( Using scheduler is good way. )
    #   Send the command to server.

    '''
    * Initializing for test
    '''
    # Server & Database Setting
    MasterServer = Server.Server(1, 22, 'ssh', '45.77.177.76', '3@mHze=5K{1wj){}', 'root', 'Wonseok.J', 970403, 'ubuntu', 'wonseokbuntu', None, '2018-03-02', None, None)
    SlaveServer = Server.Server(4, 22, 'ssh', '45.77.180.147', 'P]9p{PWKRu=+o7y]', 'root', 'Wonseok.J', 970403, 'ubuntu', 'WonseokTestCent', None, '2018-03-02', None, None)
    MasterServer.db = DatabaseClass.DB("psql", "'localhost'", "'5432'", "'testdb'", "'1234'", "'test'")
    SlaveServer.db = DatabaseClass.DB("psql", "'localhost'", "'5432'", "'testdb'", "'1234'", "'test'")
    # Connect local db
    MasterServer.db.Connect_DB()
    SlaveServer.db.Connect_DB()
    # DB = db for grammar error
    MasterServer.DB = MasterServer.db
    SlaveServer.DB = SlaveServer.db
    # Initalize Admin
    MasterServer.Admin = AdministratorClass.Administrator('Wonseok', '/root/바탕화면/ServerPlayer/Report/', 'root', 'Admin', 'root')
    SlaveServer.Admin = AdministratorClass.Administrator('Wonseok', '/root/바탕화면/ServerPlayer/Report/', 'root', 'Admin', 'root')
    # Push the admin
    MasterServer.local_admin = MasterServer.GetServerOwner()
    SlaveServer.local_admin = SlaveServer.GetServerOwner()
    
    '''
    * Real test of DBE
    '''
    # Connection test (1-1, 1-2)
    DBE = DatabaseBackupEngine(MasterServer, SlaveServer, MasterServer.Admin)
