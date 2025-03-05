import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW) # 카메라와 연결 시도

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

while True:
    ret, frame = cap.read()

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
    edge = cv.Canny(gray, 50, 200)

    concat_img = np.hstack((frame, cv.cvtColor(edge, cv.COLOR_GRAY2BGR)))


    cv.imshow('Video display', concat_img)

    key = cv.waitKey(1)
    if key==ord('q'):
        cv.destroyAllWindows()
        break