from SystemLoader import SystemLoader
from Connector import Connector

class Kernel(object) :
    # SystemLoader which kernel has provide information to connector,
    # and check if connection is successful. If not, kernel will load logger
    # to save logs for programmer.

    def __init__(self):
        print('Log : Kernel Initilizer is loaded!')
        self.Conn = Connector()

    def __init__(self, object) :
        self.SystemLoader = object
        self.SystemLoader.printInfo()
        self.Conn = Connector(self.SystemLoader)

    def __str__ (self):
        return "Kernel"
