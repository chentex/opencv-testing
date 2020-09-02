import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    winter = cv2.applyColorMap(frame, cv2.COLORMAP_WINTER)
 
    cv2.imshow('videocolor', frame)
    cv2.imshow('videowinter', winter)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()