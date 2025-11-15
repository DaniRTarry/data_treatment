"""
Convert geographic coordinates to Cartesian distances

Inputs:
    lon1 (float): Longitude of first point in degrees
    lat1 (float): Latitude of first point in degrees
    lon2 (float): Longitude of second point in degrees
    lat2 (float): Latitude of second point in degrees

Returns:
    tuple: (dx, dy) where:
        - dx (float): Distance in km Eastwards
        - dy (float): Distance in km Northwards
"""
import numpy as np

def deg2km(lon1, lat1, lon2, lat2):
    # Calculate distance in degrees
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Calculate mean latitude for projection
    latm = (lat1 + lat2) / 2.0
    
    # Convert to Cartesian distances (km)
    # Earth radius: 6371 km
    EARTH_RADIUS_M = 6371000
    DEG_TO_RAD = np.pi / 180.0
    
    dx = DEG_TO_RAD * np.cos(np.radians(latm)) * EARTH_RADIUS_M * dlon
    dy = DEG_TO_RAD * EARTH_RADIUS_M * dlat
    
    return (dx / 1000.0, dy / 1000.0)
