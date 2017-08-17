import glob
import cv2

from resize import process

for (i,image_file) in enumerate(glob.iglob('/home/pannaga/opencv-haar-classifier-training/Negative_images/*.jpg')):
        process(image_file, i)
