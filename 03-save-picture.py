
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('assets/books.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('results/booksgray.png',img)
