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

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email import encoders



from pexpect import pxssh
import getpass


# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 20
# @Last at      Aprl. 20
# @Music        Time paradox
# @Information  This class will send the report from Serverchecker or DatabaseChecker to you.
#           This class will supports user to check server conditions by watching mail from this class
#           That's why this class name is mail checker.
# 
class MailChecker( CheckerEngine ) :
    '''
    @Written by wonseok.
    @Date at 2018. 04. 20

     Dear my source code watchers! Thank you for watching my sources. If you have some issues, please mail me
    wonseok786@gmail.com! I'm glad to see all your issues and reports!
     Why I write letters in here is, this class contains my company boss' mail ID and password.
    Please do not use that and log-in. If you do that I will fell really sad and have to lock my git-hub.
    So, I hope that I won't locak any source codes and make my source open.
     +) That mail is for using test. not contain any heavy infromation, and I got the agree from him.
     But I don't want other guys use that account.
     Thanks!
     '''
     # Nothing special with ServerChecker.
    def __init__(self, LocalServer=None, LocalDatabase= None, LocalAdmin=None ) :
        # For sending mail, you need host, port, mimebase.
        # If you want to use 'Microsoft mail server', you have to change 
        #    --> MailChecker.host = 'smtp.live.com' (maybe)
        # And mimebase is for mixed mail (text+image+content ... etc)
        
        '''
            About Plain.

            The mail plain is for mail getter. Think about it, don't you think if you
            get mail just a log, it is not kind? So, I made a basis of 'mailplain'.
            The name is MailPlanText at '/LocalAdmin.PATH/MailBase/, name is 'MailPlainText'
            The content of 'mailplaintext' will be at front of mail. 
        '''
        CheckerEngine.__init__(self, LocalServer, LocalDatabase, LocalAdmin )
        self.Logger = Logger.Logger(self)
        self.EngineName = "MAILCHECKER"
        self.host = 'smtp.gmail.com'    # This is a host of smtp - googel-Gmail service.
        self.port = '587'               # This is a port of smtp at google-Gmail service..
        self.MIMEBASE = ['multipart', 'mixed'] 
        # Mail base setting starts
        self.MailBaseFile = open(self.LocalAdmin.PATH+"MailBase/MailPlainText.txt", 'r') # check the log !
        self.Content = ""               # define
        while True :                    # Here is the line for setting plain text.
            line = self.MailBaseFile.readline()
            if not line : break
            else : self.Content += (line + "\n")
        # Mail base setting ends


    # Find the report by using name which you put at parameter.
    def AddReportInContent_byName(self, Name) :
        BaseFile = open(self.LocalAdmin.PATH+str(Name), "r")
        while True :
            line = BaseFile.readline()
            if not line : break
            else : self.Content += (line+"\n")

    # This function is only for smtplib
    def MailServer_Login(self, senderAddress, senderPassword ) :
        # If you want to make your own mail server, call the smtplib.SMTP!
        # like this!
        self.mailServer = smtplib.SMTP(self.host, self.port)    # you need host and port number.
        self.mailServer.set_debuglevel(1)                       # This will print issues from google server.
        self.mailServer.ehlo()                          # This is the protocol regulation of SMTP
        self.mailServer.starttls()                      # TLS Service starts. if you don't want it, don't call this function.
        self.mailServer.ehlo()                          # After call the tls service, check the server if I can call mail functions

        self.senderAddress = senderAddress
        self.senderPassword = senderPassword

        self.mailServer.login(senderAddress, senderPassword)

    def MaillServer_CreateMail(self, recipient, Subject, Content) :
        self.MailMsg = MIMEMultipart('alternative')
        self.MailMsg['From'] = self.senderAddress
        self.MailMsg['To'] = recipient
        self.MailMsg['Subject'] = Header(Subject, 'utf-8')
        self.MailMsg.attach(MIMEText(self.Content + Content, 'plain', 'utf-8'))
        self.recipient = recipient

    def MailServer_SendMail(self) :
        try :
            if( self.MailMsg['From'] != None and self.MailMsg['To'] != None and self.MailMsg['Subject'] != None ) :
                self.mailServer.sendmail(self.senderAddress, self.recipient, self.MailMsg.as_string())
                self.mailServer.close()
            else :
                print('Error!')
        except Exception as e :
            print(e)


if __name__ == "__main__" :
    S = Server.Server(1, 22, 'ssh', '45.77.177.76', '3@mHze=5K{1wj){}', 'root', 'Wonseok.J', 970403, 'ubuntu', 'wonseokbuntu', None, '2018-03-02', None, None)
    S.DB = DatabaseClass.DB("psql", "'localhost'", "'5432'", "'testdb'", "'1234'", "'test'")
    S.DB.Connect_DB()
    S.db = S.DB
    S.Admin = AdministratorClass.Administrator('Wonseok', '/root/바탕화면/ServerPlayer/Report/', 'root', 'Admin', 'root')
    
    MailChecker = MailChecker(S, S.DB, S.Admin)
    MailChecker.MailServer_Login('pparkabiter@gmail.com', 'weareprojectar!')
    MailChecker.AddReportInContent_byName('1.wonseokbuntu.LastCommand.txt')
    msg = '\n\nTEST at, 2018-04-2001:37:35:378081 and the server host name is "wonseokbuntu" ' + '\n\n ATTENTION! THIS IS FOR TEST \n\n'
    MailChecker.MaillServer_CreateMail('wonseok786@khu.ac.kr', 'Last log from server test [test]', msg)
    MailChecker.MailServer_SendMail()

