#!/usr/bin/python

import re
import sys
import os
import fnmatch

def find_files(filepat, rootdir):
    for path, dirlist, filelist in os.walk(rootdir):
            for file_name in fnmatch.filter(filelist, filepat):
                yield os.path.join(path, file_name)


############################################################################################################################
# Image formats compressed lossless (PNG)
# Open CV supports all formats.
#
#
#
#
############################################################################################################################



# Write a program that loads a user specified image, converts it into grayscale, displays it in a window and waits for the user to press  key to close the window.


# get the image name and path

# python load_image.py -i truck.jpg

import argparse
import cv2

def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Pather to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(h, w, num_channels) = image.shape
print('h=' + str(h) + '; ' + 'w= ' + str(w) + '; ' + 'c= ' + str(num_channels))

cv2.imshow('Image', image)
cv2.waitKey(0)



