import numpy as np
import cv2
import matplotlib.pyplot as plt



test_image = cv2.imread('images/1.jpg')

#Converting to grayscale
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying the grayscale image
plt.imshow(test_image_gray, cmap='gray')