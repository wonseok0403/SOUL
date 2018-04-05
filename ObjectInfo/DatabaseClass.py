
# This class will have information between this program with program log & configure DB
# After load onnection, connector has to have connection with servers.
class DB(object) :
    def __init__(self):
        print('Log : Database initializer is loaded! ')
        # If you use sort 'PostgreSQL', input 'psql', 'MS-SQL', input 'mssql',
        # 'MySQL', input 'mysql', 'ORACLE', input 'orac', 'SQLITE', 'sqlite'
        self.SORTS = ""                     # Database management name
        self.HOST = ""                      # Database host ip xxx.xxx.xxx.xxx
        self.PORT = ""                      # Database port (1000 ~ 9999)
        self.NAME = ""                      # Database Name
        self.PW   = ""                      # Database password
        self.USER = ""                      # Database user

    def printInfo(self) :
        # STRUCTURE :
        # NAME : \nHOST : \n ...
        print('Database Information ~')
        print('Name  : ' + self.NAME)
        print('SORTS : ' + self.SORTS)
        print('PORT  : ' + self.PORT)
        print('HOST  : ' + self.HOST)
        print('USER  : ' + self.USER)
        print('PW    : ' + "Check the file (for security)")
        print('')

    def __str__(self) :
        # if you need system's db info, you can get information by
        # parsing below string.
        return(self.SORTS+ ':' + self.HOST + ':' + self.PORT+ ':' + self.NAME+ ':' + self.PW + ':' + self.USER)
