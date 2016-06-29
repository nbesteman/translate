#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Main module used to translate data from a geodatabase into shapefile and tab formats.  It also changes the projection.
# Author:      Neil Besteman
# Created:     20160607
# Modified:    20160617
#-------------------------------------------------------------------------------
src = r'C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb'
dst= r'C:\apps\python\ESRI\Translate\source\AC_Cadastral.gdb'

import os
import copyGDB2source
import selectsplitsGDB2shp
#import parcelsGDB2shp
import UnitList
import classUnit


#copyGDB2source.copytree(src,dst)
#parcelsGDB2shp.parcels()
selectsplitsGDB2shp.splits()
#UnitList.units(fmcd,unit,code,twprng,propername,shortname,unittype)
#for row in units:
#    print fmcd
#time.sleep(1)
print 'finished'

