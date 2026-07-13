import cv2
import numpy as np

# Load the image as a BGR array of shape (height, width, 3)
spire_image = cv2.imread("assets/Tall Spire Wallpaper.jpg")

# Solid array of the same shape, every B/G/R value set to 200
img = np.ones(spire_image.shape, np.uint8)*200

# Add 200 to every pixel channel to brighten the image;
# cv2.add saturates at 255 instead of wrapping around like plain uint8 addition
result = cv2.add(spire_image, img)

#Image subtraction operation
result = cv2.subtract(result, 150) # Image appears darker; cv2.subtract saturates at 0 instead of wrapping around like plain uint8 subtraction

#Image Blending with OpenCV
Outerworld_wallpaper = cv2.imread("assets/Outer World Wallpaper.jpg")

#Blending requires both images to have the same dimensions
print(spire_image.shape)
print(Outerworld_wallpaper.shape)

# addWeighted computes src1*alpha + src2*beta + gamma; both weights are 1.0 here so
# this behaves like cv2.add rather than a true 50/50 blend
result_blend = cv2.addWeighted(Outerworld_wallpaper, 1.0, spire_image, 1.0, 0)
cv2.imshow("result", result_blend)
cv2.waitKey(0)