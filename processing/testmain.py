#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Main module used to translate data from a geodatabase into shapefile and tab formats.  It also changes the projection.
# Author:      Neil Besteman
# Created:     20160607
# Modified:    20160615
#-------------------------------------------------------------------------------
#src = r'C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb'
#dst= r'C:\apps\python\ESRI\Translate\source\AC_Cadastral.gdb'

#import os
import classUnit

#classUnit.unit01.displayUnit()
#classUnit.unit59.displayUnit()
#classUnit.unit01.displayUnit()
#for value in classUnit.unitName:
  #      print value

u = classUnit.unit01.passUnit()

print u

eList = classUnit.unit01.passExtentVals()
print eList
def main():
    pass

if __name__ == '__main__':
    main()
#UnitList.units(fmcd,unit,code,twprng,propername,shortname,unittype)
#time.sleep(1)
