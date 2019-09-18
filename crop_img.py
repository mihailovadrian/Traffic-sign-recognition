from PIL import Image
import numpy as np
import cv2
import os


dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    if filename.endswith(".jpg"):
        im = Image.open(filename)  
        w,h = im.size
        im.crop((240, 70, w-100, h-75)).save('crop_'+filename)
    else:
        print('not a image')
print('done')
