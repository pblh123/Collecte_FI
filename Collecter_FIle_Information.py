# _*_ coding: utf-8 _*_
__author__ = 'pblh123'
#Find special file in windows

import os,sys
import time
import csv

#Get create time
def Ctime(File):
    ctime=time.ctime(os.path.getctime(File))
    return ctime
#Last modified time
def Mtime(File):
    mtime=time.ctime(os.path.getmtime(File))
    return mtime

#Get File size
def GetSize(File):
    Size=os.stat(File).st_size
    return Size

#Get Last access time
def Atime(File):
    atime=time.ctime(os.path.getatime(File))
    return atime

#Find special File of in special content
def Find_Files_List(Path,File_Type):
    NTS=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    with open(Path+File_Type+'_'+NTS+'.txt','w') as F:
        for root,dirs,files in os.walk(Path):
            for file in files:
                Type='.'+File_Type
                if os.path.splitext(file)[1]==Type:
                    try:
                        File=os.path.join(root,file)
                        ctime=Ctime(File)
                        mtime=Mtime(File)
                        atime=Atime(File)
                        fsize=GetSize(File)
                        Str= file+'\t'+str(fsize)+'\t'+root+'\t'+ctime+'\t'+mtime+'\t'+atime+'\n'
                        print(Str)
                        F.write(Str)
                    except:
                        print('Here is wrong!')

if __name__ == '__main__':
    print('Please input path:')
    Path=input()
    print('Please input File_Type')
    File_Type=input()
    Find_Files_List(Path,File_Type)

