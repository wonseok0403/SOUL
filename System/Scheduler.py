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

# Scheduler class make schedule using crontab command for user in easy way.
# It will check if the server is okay to connect, and if that is okay then it will send command to server.
# You don't worry to make command and send it to server.
class Scheduler(object) :

    # This function makes command for sending server.
    # This command will be exectued in user's server.
    def MakeCommand(self) :
        strTmp = ""
        for i in range(0, 5) :
            strTmp += str(self.OutputList[i]) + " "
        strTmp += self.CommandAtLst

        return ('cat < (crontab -l) < (echo "' + strTmp + '") | crontab -')

    # MIN HOUR DAY MONTH DATE
    # producedure : Month -> Date -> Day -> Hour -> Min
    def PrintAndInput(self) :
        for i in range(0, 5) :
            self.PrintValues(i)
            self.InputValue(i)

        self.PrintValues(5)

    def InputCommand(self) :
        print('Please input command you want to execute : ')
        self.CommandAtLst = raw_input()



    # This function is just for input some variables.
    # You have to check algorithm and __init__ comment before you see this lines.
    def InputValue(self, num) :
        if( num == 0 ) :
            # Month
            print('What month are you going to do it? : ')
        elif( num == 1 ) :
            # Date
            print('What date are you going to do it? \n')
            print('SUN      MON      TUE     WED     THU     FRI     SAT \n')
            print('0        1        2       3       4       5       6\n')
            print('-> ')
        elif( num == 2 ) :
            # Day
            print('What day are you going to do it? : ')
        elif( num == 3 ) :
            # Hour
            print('What hour are you going to do it? : ')
        elif( num == 4 ) :
            # Minute
            print('What minute are you going to do it? : ')


        # Korean usually say : month-> date -> day -> hour-> Minute .
        # This function change to crontab producedure.
        self.InputList[num] =  raw_input()
        self.OutputList[(self.KeyOfList[num])] = self.InputList[num]


    # This function is just for print values to help user to make command.
    # After this function, you have to execute input function to input some values.
    def PrintValues(self, num) :  # recursive function
        strTable = "MIN     HOUR    Day     MONTH   DATE"
        strTmp = ""
        for i in range(0, 5) :
            if( self.OutputList[i] == None ) :
                strTmp += '.\t'
            else :
                strTmp += str(self.OutputList[i])+'\t'

        os.system('clear')
        print('Now (Every = *) : ' + '\n' + strTable)
        print(strTmp + '\n\n')


    # This function is main function in this class
    # Whenever user wants to make schedule, this function will make special schedule.
    def MakeSchedule(self) :
        while( True ) :
            self.PrintAndInput()
            self.InputCommand()
            strTmp = self.MakeCommand()
            flag = raw_input(strTmp + '\nCommand will be excuted! is it right? (y/n) ')
            if( flag == 'y' or flag == 'Y' ) :
                print('Okay!')
                break
            else :
                print('Retry it!')
                self.InputList = [None, None, None, None, None]
                self.OutputList = [None, None, None, None, None]
                flag = raw_input()

    def SendCommandToServer(self):
        # You have to write code in here
        # -- Lst Aprl 14


    def __init__(self, object) :
        # This argument is important. Korean usually say this produce,
        # Year -> Month -> Day -> Hour -> Minute -> Second
        # But Crontab command's produce is
        # Minute -> Hour -> Day -> Month -> DATE
        # So this dict will change American's dict to Korean's
        self.KeyOfList = {
            0 : 3,
            1 : 4,
            2 : 2,
            3 : 1,
            4 : 0
        }

        self.InputList = [None, None, None, None, None]     # This list is raw list
        self.OutputList = [None, None, None, None, None]    # This list is changed for crontab command
        self.CommandAtLst = ""                          # This command is final string when you write in crontab command

        if( str(object) != "Server" ) :
            print( str(object) + "'can't register any cron service! ")



# note :
# lst update aprl 14 with 'Stronger than you - Sans and ... trio'
# Test : <None>
if __name__ == "__main__" :
    # You need server
    testServer = Server.Server()

    # You have to make scheduler
    Scheduler = Scheduler(testServer)

    # You have to execute function named 'MakeSchedule'
    Scheduler.MakeSchedule()
