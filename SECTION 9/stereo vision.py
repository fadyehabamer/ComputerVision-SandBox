import cv2
import numpy as np

minDisparity = 16

numDisparities = 192 - minDisparity
blockSize = 5

P1 = 600

P2 = 2400

stereo = cv2.StereoSGBM_create(
    minDisparity=minDisparity,
    numDisparities=numDisparities,
    blockSize=blockSize,
    P1=P1,
    P2=P2)

imgL = cv2.imread('1.jpg')
imgR = cv2.imread('2.jpg')


def update():
    stereo.setBlockSize(cv2.getTrackbarPos('blockSize', 'Disparity'))

    disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    cv2.imshow('Left', imgL)
    cv2.imshow("Right", imgR)
    cv2.imshow('Disparity', (disparity - minDisparity) / numDisparities)


cv2.namedWindow('Disparity')
cv2.createTrackbar('blockSize', 'Disparity', blockSize, 21, update)

# Initialize the disparity map. Show the disparity map and images.
update()
cv2.waitKey()
