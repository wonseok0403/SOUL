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

    def InputByUsr(self, numMax) :
        while( True ) :
            usr_input = int( raw_input('What do you want to do? : '))
            if( usr_input <= 0 or usr_input > numMax ) :
            # Zero always be 'power off'
                print('Input Error, try again!')
                flag = usr_input(''
            else :
                return usr_input


    def PrintMainMenu(self, badnum, goodnum) :
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
        usr_input = self.InputByUsr( 4 )                                    # if you add functions, you have to add '1' in parameter.
        return usr_input


    def PrintTargetMenu(self, target=[]) :
        print('                                              ')
        print(' Target Console ----------------------------------------------- ')
        for( i in target ) :
            print( '  [*]. ' + str(i) )
        print(' --------------------------------------------------- target end.')


    def PrintServerManageMenu(self, target=[]) :
        PrintTargetMenu(target)

        print('')
        print( '1 - 1. Target manage')
        print( '1 - 2. Install database ')
        print( '1 - 3. Go backup console ')
        print(' 1 - 4. Firewall manage ')

        print(' 1 - 0. Return')
        return self.InputByUsr(4)

    def TargetManageMenu(self, target=[]) :
        PrintTargetMenu(target)

        print( '1-1 - 1. Add target.')
        print( '1-1 - 2. Del target.')
    
    def PrintAllTargets(self, target=[], allTargets=[]):
        
    def AddtargetMenu(self, target=[], allTargets=[]) :
        
    def DeltargetMenu(self, target=[], allTargets=[]) :
        