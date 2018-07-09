# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18

file: gifcreator.py
@author: Tarry

Code that reads output images from CLAWPACK results and creates a GIF with them
"""

# Load libraries
import sys
import datetime
import imageio
import numpy as np


VALID_EXTENSIONS = ('png', 'jpg')

# Define in which scenario are we solving the problem
case = 6
# Select which vector de we want to plot
# q=0 for q(1), q=1 for q(2) & q=2 for q(3)
q = 0

# Obtain number of files to read
filenames = []

# Obtain how many time steps do we have from the claw2ez file
claw2ez_data_file = open("claw2ez.data")
claw2ez_data = claw2ez_data_file.read().splitlines()
nout = int(claw2ez_data[3][0:4])

tsteps = np.arange(0,nout+1)

# Create a loop to generate all the filenames
for tstep in tsteps:
#	filename = 'fig_q(1)_00'+str("{0:02d}".format(tstep))+'.png'
	filename = 'fig_q('+str(q+1)+')_00'+str("{0:02d}".format(tstep))+'.png'
	filenames.append(filename)

# Set the duration of each frame (seconds)
duration = 0.8


images = []
for filename in filenames:
	images.append(imageio.imread(filename))
	output_file = "GIF_case"+str("{0:02d}".format(case))+"_q("+str(q)+").gif"
	imageio.mimsave(output_file, images, duration=duration)


