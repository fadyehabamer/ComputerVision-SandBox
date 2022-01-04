import cv2 as cv

img = cv.imread('../logo.png', 0)

# # FAST ALGORITHM
# # Initiate FAST object with default values
# fast = cv.FastFeatureDetector_create()
#
# # find and draw the key points
#
# kp = fast.detect(img, None)
# img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
#
# # Print all default params
#
# print("Threshold: {}".format(fast.getThreshold()))
#
# print("non maxSuppression: {}".format(fast.getNonmaxSuppression()))
# print("neighborhood: {}".format(fast.getType()))
#
# print("Total Key points with non max Suppression: {}".format(len(kp)))
#
# cv.imwrite('fast_true.png', img2)
#
# # Disable non maxSuppression
#
# fast.setNonmaxSuppression(0)
# kp = fast.detect(img, None)
# print("Total Key points without non maxSuppression: {}".format(len(kp)))
#
# img3 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
#
# cv.imwrite("fast_false.png", img3)

# after run code
# 2 images will be saved in your current directory


# ============================================================================================================
# FAST ALGORITHM
img = cv.imread("../logo.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray, None)
img1 = cv.drawKeypoints(gray, kp, None)

cv.imwrite('sift_kp_1.jpg', img1)

img2 = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('sift_kp_2.jpg', img2)
