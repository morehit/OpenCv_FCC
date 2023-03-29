import cv2 as cv
import matplotlib.pyplot as plt 

#Ther are different color spaces for a image 
img  = cv.imread('images/wallpaperflare.com_wallpaper (10).jpg')
img = cv.resize(img , (700 , 700) )
cv.imshow('Cat' ,img)


#By default openCv inputs a image in BGR(Blue, Green , Red)format which is kind of inversion of the classic RGB format 

#Converting BGR image to Gray
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#convertin BGR tp hsv 
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
cv.imshow('HSV' , hsv)

#converting BGR to lab
lab = cv.cvtColor(img , cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

#converting a BGR image to RGB 
rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()



cv.waitKey(0)

