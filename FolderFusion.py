# -*- coding: UTF-8 -*-

import os    
import shutil

path1 = "C:/Users/alvar_000/Desktop/dir1/"
path2 = "C:/Users/alvar_000/Desktop/dir2/"

dir1 = os.listdir(path1)
dir2 = os.listdir(path2)

def copyIfDoesntExists(source, destination):
    shutil.copy2(source, destination)
    
def isNewerFile(source, destination):
    return os.stat(source).st_mtime - os.stat(destination).st_mtime > 1

for file in dir1:
    if not file in dir2:
        copyIfDoesntExists(path1+file, path2)
    else:
        if isNewerFile(path1+file, path2+file):
            shutil.copy2 (path1+file, path2)
        
for file in dir2:
    if not file in dir1:
        copyIfDoesntExists(path2+file, path1)
    else:
        if isNewerFile(path2+file, path1+file):
            shutil.copy2 (path2+file, path1)
            
