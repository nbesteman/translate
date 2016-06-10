#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     copy AC_Cadastral.gdb to source folder
# Author:      Neil Besteman
# Created:     20160607
# Modified:    20160609
#-------------------------------------------------------------------------------
import shutil
src = r'C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb'
dst= r'C:\apps\python\ESRI\Translate\source\test\AC_Cadastral.gdb'

def copytree(src,dst):
    shutil.copytree(src,dst)
    pass
if __name__ == '__main__':
    copytree(src,dst)
    print 'copied AC_Cadastral.gdb from C:\\data\\00 Allegan Co\\LGIM\\ to C:\\apps\\python\\ESRI\\Translate\\source\\'
