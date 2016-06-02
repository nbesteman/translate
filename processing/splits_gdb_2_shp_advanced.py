#-------------------------------------------------------------------------------
# Name:        splits_gdb_2_shp.py
# Warning:     This module is not finished
# Purpose:     Translate splits from geodatabase to shapefile format.
#
# Author:      NBesteman
#
# Created:     25/05/2016
#-------------------------------------------------------------------------------
import arcpy
arcpy.FeatureClassToFeatureClass_conversion(in_features="C:/data/00 Allegan Co/LGIM/AC_Cadastral.gdb/ParcelEditing/AC_Splits2017",out_path="C:/apps/python/ESRI/Translate/source", out_name="splits.shp", where_clause=""""MAPPING_ID" like '01%'""", config_keyword="")
