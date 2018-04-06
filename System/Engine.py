from SystemLoader import SystemLoader
from Kernel import Kernel
from Logger import Logger
import os, sys
sys.path.insert(0, os.getcwd())
from ObjectInfo import AdministratorClass
import fabric


if __name__ == "__main__" :
    print("Engine starts......... ")
    SystemLoaderObject = SystemLoader()

    SystemLoaderObject.LoadDBFiles()
    SystemLoaderObject.LoadUserFiles()

    KernelObj = Kernel(SystemLoaderObject)
