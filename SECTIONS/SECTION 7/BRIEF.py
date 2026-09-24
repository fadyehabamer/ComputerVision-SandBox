import cv2
import os

# the sample files (../logo.png, ../video.mp4, 1.jpg, ...) are relative to this folder,
# so run from here no matter which directory the script is started from
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread('../logo.png', 0)

# Initiate STAR detector
star = cv2.xfeatures2d.StarDetector_create()

# find the key points with STAR
kp = star.detect(img, None)

# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

img2 = cv2.drawKeypoints(img, kp, None)

cv2.imshow('brief', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
