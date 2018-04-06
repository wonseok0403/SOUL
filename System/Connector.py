from SystemLoader import SystemLoader
import psycopg2
import pandas.io.sql as pdsql
import pandas
import sqlalchemy


class Connector(object) :
    def __init__(self) :
        self.SystemLoader = SystemLoader()

    def __init__(self, objects):
        # you must input 'SystemLoader in here'
        self.SystemLoader = objects
        # o yes
        self.db = self.SystemLoader.DB
        self.admin = self.SystemLoader.Admin
        self.ServerList = [[]]
        self.conn_string = ""

        self.Connecting()


    # def executeQuery(qurey) :
    #     psycopg2.executeQuery(query)
    #     return psycopg2.fetch

    def Connecting(self) :
        # First, you have to connect DataBase in your local computer.
        # PostgreSQL will be the best choice. But if you want to use other version,
        # please check program version.
        self.Connect_DB()
        self.Connect_getServerDB()

        # Second, program will get server data from your local database.

    def Connect_getServerDB(self) :
        print("Log, (Connect_getServerDB), conn_string : ", self.conn_string)
        conn = psycopg2.connect(self.conn_string)
        the_frame = pdsql.read_sql_table("SERVERS", self.engine)
        print( the_frame.values.tolist() )
        self.ServerList = the_frame.values.tolist()
        print(self.ServerList)


    def Connect_DB(self):
        print('connect db')
        if self.db.SORTS == 'psql' :
            self.conn_string = "host="+self.db.HOST+" dbname="+self.db.NAME+" user="+self.db.USER+" password="+self.db.PW
            print( self.conn_string )
            # dialect+driver://username:password@host:port/database
            self.engine = sqlalchemy.create_engine("postgresql+psycopg2://" + self.db.USER.replace("'","") + ":" + self.db.PW.replace("'","")+"@" + self.db.HOST.replace("'","") + ":" + self.db.PORT.replace("'","")+ "/" + self.db.NAME.replace("'",""))
            conn = psycopg2.connect(self.conn_string)



        else :
            print ( "Sorry, " + db.SORTS + " isn't supported yet.....")
