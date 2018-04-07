import psycopg2
import os
import sys
import time, datetime

sys.path.insert(0, os.getcwd() )

from ObjectInfo import DatabaseClass
def Generate_PrivateCode():
    return str(datetime.datetime.now()).replace(" ","")


class Logger(object) :
    # If you want just define logger,
    def SQL_Select_From_Where_In(self, column_names, table_name, column_name2, values) :
        self.cursor.execute("SELECT " + column_names + " FROM " + tale_name + " WHERE " + column_name2 + " IN " + values)


    def __init__(self) :
        self.className = ""


    def Connect_LogDB(self) :
        self.conn = psycopg2.connect(self.conn_string)


    # If you define logger as something special
    def __init__(self, object) :
        # Connector
        print('Logger making start!')
        print( object )
        if( str(object) == "Connector" ):
            self.className = "Connector"
            self.conn_string ="host="+object.db.HOST+" dbname=logdb "+ "user="+object.db.USER+" password="+object.db.PW
            self.Connect_LogDB()


        elif( str(object) == "Engine" ) :
            return


        elif( str(object) == " SystemLoader" ) :
            return


        elif( str(object) == "Kernel" ) :
            return


        else :
            # I suggest you write your local host db connection script in here. [ conn_string ]
            # self.conn_string ="host="+HOST+" dbname=logdb "+ "user="+USER+" password="+PW
            self.Connect_LogDB()


    def push_log(self, req_k, ser_k, repor_key, report):
        # execution_id = [ NowYear ]_[ NowTime ]_
        #, request_key , server_key
        # report_key, origin_key
        # status_key, occur_timedetect
        # occur_timeends, return_value
        execution_id = Generate_PrivateCode()

##
##
##                                      FOR TEST                              */
##
##

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
        # self.DB.printInfo()


if __name__ == "__main__" :
    print("Logger tests ......... ")
    TestClass = testClass()
    print(Generate_PrivateCode())
    L = Logger(TestClass)
