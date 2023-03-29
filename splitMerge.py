import cv2 as cv
import numpy as np 

img  = cv.imread('images\wallpaperflare.com_wallpaper (1).jpg')
img = cv.resize(img , (1000, 500))

blank = np.zeros(img.shape[:2], dtype = 'uint8')

cv.imshow('Cat' ,img)

b,g,r = cv.split(img)

blue = cv.merge([blank , blank, b])
green = cv.merge([blank , g ,  blank])
red = cv.merge([r, blank , blank])



cv.imshow('Blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r ])
cv.imshow('Merged', merged)


cv.waitKey(0)



