# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 20:04:56 2018

@author: vinay
"""

#Get the brightness of the image

from PIL import Image
from PIL import ImageStat

image = Image.open('bright.jpg').convert('L')
stat = ImageStat.Stat(image)
print("Brighness of image: ", stat.mean[0])