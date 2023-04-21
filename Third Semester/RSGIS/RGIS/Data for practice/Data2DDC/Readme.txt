Digital topographic data is maintained at sheet level. Data
for each sheet has been implemented by classifying in nine 
classes, each class may have several layers depending on the
type of data being represented.


Data format:

Data files are created in standard ArcInfo coverages or 
ArcView shape files and the naming conventions are as follows:

Data classes	LayerName	Data Type	Remarks
						
Transportation	Trans_ln	Line		Roads
		Trans_ar	Polygon		Areas related
						to transportation
Building	Build_pt	Point		Locations of building
		Build_ar	Polygon		Built_up areas
		Vil_name	Point		Settlement name 
Topography	Topog_pt	Point		Spot elevation
		Topog_ln	Line		Contour lines	
Hydrography	Hydro_ln	Line		Rivers and Streams
		Hydro_ar	Polygon		Wide rivers and lakes
Landcover	Landc_ar	Polygon		Landcover areas
Utility		Utili_ln	Line		Electricity lines
Designated Area	Desig_ar	Polygon		National Parks and
						wild life reserves
Admin		Ward		Polygon		Ward boundaries


Attribute:

All the layers having associated attribute file have at least 
one attribute field called "FCODE", except "Vil_Name" layer, 
which holds the value as specified according to the Feature code 
table named "Feature code" an excel file included in the 
documentation.The meaning of the feature code is explained in 
the table. In addition attribute field are appended as applicable
in the attribute file related to some layers viz. "Build_pt", 
"Topog_pt", "Vil_name", "Topog_pt", "Topog_ln", "Ward", "Admin_ar".
Meaning of the name of the attribute field can be obtained from 
the "attbcode" included in this documentation. In case of Vil_Name
layer the attribute field Vil_Name holds the value 
"name of the places" implemented as a location point.

Projection:

The coordinates in the data set are based on the Modified UTM Projection
on Everest Spheroid 1830 (semi major axis, a = 6 377 276.345 m. and
semi minor axis, b = 6 356 075.413 m.) having zone width of 3 degrees East-west with
Central Meridian 81 or 84 or 87 degree longitude as applicable. The unit
of measurement is metre. The scale factor at the central meridian is 0.9999,
false easting at central meridian is 500 000 m. and false northing at the 
Equator is 0 m.

Height Reference: Mean Sea Level (India)

Note:  In case of any errors in the data, comments if any and for aditional
information please write to the following address. 

Further information:	NGIIP,
			Survey Department,
			Ministry of Land Reform and Management,
			Nepal.

	email: 		ngiip@ccsl.com.np 

	telephone:	+977-1-4499091
	fax:		+977-1-4496231
	





