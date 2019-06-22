import cv2
import numpy as np

im = cv2.imread("pink_squares_matte.jpg")
img = cv2.resize(im, (500, 400))

# load image

# add blur because of pixel artefacts
img = cv2.GaussianBlur(img, (5, 5),5)
# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# set lower and upper color limits

lower_val = (131, 37, 200)
upper_val = (255, 161, 255)
# Threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_val, upper_val)
# apply mask to original image
res = cv2.bitwise_and(img, img, mask= mask)
#show imag
cv2.imshow("Result", res)
# detect contours in image
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw filled contour on result
for cnt in contours:
    cv2.drawContours(res, [cnt], 0, (0,0,255), 2)
# detect edges in mask
edges = cv2.Canny(mask,100,100)
# to save an image use cv2.imwrite('filename.png',img)
#show images
cv2.imshow("Result_with_contours", res)
cv2.imshow("Mask", mask)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(contours)

# gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
# _, test_thing = cv2.threshold(gray, 120,255,1) # inverted threshold (light obj on dark bg)
# test_thing = cv2.dilate(test_thing, None)  # fill some holes
# test_thing = cv2.dilate(test_thing, None)
# test_thing = cv2.erode(test_thing, None)   # dilate made our shape larger, revert that
# test_thing = cv2.erode(test_thing, None)
# contours, hierarchy = cv2.findContours(test_thing, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
rc = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rc)
for p in box:
    pt = (p[0], p[1])
    print(pt)

cv2.imshow("plank", im)
cv2.waitKey(0)

