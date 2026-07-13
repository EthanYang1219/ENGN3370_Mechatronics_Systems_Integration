import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
cv2.rectangle(img,(100,100), (400,400), (123,213,203), 1, cv2.LINE_AA)
cv2.imshow("rectangle", img)
cv2.waitKey(0)

img = np.zeros((480, 640, 3), np.uint8)

# Draw FIRST, then show — imshow snapshots the image at call time
cv2.circle(img, (320, 240), 100, (0, 1, 200), 1, cv2.LINE_AA)  # center, radius, BGR, thickness
cv2.imshow("circle", img)

key = cv2.waitKey(0)          # wait AFTER the window exists
if key & 0xFF == ord("q"):
    cv2.destroyAllWindows()

#Generate a black canvas background for the ellipses
ellipse_canvas = np.zeros((400,600,3), dtype=np.uint8)

# 1. Draw a simple ellipse (horizontal major axis)
cv2.ellipse(ellipse_canvas,(150,150), (100,50), 0,0,360,(0,0,250),2)

# 2. Draw a circle (ellipse with equal axes)
cv2.ellipse(ellipse_canvas,(340,150), (75,75), 0,0,360,(0,250,250),2)

# 3. Draw a rotated ellipse (horizontal major axis)
cv2.ellipse(ellipse_canvas,(500,150), (80,40), 45,0,360,(200,0,0),2)

# 4. Draw a filled ellipse (orange)
cv2.ellipse(ellipse_canvas,(300,300), (100,50), 0,0,360,(0,165,255),-1)

cv2.imshow("Basic Ellipses", ellipse_canvas)
cv2.waitKey(0)

#Drawing lines on a fresh canvas
# Creating a triangle (closed polyline)
polyline_canvas = np.zeros((400,600,3), dtype=np.uint8)
triangle_points = np.array([[100, 100], [300, 100], [200,300]])
cv2.polylines(polyline_canvas, [triangle_points], True, (0,200,123),3)

#Creates a poly line (open shape)
polyline_points = np.array([[400,100], [450,200], [500, 150], [550, 250]])
cv2.polylines(polyline_canvas, [polyline_points], False, (255,0,0), 2)

cv2.imshow("Basic Polylines", polyline_canvas)
cv2.waitKey(0)

# Fresh canvas for the font showcase
text_canvas = np.zeros((400,600,3), dtype=np.uint8)
y = 30

fonts =[
    (cv2.FONT_HERSHEY_COMPLEX,"MESSI IS THE GOAT"),
    (cv2.FONT_HERSHEY_SIMPLEX,"MESSI IS THE GOAT"),
    (cv2.FONT_HERSHEY_PLAIN,"MESSI IS THE GOAT"),
    (cv2.FONT_HERSHEY_DUPLEX,"MESSI IS THE GOAT"),
    (cv2.FONT_HERSHEY_TRIPLEX,"MESSI IS THE GOAT"),
    (cv2.FONT_HERSHEY_COMPLEX_SMALL,"MESSI IS THE GOAT"),
    (cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,"MESSI IS THE GOAT"),
    (cv2.FONT_HERSHEY_SCRIPT_COMPLEX,"MESSI IS THE GOAT"),
]

for font_face, font_name in fonts:
    cv2.putText(text_canvas, font_name, (10,y), font_face, 0.7, (255,255,255), 1, cv2.LINE_AA)
    y+=30

cv2.imshow("Different Fonts", text_canvas)
cv2.waitKey(0)

#Practice exercise on page
exercise_canvas = np.zeros((400, 600, 3), dtype=np.uint8)

mode = "l"          # current shape: 'l' line, 'r' rectangle, 'c' circle
drawing = False      # True while the left mouse button is held down
ix, iy = -1, -1       # start point of the current shape


def draw_shape(event, x, y, flags, param):
    global mode, drawing, ix, iy, exercise_canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            preview = exercise_canvas.copy()
            if mode == "l":
                cv2.line(preview, (ix, iy), (x, y), (0, 255, 0), 2)
            elif mode == "r":
                cv2.rectangle(preview, (ix, iy), (x, y), (255, 0, 0), 2)
            elif mode == "c":
                radius = int(np.hypot(x - ix, y - iy))
                cv2.circle(preview, (ix, iy), radius, (0, 0, 255), 2)
            cv2.imshow("Practice", preview)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == "l":
            cv2.line(exercise_canvas, (ix, iy), (x, y), (0, 255, 0), 2)
        elif mode == "r":
            cv2.rectangle(exercise_canvas, (ix, iy), (x, y), (255, 0, 0), 2)
        elif mode == "c":
            radius = int(np.hypot(x - ix, y - iy))
            cv2.circle(exercise_canvas, (ix, iy), radius, (0, 0, 255), 2)
        cv2.imshow("Practice", exercise_canvas)


cv2.namedWindow("Practice")
cv2.setMouseCallback("Practice", draw_shape)

while True:
    cv2.imshow("Practice", exercise_canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("l"):
        mode = "l"
    elif key == ord("r"):
        mode = "r"
    elif key == ord("c"):
        mode = "c"
    elif key == ord("q"):
        break

cv2.destroyAllWindows()


