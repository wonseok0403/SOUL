class Administrator(object) :
    def __init__(self):
        print('Log : Administrator initializer is loaded! ')
        self.NAME = ""
        self.PW = ""
        self.ID = ""
        self.MODE = ""

    def printInfo(self) :
        # STRUCTURE :
        # NAME : \nHOST : \n ...
        print('Administrator Information ~')
        print('Name  : ' + self.NAME)
        print('ID    : ' + self.ID)
        print('MODE  : ' + self.MODE)
        print('PW    : ' + "Check the file (for security)")
        print('')

    def __str__(self) :
        return "AdministratorClass"
