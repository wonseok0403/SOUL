#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
# @Author       Wonseok
# @Designer     Wonseok
# @Start at     May 2
# @Last at      May 2
# @Music        CRAYON - G.DRAGON
# @Information  This class is only for User Interface.
#               You don't need to be worried by designing UI.

from anytree import Node, RenderTree

class UserInterface(object) :


    def clear(self) :
        # you just call this function to clean the screen.
        os.system(self.cls)

    def __init__(self, objects ) :
        # I want to make this class in GUI mode, but I don't have enough time and work force.
        self.MODE = 'CUI'
        if( objects.OS_SORT == 1 ) : # 1 is Linux
            self.cls = 'clear'
        elif( objects.OS_SORT == 2 ) :   # Windows
            self.cls = 'cls' 


        # level = 0, you have to exit menu.
        self.root = Node("Null")

        # level = UI
        self.nodUI = Node("UserInterface", parent=self.root)

        # level = 2, PSM, DM, CM, SM, PO
        self.ServerMenu = Node("PrintServerManageMenu", parent=self.nodUI)
        self.DBMenu = Node("DatabaseManage", parent=self.nodUI)
        self.ConfigMenu = Node("Configuration Mode", parent=self.nodUI)
        self.SecurityMode = Node("Security Mode", parent=self.nodUI)
        self.PowerOff =  Node("Power Off", parent=self.nodUI)

        # level = 3, TM, ID, GBC, FM
        self.TargetManage = Node("Target Manage", parent=self.ServerMenu)
        self.InstallDatabase = Node("Install database", parent=self.ServerMenu)
        self.GoBackupCons = Node("Go Backup Console", parent=self.ServerMenu)
        self.FirewallManag = Node("Firewall manage", parent=self.ServerMenu)
            
        # level = 4, TMM
        self.TMM = Node("Target Manage Menu", parent=self.TargetManage)
            
        # level = 5, AM, DM, SystemUpdate, ThrowMessage
        self.AM = Node("AddtargetMenu", parent=self.TMM)
        self.DM = Node("DeltargetMenu", parent=self.TMM)
        self.SystemUpdate = Node("System Update", parent = self.TMM)
        self.ThrowMsg = Node("Throw message", parent=self.TMM)
        
        # level = 6, OSUpgrade, Cron update
        self.OSUpgrade = Node("Operating System Upgrade", parent=self.SystemUpdate)
        self.UpdateUpgrade = Node("Update & Upgrade", parent=self.SystemUpdate)
        self.CronUpdate = Node("Cron update", parent=self.SystemUpdate)

        
    def SystemUpdateMenu(self,target, nod) :
        self.PrintTargetMenu(target)

        print('')
        print( '1 - 1. Operating System Upgrade')
        print( '1 - 2. Update & Upgrade')
        print( '1 - 3. update at cron ')
        print(' 1 - 0. return to menu ')

        usr_input = self.InputByUsr( 'Which one do you want to go?', 3 )
        if( usr_input == 1 ) :
            nod[0] = self.OSUpgrade
        elif( usr_input == 2 ) :
            nod[0] = self.UpdateUpgrade
        elif( usr_input == 3 ) :
            nod[0] = self.CronUpdate
        elif( usr_input == 0 ) :
            nod[0] = nod[0].parent

        raw_input('')

    def OperatingSystemUpgrade(self, target=[[]], nod=None ) :
        self.PrintTargetMenu(target)
        ''' 
            You can add more OS in here 
        '''
        OSList = {}
        OSList['ubuntu'] = []
        OSList['cent'] = []
        OSList['debian'] = []
        for i in target :
            if( i == [] ) :
                print("You must regist target in befre menu.")
                raw_input('')
            else :
                if( str(i[8]).find('Ubuntu') != -1 ) :
                    OSList['ubuntu'].append(i)
                elif( str(i[8]).find('Cent') != -1 ) :
                    OSList['cent'].append(i)
        print(OSList)
        raw_input()

        return OSList


    def InputByUsr(self, msg='', numMax=None) :
        
        if numMax == None :
            return raw_input(msg)

        while( True ) :
            usr_input = int( raw_input('What do you want to do? : '))
            if( usr_input < 0 or usr_input > numMax ) :
            # Zero always be 'power off'
                print('Input Error, try again!')
                flag = raw_input(msg)
            else :
                return usr_input


    def PrintMainMenu(self, badnum, goodnum, nod) :
        self.clear()
        print('                  *         *         *                 ')
        print('              *      SOUL      *             *          ')
        print('  *              * *     *       *                 *    ')
        print('                                                 ver 0.5')
        print('')
        print('    1. Server manage.                                ')
        print('    2. Database manage.                              ')
        print('    3. Configuration mode.                           ')
        print('    4. Security mode.                                ')
        print('    0. Power off.                                    ')
        print('')
        print('')
        print(' Num( bad servers  ) : ' + str(badnum))
        print(' Num( good servers ) : ' + str(goodnum))
        print('')
        usr_input = self.InputByUsr( 'Which one do you want to go?', 4 )                                    # if you add functions, you have to add '1' in parameter.
        
        if usr_input == 1  :
            nod[0] = self.ServerMenu
            raw_input()
        elif usr_input == 2  :
            nod[0] = self.DBMenu
        elif usr_input == 3 :
            nod[0] = self.ConfigMenu
        elif usr_input == 4 :
            nod[0] = self.SecurityMode
        # add additional function at this line.
        else : 
            nod[0] = self.root 

    def PrintTargetMenu(self, target=[]) :
        # Target list is chosen targets which user picked.

        print('                                              ')
        print(' Target Console ----------------------------------------------- ')
        for i in target  :
            print( '  [*]. ' + str(i) )
        print(' --------------------------------------------------- target end.')


    def PrintServerManageMenu(self, target=[[]], nod=None) :
        # Target list is chosen targets which user picked.
        self.PrintTargetMenu(target)

        print('')
        print( '1 - 1. Target manage')
        print( '1 - 2. Install database ')
        print( '1 - 3. Go backup console ')
        print(' 1 - 4. Firewall manage ')

        print(' 1 - 0. Return')
        key =  self.InputByUsr('Which one do you want to go?', 4)
        if( key == 1 ) :
            nod[0] = self.TargetManage
        elif key == 2 :
            nod[0] = self.InstallDatabase
        elif key == 3 :
            nod[0] = self.GoBackupCons
        elif key == 4 :
            nod[0] = self.FirewallManag
        else :
            print('input error!')
        raw_input('')

    def TargetManageMenu(self, target=[], nod=None) :
        self.PrintTargetMenu(target)

        print( '1-1 - 1. Add target.')
        print( '1-1 - 2. Del target.')
        print( '1-1 - 3. System Update Menu')
        print(' 1-1 - 4. Throw Messages')
        print( '1-1 - 0. Return.')
        key =  self.InputByUsr('Which one do you want to go?', 4)
        if( key == 1 ) :
            nod[0] = self.AM
        elif key == 2 :
            nod[0] = self.DM
        elif key == 3 :
            nod[0] = self.SystemUpdate
        elif key == 4 :
            nod[0] = self.ThrowMsg
        elif key == 0 :
            nod[0] = self.ServerMenu
        else :
            print('Input error!')
            raw_input()
    
    #[[2, 22, u'ssh', u'123', u'123', u'123', u'123', 123, u'test', u'test', u'YES', u'2018-05-07 21:52:48.022944', None, None], [4, 22, u'ssh', u'45.77.180.147', u'P]9p{PWKRu=+o7y]', u'root', u'Wonseok.J', 970403, u'CentOS 7 x64', u'WonseokTest2Cent', u'', u'2018-05-07 21:52:58.786149', None, None], [6, 23, u'ssh', u'1.201.140.106', u'Wonseok786!', u'swc', u'Wonseok.J', 1065, u'Ubuntu14', u'WonseokTest3', u'YES', u'2018-05-07 21:53:49.822362', None, None]]
    def PrintAllTargetsDetails(self, targets=[[]], badTargets=[[]], goodTargets=[[]] ,nod=None):
        # Target list is chosen list user picked, and allTargets list is a list of all servers.
        # [ID], [PORT], [SORT], [IP], [PASSWORD]. [USRNAME], [OWNR NAME], [ OWNR_ID ], [SERVER OS], [SERVER NAME], [IS ERROR], [LAST_LOGIN], [dbkey], [obj key]
        print("CONNECTION STATUS : BAD ")
        print("[ADDED]\t\t[ER]\t[ID]\t\t[SERVER NAME]\t\t\t\t[IP]\t\t\t\t[SSH ID]\t\t[SSH PW]\t\t\t[LAST LOGIN]")
        for badtarget in badTargets :
            if badtarget == [] : break
            print("{}\t\t{}\t{}\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t{}\t\t\t{}".format(str(badtarget in targets), str(badtarget[10]), str(badtarget[0]), str(badtarget[9]), str(badtarget[3]), str(badtarget[7]),str(badtarget[4]), str(badtarget[11])))
        print("")
        print("[ADDED]  CONNECTION STATUS : GOOD")
        for badtarget in goodTargets :    # Yes I know. badtarget must be good target. but... I'm lazy... so.. I won't change it. badtarget is good target.. you know...        
            if badtarget == [] : break
            print("{}\t\t{}\t{}\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t{}\t\t\t{}".format(str(badtarget in targets), str(badtarget[10]), str(badtarget[0]), str(badtarget[9]), str(badtarget[3]), str(badtarget[7]),str(badtarget[4]), str(badtarget[11])))

        print("\n\n")
        print("Already Targets : ")
        print("[ID]     [SERVERNAME]        [IP]        [SORT]")
        for target in targets :
            if target == [] : break
            print("{}       {}                  {}          {}".format(str(target[0]), str(target[9]), str(target[3]), str(target[2])))

        nod[0] = self.TMM
        raw_input('')

    def ChkValue(self, id, target, bad, good) :
        '''
        @return     1 - is in target,       MSG = None <type>
                    2 - is in bad           MSG = list[ that node ]
                    3 - is in good          MSG = list[ that node ]
                    4 - not found           MSG = That is not in both bad and good lists.
        '''
        # target, bad, good = [ [] ] is list in list.
        # check is in target.
        for i in target :
            if i == [] : break
            #print(id,type(id), i[0], type(i[0]))
            if( str(id) == str(i[0]) ) :
                return 1, i
        
        # check is in bad
        for i in bad :
            #print(id,type(id), i[0], type(i[0]))
            if i == [] : break
            if( str(id) == str(i[0]) ) :
                return 2, i
        
        # check is in good
        for i in good :
            #print(id,type(id), i[0], type(i[0]))
            if i == [] : break
            if( str(id) == str(i[0]) ) :
                return 3, i
        
        return 4, 'That is not in both bad and good lists.'



    def AddtargetMenu(self, target=[[]], badTargets = [[]], goodTargets = [[]], nod=None) :
        self.PrintAllTargetsDetails(target, badTargets, goodTargets,nod)
        print("\n")
        want_id = self.InputByUsr('Which one do you want to add? input [ID] value : ', None)
        num, msg = self.ChkValue(want_id, target, badTargets, goodTargets)
        if( num == 2 or num == 3 ) :
            if( target.count([]) != 0 ) : target.remove([])
            target.append( msg )
            nod[0] = nod[0].parent
        else :
            print("Caution! Error occured!")
            print("Error code : " + str(num))
            print("Error msg : " + str(msg))
            print("\nReturn before menu!")

        

        
    def DeltargetMenu(self, target=[[]], badTargets = [[]], goodTargets = [[]], nod=None) :
        self.PrintAllTargetsDetails(target, badTargets, goodTargets,nod)
        print("\n")
        want_id = self.InputByUsr('Which one do you want to delete? input [ID] value : ', None)
        num, msg = self.ChkValue(want_id, target, badTargets, goodTargets)
        if( num == 1 ) :
            target.remove( msg )
            nod[0] = nod[0].parent
        else :
            print("Caution! Error occured!")
            print("Error code : " + str(num))
            print("Error msg : " + str(msg))
            print("\nReturn before menu!")
            raw_input()
