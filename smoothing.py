import cv2 as cv

img  = cv.imread('images\wallpaperflare.com_wallpaper (3).jpg')
img = cv.resize(img , (800, 500))

cv.imshow('Cat' ,img)



cv.waitKey(0)
