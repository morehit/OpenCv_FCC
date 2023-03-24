import cv2 as cv 
import numpy as np

img  = cv.imread('images\wallpaperflare.com_wallpaper (4).jpg')
img = cv.resize(img , (1000, 500))

cv.imshow('Scarlet' ,img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Scarlet Gray', gray)

canny = cv.Canny(img , 125, 175)
cv.imshow('Canny ', canny)

ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

blank = np.zeros((500, 1000, 3) ,dtype= 'uint8')

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours , -1, (0,0,255), 1)
cv.imshow('contours',blank)

print(f'{len(contours)} contours found')
cv.waitKey(0)
