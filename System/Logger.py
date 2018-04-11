import psycopg2
import os
import sys
import time, datetime

sys.path.insert(0, os.getcwd() )

from ObjectInfo import DatabaseClass
def Generate_PrivateCode():
    # YEAR-MONTH-DAYHOUR:MIN:SEC.MICROSEC
    return str(datetime.datetime.now()).replace(" ","")


class Logger(object) :
    # If you want just define logger,
    def SQL_Select_From_Where_In(self, column_names, table_name, column_name2, values) :
        self.cursor.execute("SELECT " + column_names + " FROM " + tale_name + " WHERE " + column_name2 + " IN " + values)


    def track_exists(self, track_id):
        cur = self.conn.cursor()
        cur.execute("SELECT fma_track_id FROM tracks WHERE fma_track_id = %s", (track_id,))
        return cur.fetchone() is not None


    def SQL_Update_Set_Where(self, tale_name, column_name, value, whereCondition, whereValue ) :
        self.cursor.execute("UPDATE " + table_name + " SET " + column_name + " = " + value + " WHERE " + whereCondition + " = " + whereValue )


    def SetOrigin(self, origin_k) :
        SQL_Select_From_Where_In(   )



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
            self.className = "Engine"
            return


        elif( str(object) == " SystemLoader" ) :
            self.className = "SystemLoader"
            return


        elif( str(object) == "Kernel" ) :
            self.className = "Kernel"
            return


        else :
            # I suggest you write your local host db connection script in here. [ conn_string ]
            # self.conn_string ="host="+HOST+" dbname=logdb "+ "user="+USER+" password="+PW
            self.Connect_LogDB()


    def push_log(self, request_key, server_key, isReportRequest, ReportContent, origin_key, status_key, return_val, program_key):
        # 1) execution_id = yyyy-mm-ddhh:mm:ss.ms < Generate_PrivateCode >
        # request_key  = request_key
        # server_key = server_key
        # report_key = report_key
        # origin_key = origin_key
        # status_key =  status_key
        # return_val = return_val
        # program_key = program_key
        # 2) if ( isReportRequest ) --> publish report!
        # occur_timedetect =
        # occur_timeends, return_value

        # 1)
        execution_id = Generate_PrivateCode() # Generate by time

        # 2)
        if( isReportRequest == True ) :
            publishReport()

        program_key = self.className
        occur_timedetect = str( datetime.datetime.now() )
        if( status == "IGNORE" or status == "DONE" ) :
            # "UPDATE " + table_name + " SET " + column_name + " = " + value + " WHERE " + whereCondition + " = " + whereValue
            try :
                SQL_Update_Set_Where('"execution_logs"', '"occur_timeends"', str(datetime.datetime.now() , '"execution_id"', extraKey)

            except Exception, e:
                RepContent = " This error is occured at Logger.py, You have to check if exceution_log is deleted! "
                push_log('"CONNECT"', '"LOCALHOST"', '"PROGRAM_OWNER"', True, RepContent, '"DANGER"', None)
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
        # self.DB.printInfo()N


if __name__ == "__main__" :
    print("Logger tests ......... ")
    TestClass = testClass()
    print(Generate_PrivateCode())
    L = Logger(TestClass)
