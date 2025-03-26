import cv2

image = cv2.imread("opencvstudy\SECTION2\image_01.png")
cv2.imshow("Original", image)

#         image[yStart:yEnd, xStart:xEnd]
cropped = image[60:160, 300:380]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)