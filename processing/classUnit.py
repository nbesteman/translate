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
    def __init__(self, code, fmcd, name, nospacename, twprng,propername,shortname,xMin,yMin,xMax,yMax,unittype):
        self.code = code
        self.fmcd = fmcd
        self.name = name
        self.nospacename = nospacename
        self.twprng = twprng
        self.propername = propername
        self.shortname = shortname
        self.xMin = xMin
        self.yMin = yMin
        self.xMax = xMax
        self.yMax = yMax
        self.unittype = unittype
    def displayUnit(self):
        print "fmcd: ", self.fmcd, ", Name: ", self.name, ", Unit Code: ", self.code
    def passUnit(self):
        x = self.fmcd
        return x
    def extentVals(self):
        print "xMin = ",self.xMin
        print "yMin = ",self.yMin
        print "xMax = ",self.xMax
        print "yMax = ",self.yMax
    def passExtentVals(self):
        x1 = self.xMin
        y1 = self.yMin
        x2 = self.xMax
        y2 = self.yMax
        return [x1,y1,x2,y2]
unit01 = Unit("01","1280","Allegan Twp","AlleganTwp","T2NR13W","Allegan Township","Allegan","12710706.2154994","370432.64368309","12742488.4701762","402418.622361924","Township")
unit02 = Unit("02","13700","Casco Twp","CascoTwp","T1NR16W","Casco Township","Casco","12605000.8997312","339936.769635595","12648052.823418","372250.564259845","Township")
unit03 = Unit("03","15200","Cheshire Twp","CheshireTwp","T1NR14W","Cheshire Township","Cheshire","12679125.363963","338939.464215509","12710923.5431487","371192.461061092","Township")
unit04 = Unit("04","16720","Clyde Twp","ClydeTwp","T2NR15W","Clyde Township","Clyde","12647831.5148055","371192.46106109","12679514.8933677","403709.315974756","Township")
unit05 = Unit("05","22680","Dorr Twp","DorrTwp","T4NR12W","Dorr Township","Dorr","12743225.0631912","433126.847034595","12775281.509905","465361.674297095","Township")
unit06 = Unit("06","28120","Fillmore Twp","FillmoreTwp","T4NR15W","Fillmore Township","Fillmore","12647923.7534661","435107.680343262","12680266.0844506","466985.518818429","Township")
unit07 = Unit("07","31360","Ganges Twp","GangesTwp","T2NR16W","Ganges Township","Ganges","12616849.5561002","371764.480258256","12648057.1367295","403903.085928422","Township")
unit08 = Unit("08","35720","Gun Plain Twp","GunPlainTwp","T1NR11W","Gun Plain Township","Gun Plain","12773828.1069719","338023.954563595","12806178.731575","370071.647685928","Township")
unit09 = Unit("09","37460","Heath Twp","HeathTwp","T3NR14W","Heath Township","Heath","12679199.6850086","402394.401281759","12711647.5262808","435107.680343259","Township")
unit10 = Unit("10","39200","Hopkins Twp","HopkinsTwp","T3NR12W","Hopkins Township","Hopkins","12742458.276339","401481.293199844","12774981.7693627","433790.442820261","Township")
unit11 = Unit("11","45180","Laketown Twp","LaketownTwp","T4NR16W","Laketown Township","Laketown","12627167.7464218","435594.096365176","12648043.8647745","467356.111253092","Township")
unit12 = Unit("12","46600","Lee Twp","LeeTwp","T1NR15W","Lee Township","Lee","12647553.8001378","339230.040077924","12679514.894352","371764.480586341","Township")
unit13 = Unit("13","46760","Leighton Twp","LeightonTwp","T4NR11W","Leighton Township","Leighton","12774981.7677223","432761.869746178","12806832.7043484","464814.539236511","Township")
unit14 = Unit("14","50840","Manlius Twp","ManliusTwp","T3NR15W","Manlius Township","Manlius","12647845.7831496","403118.05239351","12680248.1668355","435594.096037094","Township")
unit15 = Unit("15","52000","Martin Twp","MartinTwp","T2NR11W","Martin Township","Martin","12774166.5403501","369840.052676677","12806586.1785947","401481.293199844","Township")
unit16 = Unit("16","55200","Monterey Twp","MontereyTwp","T3NR13W","Monterey Township","Monterey","12710706.2154994","402244.760176844","12743236.6740604","434002.130060928","Township")
unit17 = Unit("17","61640","Otsego Twp","OtsegoTwp","T1NR12W","Otsego Township","Otsego","12742278.7740733","338272.471455007","12774166.5403501","370496.016915924","Township")
unit18 = Unit("18","61820","Overisel Twp","OveriselTwp","T4NR14W","Overisel Township","Overisel","12679963.4836779","434002.130060926","12711647.5275931","466777.787278509","Township")
unit19 = Unit("19","71100","Salem Twp","SalemTwp","T4NR13W","Salem Township","Salem","12711293.8298097","433790.111128009","12743266.8682257","465731.628609676","Township")
unit20 = Unit("20","71720","Saugatuck Twp","SaugatuckTwp","T3NR16W","Saugatuck Township","Saugatucl","12622191.4509282","403709.315974757","12647923.7534661","435923.561257423","Township")
unit21 = Unit("21","80620","Trowbridge Twp","TrowbridgeTwp","T1NR13W","Trowbridge Township","Trowbridge","12710747.690154","338702.48174984","12742484.4885569","370527.206158006","Township")
unit22 = Unit("22","81580","Valley Twp","ValleyTwp","T2NR14W","Valley Township","Valley","12679199.6853367","370462.173807762","12710923.5434768","403118.052065429","Township")
unit23 = Unit("23","84580","Watson Twp","WatsonTwp","T2NR12W","Watson Township","Watson","12742420.4516115","370023.868910096","12774260.4381282","402244.760176846","Township")
unit24 = Unit("24","84900","Wayland Twp","WaylandTwp","T3NR11W","Wayland Township","Wayland","12774287.6464071","401173.053002677","12806532.4270618","433126.847034594","Township")
unit42 = Unit("42","39200","Hopkins Village","Hopkins Village","","Hopkins Village","Hopkins","12777105.273974","378627.387792259","12783742.2265793","382604.648538509","Village")
unit44 = Unit("44","52000","Martin Village","Martin Village","","Martin Village","Martin","12745300.4445391","411382.80554901","12749483.553955","414784.241987594","Village")
unit51 = Unit("51","1260","Allegan City","AlleganCity","","Allegan City","Allegan","12718715.0692323","372686.991208508","12733456.9974255","386329.184068425","City")
unit52 = Unit("52","27740","Fennville City","FennvilleCity","","Fennville City","Fennville","12651313.250296","400578.803206928","12658419.7183665","406563.971682761","City")
unit53 = Unit("53","38640","Holland City","HollandCity","","Holland City","Holland","12646622.7747689","452625.625294178","12669452.7323897","467218.295911928","City")
unit54 = Unit("54","61620","Otsego City","OtsegoCity","","Otsego City","Otsego","12758085.6246774","346355.399514846","12768662.3453218","357359.475931846","City")
unit55 = Unit("55","64740","Plainwell City","PlainwellCity","","Plainwell City","Plainwell","12773943.5722921","343530.804114177","12784537.5461829","351881.493121427","City")
unit56 = Unit("56","71700","Saugatuck City","SaugatuckCity","","Saugatuck City","Saugatuck","12775008.7597943","425130.850231342","12786675.983507","435652.824594175","City")
unit57 = Unit("57","74980","South Haven City","South HavenCity","","South Haven City","South Haven","12623891.7834855","422882.674609594","12632744.0102036","434161.478167427","City")
unit58 = Unit("58","84880","Wayland City","WaylandCity","","Wayland City","Wayland","12611712.329498","340775.554375343","12612722.3222287","342094.782708009","City")
unit59 = Unit("59","22740","Douglas City","DouglasCity","","Douglas City","Douglas","12622459.7797879","416608.619572423","12633100.2850816","424778.653429173","City")

#tuple test
#unit01t = ("01","01280","Allegan Twp","AlleganTwp","T2NR13W","Allegan Township","Allegan","Township")
#unit02t = ("02","13700","Casco Twp","CascoTwp","T1NR16W","Casco Township","Casco","Township")

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

unitxMin = [unit01.xMin,
            unit02.xMin,
            unit03.xMin,
            unit04.xMin,
            unit05.xMin,
            unit06.xMin,
            unit07.xMin,
            unit08.xMin,
            unit09.xMin,
            unit10.xMin,
            unit11.xMin,
            unit12.xMin,
            unit13.xMin,
            unit14.xMin,
            unit15.xMin,
            unit16.xMin,
            unit17.xMin,
            unit18.xMin,
            unit19.xMin,
            unit20.xMin,
            unit21.xMin,
            unit22.xMin,
            unit23.xMin,
            unit24.xMin,
            unit42.xMin,
            unit44.xMin,
            unit51.xMin,
            unit52.xMin,
            unit53.xMin,
            unit54.xMin,
            unit55.xMin,
            unit56.xMin,
            unit57.xMin,
            unit58.xMin,
            unit59.xMin]

unityMin =[unit01.yMin,
            unit02.yMin,
            unit03.yMin,
            unit04.yMin,
            unit05.yMin,
            unit06.yMin,
            unit07.yMin,
            unit08.yMin,
            unit09.yMin,
            unit10.yMin,
            unit11.yMin,
            unit12.yMin,
            unit13.yMin,
            unit14.yMin,
            unit15.yMin,
            unit16.yMin,
            unit17.yMin,
            unit18.yMin,
            unit19.yMin,
            unit20.yMin,
            unit21.yMin,
            unit22.yMin,
            unit23.yMin,
            unit24.yMin,
            unit42.yMin,
            unit44.yMin,
            unit51.yMin,
            unit52.yMin,
            unit53.yMin,
            unit54.yMin,
            unit55.yMin,
            unit56.yMin,
            unit57.yMin,
            unit58.yMin,
            unit59.yMin]

unitxMax =[unit01.xMax,
            unit02.xMax,
            unit03.xMax,
            unit04.xMax,
            unit05.xMax,
            unit06.xMax,
            unit07.xMax,
            unit08.xMax,
            unit09.xMax,
            unit10.xMax,
            unit11.xMax,
            unit12.xMax,
            unit13.xMax,
            unit14.xMax,
            unit15.xMax,
            unit16.xMax,
            unit17.xMax,
            unit18.xMax,
            unit19.xMax,
            unit20.xMax,
            unit21.xMax,
            unit22.xMax,
            unit23.xMax,
            unit24.xMax,
            unit42.xMax,
            unit44.xMax,
            unit51.xMax,
            unit52.xMax,
            unit53.xMax,
            unit54.xMax,
            unit55.xMax,
            unit56.xMax,
            unit57.xMax,
            unit58.xMax,
            unit59.xMax]

unityMax =[unit01.yMax,
            unit02.yMax,
            unit03.yMax,
            unit04.yMax,
            unit05.yMax,
            unit06.yMax,
            unit07.yMax,
            unit08.yMax,
            unit09.yMax,
            unit10.yMax,
            unit11.yMax,
            unit12.yMax,
            unit13.yMax,
            unit14.yMax,
            unit15.yMax,
            unit16.yMax,
            unit17.yMax,
            unit18.yMax,
            unit19.yMax,
            unit20.yMax,
            unit21.yMax,
            unit22.yMax,
            unit23.yMax,
            unit24.yMax,
            unit42.yMax,
            unit44.yMax,
            unit51.yMax,
            unit52.yMax,
            unit53.yMax,
            unit54.yMax,
            unit55.yMax,
            unit56.yMax,
            unit57.yMax,
            unit58.yMax,
            unit59.yMax]

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

unitFile = [unit01.code+unit01.nospacename,
            unit02.code+unit02.nospacename]

def main():
    pass
    #unit01.displayUnit()
    #for value in unitName:
     #   print value
    #for value in unitxMax:
        #print value
    unit01.extentVals()

if __name__ == '__main__':
    main()

#Test 230pm