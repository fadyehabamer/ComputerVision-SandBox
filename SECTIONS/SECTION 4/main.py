import cv2

# to draw line use following formula
# cv2.line(img,point1,point2,color,thickness)
# if img is grayscale => color of line will be white even changed
# to make color of line affected make img in rgb mode

# gray scale
# img = cv2.imread('../logo.png', 0)

# rgb
img = cv2.imread('../logo.png', 1)
# img = cv2.line(img, (0, 0), (255, 255), (178,231, 134), 3)
# cv2.imshow('img', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# =================================================================================

# to draw Arrowed line use following formula
# cv2.arrowedLine(img,point1,point2,color,thickness)

# we declare img before
# img=cv2.arrowedLine(img,(0,0),(255,255), (178,231, 134),5)
# cv2.imshow('img', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# =================================================================================

# to draw rectangle use following formula
# cv2.rectangle(img,point1,point2,color,thickness)
# point1 is the vertex of the rectangle
# point2 is the vertex opposite to point1

# img = cv2.rectangle(img, (20, 20), (255, 255), (178, 231, 134), 3)
#  if last value is = to -1 --> rectangle will be filled with the color
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# =================================================================================

# to draw circle use following formula
# cv2.circle(img,center,radius,color,thickness)


# img = cv2.circle(img, (130, 120), 100, (178, 231, 134), 3)
# if last value is = to -1 --> rectangle will be filled with the color
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# =================================================================================

# to draw ellipse use following formula
# cv2.ellipse(img,center,axes,angle,startAngle,endAngle,color,thickness)

'''
center is the center of the ellipse,
axes is the half of the size of the ellipse main axes,
angle is the ellipse rotation angle in degrees,
tartAngle is the starting angle of the elliptic arc in degrees ,
endAngle is the ending angle of the elliptic arc in degrees '''

# center = (250,250)
# axesLength= (150,100)
# angle=0
# startAngle=0
# endAngle=360

# img = cv2.ellipse(img, center, axesLength,angle ,startAngle,endAngle,(178, 231, 134), 3)
# if last value is = to -1 --> rectangle will be filled with the color
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# =================================================================================

'''
To draw text string we use the Following Function :
cv2.putText(img, text, org, fontFace, fontScale, color, thickness )
img is the source image ,
text is the text string to be drawn,
org is the Bottom-left corner of the text strip, 
fontFace is the font type see #HersheyFonts , 
fontScale is the font scale factor that is multiplied by the font-specific base size,
color is the circle color and thickness is the circle thickness and Negative values, like #FILLED
'''

font = cv2.FONT_HERSHEY_SIMPLEX
org = (150, 350)
fontScale = 2
color = (0, 0, 0)
thickness = 2

img = cv2.putText(img, 'FADY', org, font, fontScale, color, thickness)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
