from PIL import Image
import numpy as np
import cv2
import os


dir_path = os.getcwd()
i=0
for filename in os.listdir(dir_path):
    i=i+1
    if filename.endswith(".png"):
     im = Image.open(filename)
     imrez=im.resize((1200,680))
     print(filename)
     rgb_im = imrez.convert('RGB')
     rgb_im.save('resizedSign'+str(i)+'.jpg')
    else:
        print('none')
