import numpy as np
import cv2

# Uncomment line #5 and comment line #7 to use the example video as a source.
# cap = cv2.VideoCapture('assets/people-walking.mp4')
# Camera video resolution 640x480
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=100, detectShadows=False)
Treshhold = 2.5
frameCount = 0
FrameLimit = 10
cap_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
tot_pixels = cap_height * cap_width

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    mask = cv2.resize(fgmask, (fgmask.shape[1], fgmask.shape[0]))

    res = cv2.bitwise_and(fgmask, mask)

    current_movement = (np.sum(res)/tot_pixels)
    
    kernel = np.ones((2,3),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)

    if current_movement > Treshhold:
        frameCount += 1
        if frameCount > FrameLimit:    
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(erosion,'Movement detected',(50,50), font, 1, (255,255,155), 2, cv2.LINE_AA)
    else:
        frameCount = 0
     
    cv2.imshow('frame',frame)
    cv2.imshow('erosion',erosion)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()