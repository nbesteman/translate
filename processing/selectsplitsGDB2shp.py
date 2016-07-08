#-------------------------------------------------------------------------------
# Name:        selectsplitsGDB2shp
# Purpose:     Selects splits by code in deodatabase and translates them to shapefile format.
# Author:      Neil Besteman
# Created:     20160616
# Modified:    20160701
#-------------------------------------------------------------------------------
import arcpy
unitCodeNameNoSpace = ["01AlleganTwp","02CascoTwp","03CheshireTwp","04ClydeTwp","05DorrTwp","06FillmoreTwp","07GangesTwp","08GunPlainTwp","09HeathTwp","10HopkinsTwp","11LaketownTwp","12LeeTwp","13LeightonTwp","14ManliusTwp","15MartinTwp","16MontereyTwp","17OtsegoTwp","18OveriselTwp","19SalemTwp","20SaugatuckTwp","21TrowbridgeTwp","22ValleyTwp","23WatsonTwp","24WaylandTwp","42MartinVillage","44HopkinsVillage","51AlleganCity","52FennvilleCity","53HollandCity","54OtsegoCity","55PlainwellCity","56WaylandCity","57SaugatuckCity","58SouthHavenCity","59DouglasCity"]


    #unitCode = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","42","44","51","52","53","54","55","56","57","58","59"]

for val in unitCodeNameNoSpace:
        code = val[:2]
        name = val[2:]
        print "starting ", code," ", name
        arcpy.FeatureClassToFeatureClass_conversion(in_features="C:/apps/python/ESRI/Translate/source/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017",
                                                    out_path="C:/apps/python/ESRI/Translate/build/"+name+"/FTP/",
                                                    out_name= "splits.shp",
                                                    where_clause="Changed = 'Y' and Mapping_ID Like '"+code+"%'",
                                                    field_mapping="""MAPPING_ID "MAPPING_ID" true true false 20 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,MAPPING_ID,-1,-1;""", config_keyword="")

        arcpy.FeatureClassToFeatureClass_conversion(in_features="C:/apps/python/ESRI/Translate/source/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017",
                                                    out_path="C:/apps/python/ESRI/Translate/build/"+name+"/local/",
                                                    out_name= "splits.shp",
                                                    where_clause="Changed = 'Y' and Mapping_ID Like '"+code+"%'",
                                                    field_mapping="""MAPPING_ID "MAPPING_ID" true true false 20 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,MAPPING_ID,-1,-1;DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,DEED_ACRES,-1,-1;ACRES "ACRES" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,ACRES,-1,-1;COMMENT "COMMENT" true true false 50 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,COMMENT,-1,-1;ERROR "ERROR" true true false 30 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,ERROR,-1,-1;LABEL "LABEL" true true false 15 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,LABEL,-1,-1;CENTERX "CENTERX" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,CENTERX,-1,-1;CENTERY "CENTERY" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,CENTERY,-1,-1;ANGLE "ANGLE" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,ANGLE,-1,-1;OFFSETX "OFFSETX" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,OFFSETX,-1,-1;OFFSETY "OFFSETY" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,OFFSETY,-1,-1;Status "Status" true true false 2 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,Status,-1,-1;Changed "Changed" true true false 1 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,Changed,-1,-1;ExtraText1 "Extra1" true true false 50 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,ExtraText1,-1,-1;ExtraText2 "ExtraText2" true true false 50 Text 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,ExtraText2,-1,-1;ExtraDbl1 "Extra" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,ExtraDbl1,-1,-1;ExtraDbl2 "ExtraDbl2" true true false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,ExtraDbl2,-1,-1;Shape_STAr "Shape_STAr" true false false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,Shape_STArea__,-1,-1;Shape_STLe "Shape_STLe" true false false 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,Shape_STLength__,-1,-1;Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017,Shape_Area,-1,-1""", config_keyword="")

def main():
    pass

if __name__ == '__main__':
    main()