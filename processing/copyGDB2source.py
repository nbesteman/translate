#-------------------------------------------------------------------------------
# Name:        copyGDB2sourc.py
# Purpose:     copy AC_Cadastral.gdb to source folder
# Author:      Neil Besteman
# Created:     20160607
# Modified:    20160617 - adding request for input y/n regarding new copy of gdb
#-------------------------------------------------------------------------------
import shutil

src = r'C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb'
dst= r'C:\apps\python\ESRI\Translate\source\AC_Cadastral.gdb'
inputYN = 'n'
y = 'y'
inputYN = str(raw_input('copytreeCopy new .gdb to source folder? [y/n]:'))

def copytree(src,dst):
    print 'this is from the copytree'
    if inputYN == 'y':
        shutil.copytree(src,dst)
        print 'copied AC_Cadastral.gdb from C:\\data\\00 Allegan Co\\LGIM\\ to C:\\apps\\python\\ESRI\\Translate\\source\\'
    else:
        print 'last .gdb in source folder is being used'

if __name__ == '__main__':
    print 'this is from the local main'
    if inputYN == 'y':
        shutil.copytree(src,dst)
        print 'copied AC_Cadastral.gdb from C:\\data\\00 Allegan Co\\LGIM\\ to C:\\apps\\python\\ESRI\\Translate\\source\\'
    else:
        print 'last .gdb in source folder is being used'