import cv2

img = cv2.imread('../logo.png', 0)
# Initiate STAR detector
orb = cv2.ORB_create(400)

# find the keypoints with STAR
kp = orb.detect(img, None)
print(len(kp))

# compute the descriptors with ORB
des = orb.compute(img, kp)
print(orb.descriptorSize())

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
cv2.imshow('ORB', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
 