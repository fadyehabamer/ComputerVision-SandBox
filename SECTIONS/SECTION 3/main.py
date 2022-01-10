# contour

# import cv2
#
# # read imgL
# image = cv2.imread('../logo.png')
# # change to grey
# grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # get threshold
# # threshold => (image , middleValue , max value of colors  , simple)
# ret, thresh = cv2.threshold(grayimage, 127, 255, 0)
#
# # get contour
# # findContours(threeshold , mode of retreving info , method of find)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#
# # draw contours
# # drawContours(original img, contors var , nom of countors '-1 => all' , color , thickness)
# cv2.drawContours(image, contours, -1, (255, 255, 0), 3)
#
# print("Number of contours = " + str(len(contours)))
#
# # show imgs
# cv2.imshow('Image', image)
#
# cv2.imshow('Image Gray', grayimage)
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


# =====================================================================

# contours of shape
import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)

img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

img = cv2.drawContours(color, contours, -1, (255,0 ,0), 2)

cv2.imshow("contours", color)

cv2.waitKey()

cv2.destroyAllWindows()


# ====================================================================================

# DETECTING LINE
# import cv2
# import numpy as np


# img = cv2.imread('../detect.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# canny (img , threshold1 , threshold2)
# edges = cv2.Canny(gray, 50, 120)
# minLineLength = 20
# maxLineGap = 1

# houghlines( img , rho : step size (pixel) , theta : step size angle , threshold , min line Length , max line gap  )
# lines = cv2.HoughLinesP(edges, 1,   np.pi / 180.0, 20, minLineLength, maxLineGap)
#
# for x1, y1, x2, y2 in lines[0]:
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#
# cv2.imshow("edges", edges)
# cv2.imshow("lines", img)
# cv2.waitKey()
# cv2.destroyAllWindows()

