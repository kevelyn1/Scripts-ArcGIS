#-------------------------------------------------------------------------------
# Name:        shp_to_gdb
# Purpose:     Copy shapefiles to a geodatabase.
#
# Author:      Evelyn Uuemaa
#
# Created:     13/05/2019
#-------------------------------------------------------------------------------

import os
import arcpy

# Set the workspace for ListFeatureClasses
arcpy.env.workspace = "c:/Users/My_Folder"

# Use the ListFeatureClasses function to return a list of
#  shapefiles.
featureclasses = arcpy.ListFeatureClasses()

# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    arcpy.CopyFeatures_management(
        fc, os.path.join("c:/Users/My_Folder/output.gdb",
                         os.path.splitext(fc)[0]))