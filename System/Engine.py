#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 4
# @Last at      Aprl. 20
# @Music        Parallax, U-Won-Jae
# @Information  Engine class is place in System UI.
#               In UI, user has to set the some settings.
#               If not, user may have some issues to execute program.


from SystemLoader import SystemLoader
from Kernel import Kernel
from Logger import Logger
import os, sys
sys.path.insert(0, os.getcwd())
from ObjectInfo import AdministratorClass
from Scheduler import Scheduler
import fabric
import datetime
def Exit(code) :
    # code 100 : OS Error. Your os is not supported in this system.
    print("WARNNING : You can't execute program. \n Error code : " + str(code))
    SetExecuteLog('Engine initialize is failed', code)
    exit()

def clearScreen(sort) :
    if( sort == 1 ) :
        os.system('clear')
    elif( sort == 2 ) :
        os.system('cls')
    else :
        Exit(100)

BeforeTime = datetime.datetime.now()
def SetExecuteLog(code, ErrorCode) :
    global BeforeTime
    now = datetime.datetime.now()
    LogFile = open(os.getcwd() + '/UserConfig/EngineLog.txt', "a")
    LogFile.write('Code : ' + str(code) + '\n')
    if( ErrorCode ) :
        LogFile.write('ErCode : ' + str(ErrorCode) + '\n')
    LogFile.write('Written time : ' + str(now) + ' [' + str(now - BeforeTime) + ']'+ '\n')
    BeforeTime = now

def ParseSortCont_FromString(List_forParse):
    # It only returns two data which are Sort and Content of string in listself.
    # EX) NAME:Wonseok
    # Sort = Name, Content = Wonseok
    ParsedStr = List_forParse.split('=')
    Sort = str(ParsedStr[0])
    Content = str(ParsedStr[1]).strip()
    return Sort, Content

def InstallRequirements() :
    os.system('pip install -r requirements.txt')


class Engine(object) :
    # engine.py check the bash if system has enough settings.
    # one of the most important check component is these

    # check if user install postgresql.
    # check if user is using python 2.7 or upper version ( just in 2 version )
    def __init__(self) :

        SetExecuteLog('Engine initialize is started', 0)
        
        self.CheckOS() # OS check!!
        self.DBCheck() # DB Check!!
        self.PythonCheck() # Python version check!!
        clearScreen(self.OS_SORT)
        self.isLaunchFirst()
        SetExecuteLog('OS, DB, Python check is completed', 0)
        flag = raw_input('System check complete!')
    

    def CheckOS(self) :
        # Error code 100 = OS error.
        self.OS_SORT = int(raw_input('What is your OS? ( Linux = 1, Windows = 2, Others = 3 ) : '))
        clearScreen(self.OS_SORT)
        print('OS check ... [OK] ')

    def DBCheck(self) :
        # Error code 101 = DB error.
        if( self.isPostgreInstall()  == False ) :
            print('System needs postgreSQL!')
            Exit(101)
        else :
            print('Database check ... [OK] ')

    def PythonCheck(self) :
        # Error code 102 = Python version error
        if( self.isPythonVer2() == False ) :
            print('Your python version must be 2 !')
            Exit(102)
        else :
            print('Python check ... [OK] ')
    
    def isPythonVer2(self) :
        print('CHECK IF SYSTEM IS RUNNING PYTHON VERSION 2 .......... ')
        if( sys.version_info[0] == 2 ) :
            return True
        else : 
            return False

    def isPostgreInstall(self) :
        print('CHECK IF SYSTEM HAS POSTGRES VERSION ................. ')
        if( os.path.exists("/var/lib/postgresql/") ) :
            return True
        else :
            return False

    def launch(self) :

        clearScreen(self.OS_SORT)
        print('System will be loaded. Please wait!')
        self.load_SystemLoader()

        print('Kernel will be loaded. Please wait!')
        self.load_Kernel()
        L = raw_input()

    def load_SystemLoader(self) :
        self.SystemLoaderObject = SystemLoader()
        SetExecuteLog('System Loader initializer is successfully loaded',None)
        
        self.SystemLoaderObject.LoadDBFiles()
        SetExecuteLog('Database is successfully loaded.',None)
        
        self.SystemLoaderObject.LoadUserFiles()
        SetExecuteLog('User Files are successfully loaded.',None)

        SetExecuteLog('System Loadeer is loaded.',None)

    def load_Kernel(self) :
        self.KernelObj = Kernel( self.SystemLoaderObject )
        SetExecuteLog('Kernel is loaded.', None)

    def isLaunchFirst(self) :
        userConfigure = open('Configure.txt')
        ConfigureLines = userConfigure.readlines()
        for i in ConfigureLines :
            Sort, Content = ParseSortCont_FromString( i )
            if Sort == 'Execute' :
                if Content == 'no' :
                    InstallRequirements()
        
        userConfigure.close()

        userConfigure = open('Configure.txt', 'w')
        userConfigure.write('Execute=yes')
                    

'''
    Below line is for test.
    You don't need to think of it.
'''
# Aprl 15
if __name__ == "__main__" :
    E = Engine()
    E.launch()