import cv2 as cv
import sys
import numpy as np

img = cv.imread('C:\wona_CV\week1\data/soccer.jpg')
orig_img = img.copy()
pressed = False
roi = None

def draw(event, x, y, flags, param):
    global ix, iy, roi, pressed
    tmp_img = img.copy()

    if event==cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        cv.rectangle(tmp_img, (x, y), (ix+1, iy+1), (0, 0, 255), 2)
        pressed = True
    elif event == cv.EVENT_MOUSEMOVE and pressed==True:
        cv.rectangle(tmp_img, (ix, iy), (x, y), (0, 0, 255), 2)
    elif event==cv.EVENT_LBUTTONUP:
        roi = img[iy:y, ix:x]
        cv.imshow('ROI', roi)
        pressed = False

    cv.imshow('Drawing', tmp_img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

while True:

    key = cv.waitKey(1)

    if key==ord('r'):
        roi = None
    elif key==ord('s'):
        if roi is not None:
            cv.imwrite('C:\wona_CV\week1\data/roi.jpg', roi)
            print("ROI saved")
    elif key==ord('q'):
        break        
        
cv.destroyAllWindows()
        