import cv2 as cv 
import numpy as np

img  = cv.imread('images\wallpaperflare.com_wallpaper (4).jpg')
img = cv.resize(img , (1000, 500))

cv.imshow('Scarlet' ,img)

# Translation -> shifting the image to right or left in x axix or y axis 
def translate(img , x , y): 
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right 
# y --> down 

translated = translate(img , -100, 100)
cv.imshow('Translated', translated)


# Rotation 
def rotate(img , angle , rotPoint= None): 
    (height, width)= img.shape[:2]

    if(rotPoint is None):
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img , rotMat , dimensions)

rotated = rotate(img , 45)
cv.imshow('Rotated', rotated)

# flipping the image 
flip = cv.flip(img , 0)
cv.imshow('flip', flip)

cv.waitKey(0)
