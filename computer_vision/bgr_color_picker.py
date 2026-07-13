import cv2
import numpy as np


def callback(x):
    # Required by createTrackbar; we read the values in the loop instead,
    # so this just needs to exist and accept the slider position.
    pass


# Create a window (WINDOW_NORMAL lets us resize it)
cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

# Create one trackbar per colour channel, range 0-255
cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

# Create a background picture (480 high, 640 wide, 3 colour channels)
img = np.zeros((480, 640, 3), np.uint8)

while True:
    # Obtain current trackbar values
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')

    # Change the background picture colour (OpenCV uses BGR order)
    img[:] = [b, g, r]
    cv2.imshow('trackbar', img)

    # Wait 10 ms so the loop keeps redrawing while you drag the sliders
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
