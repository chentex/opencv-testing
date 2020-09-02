import cv2
import numpy as np
from matplotlib import pyplot as plt

# The 0 means that it is using the first WebCam in your computer
# if not interested on showing that one change to another index.
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('videocolor', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()