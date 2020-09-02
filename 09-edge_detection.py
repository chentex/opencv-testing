import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)

    cv2.imshow('laplacian',laplacian)

    edges = cv2.Canny(frame,50,75,L2gradient=True)
    cv2.imshow('Edges',edges)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()



cap.release()