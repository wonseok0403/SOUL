#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 10
# @Last at      Aprl. 15
# @Music        Pianoman - MAMAMOO
# @Information  This class makes report, make and throw log to local DB.
#               You have to make sure to connect your local DB with program.
import os, sys
import psycopg2
import time, datetime

sys.path.insert(0, os.getcwd() )

from ObjectInfo import DatabaseClass
def Generate_PrivateCode():
    # Return structure is :
    # YEAR-MONTH-DAYHOUR:MIN:SEC.MICROSEC
    # ex) 2017-04-03:08:40:00.010101
    return str(datetime.datetime.now()).replace(" ","")


def Generate_Filename(className, ownerName) :
    # Return structure is :
    # (ClassName).(OwnerName).log
    if( ownerName == "" ) :
        ownerName = "Logger"
    else :
        return className+"."+ ownerName +".log"


def Generate_ReportKey(FileName) :
    # Return structure is :
    # (ClassName).(OwnerName).log.(Time)
    # ex) Kernel.log.2018-04-03-08:40:00.01010...
    # https://msdn.microsoft.com/en-us/library/windows/desktop/aa365247(v=vs.85).aspx
    # for this rule (windows file name rule) ':' is changed for '-' --> ex) Kernel.log.2018-01-01-01-01-01.01010...
    return FileName + str(datetime.datetime.now()).replace(" ","")



class Logger(object) :
    # If you want just define logger,
    def MakeReport(self, ReportType, Path, Name, Content) :
        # push_log( self, request_key, server_key, ReportKey, origin_key, status_key, return_val, program_key )
        FileName = Generate_Filename(self.className, Name) # it is as same as file name
        ReportKey = Generate_ReportKey(FileName)

        isInServer, ErrorMsg = self.track_exists('report', 'report_type', ReportType)
        if( isInServer ) :
            # Make file for report
            ReportFile = open(Path+FileName+".txt", "a")
            ReportFile.write('\n'+Content)
            ReportFile.close()

            # Push log for you made a report
            vars = "'" + ReportKey + "', '" + ReportType + "', '" + str(datetime.datetime.now()).replace(" ","") + "', '" + Path +"', '" + FileName +"'"
            # Aprl 13. Name -> FileName by wonseok

            self.SQL_Insert_Into_values('report', vars)
            # Push log for return report key
            return ReportKey
        else :
            UnknownMsg = "\nAnd unknown error occured in Logger.MakeReport. You have to check it.\n"
            ReportFile = open(Path+FileName+".txt", "a")
            ReportFile.write('\n'+Content + UnknownMsg)
            ReportFile.close()
            return ReportKey
            # RK = self.MakeReport( 'WARNING_SERVICE_REPORT', Path, 'Logger', 'Report type : ' + ReportType + ' is not in DB! Please check service owner... before content : ' + Content + ' by ' + Name)
           #  vars = "'" + ReportKey + "', 'ERROR_SERVICE_REPORT', '" + str(datetime.datetime.now()).replace(" ","") + "', '" + Path + "', '" + FileName + "'"
            # self.SQL_Insert_Into_values('report', vars)
            # self.push_log( 'DB_REQUEST', 'localhost', RK, 'PROGRAM_OWNER', 'BAD', 'None', 'LOGGER')


    def SQL_Select_From_Where_In(self, column_names, table_name, column_name2, values) :
        cur = self.conn.cursor()
        cur.execute("SELECT " + column_names + " FROM " + table_name + " WHERE " + column_name2 + " IN " + values)


    def SQL_Insert_Into_values(self, table_name, values) :
        cur = self.conn.cursor()
        cur.execute("INSERT INTO " + table_name + " VALUES ( " + values + " )" )
        self.conn.commit()


    def track_exists(self, table_name, column_name2, values):
        # If there is no value in table #table_name, return None.
        # Not if, return True.
        # It is differnt at SQL_Select_From_Where_In.... But it can be same.. so plz check the code.
        # If you can think better idea at code, modify it and report me please. :)
        try :
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM " + table_name + " WHERE " + column_name2 + " =  '" + values + "' ")
        except psycopg2.Error as e :
            print(e.message)
            print('error occur!')
            return False, e
        
        except Exception as e :
            print(e)
            return False, e

        return True, None

    def SQL_Update_Set_Where(self, table_name, column_name, value, whereCondition, whereValue ) :
        self.conn.cursor.execute("UPDATE " + table_name + " SET " + column_name + " = " + value + " WHERE " + whereCondition + " = " + whereValue )


    def SetOrigin(self, origin_k) :
        if( self.track_exists(  'origin', 'origin_key', origin_k  ) == False ) :
            # No origin_k is in there [ Before test ]
            print( origin_k + 'is not in db')
        else :
            print( origin_k + 'is in db')


    def Connect_LogDB(self) :
        try :
            self.conn = psycopg2.connect(self.conn_string)
        except psycopg2.Error as e :
            # Throw error log < DB Connection failed >
            print(e.message)
            return False
        return True


    # If you define logger as something special
    def __init__(self, object=None) :
        if( object == None ) :
           print('Logger is made by nothing')
           self.className = ""
           self.Connect_LogDB()
        else:
            print('Logger making start!')
            print( object )
            self.className = str(object)
            self.object = object
            self.conn_string ="host="+object.db.HOST+" dbname=logdb "+ "user="+object.db.USER+" password="+object.db.PW
            self.DB_Connection = self.Connect_LogDB()

    def PushLog_UnknownError(self, Admin, location, ExceptionMsg=None) :
        # if( self.DB_Connection == False ) :
        #     print('DB CONNECTION FAIL CHECK THE LOGGER LOG')
        #     return
        # LogStructure :
        ## [ADMIN.ID] makes unknown error in [object], location is in [location] at [Date]
        ## Exception massage is [ExceptionMsg]. 
        ## --------------- Object info ---------------
        ## [Object.INFO]
        ## --------------- Admin  info ---------------
        ## [Admin.INFO]
        ## Log END.
        print('Unknown error occur!')
        strLogMsg = str(Admin.ID) + " makes unknown error in " + str(object) + ", location is in " + str(location) + " at " + str(datetime.datetime.now()) + "\n" + \
                    "Exception massage is " + str(ExceptionMsg) + ".\n" + \
                    "--------------- Object info ---------------\n" + \
                    str(self.object.getInfo()) + "\n" + \
                    "--------------- Admin  info ---------------\n" + \
                    str(Admin.getInfo()) + "\n" + \
                    "Log End."
        self.SetOrigin('UNKNOWN_LOG')
        RK = self.MakeReport('UNKNOWN', Admin.PATH, Admin.NAME, strLogMsg)
        self.push_log('DONT_KNOW', '404', RK, 'UNKNOWN_LOG', 'UNKNOWN', 'Logger.UnknownError', 'LOGGER')
        
    def push_log(self, request_key, server_key, Report_Key, origin_key, status_key, return_val, program_key, extraKey=None):
        # You have to check if those keys are in DB
        # push_log( self, request_key, server_key, Report_Key, origin_key, status_key, return_val, program_key )
        # 1) execution_id = yyyy-mm-ddhh:mm:ss.ms < Generate_PrivateCode >
        # request_key  = request_key
        # server_key = server_key
        # report_key = Report_key
        # origin_key = origin_key
        # status_key =  status_key
        # return_val = return_val
        # program_key = program_key
        # occur_timedetect
        # occur_timeends, return_value

        # track_exists(self, table_name, column_name2, values)
        if( self.track_exists('request_types', 'request_key', request_key) == None or  \
            self.track_exists('report',        'report_key',  Report_Key) == None or \
            self.track_exists('origin', 'origin_key', origin_key) == None or
            self.track_exists('status', 'status_key', status_key) == None or
            self.track_exists('program', 'program_key', program_key) == None) :
            # MakeReport(self, ReportType, Path, Name, Content)
            self.MakeReport('WARNING_SERVICE_REPORT', '/root/바탕화면/ServerPlayer/Report/', 'Logger', 'Please key check! : ' + \
            str(request_key, Report_Key, origin_key, status_key, program_key) )
            print('Line 129 is completed!')


        execution_id = Generate_PrivateCode() # Generate by time

        program_key = self.className
        occur_timedetect = str( datetime.datetime.now() )
        if( status_key == "IGNORE" or status_key == "DONE" ) :
            # "UPDATE " + table_name + " SET " + column_name + " = " + value + " WHERE " + whereCondition + " = " + whereValue
            try :
                self.SQL_Update_Set_Where('"execution_logs"', '"occur_timeends"', occur_timedetect , '"execution_id"', extraKey)
            # 여기 exception에서 infinite loop이 발생함.
            # sql try catch 오류 부분 해결할 것. 또한 아래 exception에서 psycopg exception이면 push log 하지 않아야함.
            # 재귀호출 ㄴㄴ
            except psycopg2.Error as e :
                print(e.message)
                print('Sorry. push log failed because of database connection')

            except Exception as e:
                RepContent = " This error is occured at Logger.py, You have to check if exceution_log is deleted! "
                #self.push_log('"CONNECT"', '"LOCALHOST"', '"PROGRAM_OWNER"', True, RepContent, '"DANGER"', None)
                print('line 144 is completed')

        else :
            # SQL_Insert_Into_values(self, table_name, values)
            # request_key, server_key, Report_Key, origin_key, status_key, return_val, program_key
            values = "'" + str(execution_id) + "', '" + request_key + "', '" + str(server_key) + "', '" + str(Report_Key) + "', '" + origin_key +"', '" + status_key + "', '" +  str(datetime.datetime.now()) + "', '" + ""+ "', '" + return_val + "', '" + program_key + "'"
            try :
                self.SQL_Insert_Into_values( 'execution_logs', values)
            except Exception as e :
                print(e.message)
                print('Sorry. push log failed because of database connection')

##                                      FOR TEST                              */
##                             Listening Roller coaster : Aprl 12.            */
##                                  Desginer. Wonseok                         */
# You don't need to check under this line.
# Test is completed at Aprl 17.

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
        return "CONNECTOR"


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
    L.SetOrigin('KNOWN_LOG')
    # self, ReportType, Path, Name, Content
    RK = L.MakeReport( 'ALERT_SERVICE_REPORT', '/root/바탕화면/ServerPlayer/Report/', 'Wonseok', 'LogCheck!' )
    # self, request_key, server_key, Report_Key, origin_key, status_key, return_val, program_key
    L.push_log( 'DONT_KNOW', 'localhost', RK, 'KNOWN_LOG', 'BAD', 'None', 'CONNECTOR')
