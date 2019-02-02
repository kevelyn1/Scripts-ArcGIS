#-------------------------------------------------------------------------------
# Name:        buffers for records
# Purpose:     Creates buffers as separate files for each record in the input file
# Author:      Evelyn Uuemaa
# Created:     12/05/2016
#-------------------------------------------------------------------------------

import arcpy
import os 

#INPUT: Your working folder path
file_workspace=r"C:\Users\Your_name\analysis"
arcpy.env.workspace = file_workspace
print file_workspace, arcpy.Exists(file_workspace)
##True  - allows to overwrite existing files, False  - does not allow overwriting of the existing files
arcpy.env.overwriteOutput = True
#Creating an output file
#INPUT: Input file name for what you need to create buffers
fc_In1= "points.shp"
print fc_In1, arcpy.Exists(fc_In1)
##Field name based on which the you want the buffers to be created. By deafult it can be for example OBJECTID which is unique ID.
fc_In1_FieldName = "OBJECTID"
fields=['SHAPE@', 'OBJECTID']

# Execute CreateFileGDB
# arcpy.CreateFileGDB_management(r"C:\Users\Evelyn\aaa_geowork\rukkirakk_gdb", "rukkiraak")
# output_gdb=r"C:\Users\Evelyn\aaa_geowork\rukkirakk_gdb\rukkiraak.gdb"

#INPUT output folder path where you want your buffer files to be created
#If the folder does not exist then it will be created
out_workspace =r"C:\Users\Evelyn\Your_name\analysis\buffers"
if not os.path.exists(out_workspace):
    print out_workspace, os.path.exists (out_workspace)
    os.makedirs(out_workspace)
    print out_workspace, arcpy.Exists(out_workspace)
else:
    print("Output folder exists")
#INSERT: buffer width
var_buffer= "1000 Meters"

##Cursor iterates through every row in the attribute table and creates buffer and names each new buffer based on the unique ID (OBJECTID) 
with arcpy.da.SearchCursor(fc_In1, fields) as cursor:
    for row in cursor:
        var_PolyS=row[0]
        var_PolygonName = row[1]
        print "Buffer" + str(var_PolygonName)
        arcpy.Buffer_analysis(var_PolyS, out_workspace + "\\" + str(var_PolygonName)+"_buff.shp", var_buffer, "FULL", "FLAT", "ALL", "")
		
print "Creating buffers successfully finished"