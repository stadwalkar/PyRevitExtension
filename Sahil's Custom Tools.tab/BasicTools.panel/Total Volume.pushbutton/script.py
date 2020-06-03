#importing relevant namespaces

import clr
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *
from Autodesk.Revit.UI import *
from Autodesk.Revit import DB
from Autodesk.Revit import UI
doc = __revit__.ActiveUIDocument.Document

__title__ = 'Total Volume'
__author__ = 'Sahil'

#collector instance
cl = DB.FilteredElementCollector(doc)
cl.OfCategory(BuiltInCategory.OST_Walls)
cl.WhereElementIsNotElementType()

#iterate and volume 
total_volume = 0.0

for wall in cl:
	vol_param = wall.LookupParameter('Volume')
	if vol_param:
		total_volume = total_volume + vol_param.AsDouble()

#results

TaskDialog.Show("Total Volume","Total volume of all the walls is: {}".format(total_volume) + " ft3")