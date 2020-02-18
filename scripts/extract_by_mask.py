
#-------------------------------------------------------------------------------
# Name:        Extract by Mask.py
# Purpose:     Extracting smaller subset from multiple raster datasets based on one mask (shp)
#
# Author:      Evelyn Uuemaa
#
# Created:     12/10/2017

#-------------------------------------------------------------------------------

# Import arcy, os and sa (spatial analyst)
import arcpy, os
from arcpy import env
from arcpy.sa import *
arcpy.

#Define the working directory
file_workspace=
arcpy.env.workspace = r"C:\Users\my_folder\my_geodatabase.gdb"
print("Folder exists", arcpy.Exists("Folder exists"))
## If True  - allows file overwrite, If false  - does not allow file overwrite
arcpy.env.overwriteOutput = True

#Define the output folder and if folder does not exist then it will be created automatically
out_workspace =r"C:\Users\my_folder\output_folder"
if not os.path.exists(out_workspace):
    print out_workspace, os.path.exists (out_workspace)
    os.makedirs(out_workspace)
print("Folder created")

#Define the mask file
inMaskData ="mask.shp"
# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

#Define the list of rasters that will be masked and print the names of the rasters
InRaster_list=arcpy.ListRasters()

for rst in InRaster_list:
    print(rst)

#Create a loop over all rasters to mask with your mask file (inMaskData)
for rst in InRaster_list:
    outExtractByMask = arcpy.sa.ExtractByMask(rst,inMaskData)
 #define the output raster names based on the input name by 1) removing file extension .tif and 2) taking only 4 last characters (define the number yoourself based on your needs); 3) add "_extr.tif" to the end
    outname = os.path.join(out_workspace, rst.replace(".tif", "")[-4:]+"_extr.tif") # Create the full out path
    outExtractByMask.save(outname)
    print(outname)

#print "Extract finished" if all finished
print("Extract finished")


