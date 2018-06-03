# @Author       Wonseok
# @Designer     Wonseok
# @Start at     June, 4
# @Last at      June, 4
# @Music        
# @Information

import os, sys
sys.path.insert( 0, os.getcwd() )
from ObjectInfo import DatabaseClass
from ObjectInfo import Server
from pexpect import pxssh
import psycopg2

class SCPCommand(object) :
    def __init__(self, _fromDir="", _connectId="", _iP="", _toDir="") :
        self.FromDir = _fromDir
        self.connectId = _connectId
        self.IP = _iP
        self.ToDir = _toDir

    def Set(self, _fromDir, _connectId, _ip, _toDir) :
        self.FromDir = _fromDir
        self.connectId = _connectId
        self.IP = _ip
        self._toDir = _toDir

    def MakeCommand(self) :
        if( self.FromDir == None or \
                self.connectId == None or \
                self.IP == None or \
                self.ToDir == None  ) :
            return False
        else :
            tmpStr = "scp " + str(self.FromDir) + " " + self.connectId + "@" + \
                        str(self.IP) + ":" + str(self.ToDir)
            return tmpStr

class SCPManager(object) :
    def __init__(self, MasterServer) :
        self.Master = MasterServer
        self.Slaves = {}

    def TryAddSlave(self,SlaveServer) :
        if( SlaveServer.IS_ERROR == "YES" ) :
            return False
        _SCPCommand = SCPCommand("", "", "", "")
        self.Slaves[SlaveServer] = _SCPCommand
        return True

    def TargetSetById(self, id) :
        _id = int(input("Input you want to set : "))
        for Serv in self.Slaves :
            if( Serv.ID == id ) :
                _fromDir = str(input("From Dir (+FileName) : "))
                _TryConID = Serv.CONECTION_USERNAME
                _IP = Serv.CONNECTION_IPADDRESS
                _toDir = str(input("Where to go? (+FileName) : "))
                Command = SCPCommand(_fromDir, _TryConID, _IP, _toDir)
                self.Slaves[Serv] = Command

    def SendToAllTargets(self) :
        for Serv in self.Slaves :
            Comm = self.Slaves[Serv].MakeCommand()
            if( Comm == False ) : continue
            Serv.ThrowCommand( self.Slaves[Serv].MakeCommand() )
