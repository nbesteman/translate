<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1463486853054" ID="ID_1589862820" MODIFIED="1464180285240" TEXT="Data Translation">
<node CREATED="1464026761074" ID="ID_664138617" MODIFIED="1464180301264" POSITION="left" TEXT="Update Local Unit Parcels mbx">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      This MapInfo mbx pushes data to
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1464026839213" ID="ID_1929640481" MODIFIED="1464177545050" POSITION="left" TEXT="Backup EQ Parcels">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Makes a backup of J:\data\01 Allegan Twp\Allegan Twp Parcels\Allegan Twp Parcels.tab (and similar) into d:\backup\jdrive\parcels_eq
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1464180288990" ID="ID_913310854" MODIFIED="1464180296339" POSITION="right" TEXT="Parcels Translation">
<node CREATED="1464024716818" ID="ID_137132450" MODIFIED="1464180260691" TEXT="push to locals in tabs format and meter projection">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      push it to the locals parcels folder that EQ used for mapping such as J:\data\01 Allegan Twp\Allegan Twp Parcels
    </p>
  </body>
</html></richcontent>
<node CREATED="1468009902484" ID="ID_1980707204" MODIFIED="1468009935392" TEXT="skip all this crap and just pull a AC_Parcels_Comb and go from there">
<node CREATED="1464025530278" ID="ID_1006979080" MODIFIED="1468008582002" TEXT="manually copy of AC_Cadastral.gdb from J:\data\00 Allegan Co\LGIM place in source folder">
<icon BUILTIN="messagebox_warning"/>
</node>
<node CREATED="1463486870773" ID="ID_926453781" MODIFIED="1468009046229" TEXT="open AC_Cadastral.gdb with ArcCatalog"/>
<node CREATED="1463486893237" ID="ID_353249958" MODIFIED="1468009351806" TEXT="&gt; ParcelPublishing\AC_Parcels2016 export to shapefile (single) and place in source">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Can use the 2016 because this is just the line
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1468009352475" ID="ID_1228181792" MODIFIED="1468009366642" TEXT="manually transfer to computer with mapinfo"/>
<node CREATED="1468009367320" ID="ID_1564273655" MODIFIED="1468009401475" TEXT="manually translate with mapinfo to .shp (will need to keeip int IntFt projection)"/>
<node CREATED="1468009402558" ID="ID_1836054740" MODIFIED="1468009536196" TEXT="manually save to meters projection using mapinfo"/>
</node>
<node CREATED="1468009944131" ID="ID_1466753521" MODIFIED="1468010360158" TEXT="use mapinfo">
<node CREATED="1468010362814" ID="ID_1335148462" MODIFIED="1468254181918" TEXT="save AC_Parcels_Comb to intlft projection in J:\apps\python\esri\translate\source\IntFt"/>
<node CREATED="1468010435965" ID="ID_197999803" MODIFIED="1468010550340" TEXT="drop all attributes except ">
<node CREATED="1468010565530" ID="ID_561019252" MODIFIED="1468010571684" TEXT="PARCELID"/>
<node CREATED="1468010552637" ID="ID_1290975985" MODIFIED="1468010564360" TEXT="PROPADDRESS"/>
<node CREATED="1468010572259" ID="ID_1148638795" MODIFIED="1468010578465" TEXT="SCHOOLDIST"/>
<node CREATED="1468010579018" ID="ID_211689330" MODIFIED="1468010584126" TEXT="PROPCLASS"/>
</node>
<node CREATED="1468011146927" ID="ID_1359606714" MODIFIED="1468254386694" TEXT="convert to shapefile"/>
<node CREATED="1468011250684" ID="ID_606012362" MODIFIED="1468345323977" TEXT="use parcelsTab2web.py"/>
<node CREATED="1468345327676" ID="ID_497755712" MODIFIED="1468345338578" TEXT="use zipparcels.py"/>
</node>
</node>
<node CREATED="1464024700229" ID="ID_261628582" MODIFIED="1464024806690" TEXT="place in j:\apps\mapbasic\lis\layerupdates\source"/>
</node>
<node CREATED="1464180306428" ID="ID_1702773572" MODIFIED="1464180313559" POSITION="right" TEXT="Splits Translation">
<node CREATED="1464180907990" ID="ID_1463337137" MODIFIED="1464181874931" TEXT="copy J:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb to C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb"/>
<node CREATED="1464187082919" ID="ID_1784944997" MODIFIED="1464187783710" TEXT="export from AC_Cadastral.gdb\ParcelEditing\AC_Splits2017 to C:\apps\python\ESRI\Reprojection\source\Splits.shp"/>
</node>
</node>
</map>
