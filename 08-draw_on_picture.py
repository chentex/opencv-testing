import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('assets/books.jpg')
cv2.line(img, (0,0),(300,300), (255,0,125), 10)



cv2.circle(img, (300,300), 66, (255,0,125), -1)

cv2.rectangle(img, (366,366), (500,500), (0,0,255), 10)

pts = np.array([[400,400],[450,400],[475,450],[500,450],[475,500],[450,500],[400,450],[400,400]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img,'your test text here...',(50,50), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.drawMarker(img, (600,300), (0,250,0), cv2.MARKER_STAR, 20, 5)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
