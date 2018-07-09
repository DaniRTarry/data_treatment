"""
@author: Tarry

type: FUNCTION

description: function to convert matlab time into number
input: time data
output: time in sec
"""

import pandas as pd

def get_time(time):
	t = pd.to_datetime(time,unit='D')
	tsec = t.minute*60 + t.second + t.microsecond*1e-6
	return(tsec)