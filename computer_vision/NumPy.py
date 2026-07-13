import cv2
import numpy as np

a = np.array([2,3,4])

b = np.array([[1.0,2.4],[3.6 ,6.7]])

c = np.zeros((480,640,3),np.uint8) # Generates an array filled with zeros (zero matrix) (np.uint8 refers to an 8 bit integer 2^8 or 0-255)

d = np.ones((480,640,3), np.uint8) #Generates an array with only ones

e = np.full((480,640,3), np.uint8)

f = np.identity(4) # Generates an square (4x4 in this case) identity matrix (all ones on the diagonal and zeros everywhere else)

g = np.eye(5,7, k=3) #Returns an array with ones on the diagonal and zeros everywhere else (differs from an identity matrix as it can be not square)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

img = np.zeros((480,640,3),np.uint8)

# print(img[100, 50])

# Generates a red line 
count = 0
while count < 200:
    img[count,100] = [0,0,255]
    count += 1

cv2.imshow("array", img)
key = cv2.waitKey(0)

if key & 0xFF == ord("q"):
    cv2.destroyAllWindows
roi = img[100:200,100:200]
img[:,:] = [0,0,255]
roi[:,:] = [0,255,0]

cv2.imshow('img', img)
    
img2 = cv2.imread("assets/profile.png")
print(img2.shape) #Displays image height, wdith, number of channels
print(img2.size) #Displays image height*width*number of channels
print(img2.dtype) #uint8

cv2.line(img, (10,20), (300,400), (0,0,255))
cv2.imshow("red line", img)
cv2.waitKey(0)
key = cv2.waitKey(0)
if key & 0xFF == ord("q"):
    cv2.destroyAllWindows