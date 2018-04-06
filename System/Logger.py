
class Logger(object) :
    # If you want just define logger,
    def __init__(self) :
        self.d = "d"


    # If you define logger as something special
    def __init__(self, object) :
        # Connector
        print('Logger making start!')
        print( object )
        if( str(object) == "Connector" ):
            print("Logger of connector is made!")
