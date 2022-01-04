import cv2
import numpy as np

# filename = '../logo.png'
# img = cv2.imread(filename)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('original', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# gray = np.float32(gray)
# corner haris take 4 params (img,block size,k-size ,k)
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking the corners, not important
# dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
#  take corners > 0.01 and color them into [0,0,255] red
# img[dst > 0.01 * dst.max()] = [0, 0, 255]
#
# cv2.imshow('dst', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ------------------------------------------------------------------------
# sh-tomasi corner detection

img = cv2.imread('../logo.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.goodFeaturesToTrack(img,n ,x,y)
# n: max nom of corners
# x: quality level (0-1)
# y: minimum euclidean distance between corners

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
# corners will be represented in an array with float numbers
corners = np.int0(corners)


# loop through values in corner array

for i in corners:
    # get center of circle
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
