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
from UserInterface import UIManager
import fabric
import datetime
from anytree import Node, RenderTree

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
            os.system('./UserConfig/ex.sh')
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
        # This directory is must be needed.
        if( os.path.exists("/var/lib/postgresql/") ) :
            return True
        else :
            return False

    def launch(self) :
        '''
        ! - ATTENTION ALL PROGRAMMERS - #!

        This is the main loop function in this program.
        As you know, this is the main function as 'void main' in C/C++ function.
        If you want to check some logis or things, just edit here.
        '''
        clearScreen(self.OS_SORT)
        print('System will be loaded. Please wait!')
        self.load_SystemLoader()

        print('Kernel will be loaded. Please wait!')
        self.load_Kernel()
        L = raw_input('Press any key to continue....')

        # if you want to check logic of UI, check below function.
        self.UIManage()

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

    def UIManage(self) :
        # After this line, User interface starts!
        # Tree must be needed.   < AnyTree >
        '''
    @ Recent 2018 05 07  23:51   Wonseok
    [Null]
    |----[UserInterface]
         |------[PrintServerManageMenu]
         |      |------[Target Manage]
         |      |      |-------[Target Manage Menu]
         |      |              |--------[AddtargetMenu]
         |      |              |--------[DeltargetMenu]
         |      |------[Install database]
         |      |------[Go Backup Console]
         |      |------[Firewall manage]
         |
         |------[DatabaseManage]
         |------[Configuration Mode]
         |------[Security Mode]
         |------[Power Off]

         '''
     
        self.UI = UIManager.UserInterface(self)
        currentNode=[]
        currentNode.append(self.UI.nodUI)
        targets = [[]]
        while True :
            print( currentNode[0]) 
            if currentNode[0].name == "Null" :
                break
            else :
                if currentNode[0].name == "UserInterface" :
                    self.UI.PrintMainMenu(len(self.KernelObj.BadServerList), len(self.KernelObj.GoodServerList), currentNode)
                    continue

                elif currentNode[0].name == "PrintServerManageMenu" :
                    self.UI.PrintServerManageMenu(targets, currentNode)

                    continue

                elif currentNode[0].name == "DatabaseManage":
                    # Not developed yet
                    pass
                elif currentNode[0].name == "Configuration Mode":
                    # Not developed yet
                    pass
                elif currentNode[0].name == "Security Mode":
                    # not developed yet
                    pass
                elif currentNode[0].name == "Power Off" :
                    print("Good bye my kkammi ................ ")
                    
                elif currentNode[0].name == "Target Manage" :
                    self.UI.PrintAllTargetsDetails(targets, self.KernelObj.BadServerList, self.KernelObj.GoodServerList, currentNode)
                    continue

                elif currentNode[0].name == "Install database" :
                    # not developed yet
                    pass

                elif currentNode[0].name == "Go Backusp Console" :
                    # not developed yet
                    pass

                elif currentNode[0].name == "Firewall manage" :
                    # not developed yet
                    pass

                elif currentNode[0].name == "Target Manage Menu" :
                    self.UI.TargetManageMenu(targets, currentNode)
                    continue
                    
                elif currentNode[0].name == "AddtargetMenu" :
                    self.UI.AddtargetMenu(targets, self.KernelObj.BadServerList, self.KernelObj.GoodServerList, currentNode)
                    continue

                elif currentNode[0].name == "DeltargetMenu" :
                    self.UI.DeltargetMenu(targets, self.KernelObj.BadServerList, self.KernelObj.GoodServerList, currentNode)
                    continue

            currentNode[0] = currentNode[0].parent
        # self.UI = UIManager.UserInterface(self)
        # target  = [[]]
        # level = 0
        # while(True) :
        #     # ? -> PrintMainMenu ( level = 0 )
        #     key = 0

        #     if( level == 0 ) :
        #         # level = 1 and key = 1
        #         key = self.UI.PrintMainMenu(len(self.KernelObj.BadServerList), len(self.KernelObj.GoodServerList))
        #         level += 1

        #     elif( key == 1 and level > 0) :
        #         # PrintMainMenu -> ServerManage
        #         clearScreen(self.OS_SORT)
        #         num = self.UI.PrintServerManageMenu(target)

        #         if( num == 1 ) :
        #             # PrintMainMenu -> ServerManage )-> TargetManage
        #             clearScreen(self.OS_SORT)
        #             num = self.UI.TargetManageMenu(target)

        #             if( num == 1 ) :
        #                 # PrintMainMenu -> ServerManage -> TargetManage) -> Add target
        #                 self.UI.AddtargetMenu(target, self.KernelObj.BadServerList, self.KernelObj.GoodServerList)
        #             elif( num == 2 ) : 
        #                 self.UI.DeltargetMenu(target, self.KernelObj.BadServerList, self.KernelObj.GoodServerList)


        #         elif( num == 2 ) :

        #         elif( num == 3 ) :
                
        #         elif( num == 4 ) :

        #     elif( key == 2 or level > 0 ) :
        #         # PrintMainMenu -> Database manage
        #         clearScreen(self.OS_SORT)
        #     elif( key == 3 or level ) :
        #         # PrintMainMenu -> Configuration mode
        #         clearScreen(self.OS_SORT)
        #     elif( key == 4 ) :
        #         # PrintMainMenu -> Seuciry mode
        #         clearScreen(self.OS_SORT)
        #     elif ( key == 0 ) :
        #         # PrintMainMenu -> Power off
        #         clearScreen(self.OS_SORT)
        #         print("Good bye kkami ...")

'''
    Below line is for test.
    You don't need to think of it.
'''
# Aprl 15
# May 2 added UI, and some class will be added.
if __name__ == "__main__" :
    E = Engine()
    E.launch()


