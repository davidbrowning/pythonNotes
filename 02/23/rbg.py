import numpy as np
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
B,G,R = cv2.split(image)
zeros = np.zeros(image.shape[:2], dtype='uint8')

cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
