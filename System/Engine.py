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

class Engine(object) :
    # engine.py check the bash if system has enough settings.
    # one of the most important check component is these

    # check if user install postgresql.
    # check if user is using python 2.7 or upper version ( just in 2 version )
    def __init__(self) :
        if( self.isPostgreInstall()  == False ) :
            print('System needs postgreSQL!')
            self.ENGINE_ENNABLE = False
        else :
            print(' [OK] ')
            self.ENGINE_ENNABLE = True
        if( self.isPythonVer2() == False ) :
            print('Your python version must be 2 !')
            self.ENGINE_ENNABLE = False
        else :
            print(' [OK] ')
            self.ENGINE_ENNABLE = True
        
        if( self.ENGINE_ENNABLE ) :
            print("Engine successfully initialized!")
        else :
            print("Engine has some error!")
    
    def load_SystemLoader(self) :
        self.SystemLoaderObject = SystemLoader()
        self.SystemLoaderObject.LoadDBFiles()
        self.SystemLoaderObject.LoadUserFiles()

    def load_Kernel(self) :
        self.KernelObj = Kernel( self.SystemLoaderObject )
        
    def launch(self) :
        self.load_SystemLoader()
        self.load_Kernel()

        
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



'''
    Below line is for test.
    You don't need to think of it.
'''
# Aprl 15
if __name__ == "__main__" :
    E = Engine()
    E.launch()
    # print("Engine starts......... ")
    # SystemLoaderObject = SystemLoader()

    # SystemLoaderObject.LoadDBFiles()
    # SystemLoaderObject.LoadUserFiles()

    # KernelObj = Kernel(SystemLoaderObject)
    # print( KernelObj.GoodServerList )
    # print( KernelObj.BadServerList )

    # testServer = KernelObj.serverToServer(KernelObj.BadServerList[0])
    # Scheduler = Scheduler(testServer)
    # Scheduler.MakeAndSendCommand()