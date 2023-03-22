import cv2 as cv

img  = cv.imread('images\wallpaperflare.com_wallpaper (7).jpg')

cv.imshow('Cat' ,img)

# converting an image to gray scale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat', gray)

# bluring an image -> used to remove the noise from the image 
blur = cv.GaussianBlur(img , (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade -> 
canny = cv.Canny(blur , 125, 164)
cv.imshow('Canny', canny)

# dilating the image 
dilated = cv.dilate(canny , (3,3), iterations= 3)
cv.imshow('Dilated', dilated)

# eroding 
eroded = cv.erode(dilated, (3,3), iterations = 2 )
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img , (400,600) , interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping

cropped = img[50:300, 300: 500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)