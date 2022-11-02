#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 7 14:13:38 2022

@author: sifundvolesihledlamini
"""

import cv2
import numpy as np
from PIL import Image
import os
import skimage
import glob
from matplotlib import pyplot as plt

print(os.getcwd())

inputFolder = "/Users/mylocaldrive"
folderlen = len(inputFolder)

os.mkdir('/Users/AugmentedData')
i = 0

#ROTATION
for img in glob.glob(inputFolder + "/*.*"):
    image = cv2.imread(img)
    height, width = image.shape[:2]
    rotation_matrix1 = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) #90
    rotation_matrix2 = cv2.getRotationMatrix2D((width/2, height/2), 180, 1) #180
    rotation_matrix3 = cv2.getRotationMatrix2D((width/2, height/2), 270, 1) #270
    rotated_image1 = cv2.warpAffine(image, rotation_matrix1, (width, height))
    rotated_image2 = cv2.warpAffine(image, rotation_matrix2, (width, height))
    rotated_image3 = cv2.warpAffine(image, rotation_matrix3, (width, height))
    cv2.imwrite('/Users/AugmentedData' + img[folderlen:], rotated_image1, rotated_image2, rotated_image3)

#FLIPS
for img in glob.glob(inputFolder + "/*.*"):
    image = cv2.imread(img)
    hflip = cv2.flip(image, 0) #HF
    vflip = cv2.flip(image, 1) #VF
    cv2.imwrite('/Users/AugmentedData' + img[folderlen:], hflip, vflip)

#NOISE
for img in glob.glob(inputFolder + "/*.*"):
    image = skimage.io.imread(img)/255.0
    img1 = skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True)
    gaussian = skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True) #GAUSSIAN
    speckle = skimage.util.random_noise(img, mode='speckle', seed=None, clip=True) #SPECKLE
    gnoise = (255*gaussian).astype(np.uint8)
    snoise = (255*speckle).astype(np.uint8)
    cv2.imwrite('/Users/AugmentedData' + img[folderlen:], gnoise, snoise)
    


 
