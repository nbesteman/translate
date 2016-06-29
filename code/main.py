#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NBesteman
#
# Created:     07/06/2016
# Copyright:   (c) NBesteman 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

src = r'C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb'
dst= r'C:\apps\python\ESRI\Translate\source\AC_Cadastral.gdb'

import os
import copyGDB2source
#import splits_gdb_2_shp need to fix this one
print 'need to fix line 17 of main.py'
##def main():
##    pass
##if __name__ == '__main__':
##    main()

print 'copy gdb'
# this will replace the .bat file containing xcopy "C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb" C:\apps\python\ESRI\Translate\source\AC_Cadastral.gdb

copyGDB2source.copytree(src,dst)

#time.sleep(1)

print 'finished'