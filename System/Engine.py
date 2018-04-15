from SystemLoader import SystemLoader
from Kernel import Kernel
from Logger import Logger
import os, sys
sys.path.insert(0, os.getcwd())
from ObjectInfo import AdministratorClass
from Scheduler import Scheduler
import fabric


if __name__ == "__main__" :
    print("Engine starts......... ")
    SystemLoaderObject = SystemLoader()

    SystemLoaderObject.LoadDBFiles()
    SystemLoaderObject.LoadUserFiles()

    KernelObj = Kernel(SystemLoaderObject)
    print( KernelObj.GoodServerList )
    print( KernelObj.BadServerList )

    testServer = KernelObj.serverToServer(KernelObj.BadServerList[0])
    Scheduler = Scheduler(testServer)
    Scheduler.MakeAndSendCommand()