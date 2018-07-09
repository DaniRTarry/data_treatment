'''
autor: @Tarry

type: FUNCTION

Moving average filter

IN:
	- dx:		Distance in km Eastwards
	- dy:		Distance in km Northwards
	- latm:		Latitude mean of the two points

OUT:
	- dlon:		Distance in degrees Eastwards
	- dlat:		Distance in degrees Northwards
'''

import numpy as np

def km2deg(dx,dy,latm):
	# Degree distance calculation
	dlon = dx*1000/np.pi*180/np.cos(np.radians(latm))/6371000
	dlat = dy*1000/np.pi*180/6371000

	return (dlon,dlat)
