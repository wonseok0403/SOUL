#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 13
# @Last at      Aprl. 15
# @Music        Angel - Drunken Tiger with Yoon - mire, bizzy
# @Information  This class supports you that you can do cron service easy.
#               If you want to execute program at regular time, you can regist it easily.
#               And also, cron service remains logs in log DB.
import os, sys
sys.path.insert(0, os.getcwd() )
from Logger import Logger
from ObjectInfo import Server
import time, datetime

# Scheduler class make schedule using crontab command for user in easy way.
# It will check if the server is okay to connect, and if that is okay then it will send command to server.
# You don't worry to make command and send it to server.
class Scheduler(object) :

    def __init__(self, object) :
        # This argument is important. Korean usually say this produce,
        # Year -> Month -> Day -> Hour -> Minute -> Second
        # But Crontab command's produce is
        # Minute -> Hour -> Day -> Month -> DATE
        # So this dict will change American's dict to Korean's

        if( str(object) != "Server" ) :
            # remain the log if you have more time.
            print( str(object) + "'can't register any cron service! ")
        else :
            self.Server = object

        self.KeyOfList = {
            0 : 3,
            1 : 4,
            2 : 2,
            3 : 1,
            4 : 0
        }
        self.db = object.db
        self.InputList = [None, None, None, None, None]     # This list is raw list
        self.OutputList = [None, None, None, None, None]    # This list is changed for crontab command
        self.CommandAtLst = ""                          # This command is final string when you write in crontab command


    # This function makes command for sending server.
    # This command will be exectued in user's server.
    def MakeCommand(self) :
        strTmp = ""
        for i in range(0, 5) :
            strTmp += str(self.OutputList[i]) + " "
        strTmp += self.CommandAtLst

        return ('cat <(crontab -l) <(echo "' + strTmp + '") | crontab -')

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
                print('Sending...')
                break
            else  :
                print('Do you want to exit? (y/n) ')
                falg = raw_input()
                if( flag == 'y' or flag == 'Y') :
                    return

                print('Retry it!')
                self.InputList = [None, None, None, None, None]
                self.OutputList = [None, None, None, None, None]
                flag = raw_input()
        
        # from break command
        return strTmp


    # This function is for send command server. 
    # Main alogorithm is, check the server if service is online, send the command, remain the log.
    # Lst updated at Aprl 15 with I'm not laughing ( Leesang )
    def MakeAndSendCommand(self):
        # Is server okay to connect ?
        # Make Logger for if you have some issue to connect server, make report and send log to DB.
        SchedulerLogger = Logger(self)              # This is for before line.
        
        if( self.Server.IS_ERROR == 'YES' ) :
            # The server has some error. Try connect?
            print('The report says server is not online. Do you want to test the server? (y/n)')
            isOkay = raw_input()
            if( (isOkay is not 'y') and (isOkay is not 'Y')) : 
                # Server status is BAD < report >
                # No I don't want to connect.
                print('return to before menu!')
                flag = raw_input()
                return

            isOkayServer, ServerMsg = self.Server.isTryConnect()
            if( isOkayServer == False ) :
                # Server status is BAD < report >
                # Yes I wanted to connect. But server is still BAD.
                print('Sorry, the server connection is so bad.')
                self.SendLog_ConnectionBad(SchedulerLogger, ServerMsg)
                # Send log < Not connect >
                return
                
        print('Server connection is successful!')
        print('Press any key to continue!')
        flag = raw_input()  # just UI

        # Server is good or was not good but now good.
        # You have to connect the server and send message to DB ! below here
        Usr_Comd = self.MakeSchedule()                          # Get Command.
        isSuccess, msg = self.Server.ThrowCommand(Usr_Comd)     # This function returns if success, and message from try ~ catch
        if( isSuccess == True ) :
            self.Server.ThrowCommand('crontab -l')
            print('I sent message successfully!')
        else :
            print("I coudln't send message to server!")
            # Send log < Not connect or cron msg >


    def SendLog_ConnectionBad (self, Logger, ExceptionMsg) :
        # Log structure :
        ##   [ADMIN.ID] tried to connect [ServerID] by [ServerRole]@[Host] at [Date.time]
        ##   Server was [Server.isOkay]. And program tried to connect, but server connection is BAD.
        ##   specific report which pssh says is here : [Exception E]
        strLogMsg = str(self.Server.admin.ID) + " tried to connect " + str(self.Server.ID) + " by " + str(self.Server.CONNECTION_USERNAME)+"@" + str(self.Server.CONNECTION_IPADDRESS)  + " at " + str(datetime.datetime.now()) + "\n" + \
                    "Server was " + self.Server.IS_ERROR + ". And program tried to connect, but server connection is BAD." + "\n" + \
                    "specific report which pssh says is here : " + str(ExceptionMsg)
        Logger.SetOrigin('KNOWN_LOG')
        RK = Logger.MakeReport( 'SERVICE_STATUS_CHECK', self.Server.admin.PATH, 'Wonseok', strLogMsg)
        Logger.push_log( 'CONNECT', self.Server.ID, RK, 'KNOWN_LOG', 'BAD', 'Scheduler.SendLog_ConnectionBad', 'SCHEDULER')


    def __str__(self) :
        return "Scheduler" 



        


# note :
# lst update aprl 14 with 'Stronger than you - Sans and ... trio'
# Test : <None>
if (__name__ == "__main__") :
    '''
    # You need server
    testServer = Server.Server()

    # You have to make scheduler
    Scheduler = Scheduler(testServer)

    # You have to execute function named 'MakeSchedule'
    Scheduler.MakeSchedule()

    # Test completed. it was successful. ( ~ Aprl 15 )
    '''
    testServer = Server.Server(1, 22, 'ssh', '45.77.177.76', '3@mHze=5K{1wj){}', 'root', 'Wonseok', 970403, 'ubuntu', 'WonseokTestbuntu',None,'2018-01010101')
    Scheduler = Scheduler(testServer)

    Scheduler.MakeAndSendCommand()
