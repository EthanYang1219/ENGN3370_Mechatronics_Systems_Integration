import cv2
import numpy as np

background = cv2.imread("assets/Outer World Wallpaper.jpg") # image is 1920 x 1080

new_background =cv2.resize(background,(1280,720)) # Resized to 66.6% of the original image size

new = cv2.resize(background, None, fx = 0.5, fy = 0.5) #Resize to 50% of the orignal size 
# cv2.imshow("original", background)
# cv2.imshow("resized", new_background)
# cv2.imshow("50%", new)
# cv2.waitKey(0)

# Flipping Images
# vertical_flip = cv2.flip(new, 0) # Reflects along the x-axis
# horizontal_flip = cv2.flip(new, 1) # Reflects along the y-axis
# both_flip = cv2.flip(new, -1) # Reflects along the x and y axis

# #Displays the flipped images

# cv2.imshow("Flipped Vertically", vertical_flip)
# cv2.imshow("Flipped Horizontally", horizontal_flip)
# cv2.imshow("Both Flip", both_flip)
# cv2.waitKey(0)

# #Image rotations

# rot_90_cw = cv2.rotate(new, cv2.ROTATE_90_CLOCKWISE)
# rot_90_ccw = cv2.rotate(new, cv2.ROTATE_90_COUNTERCLOCKWISE)
# rot_180 = cv2.rotate(new, cv2.ROTATE_180) # Rotates 180 degrees (same thing as reflecting over the x and y axis so it will be the same as both_flip)

# #Display results
# cv2.imshow("Rotate 90 degrees clockwise", rot_90_cw)
# cv2.imshow("Rotate 90 degrees counterclockwise", rot_90_ccw)
# cv2.imshow("Both Flip", both_flip) # Just to showcase that this is equivalent to rotate 180 degrees
# cv2.imshow("Rotates 180 degrees", rot_180)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

#Image Affine Translations


h, w = new.shape[:2]
center = (w // 2, h // 2 ) #Calculates the center for the image (// (floor) rounds DOWN to the nearest whole number)
#Move the image 100px right 50px down
Move = np.float32([[1,0,100], # [1 0 tx]
                  [0,1,50]])  # [0 1 ty]

# Create a rotation matrix

r = cv2.getRotationMatrix2D(center, 45, 1)
translated = cv2.warpAffine(new,Move,(w,h))

rotated = cv2.warpAffine(new, r, (w,h))
cv2.imshow("Translated background", translated)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

