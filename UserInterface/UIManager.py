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
        print('    4. Security check mode.                          ')
        print('')
        print('')
        print(' Num( bad servers  ) : ' + str(badnum))
        print(' Num( good servers ) : ' + str(goodnum))
        print('')
        usr_input = int(raw_input('What do you want to do? : '))
        return usr_input