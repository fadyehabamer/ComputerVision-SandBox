import cv2

# get image
img = cv2.imread('../logo.png', cv2.IMREAD_GRAYSCALE)

# create surf object
# line 9 will not work as it is deprecated as found on stackoverflow..
# instead use  line 10
# surf = cv2.xfeatures2d.SURF_create(500)
surf = cv2.SIFT_create(500)

# find the key points with surf
kp = surf.detect(img)

# compute the descriptors with surf
des = surf.compute(img, kp)

# get number af all features in img
print(len(kp))

# get number of descriptor
print(surf.descriptorSize())

# draw only key points location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, (0, 0, 255))

cv2.imshow('SURF', img2)
cv2.waitKey(0)

