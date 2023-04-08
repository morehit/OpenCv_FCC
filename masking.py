import cv2 as cv
import numpy as np 

img  = cv.imread('images\wallpaperflare.com_wallpaper (6).jpg')

cv.imshow('Cat' ,img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image' , blank)

mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2+200, img.shape[0]//2 +200), 255 , -1 )
cv.imshow('Mask', mask )

masked= cv.bitwise_and(img , img , mask= mask)
cv.imshow('Masked Image', masked)



cv.waitKey(0)

