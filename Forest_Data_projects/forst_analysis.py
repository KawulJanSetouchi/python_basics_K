# coding: cp932
#
# ------------------------------------------------- ---------------------------------
# Name: Rinso
# Purpose: Change forest physiognomy names of polygons with less than specified area to surrounding polygons with larger area
# Overwrite with physiognomy name. (1) Merge items that are less than the specified area with items that are greater than the specified area,
# ?Merge with the largest one in the same subgroup ?Delete the smallest record
#
#
# Created: 29/08/2021
# ------------------------------------------------- ---------------------------------

import arcpy


def main():
    """
    Please change the following parameters before using this script.
    """


# ********************************【from here】************* *****************

# Feature name to be processed (must be changed)
targetFeature = 'Test'
# Geodatabase path where features are stored & output results (must be changed)
workSpacePath = 'C:\\Users\\IT05\\Desktop\\GIS_Subgroup\\Geodatabases\\test data.gdb'

# number of trials (adjacent merge process)
neighbors
Trials = 5

# Base area to override attributes
targetArea = 600

# number of trials (rewrite processing with maximum feature less than specified area)
smallAreaTrials = 5

# whether to remove objects less than a certain area
isDelete = False

# Reference area to be deleted
deleteArea = 1

# ********************************[So far]>************ ********************

# If the number of attempts is 0, terminate the program
if neighborsTrials == 0 and smallAreaTrials == 0:
    return

for i in range(neighbors Trials):
    if i != 0:
# prepare for next process
if arcpy.Exists('Target_Single'):
    arcpy.management.Delete('Target_Single')
if arcpy.Exists('Target_Single_Neighbors'):
    arcpy.management.Delete('Target_Single_Neighbors')
if arcpy.Exists('Test'):
    arcpy.management.Delete('Test')
if arcpy.Exists('Result'):
    arcpy.management.Rename('Result', 'Test')

# Pre-preparation (for less than the specified area, change depending on the situation)
Preprocessing(targetFeature, targetArea, workSpacePath)

# actual processing
ReplaceAttribute(workSpacePath)

# Dissolve processing
DoDissolve('Target_Single', workSpacePath)

for i in range(smallAreaTrials):
# When there are only small features in the same subsection
if arcpy.Exists('Target_Single'):
    arcpy.management.Delete('Target_Single')
if arcpy.Exists('Target_Single_Neighbors'):
    arcpy.management.Delete('Target_Single_Neighbors')
if arcpy.Exists('Test'):
    arcpy.management.Delete('Test')
if arcpy.Exists('Result'):
    arcpy.management.Rename('Result', 'Test')
SmallAreaMarge(targetFeature, targetArea, workSpacePath)

if is Delete:
    DeleteOneSquareMeter(workSpacePath, deleteArea)


def DeleteOneSquareMeter(workSpacePath, deleteArea):
    """
    Method name: DeleteOneSquareMeter method
    Argument 1 : Geodatabase path where the layer resides
    Argument 2 : Deletion area criterion
    What it does: Delete records of tiny polygons
    """


# set workspace
arcpy.env.workspace = workSpacePath

# Processing object
tblName = 'Result'
fldShpArea = 'Shape_Area'

cursor = arcpy.UpdateCursor(tblName)
for record in cursor:
    if record.getValue(fldShpArea) < deleteArea:
        cursor.deleteRow(record)
cursor.updateRow(record)


def SmallAreaMarge(target, targetArea, workSpacePath):
    """
    Method name: SmallAreaMarge method
    Overview: Overwrite with the forest type name of the largest feature within the specified area
    """


Preprocessing(target, targetArea, workSpacePath)

# set workspace
arcpy.env.workspace = workSpacePath

# table name
tblName = 'Target_Single_Neighbors'  # output name of Polygon Neighbors
featureName = 'Target_Single'  # Name of sub-group data to be finally rewritten

# field name
fldObjId = 'OBJECTID'
fldSrc = 'src_U_Key'
fldNbr = 'nbr_U_Key'
fldSrcShpArea = 'src_Shape_Area'
fldNbrShpArea = 'nbr_Shape_Area'
fldSrcIsMarge = 'src_Is_Marge'
fldNbrIsMarge = 'nbr_Is_Marge'
fldSrcShohan = 'src_Shohan'
fldNbrShohan = 'nbr_Shohan'
fldIsUse = 'Is_Use'
fldNbrRinso = 'nbr_forest name'
fldFeatureRinso = 'forest name'
fldFeatureUniqueKey = 'U_Key'
fldNodeCount = 'NODE_COUNT'

# Delete records that are not for merging (src side only)
cursor = arcpy.UpdateCursor(tblName)
for record in cursor:
    if record.getValue(fldSrcIsMarge) == 0:
        cursor.deleteRow(record)
cursor.updateRow(record)

# delete anything that isn't in the same subgroup
cursor = arcpy.UpdateCursor(tblName)
for record in cursor:
    if record.getValue(fldSrcShohan) != record.getValue(fldNbrShohan):
        cursor.deleteRow(record)
cursor.updateRow(record)

# Adjacent polygons that only intersect at one point are excluded.
cursor = arcpy.UpdateCursor(tblName)
for record in cursor:
    if record.getValue(fldNodeCount) > 0:
        cursor.deleteRow(record)
cursor.updateRow(record)

# count the number of records
cursor = arcpy.UpdateCursor(tblName)
recordCount = 0
for record in cursor:
    recordCount += 1

# Identify the largest concatenated object
cursor = arcpy.UpdateCursor(tblName)
recordSrcObjArea = 0  # Area on the source side
beforeRecordSrcObjId = 0  # Object ID of previous record (source side)
beforeRecordNbrObjArea = 0  # object id of previous record (neighborhood)
objectId = 0  # object id
cnt = 0
useObjId = []  # Object ID to use
for record in cursor:
# If it's not the first record and the object ID on the source side has changed
if (cnt != 0) and (beforeRecordSrcObjId != record.getValue(fldSrc)):
    if beforeRecordNbrObjArea > recordSrcObjArea:
        useObjId.append(objectId)
# Get the data of the current record and continue
recordSrcObjArea = record.getValue(fldSrcShpArea)
beforeRecordSrcObjId = record.getValue(fldSrc)
beforeRecordNbrObjArea = record.getValue(fldNbrShpArea)
objectId = record.getValue(fldObjId)
cnt += 1
# Object ID of last record
if recordCount == cnt:
    if beforeRecordNbrObjArea > recordSrcObjArea:
        useObjId.append(objectId)
continue
# final record processing
elif recordCount == (cnt + 1):
    if record.getValue(fldNbrShpArea) > b :
        cnt +=1
