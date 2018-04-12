#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 12
# @Last at      Aprl. 12
# @Music        X-Girlfriend (san-E)
# @Information  This class is only for server each of being managed.
#               Unfortunately, now, if your DB is not 'postgreSQl', you can't control it.
from Logger import Logger
sys.path.insert(0, os.getcwd() )
from ObjectInfo import DatabaseClass

class Configurator(object) :

    def __init__(self) :
        self.Logger = Logger( Configurator )


    def __init__(self, object) :
        self.Logger = Logger(object)


    def __str__(self) :
        return 'Configurator'


def ParseDataList_FromPath(FilePath) :
    # returns file contents in 'FilePath'
    # You can check your dir by using'print(os.getcwd())'
    File = open(str(FilePath), "r")
    return File.readlines()


def ParseSortCont_FromString(List_forParse):
    # It only returns two data which are Sort and Content of string in listself.
    # EX) NAME:Wonseok
    # Sort = Name, Content = Wonseok
    ParsedStr = List_forParse.split('=')
    Sort = str(ParsedStr[0])
    Content = str(ParsedStr[1]).strip()
    return Sort, Content


class testClass(object):

    def __init__ (self) :
        # logger SETTINGS
        print("DB class is made")
        self.db = DatabaseClass.DB()
        self.LoadDBFiles()


    def __str__(self) :
        return "Connector"


    def LoadDBFiles(self):
        # ParseDataFromPath returns list in file contents
        # This function returns nothing
        print("load is complete")
        DatabaseData = ParseDataList_FromPath("./ProgramSettings/DataBaseSettings.txt")
        for i in range(0, len(DatabaseData)) :
            Sort, Content = ParseSortCont_FromString( DatabaseData[i] )
            if Sort == 'SORTS' :
                self.db.SORTS = Content
            elif Sort == 'USER' :
                self.db.USER = Content
            elif Sort == 'HOST' :
                self.db.HOST = Content
            elif Sort == 'PORT' :
                self.db.PORT = Content
            elif Sort == 'NAME' :
                self.db.NAME = Content
            elif Sort == 'PW' :
                self.db.PW = Content
            else : # For catch the error
                print (' INPUT ERROR AT DB SETTINGS.TXT ' )
                print (' (Input) Sort : ', Sort, ' Content : ', Content)
        # # END LOOP & for check
        # self.DB.printInfo()N

if __name__ == "__main__" :
    TestClass = testClass()
    Conf1 = Configurator(TestClass)
