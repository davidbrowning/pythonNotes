
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Pather to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(h, w, num_channels) = image.shape
print('h=' + str(h) + '; ' + 'w= ' + str(w) + '; ' + 'c= ' + str(num_channels))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscaled', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('Image', image)
cv2.waitKey(0)
