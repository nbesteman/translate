#http://www.tutorialspoint.com/python/python_classes_objects.htm
#-------------------------------------------------------------------------------
# Name:        classUnit
# Purpose:     creates a class of County Units for use in data process automation
# Author:      Neil Besteman
# Created:     20160613
# Modified     20160616
#-------------------------------------------------------------------------------
class Unit:
    unitcount = 0
    def __init__(self, code, fmcd, name, nospacename, twprng,propername,shortname,unittype):
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
    def passUnit(x):
        x = self.fmcd

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

unitCode = [unit01.code,
            unit02.code,
            unit03.code,
            unit04.code,
            unit05.code,
            unit06.code,
            unit07.code,
            unit08.code,
            unit09.code,
            unit10.code,
            unit11.code,
            unit12.code,
            unit13.code,
            unit14.code,
            unit15.code,
            unit16.code,
            unit17.code,
            unit18.code,
            unit19.code,
            unit20.code,
            unit21.code,
            unit22.code,
            unit23.code,
            unit24.code,
            unit42.code,
            unit44.code,
            unit51.code,
            unit52.code,
            unit53.code,
            unit54.code,
            unit55.code,
            unit56.code,
            unit57.code,
            unit58.code,
            unit59.code]

unitFmcd = [unit01.fmcd,
            unit02.fmcd,
            unit03.fmcd,
            unit04.fmcd,
            unit05.fmcd,
            unit06.fmcd,
            unit07.fmcd,
            unit08.fmcd,
            unit09.fmcd,
            unit10.fmcd,
            unit11.fmcd,
            unit12.fmcd,
            unit13.fmcd,
            unit14.fmcd,
            unit15.fmcd,
            unit16.fmcd,
            unit17.fmcd,
            unit18.fmcd,
            unit19.fmcd,
            unit20.fmcd,
            unit21.fmcd,
            unit22.fmcd,
            unit23.fmcd,
            unit24.fmcd,
            unit42.fmcd,
            unit44.fmcd,
            unit51.fmcd,
            unit52.fmcd,
            unit53.fmcd,
            unit54.fmcd,
            unit55.fmcd,
            unit56.fmcd,
            unit57.fmcd,
            unit58.fmcd,
            unit59.fmcd]

unitName = [unit01.name,
            unit02.name,
            unit03.name,
            unit04.name,
            unit05.name,
            unit06.name,
            unit07.name,
            unit08.name,
            unit09.name,
            unit10.name,
            unit11.name,
            unit12.name,
            unit13.name,
            unit14.name,
            unit15.name,
            unit16.name,
            unit17.name,
            unit18.name,
            unit19.name,
            unit20.name,
            unit21.name,
            unit22.name,
            unit23.name,
            unit24.name,
            unit42.name,
            unit44.name,
            unit51.name,
            unit52.name,
            unit53.name,
            unit54.name,
            unit55.name,
            unit56.name,
            unit57.name,
            unit58.name,
            unit59.name]

unitNospacename = [unit01.nospacename,
            unit02.nospacename,
            unit03.nospacename,
            unit04.nospacename,
            unit05.nospacename,
            unit06.nospacename,
            unit07.nospacename,
            unit08.nospacename,
            unit09.nospacename,
            unit10.nospacename,
            unit11.nospacename,
            unit12.nospacename,
            unit13.nospacename,
            unit14.nospacename,
            unit15.nospacename,
            unit16.nospacename,
            unit17.nospacename,
            unit18.nospacename,
            unit19.nospacename,
            unit20.nospacename,
            unit21.nospacename,
            unit22.nospacename,
            unit23.nospacename,
            unit24.nospacename,
            unit42.nospacename,
            unit44.nospacename,
            unit51.nospacename,
            unit52.nospacename,
            unit53.nospacename,
            unit54.nospacename,
            unit55.nospacename,
            unit56.nospacename,
            unit57.nospacename,
            unit58.nospacename,
            unit59.nospacename]

unitTwprng = [unit01.twprng,
            unit02.twprng,
            unit03.twprng,
            unit04.twprng,
            unit05.twprng,
            unit06.twprng,
            unit07.twprng,
            unit08.twprng,
            unit09.twprng,
            unit10.twprng,
            unit11.twprng,
            unit12.twprng,
            unit13.twprng,
            unit14.twprng,
            unit15.twprng,
            unit16.twprng,
            unit17.twprng,
            unit18.twprng,
            unit19.twprng,
            unit20.twprng,
            unit21.twprng,
            unit22.twprng,
            unit23.twprng,
            unit24.twprng,
            unit42.twprng,
            unit44.twprng,
            unit51.twprng,
            unit52.twprng,
            unit53.twprng,
            unit54.twprng,
            unit55.twprng,
            unit56.twprng,
            unit57.twprng,
            unit58.twprng,
            unit59.twprng]

unitPropername = [unit01.propername,
            unit02.propername,
            unit03.propername,
            unit04.propername,
            unit05.propername,
            unit06.propername,
            unit07.propername,
            unit08.propername,
            unit09.propername,
            unit10.propername,
            unit11.propername,
            unit12.propername,
            unit13.propername,
            unit14.propername,
            unit15.propername,
            unit16.propername,
            unit17.propername,
            unit18.propername,
            unit19.propername,
            unit20.propername,
            unit21.propername,
            unit22.propername,
            unit23.propername,
            unit24.propername,
            unit42.propername,
            unit44.propername,
            unit51.propername,
            unit52.propername,
            unit53.propername,
            unit54.propername,
            unit55.propername,
            unit56.propername,
            unit57.propername,
            unit58.propername,
            unit59.propername]

unitShortname = [unit01.shortname,
            unit02.shortname,
            unit03.shortname,
            unit04.shortname,
            unit05.shortname,
            unit06.shortname,
            unit07.shortname,
            unit08.shortname,
            unit09.shortname,
            unit10.shortname,
            unit11.shortname,
            unit12.shortname,
            unit13.shortname,
            unit14.shortname,
            unit15.shortname,
            unit16.shortname,
            unit17.shortname,
            unit18.shortname,
            unit19.shortname,
            unit20.shortname,
            unit21.shortname,
            unit22.shortname,
            unit23.shortname,
            unit24.shortname,
            unit42.shortname,
            unit44.shortname,
            unit51.shortname,
            unit52.shortname,
            unit53.shortname,
            unit54.shortname,
            unit55.shortname,
            unit56.shortname,
            unit57.shortname,
            unit58.shortname,
            unit59.shortname]

unitType = [unit01.unittype,
            unit02.unittype,
            unit03.unittype,
            unit04.unittype,
            unit05.unittype,
            unit06.unittype,
            unit07.unittype,
            unit08.unittype,
            unit09.unittype,
            unit10.unittype,
            unit11.unittype,
            unit12.unittype,
            unit13.unittype,
            unit14.unittype,
            unit15.unittype,
            unit16.unittype,
            unit17.unittype,
            unit18.unittype,
            unit19.unittype,
            unit20.unittype,
            unit21.unittype,
            unit22.unittype,
            unit23.unittype,
            unit24.unittype,
            unit42.unittype,
            unit44.unittype,
            unit51.unittype,
            unit52.unittype,
            unit53.unittype,
            unit54.unittype,
            unit55.unittype,
            unit56.unittype,
            unit57.unittype,
            unit58.unittype,
            unit59.unittype]

def main():
    pass
    unit01.displayUnit()
    for value in unitName:
        print value

if __name__ == '__main__':
    main()
