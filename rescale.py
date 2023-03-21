import cv2 as cv 


img = cv.imread('images/wallpaperflare.com_wallpaper (1).jpg')
cv.imshow('Cap', img) 

def rescaleFrame(frame, scale= 0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]* scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions , interpolation= cv.INTER_AREA)




capture = cv.VideoCapture('videos/video.mp4')

while True:
    isTrue , frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video resized ', frame_resized)
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)