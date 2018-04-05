from SystemLoader import SystemLoader
from Kernel import Kernel
import os, sys
sys.path.insert(0, os.getcwd())
from ObjectInfo import AdministratorClass


if __name__ == "__main__" :
    print("Engine starts......... ")
    SystemLoaderObject = SystemLoader()

    SystemLoaderObject.LoadDBFiles()
    SystemLoaderObject.LoadUserFiles()

    KernelObj = Kernel(SystemLoaderObject)
