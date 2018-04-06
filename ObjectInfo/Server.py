class Server(object) :
    def __init__ (self) :
        self.ID = ""
        self.CONNECTION_PORT = ""
        self.CONNECTION_SORT = ""
        self.CONNECTION_IPADDRESS = ""
        self.CONNECTION_PASSWORD = ""
        self.CONNECTION_USERNAME = ""
        self.OWNER_NAME = ""
        self.OWNER_ID = ""
        self.SERVER_OS = ""
        self.SERVER_NAME = ""
        self.IS_ERROR = ""

    def __init__(slef, i, p, s, ip, pa, u, n, id, os, Na, IE) :
        self.ID = i
        self.CONNECTION_PORT = p
        self.CONNECTION_SORT = s
        self.CONNECTION_IPADDRESS = ip
        self.CONNECTION_PASSWORD = pa
        self.CONNECTION_USERNAME = u
        self.OWNER_NAME = n
        self.OWNER_ID = id
        self.SERVER_OS = os
        self.SERVER_NAME = Na
        self.IS_ERROR = IE

    def __str__ :
        return "Server"
