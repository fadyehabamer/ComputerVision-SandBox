# BGR IMAGE TO GREY
# import cv2
#
# originalImage = cv2.imread('../logo.png')
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# cv2.imshow("original", originalImage)
# cv2.imshow("gray", grayImage)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ===================================================

# GRAY TO BINARY
# import cv2
#
# originalImage = cv2.imread()
# # gray'../logo.png'
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# # binary
# (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("gray", grayImage)
# cv2.imshow("binary", blackAndWhiteImage)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ===================================================

# BGR TO RGB

# import cv2
#
# originalImage = cv2.imread('../logo.png')
# RGBImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
# cv2.imshow("original", originalImage)
# cv2.imshow("rgb", RGBImage)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ===================================================

# SPLIT , MERGE
# import cv2
#
# originalImage = cv2.imread('../logo.png' )
# B, G, R = cv2.split(originalImage)
# cv2.imshow("original", originalImage)
# cv2.imshow("blue", B)
# cv2.imshow("Green", G)
# cv2.imshow("red", R)
# m=cv2.merge((B, G, R))
# cv2.imshow("merged", m)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ===================================================

# BGR TO HSV
# import cv2
#
# originalImage = cv2.imread('../logo.png')
# hsvImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
# cv2.imshow("original", originalImage)
# cv2.imshow("HSV", hsvImage)
# H = hsvImage[:, :, 0]
# S = hsvImage[:, :, 1]
# V = hsvImage[:, :, 2]
#
# cv2.imshow("hue", H)
# cv2.imshow("saturation", S)
# cv2.imshow("value", V)
# cv2.waitKey()
# cv2.destroyAllwindows()

# ================================================================

# HSV FOR SPECIFIC

# import cv2
# import numpy as np
#
# originalImage = cv2.imread('../logo.png')
# hsvImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
#
# cv2.imshow('original',originalImage)
#
# lower = np.array([ 0, 100, 100])
#
# upper = np.array([10, 255, 255])
#
# Mask = cv2.inRange(hsvImage, lower, upper)
#
# shape = cv2.bitwise_and(originalImage, originalImage, mask=Mask)
# cv2.imshow('mask',Mask)
#
# cv2.imshow('orange shape',shape)
# cv2.waitKey()
# cv2.destroyAllwindows()


# ================================================================

# RESIZE AN IMAGE

# import cv2
#
# image = cv2.imread('../logo.png')
#
# half = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
#
# bigger = cv2.resize(image, (1050, 1610))
#
# stretch_near = cv2.resize(image, (780, 540), interpolation=cv2.INTER_NEAREST)
#
# cv2.imshow('img', image)
# cv2.imshow('half', half)
# cv2.imshow('bigger', bigger)
# cv2.imshow('stretch', stretch_near)
#
# cv2.waitKey()
# cv2.destroyAllWindows()


# ================================================================

# LOW PASS FILTER ( BLURRING )

# import cv2
#
# image = cv2.imread('../logo.png')
# cv2.imshow('img',image)
#
# blurImage = cv2.blur(image, (5, 5))
# cv2.imshow('blured', blurImage)
#
# Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
# cv2.imshow('gaussian', Gaussian)
#
# median = cv2.medianBlur(image, 5)
# cv2.imshow('median', median)
#
# bilateral = cv2.bilateralFilter(image, 9, 75, 75)
# cv2.imshow( 'bilateral',bilateral)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ================================================================
# HIGH PASS FILTER VS LOW PASS FILTER
# import cv2
# import numpy as np
#
# img = cv2.imread('../logo.png')
#
# # smooth filter
#
# kernel1 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
#                     [0.04, 0.04, 0.04, 0.04, 0.04],
#                     [0.04, 0.04, 0.04, 0.04, 0.04],
#                     [0.04, 0.04, 0.04, 0.04, 0.04],
#                     [0.04, 0.04, 0.04, 0.04, 0.04]])
#
# # sharp filter
# kernel2 = np.array([
#     [-1, -1, -1],
#     [-1, 9, -1],
#     [-4, -1, -1]])
#
# smooth = cv2.filter2D(img, -1, kernel1)
# sharp = cv2.filter2D(img, -1, kernel2)
# cv2.imshow("original", img)
# cv2.imshow("smooth", smooth)
# cv2.imshow("sharp", sharp)

# cv2.waitKey()
# cv2.destroyAllWindows()

# =========================================================================================================


# EDGE DETECTION

# import cv2
# import numpy as np
#
# from scipy import ndimage
#
# kernel_3x3 = np.array([[-1, -1, -1],
#                        [-1, 8, -1],
#                        [-1, -1, -1]])
# kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
#                        [-1, 1, 2, 1, -1],
#                        [-1, 2, 4, 2, -1],
#                        [-1, 1, 2, 1, -1],
#                        [-1, -1, -1, -1, -1]])
#
# img = cv2.imread('../logo.png', 0)
# k3 = ndimage.convolve(img, kernel_3x3)
# k5 = ndimage.convolve(img, kernel_5x5)
# blurred = cv2.GaussianBlur(img, (17, 17), 0)
# g_hpf = img - blurred
# cv2.imshow("3x3", k3)
# cv2.imshow("5x5", k5)
# cv2.imshow("blurred", blurred)
# cv2.imshow("g_hpf", g_hpf)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ============================================================================

# Derevative

# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread( '../logo.png',0 )
# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# sobelImg= cv2.add(sobelx, sobely)
# schx= cv2.Scharr(img, cv2.CV_64F, 1, 0)
# schy= cv2.Scharr(img, cv2.CV_64F, 0, 1)
# plt.subplot(2,3,1),plt.imshow(img, cmap='gray'), plt.title('gray')
# plt.subplot(2,3,2),plt.imshow(laplacian, cmap='gray'), plt.title('laplacian')
# plt.subplot(2,3,3),plt.imshow(sobelx, cmap='gray'), plt.title('sobelx')
# plt.subplot(2,3,4),plt.imshow(sobely, cmap='gray'), plt.title('sobely')
# plt.subplot(2,3,5),plt.imshow(schx, cmap='gray'), plt.title('scharrx')
# plt.subplot(2,3,6),plt.imshow(schy, cmap='gray'), plt.title('scharry')
# plt.show()

# ================================================================================

# Canny
#
# import cv2
#
# img = cv2.imread('../logo.png', 0)
# imcanny = cv2.Canny(img, 200, 300)
# cv2.imwrite("canny.jpg", imcanny)
# cv2.imshow("original", img)
# cv2.imshow("canny", imcanny)
# cv2.waitKey()
# cv2.destroyAllWindows()
