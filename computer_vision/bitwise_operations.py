import cv2
import numpy as np

#Generate a new picture (bitwise_not operation)

# img = np.zeros((200,200), np.uint8)

# img[50:150, 50:150] = 255

# new_img = cv2.bitwise_not(img)

# cv2.imshow("original image", img)
# cv2.imshow("New image", new_img)
# cv2.waitKey(0)

# Bitwise_and operation

# test1 = np.zeros((200,200),np.uint8)
# test2 = np.zeros((200,200), np.uint8)

# test1[20:120,20:120] = 255
# test2[80:180,80:180] = 255

# new_image = cv2.bitwise_and(test1, test2)
# or_image = cv2.bitwise_or(test1,test2)
# xor_image = cv2.bitwise_xor(test1,test2)
# # cv2.imshow("Top left",test1)
# # cv2.imshow("Bottom right",test2)
# cv2.imshow("Combined",new_image) #Displays the areas where both squares intersect (Intersect in set theory)
# cv2.imshow("Or operation",or_image) #Displays the areas from either square (Union in set theory)
# cv2.imshow("xor",xor_image) #Displays the areas where either sqaures are NOT touching (Everything in the union minus the intersection)
# cv2.waitKey(0)

# Practice exercise page 161

image = cv2.imread("assets/Tall Spire Wallpaper.jpg")

# 1. Generate the base logo canvas
logo_part1 = np.zeros((200,200,3), np.uint8) # 200x200 blank canvas, 3 BGR colour channels
logo_part1[20:120, 20:120, 2] = 255 # red square (channel 2 = R in BGR order)
logo_part1[80:180, 80:180, 2] = 0 # clear red where green will be drawn, so the overlap doesn't blend to yellow
logo_part1[80:180, 80:180, 1] = 255 # green square (channel 1 = G); overwrites red in the overlap

# 2. Create the binary masks
binary_mask = np.zeros((200,200), np.uint8)
binary_mask[50:150,50:150] = 255 # the region of the wallpaper that will be replaced by the logo
inverted = cv2.bitwise_not(binary_mask) # everything except that region

# 3. Create a hole within the wallpaper
wallpaper_crop = image[0:200, 0:200]

# bitwise_and(img, img, mask=...) keeps pixels where mask is 255 and zeroes the rest,
# so this punches a black hole where the logo will go
background_hole = cv2.bitwise_and(wallpaper_crop,wallpaper_crop,mask=inverted)

# same trick, inverse mask: keeps only the logo pixels inside binary_mask, zeroes the rest
logo_cutout = cv2.bitwise_and(logo_part1,logo_part1,mask=binary_mask)

# the hole and the cutout occupy disjoint pixels (opposite masks), so a plain add
# combines them into the wallpaper-with-logo composite
final = cv2.add(background_hole, logo_cutout)

# 4. Displays everything
cv2.imshow("Original image", image)
cv2.imshow("Part1 (BASE LOGO)", logo_part1)
cv2.imshow("Binary Mask", binary_mask)
cv2.imshow("Inverted binary mask", inverted )
cv2.imshow("Hole (wallpaper image)", background_hole)
cv2.imshow("Logo cutout", logo_cutout)
cv2.imshow("Final Result", final)

cv2.waitKey(0)
cv2.destroyAllWindows()

