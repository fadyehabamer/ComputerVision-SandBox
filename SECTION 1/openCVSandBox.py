import numpy as np
import cv2 as cv
import os


# img1 = np.zeros((3,3),dtype=np.uint8)
# print(img1)
# print(img1.shape)


# img2 = cv.cvtColor(img1,cv.COLOR_GRAY2BGR)
# print(img2)
# print(img2.shape)


# img3 = cv.imread('../logo.png')
# cv.imshow('image' , img3)
# cv.waitKey(10000)
# cv.destroyAllWindows()


# MODES of Reading IMAGE
# cv.IMREAD_COLOR
# cv.IMREAD_GRAYSCALE
# cv.IMREAD_ANYCOLOR
# cv.IMREAD_ANYDEPTH
# cv.IMREAD_UNCHANGED
# cv.IMREAD_REDUCED_GRAYSCALE_2
# cv.IMREAD_REDUCED_COLOR_2



# Image writing
# cv.imwrite('img name',var)
# cv.imwrite(r'path',var)



# Make an array of 120,000 random bytes.
# randomByteArray = bytearray(os.urandom(120000))
# flatNumpyArray = np.array(randomByteArray)
# # Convert the array to make a 400x300 grayscale image.
# grayImage = flatNumpyArray.reshape(300, 400)
# cv.imwrite('RandomGray.png', grayImage)
# # Convert the array to make a 400x100 color image.
# bgrImage = flatNumpyArray.reshape(100, 400, 3)
# cv.imwrite('RandomColor.png', bgrImage)
# grayImage = np.random.randint(0, 256,120000).reshape (300, 400)



# videoCapture = cv.VideoCapture('../earth.avi')
# fps = videoCapture.get(cv.CAP_PROP_FPS)
# size = (int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
#         int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
# videoWriter = cv.VideoWriter('MyOutputVid.avi', cv.VideoWriter_fourcc('I','4','2','0'), fps, size)
#
# success, frame = videoCapture.read()
# while success: # Loop until there are no more frames.
#     videoWriter.write(frame)
#     success, frame = videoCapture.read()



# videoCapture = cv.VideoCapture('../earth.avi')
# fps = videoCapture.get(cv.CAP_PROP_FPS)
# size = (int(videoCapture.get (cv.CAP_PROP_FRAME_WIDTH)),
#         int(videoCapture.get (cv.CAP_PROP_FRAME_HEIGHT)))
# videoWriter = cv.VideoWriter('MyOutputVid.avi',cv.VideoWriter_fourcc('I','4','2','0'), fps, size)
#
# c=0
# success, frame = videoCapture.read()
# while success: # Loop until there are no more frames.
# # Saves image in jpg file in folder
#     name = r'C:\Users\Fady Ehab Amer\Desktop\Python\SECTION 1\samples/' + str(c) + '.jpg'
#     print('Creating...'+ name)
#     cv.imwrite(name, frame)
#     c+=1
#     videoWriter.write(frame)
#     success, frame = videoCapture.read()


