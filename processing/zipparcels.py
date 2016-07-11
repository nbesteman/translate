#-------------------------------------------------------------------------------
# Name:        zip parcels for web
# Purpose:     Creates zipfile to push parcel data to the web with.
# Author:      NBesteman
# Created:     20160711
# Modified:    20160711
#-------------------------------------------------------------------------------
import os
import zipfile
unitCodeNameNoSpace = ["01AlleganTwp","02CascoTwp","03CheshireTwp","04ClydeTwp","05DorrTwp","06FillmoreTwp","07GangesTwp","08GunPlainTwp","09HeathTwp","10HopkinsTwp","11LaketownTwp","12LeeTwp","13LeightonTwp","14ManliusTwp","15MartinTwp","16MontereyTwp","17OtsegoTwp","18OveriselTwp","19SalemTwp","20SaugatuckTwp","21TrowbridgeTwp","22ValleyTwp","23WatsonTwp","24WaylandTwp","42MartinVillage","44HopkinsVillage","51AlleganCity","52FennvilleCity","53HollandCity","54OtsegoCity","55PlainwellCity","56WaylandCity","57SaugatuckCity","58SouthHavenCity","59DouglasCity"]
oldwd = os.getcwd()
#os.chdir('C:/apps/python/ESRI/Translate/build')
#Local units layer.
print "creating archive:"
for val in unitCodeNameNoSpace:
        code = val[:2]
        name = val[2:]
        print "    ",code," ", name
        os.chdir('C:/apps/python/ESRI/Translate/build/'+name+'/web/')
        #zf = zipfile.ZipFile("C:/apps/python/ESRI/Translate/build/"+name+"/web/"+name+"_parcels.zip", mode='w')
        print 'creating archive for ', name
        zf = zipfile.ZipFile(name+"_parcels.zip", mode='w')
        try:
            print 'adding '+name+'_parcels.shp'
            #zf.write('C:/apps/python/ESRI/Translate/build/'+name+'/web/'+name+'_parcels.shp')  #this results in the folder path plus file
            zf.write(name+'_parcels.shp')
            zf.write(name+'_parcels.prj')
            zf.write(name+'_parcels.dbf')
            zf.write(name+'_parcels.shx')
        finally:
            zf.close()

def main():
    pass

if __name__ == '__main__':
    main()