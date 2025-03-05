import cv2 as cv
import sys
import numpy as np

img = cv.imread('C:\wona_CV\week1\data/soccer.jpg')

if img is None:
	sys.exit('파일이 존재하지 않습니다.')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR 컬러 영상을 명암 영상으로 변환
gray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
print(img.shape, gray.shape)
concat_img = np.hstack((img, gray))

while True:
	cv.imshow('concatenated image', concat_img)

	key = cv.waitKey(1)
	if key==ord('q'):
		cv.destroyAllWindows()
		cv.imwrite('C:\wona_CV\week1\data/soccer_concatenated.jpg', concat_img)
		break