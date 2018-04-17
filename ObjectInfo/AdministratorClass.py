# @Author       Wonseok
# @Designer     Wonseok
# @Start at     Aprl. 13
# @Last at      Aprl. 13
# @Music        Paranoid - U Won Jae
# @Information  Ths class is for 'Human'. If you have more time, You can design it using 'Heritance'


class Administrator(object) :
    def __init__(self, Name=None, Path=None, Pw=None, Mode=None, Id=None):
        print('Log : Administrator initializer is loaded! ')
        self.NAME = Name
        self.PATH = Path
        self.PW = Pw
        self.MODE = Mode
        self.ID = Id

    def printInfo(self) :
        # STRUCTURE :
        # NAME : \nHOST : \n ...
        print('Administrator Information ~')
        print('Name  : ' + str(self.NAME))
        print('PATH  : ' + self.PATH)
        print('ID    : ' + str(self.ID))
        print('MODE  : ' + self.MODE)
        print('PW    : ' + "Check the file (for security)")
        print('')
    
    def getInfo(self) :
        strMsg = "NAME = " + str(self.NAME) + \
            "PATH = " + str(self.PATH) + \
            "PW = " + str(self.PW) + \
            "MODE = " + str(self.MODE) + \
            "ID = " + str(self.ID)
        return strMsg

    def __str__(self) :
        return "ADMINISTRATORCLASS"
