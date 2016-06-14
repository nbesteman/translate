#http://www.tutorialspoint.com/python/python_classes_objects.htm
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NBesteman
#
# Created:     13/06/2016
# Copyright:   (c) NBesteman 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
self = ""

class Unit:
    unitcount = 0
    def __init__(self, fmcd, name, nospacename, code, twprng,propername,shortname,unittype):
        self.code = code
        self.fmcd = fmcd
        self.name = name
        self.nospacename = nospacename
        self.twprng = twprng
        self.propername = propername
        self.shortname = shortname
        self.unittype = unittype
    def displayUnit(self):
        print "fmcd: ", self.fmcd, ", Name: ", self.name, ", Unit Code: ", self.code

unit01 = Unit("01","01280","Allegan Twp","AlleganTwp","T2NR13W","Allegan Township","Allegan","Township")
unit02 = Unit("02","13700","Casco Twp","CascoTwp","T1NR16W","Casco Township","Casco","Township")
unit03 = Unit("03","15200","Cheshire Twp","CheshireTwp","T1NR14W","Cheshire Township","Cheshire","Township")
unit04 = Unit("04","16720","Clyde Twp","ClydeTwp","T2NR15W","Clyde Township","Clyde","Township")
unit05 = Unit("05","22680","Dorr Twp","DorrTwp","T4NR12W","Dorr Township","Dorr","Township")
unit06 = Unit("06","28120","Fillmore Twp","FillmoreTwp","T4NR15W","Fillmore Township","Fillmore","Township")
unit07 = Unit("07","31360","Ganges Twp","GangesTwp","T2NR16W","Ganges Township","Ganges","Township")
unit08 = Unit("08","35720","Gun Plain Twp","GunPlainTwp","T1NR11W","Gun Plain Township","Gun Plain","Township")
unit09 = Unit("09","37460","Heath Twp","HeathTwp","T3NR14W","Heath Township","Heath","Township")
unit10 = Unit("10","39200","Hopkins Twp","HopkinsTwp","T3NR12W","Hopkins Township","Hopkins","Township")
unit11 = Unit("11","45180","Laketown Twp","LaketownTwp","T4NR16W","Laketown Township","Laketown","Township")
unit12 = Unit("12","46600","Lee Twp","LeeTwp","T1NR15W","Lee Township","Lee","Township")
unit13 = Unit("13","46760","Leighton Twp","LeightonTwp","T4NR11W","Leighton Township","Leighton","Township")
unit14 = Unit("14","50840","Manlius Twp","ManliusTwp","T3NR15W","Manlius Township","Manlius","Township")
unit15 = Unit("15","52000","Martin Twp","MartinTwp","T2NR11W","Martin Township","Martin","Township")
unit16 = Unit("16","55200","Monterey Twp","MontereyTwp","T3NR13W","Monterey Township","Monterey","Township")
unit17 = Unit("17","61640","Otsego Twp","OtsegoTwp","T1NR12W","Otsego Township","Otsego","Township")
unit18 = Unit("18","61820","Overisel Twp","OveriselTwp","T4NR14W","Overisel Township","Overisel","Township")
unit19 = Unit("19","71100","Salem Twp","SalemTwp","T4NR13W","Salem Township","Salem","Township")
unit20 = Unit("20","71720","Saugatuck Twp","SaugatuckTwp","T3NR16W","Saugatuck Township","Saugatucl","Township")
unit21 = Unit("21","80620","Trowbridge Twp","TrowbridgeTwp","T1NR13W","Trowbridge Township","Trowbridge","Township")
unit22 = Unit("22","81580","Valley Twp","ValleyTwp","T2NR14W","Valley Township","Valley","Township")
unit23 = Unit("23","84580","Watson Twp","WatsonTwp","T2NR12W","Watson Township","Watson","Township")
unit24 = Unit("24","84900","Wayland Twp","WaylandTwp","T3NR11W","Wayland Township","Wayland","Township")
unit42 = Unit("42","39200","Hopkins Village","Hopkins Village","","Hopkins Village","Hopkins","Village")
unit44 = Unit("44","52000","Martin Village","Martin Village","","Martin Village","Martin","Village")
unit51 = Unit("51","01260","Allegan City","AlleganCity","","Allegan City","Allegan","City")
unit52 = Unit("52","27740","Fennville City","FennvilleCity","","Fennville City","Fennville","City")
unit53 = Unit("53","38640","Holland City","HollandCity","","Holland City","Holland","City")
unit54 = Unit("54","61620","Otsego City","OtsegoCity","","Otsego City","Otsego","City")
unit55 = Unit("55","64740","Plainwell City","PlainwellCity","","Plainwell City","Plainwell","City")
unit56 = Unit("56","71700","Saugatuck City","SaugatuckCity","","Saugatuck City","Saugatuck","City")
unit57 = Unit("57","74980","South Haven City","South HavenCity","","South Haven City","South Haven","City")
unit58 = Unit("58","84880","Wayland City","WaylandCity","","Wayland City","Wayland","City")
unit59 = Unit("59","22740","Douglas City","DouglasCity","","Douglas City","Douglas","City")

def main():
    pass
    unit01.displayUnit()
    unit59.displayUnit()
if __name__ == '__main__':
    main()
