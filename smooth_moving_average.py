'''
autor: @Tarry

type: FUNCTION

Moving average filter

IN:
	- data:		time serie to filter
	- span:		sets the span of the moving average (SPAN MUST BE ODD)

OUT:
	- data_smooth:	filtered data
'''

import numpy as np


def mov_average(data,span):
	# Number of points at each side
	p = int(np.floor(span/2))

	# Initialize output vector
	data_smooth = np.ones(data.shape)*np.nan

	for i in range(len(data)):
		if i < p:
			data_smooth[i] = np.sum(data[:i+p+1])/float(len(data[:i+p+1]))
		elif i > (len(data)-p-1):
			data_smooth[i] = np.sum(data[i-p:])/float(len(data[i-p:]))
		else:
			data_smooth[i] = np.sum(data[i-p:i+p+1])/float(span)

	# Return output vector
	return data_smooth
