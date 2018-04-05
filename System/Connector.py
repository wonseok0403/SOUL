from SystemLoader import SystemLoader
import psycopg2


class Connector(object) :
    def __init__(self) :
        self.SystemLoader = SystemLoader()

    def __init__(self, objects):
        # you must input 'SystemLoader in here'
        self.SystemLoader = objects
        self.db = self.SystemLoader.DB
        self.admin = self.SystemLoader.Admin

        self.Connecting()


    # def executeQuery(qurey) :
    #     psycopg2.executeQuery(query)
    #     return psycopg2.fetch

    def Connecting(self) :
        self.Connect_DB()



    def Connect_DB(self):
        print('connect db')
        if self.db.SORTS == 'psql' :
            conn_string = "host="+self.db.HOST+" dbname="+self.db.NAME+" user="+self.db.USER+" password="+self.db.PW
            print( conn_string )
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()

        else :
            print ( "Sorry, " + db.SORTS + " isn't supported yet.....")
