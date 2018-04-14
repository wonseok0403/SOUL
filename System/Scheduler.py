# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 13
# @Last at      Aprl. 14
# @Music        Angel - Drunken Tiger with Yoon - mire, bizzy
# @Information  This class supports you that you can do cron service easy.
#               If you want to execute program at regular time, you can regist it easily.
#               And also, cron service remains logs in log DB.
import os, sys
sys.path.insert(0, os.getcwd() )
from ObjectInfo import Server

class Scheduler(object) :
    # MIN HOUR DAY MONTH DATE
    # producedure : Month -> Date -> Day -> Hour -> Min
    def Print_WhichDoYouWant(self) :
        for i in range(0, 5) :
            self.PrintValues(i)
            self.InputValue(i)

        self.PrintValues(5)


    def InputValue(self, num) :
        if( num == 0 ) :
            print('What month are you going to do it? : ')
        elif( num == 1 ) :
            print('What date are you going to do it? (Sunday -> 0 ~ Saturday -> 6) : ')
        elif( num == 2 ) :
            print('What day are you going to do it? : ')
        elif( num == 3 ) :
            print('What hour are you going to do it? : ')
        elif( num == 4 ) :
            print('What minute are you going to do it? : ')

        self.InputList[num] = input()
        self.OutputList[(self.KeyOfList[num])] = self.InputList[num]



    def PrintValues(self, num) :  # recursive function
        strTmp = ""
        for i in range(0, 5) :
            if( self.OutputList[i] == None ) :
                strTmp += '.\t'
            else :
                strTmp += str(self.OutputList[i])+'\t'

        os.system('clear')
        print('Now : ')
        print(strTmp + '\n\n')


    def __init__(self, object) :
        self.KeyOfList = {
            0 : 3,
            1 : 4,
            2 : 2,
            3 : 1,
            4 : 0
        }
        self.InputList = [None, None, None, None, None]
        self.OutputList = [None, None, None, None, None]
        if( str(object) != "Server" ) :
            print( str(object) + "'can't register any cron service! ")



# note :
# lst update aprl 14 with 'Stronger than you - Sans and ... trio'
# Test : <None>
if __name__ == "__main__" :
    testServer = Server.Server()
    Scheduler = Scheduler(testServer)
    Scheduler.Print_WhichDoYouWant()
