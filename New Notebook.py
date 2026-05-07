  
                    
import arcpy
from arcpy.mp import *
from IPython.display import Image
path = "D:/Ottawa/winter/Coding Python/6th lecture/Lecture6_Data/Module6_Data/Q2/Q2.aprx"
apdoc = ArcGISProject(path)
my_layouts = apdoc.listLayouts()[0]

outpath= "D:/Ottawa/winter/Coding Python/6th lecture/SUBMISSION/layout.png"

# Move the north arrow to the top right corner of the page

scale_bar=my_layouts.listElements('MAPSURROUND_ELEMENT','North Arrow')[0]
scale_bar.elementPositionX = 10
scale_bar.elementPositionY = 7.8

#Change the title of the map to “Neighborhoods 2016” and move this to the top left corner of the page
elems=my_layouts.listElements('TEXT_ELEMENT')
for element in elems:    
    if element.name == 'Title Text':
        element.text = 'Neighborhoods 2016'        
        element.elementPositionX=1
#Move the scale bar to the lower right corner of the page.
scale_bar=my_layouts.listElements('MAPSURROUND_ELEMENT','Scale Line')[0]
scale_bar.elementPositionX = 8
scale_bar.elementPositionY = 1
 
my_layouts.exportToPNG(outpath)

Image(outpath)




