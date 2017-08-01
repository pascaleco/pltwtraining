# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
   
'''Read the image data'''
   # Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
  # Build an absolute filename from directory + filename

filename = os.path.join(directory, 'flower.jpg')
  # Read the image data into an array

img = plt.imread(filename)
'''Show the image data'''
  # Create figure with 1 subplot
fig, ax = plt.subplots(1, 2) #second number tells you how mnay plots you have
  # Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img,interpolation='none')
  # Show the figure on the screen
fig.show()


###
  # Make a rectangle of pixels yellow
  ###
  
height = len(img)
width = len(img[0])
for row in range(200, 220):
      for column in range(50, 100):
          img[row][column] = [255, 255, 0] # red + green = yellow
          
          img = plt.imread(filename)
  
