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
# @Last at      Aprl. 20
# @Music        Sing a song at TV program - Shin Yong Jae.
# @Information  This class is made for checking the database system. This system is a child class of Checker Engine.
#           You must add some functions and values in this functions. that's all.

class ServerChecker( CheckerEngine) :

    '''
    @ Written by wonseok.
    @ Date at 2018.04.20

     You don't need to define ConditionChecker function or sending log function 
    which sends 'server connection bad' or 'database connection bad' status.
     Server checker just needs to define some functions which can control servers,
    check attacks from bad hackers.
     And also, ServerChecker needs to make a report which can be seen easily.

     Day 18 :
        Define class and functions < Checker engine which are parent class of this class >
     Day 19 :
        Define this class and some functions which are initailizer, condition checker,
        shell commands, SSH commanding functions, some functions for security check.
     Day 20 :
        I will make some functions about making report, and for sending this mail,
        I will make a mail class named, 'mailchecker'.
    '''

    # Nothing special.
    # But you have to notice that this class uses parent class's initializer.
    def __init__(self, LocalServer=None, LocalDatabase=None, LocalAdmin=None ) :
        CheckerEngine.__init__(self, LocalServer, LocalDatabase, LocalAdmin)
        self.Logger = Logger.Logger(self)
        self.EngineName = "SERVERCHECKER"

    # This program will check condition of local Database and etc.
    # If checking status is bad, parent class will remains log.
    def ServerChecker_ConditionCheck(self) :
        isOkay, msg = self.CheckerConditionCheck()
        if( isOkay ) : 
            return True, "Good"
        else :
            return False, msg

    # Pexpect defines wonderful functions for using shell script in remote server.
    # It's really good to use, and don't need hard codes.
    def MakeShell(self) :
        # For using shell script at remote server, you have to define shell.
        self.Shell = pxssh.pxssh()
        
    def LoginShell(self) :
        # After execute makeshell function, you have to login in server.
        host = self.LocalServer.CONNECTION_IPADDRESS    # local server is
        user = self.LocalServer.CONNECTION_USERNAME     # master server.
        pw = self.LocalServer.CONNECTION_PASSWORD
        self.Shell.login(host, user, pw)                # This is the most important line

    # You just execute this function and putting msg in this function's parameter,
    # you can send message to remote server.
    def ThrowMsg_Shell(self, msg) :
        self.Shell.sendline(msg)    # run a command
        self.Shell.prompt()         # match the prompt  - pexpect github.
    
    def LogoutShell(self) :
        self.Shell.logout()

    '''
     From this line, program will check some security checks at remote server.
    You don't need to execute these commands in every servers.
    This commands will execute for you automatically.
    What you just need to check is, execute this function, check the report. That's all!
    '''
    def LastCommand(self) :
        # Last command tells you who visited and succeed to login in your server.
        # It's a very basic command of checking security.

        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("last")
        data = self.Shell.before
        self.LogoutShell()

        return data


    def SSHAttemptsCommand_Debian(self, num) :
        # This commands will tell you who wanted to log in your remote server.
        # This function is for debian( ubuntu is based at debian ) OS.
        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("tail -n "+str(num)+" /var/log/auth.log | grep sshd")
        data = self.Shell.before
        self.LogoutShell()

        return data

    def SSHAttemptsCommand_CentRedHat(self, num) :
        # CentOS and RedHat have to execute this function.
        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("tail -n "+str(num)+" /var/log/secure | grep 'sshd'")
        data = self.Shell.before
        self.LogoutShell()

        return data

    def BashHistory(self, num) :
        # This function tells you what hackers did in your server.
        # But you have to know that, history includes commands that you did.
        self.MakeShell()
        self.LoginShell()
        self.ThrowMsg_Shell("tail -n "+str(num)+" ~/.bash_history")
        data = str(self.Shell.before)
        print(self.Shell.before)
        self.LogoutShell()

        return data

    '''
     From this line, program will make the result from command to report.
    You can check the reports by using below functions.
    '''

    #@param     content is the msg from server. You have to make report this value.
    #           caller is the command which you used in server.
    #              - if you use 'last' command at server, caller will be 'last'
    def MakeReport(self, content, caller) :
        # LogStructure :
        #
        # File name : (ServerID).(ServerName).(Command).(Date) - new file
        #          +  (ServerID).(ServerName).(Command) - based file.

        FileName_new = str(self.LocalServer.ID)+"."+str(self.LocalServer.SERVER_NAME)+"."+str(caller)+"."+ (str(datetime.datetime.now()).replace(" ",""))
        FileName_base = str(self.LocalServer.ID)+"."+str(self.LocalServer.SERVER_NAME)+"."+str(caller)

        newFile = open(self.LocalAdmin.PATH + FileName_new + ".txt", "w")
        baseFile = open(self.LocalAdmin.PATH + FileName_base + ".txt", "a")
        
        newFile.write(content+'\n\n')
        baseFile.write(content+'\n\n')

        newFile.close()
        baseFile.close()


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
    data = ServerChecker.BashHistory(500)
    ServerChecker.MakeReport( data , 'BashHistory')
    data = ServerChecker.LastCommand()
    ServerChecker.MakeReport( data, 'LastCommand' )