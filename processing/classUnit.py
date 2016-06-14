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
        self.fmcd = fmcd
        self.name = name
        self.nospacename = nospacename
        self.code = code
        self.twprng = twprng
        self.propername = propername
        self.shortname = shortname
        self.unittype = unittype
    def displayUnit(self):
        print "fmcd: ", self.fmcd, ", Name: ", self.name, ", Unit Code: ", self.code

unit01 = Unit("01280", "Allegan Twp","AlleganTwp", "01","T3NR13W","Allegan Township","Allegan","Township")
unit02 = Unit("xxxxx", "Casco Twp","CascoTwp", "02","xxxxxx","Casco Township","Casco","Township")

def main():
    pass
    unit01.displayUnit()
    unit02.displayUnit()
if __name__ == '__main__':
    main()
