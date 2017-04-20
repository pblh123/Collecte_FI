# _*_ coding: utf-8 _*_
__author__ = 'pblh123'
#Find special file in windows Python3

import os,sys
import time


#Get create time
def Ctime(File):
    ctime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(File)))
    return ctime
#Last modified time
def Mtime(File):
    mtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(File)))
    return mtime

#Get File size
def GetSize(File):
    Size=os.stat(File).st_size
    return Size

#Get Last access time
def Atime(File):
    atime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getatime(File)))
    return atime

#Find special File of in special content
def Find_Files_List(Path,File_Type):
    NTS=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    with open(Path+File_Type+'_'+NTS+'.txt','w') as F:
        Title="文件名"+'\t'+"文件大小"+'\t'+"文件路径"+'\t'+"文件创建时间"+'\t'+"文件修改时间"+'\t'+"最后访问时间"+'\n'
        F.write(Title)
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

