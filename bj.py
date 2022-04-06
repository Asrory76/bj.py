import cv2 as cv
gambar = cv.imread('mina.jpg')

ubahKeGray = cv.cvtColor(gambar, cv.COLOR_BGR2GRAY)
ubahKeGray = cv.medianBlur(ubahKeGray, 7)
tepi = cv.adaptiveThreshold(ubahKeGray, 350, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 2.5)

cv.imshow("Tepi", tepi)
cv.waitKey()
