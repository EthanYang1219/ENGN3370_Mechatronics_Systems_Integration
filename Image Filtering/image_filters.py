import cv2
import numpy as np

img = cv2.imread("assets/profile.png")
kernel = np.ones((5,5), np.float32) / 25  # (Creating a 5x5 Kernel consisting of ones) /25

dst = cv2.filter2D(img,-1 , kernel) #Blurs image
test_blur = cv2.blur(img,(5,5))
gaussian_blur = cv2.GaussianBlur(img, (5,5),sigmaX=1)
pepper_blur = cv2.medianBlur(img,5) #Great for getting rid of extreme outliers. E.x "Salt and Pepper Images"
bilater_blur = cv2.bilateralFilter(img, 7, 20, 50)
cv2.imshow("Original Image", img)
cv2.imshow("dst", dst) #Displays the blurred image, low pass filter
cv2.imshow("Blurred image", test_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", pepper_blur)
cv2.imshow("Bilateral Filter", bilater_blur)
cv2.waitKey(0)