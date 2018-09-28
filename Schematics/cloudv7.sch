<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="8.2.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="50" name="dxf" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="53" name="tGND_GNDA" color="7" fill="9" visible="no" active="no"/>
<layer number="54" name="bGND_GNDA" color="1" fill="9" visible="no" active="no"/>
<layer number="56" name="wert" color="7" fill="1" visible="no" active="no"/>
<layer number="57" name="tCAD" color="7" fill="1" visible="no" active="no"/>
<layer number="59" name="tCarbon" color="7" fill="1" visible="no" active="no"/>
<layer number="60" name="bCarbon" color="7" fill="1" visible="no" active="no"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="yes" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
<layer number="99" name="SpiceOrder" color="7" fill="1" visible="no" active="no"/>
<layer number="100" name="Perimeter" color="7" fill="1" visible="no" active="no"/>
<layer number="101" name="Patch_Top" color="12" fill="4" visible="yes" active="yes"/>
<layer number="102" name="Vscore" color="7" fill="1" visible="yes" active="yes"/>
<layer number="103" name="tMap" color="7" fill="1" visible="yes" active="yes"/>
<layer number="104" name="Name" color="16" fill="1" visible="yes" active="yes"/>
<layer number="105" name="tPlate" color="7" fill="1" visible="yes" active="yes"/>
<layer number="106" name="bPlate" color="7" fill="1" visible="yes" active="yes"/>
<layer number="107" name="Crop" color="7" fill="1" visible="yes" active="yes"/>
<layer number="108" name="tplace-old" color="10" fill="1" visible="yes" active="yes"/>
<layer number="109" name="ref-old" color="11" fill="1" visible="yes" active="yes"/>
<layer number="110" name="fp0" color="7" fill="1" visible="yes" active="yes"/>
<layer number="111" name="LPC17xx" color="7" fill="1" visible="yes" active="yes"/>
<layer number="112" name="tSilk" color="7" fill="1" visible="yes" active="yes"/>
<layer number="113" name="IDFDebug" color="4" fill="1" visible="yes" active="yes"/>
<layer number="114" name="Badge_Outline" color="7" fill="1" visible="yes" active="yes"/>
<layer number="115" name="ReferenceISLANDS" color="7" fill="1" visible="yes" active="yes"/>
<layer number="116" name="Patch_BOT" color="9" fill="4" visible="yes" active="yes"/>
<layer number="117" name="Perimeter" color="2" fill="1" visible="yes" active="yes"/>
<layer number="118" name="Rect_Pads" color="7" fill="1" visible="yes" active="yes"/>
<layer number="121" name="_tsilk" color="7" fill="1" visible="yes" active="yes"/>
<layer number="122" name="_bsilk" color="7" fill="1" visible="yes" active="yes"/>
<layer number="123" name="tTestmark" color="7" fill="1" visible="yes" active="yes"/>
<layer number="124" name="bTestmark" color="7" fill="1" visible="yes" active="yes"/>
<layer number="125" name="_tNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="126" name="_bNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="127" name="_tValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="128" name="_bValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="129" name="Mask" color="7" fill="1" visible="yes" active="yes"/>
<layer number="131" name="tAdjust" color="7" fill="1" visible="yes" active="yes"/>
<layer number="132" name="bAdjust" color="7" fill="1" visible="yes" active="yes"/>
<layer number="144" name="Drill_legend" color="7" fill="1" visible="yes" active="yes"/>
<layer number="150" name="Notes" color="7" fill="1" visible="yes" active="yes"/>
<layer number="151" name="HeatSink" color="7" fill="1" visible="yes" active="yes"/>
<layer number="152" name="_bDocu" color="7" fill="1" visible="yes" active="yes"/>
<layer number="153" name="FabDoc1" color="7" fill="1" visible="yes" active="yes"/>
<layer number="154" name="FabDoc2" color="7" fill="1" visible="yes" active="yes"/>
<layer number="155" name="FabDoc3" color="7" fill="1" visible="yes" active="yes"/>
<layer number="199" name="Contour" color="7" fill="1" visible="yes" active="yes"/>
<layer number="200" name="200bmp" color="1" fill="10" visible="yes" active="yes"/>
<layer number="201" name="201bmp" color="2" fill="10" visible="yes" active="yes"/>
<layer number="202" name="202bmp" color="3" fill="10" visible="yes" active="yes"/>
<layer number="203" name="203bmp" color="4" fill="10" visible="yes" active="yes"/>
<layer number="204" name="204bmp" color="5" fill="10" visible="yes" active="yes"/>
<layer number="205" name="205bmp" color="6" fill="10" visible="yes" active="yes"/>
<layer number="206" name="206bmp" color="7" fill="10" visible="yes" active="yes"/>
<layer number="207" name="207bmp" color="8" fill="10" visible="yes" active="yes"/>
<layer number="208" name="208bmp" color="9" fill="10" visible="yes" active="yes"/>
<layer number="209" name="209bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="210" name="210bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="211" name="211bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="212" name="212bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="213" name="213bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="214" name="214bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="215" name="215bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="216" name="216bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="217" name="217bmp" color="18" fill="1" visible="no" active="no"/>
<layer number="218" name="218bmp" color="19" fill="1" visible="no" active="no"/>
<layer number="219" name="219bmp" color="20" fill="1" visible="no" active="no"/>
<layer number="220" name="220bmp" color="21" fill="1" visible="no" active="no"/>
<layer number="221" name="221bmp" color="22" fill="1" visible="no" active="no"/>
<layer number="222" name="222bmp" color="23" fill="1" visible="no" active="no"/>
<layer number="223" name="223bmp" color="24" fill="1" visible="no" active="no"/>
<layer number="224" name="224bmp" color="25" fill="1" visible="no" active="no"/>
<layer number="225" name="225bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="226" name="226bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="227" name="227bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="228" name="228bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="229" name="229bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="230" name="230bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="231" name="231bmp" color="7" fill="1" visible="yes" active="yes"/>
<layer number="232" name="Eagle3D_PG2" color="7" fill="1" visible="yes" active="yes"/>
<layer number="233" name="Eagle3D_PG3" color="7" fill="1" visible="yes" active="yes"/>
<layer number="248" name="Housing" color="7" fill="1" visible="yes" active="yes"/>
<layer number="249" name="Edge" color="7" fill="1" visible="yes" active="yes"/>
<layer number="250" name="Descript" color="3" fill="1" visible="no" active="no"/>
<layer number="251" name="SMDround" color="12" fill="11" visible="no" active="no"/>
<layer number="254" name="cooling" color="7" fill="1" visible="yes" active="yes"/>
<layer number="255" name="routoute" color="7" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="clouddemo">
<packages>
<package name="BM240">
<dimension x1="-6.35" y1="2.54" x2="6.35" y2="2.54" x3="0" y3="10.16" textsize="1.27" layer="21"/>
<dimension x1="-6.35" y1="10.16" x2="-6.35" y2="-10.16" x3="6.35" y3="0" textsize="1.27" layer="21"/>
<smd name="P$1" x="-5.08" y="7.62" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$2" x="-5.08" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$3" x="-5.08" y="2.54" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$4" x="-5.08" y="0" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$5" x="5.08" y="7.62" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$6" x="5.08" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$7" x="5.08" y="2.54" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$8" x="5.08" y="0" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$9" x="5.08" y="-2.54" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$10" x="5.08" y="-5.08" dx="1.27" dy="0.635" layer="1"/>
<wire x1="-6.35" y1="10.16" x2="-6.35" y2="-10.16" width="0.127" layer="21"/>
<wire x1="-6.35" y1="-10.16" x2="6.35" y2="-10.16" width="0.127" layer="21"/>
<wire x1="6.35" y1="-10.16" x2="6.35" y2="10.16" width="0.127" layer="21"/>
<wire x1="6.35" y1="10.16" x2="-6.35" y2="10.16" width="0.127" layer="21"/>
<wire x1="-6.35" y1="10.16" x2="-6.35" y2="-10.16" width="0.127" layer="100"/>
<wire x1="-6.35" y1="-10.16" x2="6.35" y2="-10.16" width="0.127" layer="100"/>
<wire x1="6.35" y1="-10.16" x2="6.35" y2="10.16" width="0.127" layer="100"/>
<wire x1="6.35" y1="10.16" x2="-6.35" y2="10.16" width="0.127" layer="100"/>
</package>
<package name="USB">
<dimension x1="-5.08" y1="2.54" x2="15.24" y2="2.54" x3="5.08" y3="6.35" textsize="1.27" layer="21"/>
<dimension x1="-5.08" y1="6.35" x2="-5.08" y2="-5.08" x3="-8.89" y3="0.635" textsize="1.27" layer="21"/>
<wire x1="-5.08" y1="6.35" x2="-5.08" y2="-5.08" width="0.127" layer="1"/>
<wire x1="-5.08" y1="-5.08" x2="15.24" y2="-5.08" width="0.127" layer="1"/>
<wire x1="15.24" y1="-5.08" x2="15.24" y2="6.35" width="0.127" layer="1"/>
<wire x1="15.24" y1="6.35" x2="-5.08" y2="6.35" width="0.127" layer="1"/>
<smd name="P$1" x="0" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$2" x="2.54" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$3" x="5.08" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$4" x="7.62" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$5" x="10.16" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<wire x1="-5.08" y1="6.35" x2="-5.08" y2="-5.08" width="0.127" layer="100"/>
<wire x1="-5.08" y1="-5.08" x2="15.24" y2="-5.08" width="0.127" layer="100"/>
<wire x1="15.24" y1="-5.08" x2="15.24" y2="6.35" width="0.127" layer="100"/>
<wire x1="15.24" y1="6.35" x2="-5.08" y2="6.35" width="0.127" layer="100"/>
</package>
<package name="CHARGE">
<dimension x1="-2.54" y1="3.81" x2="17.78" y2="3.81" x3="7.62" y3="6.35" textsize="1.27" layer="21"/>
<dimension x1="-2.54" y1="6.35" x2="-2.54" y2="-13.97" x3="-6.35" y3="-3.81" textsize="1.27" layer="21"/>
<wire x1="-2.54" y1="-13.97" x2="17.78" y2="-13.97" width="0.127" layer="1"/>
<wire x1="17.78" y1="-13.97" x2="17.78" y2="3.81" width="0.127" layer="1"/>
<smd name="P$1" x="2.54" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$2" x="5.08" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$3" x="7.62" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$4" x="10.16" y="5.08" dx="1.27" dy="0.635" layer="1"/>
<wire x1="-2.54" y1="-13.97" x2="-2.54" y2="6.35" width="0.127" layer="1"/>
<wire x1="-2.54" y1="6.35" x2="17.78" y2="6.35" width="0.127" layer="1"/>
<wire x1="17.78" y1="6.35" x2="17.78" y2="3.81" width="0.127" layer="1"/>
<wire x1="-2.54" y1="6.35" x2="-2.54" y2="-13.97" width="0.127" layer="100"/>
<wire x1="-2.54" y1="-13.97" x2="17.78" y2="-13.97" width="0.127" layer="100"/>
<wire x1="17.78" y1="-13.97" x2="17.78" y2="6.35" width="0.127" layer="100"/>
<wire x1="17.78" y1="6.35" x2="-2.54" y2="6.35" width="0.127" layer="100"/>
</package>
<package name="BATTERY">
<wire x1="0" y1="0" x2="30.48" y2="0" width="0.127" layer="21"/>
<wire x1="30.48" y1="0" x2="30.48" y2="-19.05" width="0.127" layer="21"/>
<wire x1="30.48" y1="-19.05" x2="0" y2="-19.05" width="0.127" layer="21"/>
<wire x1="0" y1="-19.05" x2="0" y2="0" width="0.127" layer="21"/>
<wire x1="0" y1="0" x2="0" y2="-19.05" width="0.127" layer="100"/>
<wire x1="0" y1="-19.05" x2="30.48" y2="-19.05" width="0.127" layer="100"/>
<wire x1="30.48" y1="-19.05" x2="30.48" y2="0" width="0.127" layer="100"/>
<wire x1="30.48" y1="0" x2="0" y2="0" width="0.127" layer="100"/>
<smd name="P$1" x="1.27" y="-6.35" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$2" x="1.27" y="-12.7" dx="1.27" dy="0.635" layer="1"/>
</package>
<package name="LED">
<circle x="0" y="0" radius="5.23634375" width="0.127" layer="21"/>
<circle x="0" y="0" radius="5.6796125" width="0.127" layer="100"/>
<smd name="P$1" x="-2.54" y="0" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$2" x="2.54" y="0" dx="1.27" dy="0.635" layer="1"/>
</package>
<package name="1KOHM">
<wire x1="0" y1="0" x2="0" y2="2.54" width="0.127" layer="1"/>
<wire x1="0" y1="2.54" x2="7.62" y2="2.54" width="0.127" layer="1"/>
<wire x1="7.62" y1="2.54" x2="7.62" y2="0" width="0.127" layer="1"/>
<wire x1="7.62" y1="0" x2="0" y2="0" width="0.127" layer="1"/>
<smd name="P$1" x="0" y="1.27" dx="1.27" dy="0.635" layer="1"/>
<smd name="P$2" x="7.62" y="1.27" dx="1.27" dy="0.635" layer="1"/>
<wire x1="0" y1="2.54" x2="7.62" y2="2.54" width="0.127" layer="100"/>
<wire x1="7.62" y1="2.54" x2="7.62" y2="0" width="0.127" layer="100"/>
<wire x1="7.62" y1="0" x2="0" y2="0" width="0.127" layer="100"/>
<wire x1="0" y1="0" x2="0" y2="2.54" width="0.127" layer="100"/>
</package>
<package name="RN41">
<dimension x1="-8.89" y1="5.08" x2="17.78" y2="5.08" x3="4.445" y3="8.89" textsize="1.27" layer="1"/>
<wire x1="-8.89" y1="5.08" x2="17.78" y2="5.08" width="0.127" layer="1"/>
<dimension x1="-8.89" y1="5.08" x2="-8.89" y2="-10.16" x3="-11.43" y3="-2.54" textsize="1.27" layer="1"/>
<wire x1="-8.89" y1="5.08" x2="-8.89" y2="-10.16" width="0.127" layer="1"/>
<wire x1="-8.89" y1="-10.16" x2="17.78" y2="-10.16" width="0.127" layer="1"/>
<wire x1="17.78" y1="-10.16" x2="17.78" y2="5.08" width="0.127" layer="1"/>
<smd name="P$1" x="15.24" y="5.08" dx="1.27" dy="0.635" layer="1" rot="R90"/>
<smd name="P$2" x="13.97" y="5.08" dx="1.27" dy="0.635" layer="1" rot="R90"/>
<smd name="P$3" x="13.97" y="-10.16" dx="1.27" dy="0.635" layer="1" rot="R90"/>
<smd name="P$4" x="15.24" y="-10.16" dx="1.27" dy="0.635" layer="1" rot="R90"/>
<wire x1="-10.16" y1="6.35" x2="-10.16" y2="-12.7" width="0.127" layer="100"/>
<wire x1="-10.16" y1="-12.7" x2="19.05" y2="-12.7" width="0.127" layer="100"/>
<wire x1="19.05" y1="-12.7" x2="19.05" y2="6.35" width="0.127" layer="100"/>
<wire x1="19.05" y1="6.35" x2="-10.16" y2="6.35" width="0.127" layer="100"/>
</package>
<package name="MSP430G553">
<wire x1="12.695" y1="2.921" x2="-12.705" y2="2.921" width="0.1524" layer="21"/>
<wire x1="-12.705" y1="-2.921" x2="12.695" y2="-2.921" width="0.1524" layer="21"/>
<wire x1="12.695" y1="2.921" x2="12.695" y2="-2.921" width="0.1524" layer="21"/>
<wire x1="-12.705" y1="2.921" x2="-12.705" y2="1.016" width="0.1524" layer="21"/>
<wire x1="-12.705" y1="-2.921" x2="-12.705" y2="-1.016" width="0.1524" layer="21"/>
<wire x1="-12.705" y1="1.016" x2="-12.705" y2="-1.016" width="0.1524" layer="21" curve="-180"/>
<circle x="-12.065" y="-1.905" radius="0.381" width="0.127" layer="21"/>
<pad name="1" x="-11.435" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="2" x="-8.895" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="7" x="3.805" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="14" x="3.805" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="3" x="-6.355" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="4" x="-3.815" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="6" x="1.265" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="5" x="-1.275" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="15" x="1.265" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="16" x="-1.275" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="17" x="-3.815" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="18" x="-6.355" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="19" x="-8.895" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="20" x="-11.435" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="10" x="11.425" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="9" x="8.885" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="8" x="6.345" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="11" x="11.425" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="12" x="8.885" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="13" x="6.345" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<text x="-13.086" y="-2.921" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="-10.038" y="-0.635" size="1.27" layer="27" ratio="10">&gt;VALUE</text>
<wire x1="-15.24" y1="6.35" x2="-15.24" y2="-7.62" width="0.127" layer="100"/>
<wire x1="-15.24" y1="-7.62" x2="16.51" y2="-7.62" width="0.127" layer="100"/>
<wire x1="16.51" y1="-7.62" x2="16.51" y2="6.35" width="0.127" layer="100"/>
<wire x1="16.51" y1="6.35" x2="-15.24" y2="6.35" width="0.127" layer="100"/>
</package>
</packages>
<symbols>
<symbol name="BM240">
<dimension x1="-7.62" y1="5.08" x2="5.08" y2="5.08" x3="-1.27" y3="12.7" textsize="1.778" layer="94"/>
<dimension x1="-7.62" y1="5.08" x2="-7.62" y2="-15.24" x3="-17.78" y3="-5.08" textsize="1.778" layer="94"/>
<wire x1="-7.62" y1="-15.24" x2="-7.62" y2="5.08" width="0.254" layer="94"/>
<wire x1="-7.62" y1="5.08" x2="5.08" y2="5.08" width="0.254" layer="94"/>
<wire x1="5.08" y1="5.08" x2="5.08" y2="-15.24" width="0.254" layer="94"/>
<wire x1="5.08" y1="-15.24" x2="-7.62" y2="-15.24" width="0.254" layer="94"/>
<pin name="GND" x="-12.7" y="2.54" length="middle"/>
<pin name="3.3V" x="-12.7" y="0" length="middle"/>
<pin name="SDA" x="-12.7" y="-2.54" length="middle"/>
<pin name="SCL" x="-12.7" y="-5.08" length="middle"/>
<pin name="GND1" x="10.16" y="2.54" length="middle" rot="R180"/>
<pin name="VCC" x="10.16" y="0" length="middle" rot="R180"/>
<pin name="SCK" x="10.16" y="-2.54" length="middle" rot="R180"/>
<pin name="SDD" x="10.16" y="-5.08" length="middle" rot="R180"/>
<pin name="SDI" x="10.16" y="-7.62" length="middle" rot="R180"/>
<pin name="CS" x="10.16" y="-10.16" length="middle" rot="R180"/>
<wire x1="-7.62" y1="5.08" x2="-7.62" y2="-15.24" width="0.254" layer="100"/>
<wire x1="-7.62" y1="-15.24" x2="5.08" y2="-15.24" width="0.254" layer="100"/>
<wire x1="5.08" y1="-15.24" x2="5.08" y2="5.08" width="0.254" layer="100"/>
<wire x1="5.08" y1="5.08" x2="-7.62" y2="5.08" width="0.254" layer="100"/>
</symbol>
<symbol name="USB">
<dimension x1="-7.62" y1="7.62" x2="12.7" y2="7.62" x3="2.54" y3="17.78" textsize="1.27" layer="94"/>
<dimension x1="-7.62" y1="7.62" x2="-7.62" y2="-5.08" x3="-15.24" y3="1.27" textsize="1.27" layer="94"/>
<wire x1="-7.62" y1="-5.08" x2="-7.62" y2="7.62" width="0.254" layer="94"/>
<wire x1="-7.62" y1="7.62" x2="12.7" y2="7.62" width="0.254" layer="94"/>
<wire x1="12.7" y1="7.62" x2="12.7" y2="-5.08" width="0.254" layer="94"/>
<wire x1="12.7" y1="-5.08" x2="-7.62" y2="-5.08" width="0.254" layer="94"/>
<pin name="VCC" x="-2.54" y="10.16" length="middle" rot="R270"/>
<pin name="D-" x="0" y="10.16" length="middle" rot="R270"/>
<pin name="D+" x="2.54" y="10.16" length="middle" rot="R270"/>
<pin name="ID" x="5.08" y="10.16" length="middle" rot="R270"/>
<pin name="GND" x="7.62" y="10.16" length="middle" rot="R270"/>
<wire x1="-7.62" y1="7.62" x2="-7.62" y2="-5.08" width="0.254" layer="100"/>
<wire x1="-7.62" y1="-5.08" x2="12.7" y2="-5.08" width="0.254" layer="100"/>
<wire x1="12.7" y1="-5.08" x2="12.7" y2="7.62" width="0.254" layer="100"/>
<wire x1="12.7" y1="7.62" x2="-7.62" y2="7.62" width="0.254" layer="100"/>
</symbol>
<symbol name="CHARGE">
<dimension x1="-10.16" y1="2.54" x2="10.16" y2="2.54" x3="0" y3="5.08" textsize="1.778" layer="94"/>
<wire x1="10.16" y1="5.08" x2="10.16" y2="-15.24" width="0.254" layer="94"/>
<wire x1="10.16" y1="-15.24" x2="-10.16" y2="-15.24" width="0.254" layer="94"/>
<pin name="VCC" x="-5.08" y="7.62" length="middle" rot="R270"/>
<pin name="GND" x="-2.54" y="7.62" length="middle" rot="R270"/>
<pin name="BGND" x="0" y="7.62" length="middle" rot="R270"/>
<pin name="VBAT" x="2.54" y="7.62" length="middle" rot="R270"/>
<wire x1="-10.16" y1="-15.24" x2="-10.16" y2="5.08" width="0.254" layer="94"/>
<wire x1="-10.16" y1="5.08" x2="10.16" y2="5.08" width="0.254" layer="94"/>
<wire x1="-10.16" y1="5.08" x2="-10.16" y2="-15.24" width="0.254" layer="100"/>
<wire x1="-10.16" y1="-15.24" x2="10.16" y2="-15.24" width="0.254" layer="100"/>
<wire x1="10.16" y1="-15.24" x2="10.16" y2="5.08" width="0.254" layer="100"/>
<wire x1="10.16" y1="5.08" x2="-10.16" y2="5.08" width="0.254" layer="100"/>
</symbol>
<symbol name="BATTERY">
<wire x1="0" y1="0" x2="30.48" y2="0" width="0.254" layer="94"/>
<wire x1="30.48" y1="0" x2="30.48" y2="20.32" width="0.254" layer="94"/>
<wire x1="30.48" y1="20.32" x2="0" y2="20.32" width="0.254" layer="94"/>
<wire x1="0" y1="20.32" x2="0" y2="0" width="0.254" layer="94"/>
<pin name="GND" x="-2.54" y="12.7" length="middle"/>
<pin name="VCC" x="-2.54" y="7.62" length="middle"/>
<wire x1="30.48" y1="20.32" x2="0" y2="20.32" width="0.254" layer="100"/>
<wire x1="0" y1="20.32" x2="0" y2="0" width="0.254" layer="100"/>
<wire x1="0" y1="0" x2="30.48" y2="0" width="0.254" layer="100"/>
<wire x1="30.48" y1="0" x2="30.48" y2="20.32" width="0.254" layer="100"/>
</symbol>
<symbol name="LED">
<wire x1="-5.08" y1="0" x2="5.08" y2="0" width="0.254" layer="94"/>
<wire x1="5.08" y1="0" x2="5.08" y2="12.7" width="0.254" layer="94"/>
<wire x1="5.08" y1="12.7" x2="-5.08" y2="12.7" width="0.254" layer="94"/>
<wire x1="-5.08" y1="12.7" x2="-5.08" y2="0" width="0.254" layer="94"/>
<pin name="P$1" x="0" y="15.24" length="middle" rot="R270"/>
<pin name="P$2" x="0" y="-2.54" length="middle" rot="R90"/>
<wire x1="-5.08" y1="12.7" x2="-5.08" y2="0" width="0.254" layer="100"/>
<wire x1="-5.08" y1="0" x2="5.08" y2="0" width="0.254" layer="100"/>
<wire x1="5.08" y1="0" x2="5.08" y2="12.7" width="0.254" layer="100"/>
<wire x1="5.08" y1="12.7" x2="-5.08" y2="12.7" width="0.254" layer="100"/>
</symbol>
<symbol name="1KOHM">
<wire x1="0" y1="0" x2="7.62" y2="0" width="0.254" layer="94"/>
<wire x1="7.62" y1="0" x2="7.62" y2="2.54" width="0.254" layer="94"/>
<wire x1="7.62" y1="2.54" x2="0" y2="2.54" width="0.254" layer="94"/>
<wire x1="0" y1="2.54" x2="0" y2="0" width="0.254" layer="94"/>
<pin name="P$1" x="-2.54" y="0" length="middle"/>
<pin name="P$2" x="12.7" y="2.54" length="middle" rot="R180"/>
<wire x1="0" y1="2.54" x2="0" y2="0" width="0.254" layer="100"/>
<wire x1="0" y1="0" x2="7.62" y2="0" width="0.254" layer="100"/>
<wire x1="7.62" y1="0" x2="7.62" y2="2.54" width="0.254" layer="100"/>
<wire x1="7.62" y1="2.54" x2="0" y2="2.54" width="0.254" layer="100"/>
</symbol>
<symbol name="RN41">
<wire x1="-22.86" y1="7.62" x2="-22.86" y2="-7.62" width="0.254" layer="94"/>
<wire x1="-22.86" y1="-7.62" x2="5.08" y2="-7.62" width="0.254" layer="94"/>
<wire x1="5.08" y1="-7.62" x2="5.08" y2="7.62" width="0.254" layer="94"/>
<wire x1="5.08" y1="7.62" x2="-22.86" y2="7.62" width="0.254" layer="94"/>
<pin name="TX" x="0" y="12.7" length="middle" rot="R270"/>
<pin name="RX" x="2.54" y="12.7" length="middle" rot="R270"/>
<pin name="VCC" x="0" y="-12.7" length="middle" rot="R90"/>
<pin name="GND" x="2.54" y="-12.7" length="middle" rot="R90"/>
<wire x1="-22.86" y1="7.62" x2="-22.86" y2="-7.62" width="0.254" layer="100"/>
<wire x1="-22.86" y1="-7.62" x2="5.08" y2="-7.62" width="0.254" layer="100"/>
<wire x1="5.08" y1="-7.62" x2="5.08" y2="7.62" width="0.254" layer="100"/>
<wire x1="5.08" y1="7.62" x2="-22.86" y2="7.62" width="0.254" layer="100"/>
</symbol>
<symbol name="MSP430G553">
<wire x1="-19.05" y1="12.7" x2="17.78" y2="12.7" width="0.254" layer="94"/>
<wire x1="17.78" y1="12.7" x2="17.78" y2="-17.78" width="0.254" layer="94"/>
<wire x1="17.78" y1="-17.78" x2="-19.05" y2="-17.78" width="0.254" layer="94"/>
<wire x1="-19.05" y1="-17.78" x2="-19.05" y2="12.7" width="0.254" layer="94"/>
<circle x="-15.24" y="10.16" radius="1.27" width="0.254" layer="94"/>
<text x="-17.78" y="12.7" size="1.778" layer="96">MSP430G2X[0/3]2</text>
<text x="-17.78" y="-20.32" size="1.778" layer="95">&gt;Name</text>
<text x="-17.78" y="7.62" size="0.7112" layer="95" font="vector">DVcc</text>
<text x="-17.78" y="5.08" size="0.7112" layer="95" font="vector">P1.0/TA0CLK/ACLK/A0</text>
<text x="-17.78" y="2.54" size="0.7112" layer="95" font="vector">P1.1/TA0.0/A1</text>
<text x="-17.78" y="0" size="0.7112" layer="95" font="vector">P1.2/TA0.1/A2</text>
<text x="-17.78" y="-2.54" size="0.6096" layer="95" font="vector">P1.3/ADC10CLK/A3/VREF-/VEREF-</text>
<text x="-17.78" y="-5.08" size="0.7112" layer="95" font="vector">P1.4/SMCLK/A4/VREF+/VEREF+/TCK</text>
<text x="-17.78" y="-7.62" size="0.7112" layer="95" font="vector">P1.5/TA0.0/A5/SCLK/TMS</text>
<text x="-1.27" y="-7.62" size="0.7112" layer="95" font="vector">P1.6/TA0.1/A6/SDO/SCL/TDI/TCLK</text>
<text x="3.81" y="-5.08" size="0.7112" layer="95" font="vector">P1.7/A7/SDI/SDA/TDO/TDI</text>
<text x="7.62" y="-2.54" size="0.7112" layer="95" font="vector">_RST/NMI/SBWTDIO</text>
<text x="10.16" y="0" size="0.7112" layer="95" font="vector">TEST/SBWTCK</text>
<text x="11.43" y="2.54" size="0.7112" layer="95" font="vector">XOUT/P2.7</text>
<text x="8.89" y="5.08" size="0.7112" layer="95" font="vector">XIN/P2.6/TA0.1</text>
<text x="13.97" y="7.62" size="0.7112" layer="95" font="vector">DVSS</text>
<text x="-17.78" y="-10.16" size="0.7112" layer="95" font="vector">P2.0</text>
<text x="-17.78" y="-12.7" size="0.7112" layer="95" font="vector">P2.1</text>
<text x="-17.78" y="-15.24" size="0.7112" layer="95" font="vector">P2.2</text>
<text x="12.7" y="-15.24" size="0.7112" layer="95" font="vector">P2.3</text>
<text x="12.7" y="-12.7" size="0.7112" layer="95" font="vector">P2.4</text>
<text x="12.7" y="-10.16" size="0.7112" layer="95" font="vector">P2.5</text>
<pin name="1" x="-24.13" y="7.62" visible="pad" length="middle"/>
<pin name="2" x="-24.13" y="5.08" visible="pad" length="middle"/>
<pin name="3" x="-24.13" y="2.54" visible="pad" length="middle"/>
<pin name="4" x="-24.13" y="0" visible="pad" length="middle"/>
<pin name="5" x="-24.13" y="-2.54" visible="pad" length="middle"/>
<pin name="6" x="-24.13" y="-5.08" visible="pad" length="middle"/>
<pin name="7" x="-24.13" y="-7.62" visible="pad" length="middle"/>
<pin name="14" x="22.86" y="-7.62" visible="pad" length="middle" rot="R180"/>
<pin name="15" x="22.86" y="-5.08" visible="pad" length="middle" rot="R180"/>
<pin name="16" x="22.86" y="-2.54" visible="pad" length="middle" rot="R180"/>
<pin name="17" x="22.86" y="0" visible="pad" length="middle" rot="R180"/>
<pin name="18" x="22.86" y="2.54" visible="pad" length="middle" rot="R180"/>
<pin name="19" x="22.86" y="5.08" visible="pad" length="middle" rot="R180"/>
<pin name="20" x="22.86" y="7.62" visible="pad" length="middle" rot="R180"/>
<pin name="8" x="-24.13" y="-10.16" visible="pad" length="middle"/>
<pin name="9" x="-24.13" y="-12.7" visible="pad" length="middle"/>
<pin name="10" x="-24.13" y="-15.24" visible="pad" length="middle"/>
<pin name="13" x="22.86" y="-10.16" visible="pad" length="middle" rot="R180"/>
<pin name="12" x="22.86" y="-12.7" visible="pad" length="middle" rot="R180"/>
<pin name="11" x="22.86" y="-15.24" visible="pad" length="middle" rot="R180"/>
<wire x1="-19.05" y1="12.7" x2="17.78" y2="12.7" width="0.254" layer="100"/>
<wire x1="17.78" y1="12.7" x2="17.78" y2="-17.78" width="0.254" layer="100"/>
<wire x1="17.78" y1="-17.78" x2="-19.05" y2="-17.78" width="0.254" layer="100"/>
<wire x1="-19.05" y1="-17.78" x2="-19.05" y2="12.7" width="0.254" layer="100"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="BM240">
<gates>
<gate name="G$1" symbol="BM240" x="-15.24" y="5.08"/>
</gates>
<devices>
<device name="BM240" package="BM240">
<connects>
<connect gate="G$1" pin="3.3V" pad="P$1"/>
<connect gate="G$1" pin="CS" pad="P$2"/>
<connect gate="G$1" pin="GND" pad="P$3"/>
<connect gate="G$1" pin="GND1" pad="P$4"/>
<connect gate="G$1" pin="SCK" pad="P$5"/>
<connect gate="G$1" pin="SCL" pad="P$6"/>
<connect gate="G$1" pin="SDA" pad="P$7"/>
<connect gate="G$1" pin="SDD" pad="P$8"/>
<connect gate="G$1" pin="SDI" pad="P$9"/>
<connect gate="G$1" pin="VCC" pad="P$10"/>
</connects>
<technologies>
<technology name="">
<attribute name="HEIGHT" value="15.0" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="USB">
<gates>
<gate name="G$1" symbol="USB" x="-5.08" y="-2.54"/>
</gates>
<devices>
<device name="USB" package="USB">
<connects>
<connect gate="G$1" pin="D+" pad="P$1"/>
<connect gate="G$1" pin="D-" pad="P$2"/>
<connect gate="G$1" pin="GND" pad="P$3"/>
<connect gate="G$1" pin="ID" pad="P$4"/>
<connect gate="G$1" pin="VCC" pad="P$5"/>
</connects>
<technologies>
<technology name="">
<attribute name="HEIGHT" value="15.00" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="CHARGE">
<gates>
<gate name="G$1" symbol="CHARGE" x="0" y="0"/>
</gates>
<devices>
<device name="CHARGE" package="CHARGE">
<connects>
<connect gate="G$1" pin="BGND" pad="P$1"/>
<connect gate="G$1" pin="GND" pad="P$2"/>
<connect gate="G$1" pin="VBAT" pad="P$3"/>
<connect gate="G$1" pin="VCC" pad="P$4"/>
</connects>
<technologies>
<technology name="">
<attribute name="HEIGHT" value="15.00" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="BATTERY">
<gates>
<gate name="G$1" symbol="BATTERY" x="-15.24" y="-10.16"/>
</gates>
<devices>
<device name="BATTERY" package="BATTERY">
<connects>
<connect gate="G$1" pin="GND" pad="P$1"/>
<connect gate="G$1" pin="VCC" pad="P$2"/>
</connects>
<technologies>
<technology name="">
<attribute name="HEIGHT" value="10" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="LED">
<gates>
<gate name="G$1" symbol="LED" x="0" y="-5.08"/>
</gates>
<devices>
<device name="LED" package="LED">
<connects>
<connect gate="G$1" pin="P$1" pad="P$1"/>
<connect gate="G$1" pin="P$2" pad="P$2"/>
</connects>
<technologies>
<technology name="">
<attribute name="HEIGHT" value="10.0" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="1KOHM">
<gates>
<gate name="G$1" symbol="1KOHM" x="-5.08" y="0"/>
</gates>
<devices>
<device name="1KOHM" package="1KOHM">
<connects>
<connect gate="G$1" pin="P$1" pad="P$1"/>
<connect gate="G$1" pin="P$2" pad="P$2"/>
</connects>
<technologies>
<technology name="">
<attribute name="HEIGTH" value="10"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="RN41">
<gates>
<gate name="G$1" symbol="RN41" x="-2.54" y="5.08"/>
</gates>
<devices>
<device name="RN41" package="RN41">
<connects>
<connect gate="G$1" pin="GND" pad="P$4"/>
<connect gate="G$1" pin="RX" pad="P$2"/>
<connect gate="G$1" pin="TX" pad="P$1"/>
<connect gate="G$1" pin="VCC" pad="P$3"/>
</connects>
<technologies>
<technology name="">
<attribute name="HEIGHT" value="0.7" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="MSP430G553">
<gates>
<gate name="G$1" symbol="MSP430G553" x="0" y="2.54"/>
</gates>
<devices>
<device name="" package="MSP430G553">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="10" pad="10"/>
<connect gate="G$1" pin="11" pad="11"/>
<connect gate="G$1" pin="12" pad="12"/>
<connect gate="G$1" pin="13" pad="13"/>
<connect gate="G$1" pin="14" pad="14"/>
<connect gate="G$1" pin="15" pad="15"/>
<connect gate="G$1" pin="16" pad="16"/>
<connect gate="G$1" pin="17" pad="17"/>
<connect gate="G$1" pin="18" pad="18"/>
<connect gate="G$1" pin="19" pad="19"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="20" pad="20"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
<connect gate="G$1" pin="7" pad="7"/>
<connect gate="G$1" pin="8" pad="8"/>
<connect gate="G$1" pin="9" pad="9"/>
</connects>
<technologies>
<technology name="MSP430G2553">
<attribute name="HEIGHT" value="20" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply1" urn="urn:adsk.eagle:library:371">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
 GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
 Please keep in mind, that these devices are necessary for the
 automatic wiring of the supply signals.&lt;p&gt;
 The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
 In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
 &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="GND" library_version="1">
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
<symbol name="VCC" library_version="1">
<wire x1="1.27" y1="-1.905" x2="0" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="-1.27" y2="-1.905" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="VCC" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GND" prefix="GND" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="VCC" prefix="P+" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="VCC" symbol="VCC" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="GND1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND3" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="P+1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="VCC" device=""/>
<part name="P+2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="VCC" device=""/>
<part name="P+4" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="VCC" device=""/>
<part name="GND5" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND6" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="P+5" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="VCC" device=""/>
<part name="U$6" library="clouddemo" deviceset="BM240" device="BM240"/>
<part name="U$1" library="clouddemo" deviceset="USB" device="USB"/>
<part name="U$2" library="clouddemo" deviceset="CHARGE" device="CHARGE"/>
<part name="U$4" library="clouddemo" deviceset="BATTERY" device="BATTERY"/>
<part name="U$8" library="clouddemo" deviceset="LED" device="LED"/>
<part name="U$5" library="clouddemo" deviceset="1KOHM" device="1KOHM"/>
<part name="U$7" library="clouddemo" deviceset="RN41" device="RN41"/>
<part name="GND4" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="P+3" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="VCC" device=""/>
<part name="U$3" library="clouddemo" deviceset="MSP430G553" device="" technology="MSP430G2553"/>
</parts>
<sheets>
<sheet>
<plain>
<text x="-414.02" y="101.6" size="1.778" layer="91">LED</text>
</plain>
<instances>
<instance part="GND1" gate="1" x="-353.06" y="134.62"/>
<instance part="GND2" gate="1" x="-327.66" y="149.86" rot="R270"/>
<instance part="GND3" gate="1" x="-347.98" y="124.46" rot="R90"/>
<instance part="P+1" gate="VCC" x="-297.18" y="177.8"/>
<instance part="P+2" gate="VCC" x="-403.86" y="124.46" rot="R90"/>
<instance part="P+4" gate="VCC" x="-340.36" y="86.36"/>
<instance part="GND5" gate="1" x="-337.82" y="88.9" rot="R180"/>
<instance part="GND6" gate="1" x="-411.48" y="83.82"/>
<instance part="P+5" gate="VCC" x="-317.5" y="129.54" rot="R180"/>
<instance part="U$6" gate="G$1" x="-340.36" y="55.88" rot="R270"/>
<instance part="U$1" gate="G$1" x="-381" y="154.94" rot="R270"/>
<instance part="U$2" gate="G$1" x="-297.18" y="144.78" rot="R90"/>
<instance part="U$4" gate="G$1" x="-307.34" y="175.26" rot="R90"/>
<instance part="U$8" gate="G$1" x="-411.48" y="93.98"/>
<instance part="U$5" gate="G$1" x="-330.2" y="134.62"/>
<instance part="U$7" gate="G$1" x="-441.96" y="119.38" rot="R270"/>
<instance part="GND4" gate="1" x="-454.66" y="114.3"/>
<instance part="P+3" gate="VCC" x="-459.74" y="119.38" rot="R90"/>
<instance part="U$3" gate="G$1" x="-375.92" y="116.84"/>
</instances>
<busses>
</busses>
<nets>
<net name="N$2" class="0">
<segment>
<wire x1="-353.06" y1="114.3" x2="-337.82" y2="114.3" width="0.1524" layer="91"/>
<wire x1="-370.84" y1="154.94" x2="-337.82" y2="144.78" width="0.1524" layer="91"/>
<wire x1="-337.82" y1="144.78" x2="-332.74" y2="134.62" width="0.1524" layer="91"/>
<wire x1="-337.82" y1="114.3" x2="-337.82" y2="144.78" width="0.1524" layer="91"/>
<junction x="-337.82" y="144.78"/>
<pinref part="U$1" gate="G$1" pin="D-"/>
<pinref part="U$5" gate="G$1" pin="P$1"/>
<pinref part="U$3" gate="G$1" pin="16"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<wire x1="-353.06" y1="111.76" x2="-342.9" y2="111.76" width="0.1524" layer="91"/>
<wire x1="-342.9" y1="111.76" x2="-342.9" y2="68.58" width="0.1524" layer="91"/>
<pinref part="U$6" gate="G$1" pin="SDA"/>
<pinref part="U$3" gate="G$1" pin="15"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<wire x1="-345.44" y1="68.58" x2="-345.44" y2="109.22" width="0.1524" layer="91"/>
<wire x1="-345.44" y1="109.22" x2="-353.06" y2="109.22" width="0.1524" layer="91"/>
<pinref part="U$6" gate="G$1" pin="SCL"/>
<pinref part="U$3" gate="G$1" pin="14"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<wire x1="-370.84" y1="157.48" x2="-304.8" y2="139.7" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="VCC"/>
<pinref part="U$2" gate="G$1" pin="VCC"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="GND1" gate="1" pin="GND"/>
<wire x1="-370.84" y1="147.32" x2="-353.06" y2="137.16" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="GND"/>
</segment>
<segment>
<pinref part="GND2" gate="1" pin="GND"/>
<wire x1="-304.8" y1="142.24" x2="-325.12" y2="149.86" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="GND"/>
</segment>
<segment>
<pinref part="GND5" gate="1" pin="GND"/>
<wire x1="-337.82" y1="68.58" x2="-337.82" y2="86.36" width="0.1524" layer="91"/>
<pinref part="U$6" gate="G$1" pin="GND"/>
</segment>
<segment>
<pinref part="GND3" gate="1" pin="GND"/>
<wire x1="-350.52" y1="124.46" x2="-353.06" y2="124.46" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="20"/>
</segment>
<segment>
<pinref part="GND6" gate="1" pin="GND"/>
<wire x1="-411.48" y1="93.98" x2="-411.48" y2="86.36" width="0.1524" layer="91"/>
<pinref part="U$8" gate="G$1" pin="P$2"/>
<junction x="-411.48" y="86.36"/>
<wire x1="-411.48" y1="86.36" x2="-411.48" y2="91.44" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$9" class="0">
<segment>
<wire x1="-320.04" y1="172.72" x2="-320.04" y2="152.4" width="0.1524" layer="91"/>
<wire x1="-320.04" y1="152.4" x2="-304.8" y2="144.78" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="BGND"/>
<pinref part="U$4" gate="G$1" pin="GND"/>
</segment>
</net>
<net name="VCC" class="0">
<segment>
<wire x1="-304.8" y1="147.32" x2="-304.8" y2="170.18" width="0.1524" layer="91"/>
<pinref part="P+1" gate="VCC" pin="VCC"/>
<wire x1="-304.8" y1="170.18" x2="-297.18" y2="175.26" width="0.1524" layer="91"/>
<junction x="-304.8" y="170.18"/>
<pinref part="U$2" gate="G$1" pin="VBAT"/>
<pinref part="U$4" gate="G$1" pin="VCC"/>
<wire x1="-314.96" y1="172.72" x2="-314.96" y2="170.18" width="0.1524" layer="91"/>
<wire x1="-314.96" y1="170.18" x2="-304.8" y2="170.18" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="P+4" gate="VCC" pin="VCC"/>
<wire x1="-340.36" y1="83.82" x2="-340.36" y2="68.58" width="0.1524" layer="91"/>
<pinref part="U$6" gate="G$1" pin="3.3V"/>
</segment>
<segment>
<pinref part="P+2" gate="VCC" pin="VCC"/>
<wire x1="-401.32" y1="124.46" x2="-400.05" y2="124.46" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="1"/>
</segment>
<segment>
<pinref part="P+5" gate="VCC" pin="VCC"/>
<wire x1="-317.5" y1="132.08" x2="-317.5" y2="137.16" width="0.1524" layer="91"/>
<pinref part="U$5" gate="G$1" pin="P$2"/>
</segment>
<segment>
<pinref part="P+3" gate="VCC" pin="VCC"/>
<pinref part="U$7" gate="G$1" pin="VCC"/>
<wire x1="-457.2" y1="119.38" x2="-454.66" y2="119.38" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$10" class="0">
<segment>
<wire x1="-411.48" y1="109.22" x2="-411.48" y2="111.76" width="0.1524" layer="91"/>
<wire x1="-411.48" y1="111.76" x2="-400.05" y2="111.76" width="0.1524" layer="91"/>
<pinref part="U$8" gate="G$1" pin="P$1"/>
<pinref part="U$3" gate="G$1" pin="6"/>
</segment>
</net>
<net name="N$8" class="0">
<segment>
<wire x1="-370.84" y1="152.4" x2="-345.44" y2="142.24" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="D+"/>
<wire x1="-353.06" y1="116.84" x2="-342.9" y2="116.84" width="0.1524" layer="91"/>
<wire x1="-342.9" y1="116.84" x2="-342.9" y2="142.24" width="0.1524" layer="91"/>
<wire x1="-342.9" y1="142.24" x2="-345.44" y2="142.24" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="17"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<wire x1="-429.26" y1="119.38" x2="-400.05" y2="119.38" width="0.1524" layer="91"/>
<pinref part="U$7" gate="G$1" pin="TX"/>
<pinref part="U$3" gate="G$1" pin="3"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<wire x1="-400.05" y1="116.84" x2="-429.26" y2="116.84" width="0.1524" layer="91"/>
<pinref part="U$7" gate="G$1" pin="RX"/>
<pinref part="U$3" gate="G$1" pin="4"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, Eagle supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
</compatibility>
</eagle>
