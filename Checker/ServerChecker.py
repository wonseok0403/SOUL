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

from pexpect import pxssh
import getpass

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 18
# @Last at      Aprl. 18
# @Music        Sing a song at TV program - Shin Yong Jae.
# @Information  This class is made for checking the database system. This system is a child class of Checker Engine.
#           You must add some functions and values in this functions. that's all.

class ServerChecker( CheckerEngine) :
    def __init__(self, LocalServer=None, LocalDatabase=None, LocalAdmin=None ) :
        CheckerEngine.__init__(self, LocalServer, LocalDatabase, LocalAdmin)
        self.Logger = Logger.Logger(self)
        self.EngineName = "SERVERCHECKER"

    def ServerChecker_ConditionCheck(self) :
        isOkay, msg = self.CheckerConditionCheck()
        if( isOkay ) : 
            return True, "Good"
        else :
            return False, msg

    def MakeShell(self) :
        self.Shell = pxssh.pxssh()
        
    def LoginShell(self) :
        host = self.LocalServer.CONNECTION_IPADDRESS
        user = self.LocalServer.CONNECTION_USERNAME
        pw = self.LocalServer.CONNECTION_PASSWORD
        self.Shell.login(host, user, pw)

    def ThrowMsg_Shell(self, msg) :
        self.Shell.sendline(msg)    # run a command
        self.Shell.prompt()         # match the prompt
    
    def LogoutShell(self) :
        self.Shell.logout()

    def LastCommand(self) :
        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("last")
        data = self.Shell.before
        print(data)
        print(type(data))
        self.LogoutShell()


    def SSHAttemptsCommand_Debian(self, num) :
        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("tail -n "+str(num)+" /var/log/auth.log | grep sshd")
        data = self.Shell.before
        print(data)
        print(type(data))
        self.LogoutShell()

    def SSHAttemptsCommand_CentRedHat(self, num) :
        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("tail -n "+str(num)+" /var/log/secure | grep 'sshd'")
        data = self.Shell.before
        print(data)
        print(type(data))
        self.LogoutShell()

    def BashHistory(self, num) :
        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("tail -n "+str(num)+" ~/.bash_history")
        data = self.Shell.before
        print(data)
        print(type(data))
        self.LogoutShell()

    def __str__(self) :
        return "SERVERCHECKER"

if __name__ == "__main__" :
    S = Server.Server(1, 22, 'ssh', '45.77.177.76', '3@mHze=5K{1wj){}', 'root', 'Wonseok.J', 970403, 'ubuntu', 'wonseokbuntu', None, '2018-03-02', None, None)
    S.DB = DatabaseClass.DB("psql", "'localhost'", "'5432'", "'testdb'", "'1234'", "'test'")
    S.DB.Connect_DB()
    S.db = S.DB
    S.Admin = AdministratorClass.Administrator('Wonseok', '/root/바탕화면/ServerPlayer/Report/', 'root', 'Admin', 'root')
    
    ServerChecker = ServerChecker(S, S.DB, S.Admin)
    #S.ThrowCommand('last')
    print( ServerChecker.ServerChecker_ConditionCheck() )
    #ServerChecker.LastCommand()
    #ServerChecker.SSHAttemptsCommand_Debian()
    #ServerChecker.dont()
    ServerChecker.BashHistory(500)