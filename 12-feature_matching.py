import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread('assets/mess_desk_close.jpg',0)
template = cv2.imread('assets/cupholder_template.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img_rgb,None)
kp2, des2 = orb.detectAndCompute(template,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img_rgb,kp1,template,kp2,matches[:20],None, flags=2)

plt.imshow(img3)
plt.show()
