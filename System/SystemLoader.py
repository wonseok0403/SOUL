import os
import sys
sys.path.insert(0, os.getcwd() )
# {value for value in variable}ys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#
from ObjectInfo import AdministratorClass
from ObjectInfo import DatabaseClass

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

class SystemLoader(object) :

    def __init__ (self):
        # self.Admin = Administrator()
        self.Admin = AdministratorClass.Administrator()
        self.DB = DatabaseClass.DB()
        print('System Loader Execute : ')
        print(os.getcwd())

    def EndProgram(self, Code):
        print('System End.')

    def LoadDBFiles(self):
        # ParseDataFromPath returns list in file contents
        # This function returns nothing
        DatabaseData = ParseDataList_FromPath("./ProgramSettings/DataBaseSettings.txt")
        for i in range(0, len(DatabaseData)) :
            Sort, Content = ParseSortCont_FromString( DatabaseData[i] )
            if Sort == 'SORTS' :
                self.DB.SORTS = Content
            elif Sort == 'USER' :
                self.DB.USER = Content
            elif Sort == 'HOST' :
                self.DB.HOST = Content
            elif Sort == 'PORT' :
                self.DB.PORT = Content
            elif Sort == 'NAME' :
                self.DB.NAME = Content
            elif Sort == 'PW' :
                self.DB.PW = Content
            else : # For catch the error
                print (' INPUT ERROR AT DB SETTINGS.TXT ' )
                print (' (Input) Sort : ', Sort, ' Content : ', Content)
        # # END LOOP & for check
        # self.DB.printInfo()

    def LoadUserFiles(self):
        # This function returns nothing
        UserData = ParseDataList_FromPath("./ProgramSettings/UserSetting.txt")
        for i in range (0, len(UserData)) :
            Sort, Content = ParseSortCont_FromString( UserData[i] )
            if Sort == 'NAME' :
                self.Admin.NAME = Content
            elif Sort == 'PW' :
                self.Admin.PW = Content
            elif Sort == 'ID' :
                self.Admin.ID = Content
            elif Sort == 'MODE' :
                self.Admin.MODE = Content
            else :
                print (' INPUT ERROR AT USER SETTINGS.TXT ' )
                print (' (Input) Sort : ', Sort, ' Content : ', Content)
        # # END LOOP & for check
        # self.Admin.printInfo()

    def printInfo(self) :
        self.Admin.printInfo()
        self.DB.printInfo()

    def __str__(self) :
        return "SystemLoader"
