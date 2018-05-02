''' 
 If you want to share this system to others or another people,
you have to execute this file to remove your own data. 
unless, your data will be get fire by someone.
So please erase your local data from here. I believe you may understand.
'''
import os, sys

def ConfigureFire() :
    Configure = open('Configure.txt', 'w')
    Configure.write('Execute=no')
    Configure.close()
    
def UserConfigFire() :
    os.system('rm ./UserConfig/*.txt')    

def ReportFire() :
    os.system('rm ./Report/*.txt')

def srcFire() :
    os.system('rm -r src')

def FireForGit() :
    ConfigureFire()
    UserConfigFire()
    ReportFire()
    srcFire()


# If you want to share your project to git, 
# just execute it!
if __name__ == '__main__' :
    FireForGit()
