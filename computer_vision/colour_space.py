import cv2
import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # avoid cv2's bundled Qt plugins clashing with matplotlib's Qt backend
import matplotlib.pyplot as plt

# Load the image (OpenCV reads it in BGR order)
image_bgr = cv2.imread("assets/profile.png")

if image_bgr is None:
    print("❌ Could not load profile.png — check the filename/path")
else:
    # Convert the same image into several colour spaces
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    image_bgra = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGBA)
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    image_hsvfull = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV_FULL)
    image_YUV = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)

    # Pick which converted image to display (swap in image_rgb, image_hsv, etc.)
    image_show = image_hsv

    # Grayscale is 2-D, so tell matplotlib to draw it in true gray (not false colour)
    plt.imshow(image_show)

    plt.axis("off")
    plt.show()
