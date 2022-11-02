#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:41:00 2022

@author: sifundvolesihledlamini
"""

from pathlib import Path
import pandas as pd
import re
import shutil
import random
import cv2
import os.path
import skimage
import numpy as np


scr = Path("/Users/mylocaldrive")
path = scr.glob('*.*')

filenames = []
for file in path:
    img = cv2.imread(str(file))
    filenames.append(file)

filenames.sort() 
random.seed(42)
random.shuffle(filenames)

split_1 = int(0.7 * len(filenames))
split_2 = int(0.9 * len(filenames))
train_filenames = filenames[:split_1]
valid_filenames = filenames[split_1:split_2]
test_filenames = filenames[split_2:]

os.mkdir('/User/trainData')
os.mkdir('/User/validData')
os.mkdir('/User/testData')

trainData_dir = Path('/Users/trainData')
validData_dir = Path('/Users/validData')
testData_dir = Path('/Users/testData')

for file in train_filenames:
    shutil.copyfile(file, str(trainData_dir) +'\\'+ file.stem + file.suffix)

for file in valid_filenames:
    shutil.copyfile(file, str(validData_dir) +'\\'+ file.stem + file.suffix)

for file in test_filenames:
    shutil.copyfile(file, str(testData_dir) +'\\'+ file.stem + file.suffix)



