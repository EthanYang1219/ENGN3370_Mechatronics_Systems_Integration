import cv2
print(f"✅ OpenCV installed successfully! Version: {cv2.__version__}")

import numpy as np
img = np.ones((100, 100, 3), dtype=np.uint8) * 255
cv2.imwrite("assets/test.jpg", img)
print("✅ Test images saved as test.jpg")

img = cv2.imread("assets/profile.png")

if img is None:
    print("❌ Could not load image — please check the filename/path")
else:
    # Scale down so the longest side fits on screen; 1080 suits a typical laptop display
    max_side = 1080
    h, w = img.shape[:2]
    scale = max_side / max(h, w)
    if scale < 1:                       # only shrink, never enlarge
        img = cv2.resize(img, (int(w * scale), int(h * scale)))
    print(f"✅ Showing image at {img.shape[1]}x{img.shape[0]}")

    # Show the image and wait for any key, then clean up
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
