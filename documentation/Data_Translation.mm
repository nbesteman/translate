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
</html>
</richcontent>
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
</html>
</richcontent>
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
<node CREATED="1464025530278" ID="ID_1006979080" MODIFIED="1464026082096" TEXT="get copy of AC_Cadastral.gdb from J:\data\00 Allegan Co\LGIM place in source folder"/>
<node CREATED="1463486870773" ID="ID_926453781" MODIFIED="1464026111254" TEXT="open AC_Cadastral.gdb with ArcCatalog"/>
<node CREATED="1463486893237" ID="ID_353249958" MODIFIED="1464026173858" TEXT="&gt; ParcelPublishing\AC_Parcels2016 export to shapefile (single)"/>
</node>
<node CREATED="1464024700229" ID="ID_261628582" MODIFIED="1464024806690" TEXT="place in j:\apps\mapbasic\lis\layerupdates\source"/>
</node>
<node CREATED="1464180306428" ID="ID_1702773572" MODIFIED="1464180313559" POSITION="right" TEXT="Splits Translation">
<node CREATED="1464180907990" ID="ID_1463337137" MODIFIED="1464181874931" TEXT="copy J:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb to C:\data\00 Allegan Co\LGIM\AC_Cadastral.gdb"/>
<node CREATED="1464187082919" ID="ID_1784944997" MODIFIED="1464187783710" TEXT="export from AC_Cadastral.gdb\ParcelEditing\AC_Splits2017 to C:\apps\python\ESRI\Reprojection\source\Splits.shp"/>
</node>
</node>
</map>
