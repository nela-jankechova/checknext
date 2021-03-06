
"""
simplified version of project


INITIAL IMAGE PROCESSING
_______________________________________________________________
static image
load into opencv
crop based on mark
resize to square for later processing
_______________________________________________________________



CELL/FIELD-BASED PROCESSING
_______________________________________________________________
Mark edges (where color intersects) (mainapp/conf.cfg, splitpoints (?))
	they seem to hard-code pixels that are splitpoints?
	have some slight success with canny --> findcontours --> array of contours --> then can do cell detection
go cell-by-cell:
	use Hough circle detection for pieces (see searchforpawn)
	detect color
Load array into pre-specified data structure for storing gamestate
_______________________________________________________________


MOVE PLANNING
_______________________________________________________________

Input gamestate into checkers heuristic
Output optimal move/log to console
_______________________________________________________________




Avg COLORS (within certain tolerances)
_______________________________________________________________
Black square: rgb(112, 91, 85)
White square: rgb(197, 184, 171)

Black peice: rgb(52, 51, 51)
White piece: rgb(208, 214, 170)


Ranges for pink squares:
R: 208-255
G: 37-161
B: 131-255

Ranges for blue dots (RGB)
(4, 0, 2)
(75, 29, 102)
"""
import cv2
import copy
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('pink_squares_matte.jpg')

# print(img[1,1])
res = cv2.resize(img, (500, 400))
# res2 = copy.deepcopy(res)

lowerp = [131, 37, 200]
upperp = [255, 161, 255]

lowerb = [2, 0, 4]
upperb = [47, 24, 50]
lower = np.array(lowerp)
upper = np.array(upperp)
p_in_range = []

for i in range(res.shape[1]):
    for j in range(res.shape[0]):
        if lower[0] <= res[j,i][0] <= upper[0] and lower[1] <= res[j,i][1] <= upper[1] and lower[2] <= res[j,i][2] <= upper[2]:
            p_in_range.append((i,j))

mask = cv2.inRange(res, lower, upper)
output = cv2.bitwise_and(res, res, mask=mask)

# print(res.size()[1])
#
cv2.imshow('image', output)
# print(mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(len(p_in_range))
print(p_in_range)

