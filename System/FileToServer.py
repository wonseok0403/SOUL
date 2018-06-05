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
            tmpStr = " scp -o StrictHostKeyChecking=no " + str(self.FromDir) + " " + self.connectId + "@" + \
                        str(self.IP) + ":" + str(self.ToDir)
            return tmpStr

    def __str__(self) :
        return self.MakeCommand()

class SCPManager(object) :
    def __init__(self) :
        self.Slaves = {}

    def PrintTargetCommands(self) : 
        for i in (self.Slaves.keys()) :
            print("{}\t\t{}".format(str(i.ID), str(self.Slaves[i].MakeCommand())))

    def TryAddSlave(self,SlaveServer) :
        if( SlaveServer.IS_ERROR == "YES" ) :
            return False
        _SCPCommand = SCPCommand("", "", "", "")
        self.Slaves[SlaveServer] = _SCPCommand
        return True

    def TargetSetById(self, id) :
        SlaveList = self.Slaves.keys()
        for Serv in SlaveList :
            print(type(Serv), Serv.getInfo())
            if( id == 'all') :
                _fromDir = str(raw_input("From Dir (+FileName) : "))
                _TryConID = Serv.CONNECTION_USERNAME
                _IP = Serv.CONNECTION_IPADDRESS
                _toDir = str(raw_input("Where to go? (+FileName) : "))
                Command = SCPCommand(_fromDir, _TryConID, _IP, _toDir)
                self.Slaves[Serv] = Command

            if( Serv.ID == id ) :
                _fromDir = str(raw_input("From Dir (+FileName) : "))
                _TryConID = Serv.CONNECTION_USERNAME
                _IP = Serv.CONNECTION_IPADDRESS
                _toDir = str(raw_input("Where to go? (+FileName) : "))
                Command = SCPCommand(_fromDir, _TryConID, _IP, _toDir)
                self.Slaves[Serv] = Command

    def SetCommandForAllTargets(self, Comm) :
        for Serv in self.Slaves :
            self.Slaves[Serv] = Comm

    def SendToAllTargets(self) :
        for Serv in self.Slaves :
            Comm = self.Slaves[Serv].MakeCommand()
            if( Comm == False ) : continue
            print(Serv.CONNECTION_PASSWORD)
            os.system( "sshpass -p" + Serv.CONNECTION_PASSWORD  + self.Slaves[Serv].MakeCommand() )
            print('done!')
            raw_input()

    def DeleteServerInTargets(self, ServerKey) :
        self.Slaves.pop(ServerKey)