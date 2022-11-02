#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 2 11:17:56 2022

@author: sifundvolesihledlamini
"""

# code to plot histogram in python 

import os
import cv2
import glob
import numpy as np


basepath = "Users/mylocaldrive"
folderlen = len(basepath)
path = glob.glob(basepath + '/*.*')

HistEq = []
BilatFilt = []

# HISTOGRAM EQUALIZATION
for i in path:
    img_in = cv2.imread(str(i))
    hist, bins = np.histogram(img_in.flatten(), 256, [0, 256])
    plt.hist(img_in.flatten(), 256, [0, 256], color = 'y')
    
    b, g, r = cv2.split(img_in)
    h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256])
    h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
    h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
    
    cdf_b = np.cumsum(h_b)
    cdf_g = np.cumsum(h_g)
    cdf_r = np.cumsum(h_r)
    
    cdf_m_b = np.ma.masked_equal(cdf_b, 0)
    cdf_m_b = (cdf_m_b - cdf_m_b.min())*255/(cdf_m_b.max() - cdf_m_b.min())
    cdf_final_b = np.ma.filled(cdf_m_b, 0).astype('uint8')
    
    cdf_m_g = np.ma.masked_equal(cdf_g, 0)
    cdf_m_g = (cdf_m_g - cdf_m_g.min())*255/(cdf_m_g.max() - cdf_m_g.min())
    cdf_final_g = np.ma.filled(cdf_m_g, 0).astype('uint8')
    
    cdf_m_r = np.ma.masked_equal(cdf_r, 0)
    cdf_m_r = (cdf_m_r - cdf_m_r.min())*255/(cdf_m_r.max() - cdf_m_r.min())
    cdf_final_r = np.ma.filled(cdf_m_r, 0).astype('uint8')
    
    img_b = cdf_final_b[b]
    img_g = cdf_final_g[g]
    img_r = cdf_final_r[r]
    
    img_out = cv2.merge((img_b, img_g, img_r))
    
    equ_b = cv2.equalizeHist(b)
    equ_g = cv2.equalizeHist(g)
    equ_r = cv2.equalizeHist(r)
    equ = cv2.merge((equ_b, equ_g, equ_r))

    HistEq.append(equ)
 

# BILATERAL FILTER
for j in range(1, len(HistEq)+1):
    img = cv2.bilateralFilter(j, 5, sigmaColor=50, sigmaSpace=75, borderType=cv2.BORDER_CONSTANT)
    BilatFilt.append(img)

