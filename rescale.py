import cv2 as cv 


# img = cv.imread('images/wallpaperflare.com_wallpaper (1).jpg')
# cv.imshow('Cap', img) 

def rescaleFrame(frame, scale= 0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]* scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions , interpolation= cv.INTER_AREA)




# capture = cv.VideoCapture('videos/video.mp4')

# while True:
#     isTrue , frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Video resized ', frame_resized)
#     cv.imshow('Video', frame)
    
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)

# works for only live videos 
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

img  = cv.imread('images\wallpaperflare.com_wallpaper (3).jpg')

img_resized = rescaleFrame(img); 

cv.imshow('Cap resized' , img_resized)
cv.imshow('Cat' ,img)

cv.waitKey(0)

