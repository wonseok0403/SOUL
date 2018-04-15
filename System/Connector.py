from SystemLoader import SystemLoader
from Logger import Logger
import psycopg2
import pandas.io.sql as pdsql
import pandas
import sqlalchemy
from pexpect import pxssh
import time, datetime
# from fabric.api import run, roles, env, execute
def Shell_login(Shell, Hostname, Username, Password):
    Shell.login( Hostname, Username, Password)
    Shell.sendline('ls -al')
    Shell.prompt()
    print ("before\n"+ Shell.before)

def Update_Success(cursor, conn, Id, isSuccess) :
    if isSuccess == True :
        cursor.execute("UPDATE servers SET \"LAST_LOGIN\"=\'"+str(datetime.datetime.now())+"\' WHERE \"ID\"="+str(Id))
        cursor.execute("UPDATE servers SET \"IS_ERROR\"=\'"+str("")+"\' WHERE \"ID\"="+str(Id))
        conn.commit()
        # Push Log in here
        # self.logger.push_log()

    else :
        cursor.execute("UPDATE servers SET \"LAST_LOGIN\"=\'"+str(datetime.datetime.now())+"\' WHERE \"ID\"="+str(Id))
        cursor.execute("UPDATE servers SET \"IS_ERROR\"=\'"+str("YES")+"\' WHERE \"ID\"="+str(Id))

        conn.commit()

    conn.commit()
    cursor.close()

class Connector(object) :
    # def __init__(self) :
    #     self.SystemLoader = SystemLoader()


    def __init__(self, objects = None):
        # you must input 'SystemLoader in here'
        self.SystemLoader = objects
        # o yes
        self.db = self.SystemLoader.DB
        self.admin = self.SystemLoader.Admin
        self.ServerList = [[]]
        self.conn_string = ""
        self.logger = Logger(self)
        self.GoodServerList= []
        self.BadServerList = []

        self.Connecting()


    def Connecting(self) :
        # First, you have to connect DataBase in your local computer.
        # PostgreSQL will be the best choice. But if you want to use other version,
        # please check program version.
        self.Connect_DB()

        # Second, program will get server data from your local database.
        self.Connect_getServerDB()

        # Third, program check the servers okay to connectt
        self.Connect_Servers()

    def Connect_Servers(self) :
        # In this function, program check servers which owner has in local DB.
        # If there are errors in this logic, program will send log in DB.
        # You can check your error log in this program, and in other module.

        # i is each server list of serverlists
        for i in self.ServerList :
            # The rule of env.host = 'user@host:port'
            str_tmp = str(i[5])+"@"+str(i[3])+":"+str(i[1])

            try :
                # shell and host setting
                s = pxssh.pxssh()
                hostname = str(i[3])
                username = str(i[5])
                password = str(i[4])

                # Login to shell, if it has error, it may goes under 'except' lines.
                Shell_login(s, hostname, username, password)

                # If you want check what if server respond in pxssh, execute under lines.
                #######  s.sendline('whoami')
                #######  s.prompt()
                #######  print( "before:\n"+ s.before )

                s.logout()

                cursor = self.conn.cursor()
                Update_Success(cursor, self.conn, i[0], True)

                # Added Aprl 12
                self.GoodServerList.append(i)

            except pxssh.ExceptionPxssh as e :
                cursor = self.conn.cursor()
                Update_Success(cursor, self.conn, i[0],  False)
                print( "pxssh failed on login.")
                print( str(e) )

                # Added Aprl 12
                self.BadServerList.append(i)


    def Connect_getServerDB(self) :
        print("Log, (Connect_getServerDB), conn_string : ", self.conn_string)
        self.conn = psycopg2.connect(self.conn_string)
        the_frame = pdsql.read_sql_table("servers", self.engine)
        print( the_frame.values.tolist() )
        self.ServerList = the_frame.values.tolist()
        print("Log, ServerList : ", self.ServerList)


    def Connect_DB(self):
        print('connect db')
        if self.db.SORTS == 'psql' :
            self.conn_string = "host="+self.db.HOST+" dbname="+self.db.NAME+" user="+self.db.USER+" password="+self.db.PW
            print( self.conn_string )
            # dialect+driver://username:password@host:port/database
            self.engine = sqlalchemy.create_engine("postgresql+psycopg2://" + self.db.USER.replace("'","") + ":" + self.db.PW.replace("'","")+"@" + self.db.HOST.replace("'","") + ":" + self.db.PORT.replace("'","")+ "/" + self.db.NAME.replace("'",""))
            self.conn = psycopg2.connect(self.conn_string)


        else :
            print ( "Sorry, " + self.db.SORTS + " isn't supported yet.....")

    def __str__(self) :
        return "Connector"

# 
#       Develop Log ( Aprl 15 )
#

# Aprl 15
#  Desginer Wonseok. J
#
#   Some lines are deleted and added some '\n' characters.
#   Becuase I changed IDE from atom to VS Code.