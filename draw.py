import cv2 as cv
import numpy as np 

blank = np.zeros((500,500, 3), dtype= 'uint8')

# cv.imshow('Blank', blank)

# painting image 
blank[299:400 , 300:400] = 0,255,0

cv.imshow('Green', blank)

# drawing a rectangle in the image 
cv.rectangle(blank, (100,100) , (300,300), (0,255,0), thickness = 3 )
cv.rectangle(blank, (100,100) , (300,300), (0,255,0), thickness = -1 )
cv.imshow('Rectangle', blank)


# draw a circle 
cv.circle(blank, (blank.shape[1]//2 , blank.shape[0]//2), 40 ,(0,0,255), thickness=-2) 
cv.imshow('Rectangle', blank)

# draw a line 
cv.line(blank,(0,0) ,  (blank.shape[1]//2 , blank.shape[0]//2) ,(255,255,255), thickness=4)
cv.imshow('Rectangle', blank)

# write text on an image 
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,25,0), thickness=3)
cv.imshow('Text', blank)

cv.waitKey(0)