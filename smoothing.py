import cv2 as cv

img  = cv.imread('images\wallpaperflare.com_wallpaper (3).jpg')
img = cv.resize(img , (800, 500))

cv.imshow('Cat' ,img)

#average blur 
average = cv.blur(img, (7,7))
cv.imshow('average', average)

# Gaussia Bluring 
gauss = cv.GaussianBlur(img , (7,7), 0)
cv.imshow('Gauss', gauss)

# Median Blurring 
mean = cv.medianBlur(img , 7)
cv.imshow('median', mean)

# Bilateral blurring -> most effective (applies bluring but retains the edges as well)
bilateral = cv.bilateralFilter(img ,10, 35, 25)
cv.imshow('BIlatrera ', bilateral)


cv.waitKey(0)
