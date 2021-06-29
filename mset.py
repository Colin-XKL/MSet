from shutil import which
import os
commands={}

def installed(name:str):
    return which(name) is not None

def new_command_map(cmd:list,func):
    global commands
    for k in cmd:
        commands[k]=func

def pypi():
    return os.system('pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple')
    
if __name__=='__main__':
    print("MSet")
    failed=pypi()
    if failed:
        print('ooops')
