'''
autor: @Tarry

type: FUNCTION

Moving average filter

IN:
	- lon1:		Longitude of first point
	- lat1:		Longitude of first point
	- lon2:		Longitude of second point
	- lat2:		Longitude of second point

OUT:
	- dx:		Distance in km Eastwards
	- dy:		Distance in km Northwards
'''

import numpy as np

def deg2km(lon1,lat1,lon2,lat2):
	# Distance in degrees calculation
	dlon = lon2 - lon1
	dlat = lat2 - lat1

	# Latitude mean calculation
	latm = (lat1+lat2)/2.

	# Cartesian distance calculation
	dx = np.pi/180.*np.cos(np.radians(latm))*6371000*dlon
	dy = np.pi/180.*6371000*dlat

	return (dx/1000.,dy/1000.)
