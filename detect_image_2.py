 # There is a problem when you're detecting images of same coour then the values stored in same list instead of seperate lists Else works Fine in Window
  
# Importing Modules
import cv2
import numpy as np
import os

# Global variable for details of shapes found in image
shapes = {}
"""
    details of colored (non-white) shapes present in image at img_file_path
    stored in a dictionary: { 'Shape' : ['color', Area, cX, cY] }
    e.g., { 'circle' : ['red', 24469.3, 540, 830] }
"""

img = cv2.imread(r'G:\programming\EYRC#2021\bm_task_1a\Task 1A\test_images\test_image_3.png')

# Converting the image into hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Defining Masking Range for yellow, green, red and blue colors
lower_orange = np.array([10, 100, 20])
upper_orange = np.array([25, 255, 255])

lower_green = np.array([40, 70, 80])
upper_green = np.array([70, 255, 255])

lower_red = np.array([0, 50, 120])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([90, 60, 0])
upper_blue = np.array([121, 255, 255])

# Creating Masks
mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Finding Contours in each mask
contour_orange, _ = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contour_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contour_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contour_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# yellow Shape
list1 = []
for contour in contour_orange:
    list1.append('orange')
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    # compute the center of the contour
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # area of contour
    area_orange = cv2.contourArea(contour)
    if len(approx) == 3:

        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['triangle'] = ['yellow', area_orange, cX, cY]
        list1.append('triangle')
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['square'] = ['yellow', area_orange, cX, cY]
            list1.append('square')
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['reactangle'] = ['yellow', area_orange, cX, cY]
            list1.append('rectangle')
    elif len(approx) == 5:
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['pentagon'] = ['yellow', area_orange, cX, cY]
        list1.append('pentagon')
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['hexagon'] = ['yellow', area_orange, cX, cY]
        list1.append('hexagon')
    elif len(approx) == 10:
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['star'] = ['yellow', area_orange, cX, cY]
        list1.append('star')
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['circle'] = ['yellow', area_orange, cX, cY]
        list1.append('circle')

    a = (cX, cY)
    list1.append(a)
# green shape
list2 = []
for contour in contour_green:
    list2.append('green')
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    # compute the center of the contour
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # area of contour
    area_green = cv2.contourArea(contour)
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['triangle'] = ['green', area_green, cX, cY]
        list2.append('triangle')
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if 0.95 <= aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['square'] = ['green', area_green, cX, cY]
            list2.append('square')
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['rectangle'] = ['green', area_green, cX, cY]
            list2.append('rectangle')
    elif len(approx) == 5:
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['pentagon'] = ['green', area_green, cX, cY]
        list2.append('pentagon')
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['hexagon'] = ['green', area_green, cX, cY]
        list2.append('hexagon')
    elif len(approx) == 10:
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['star'] = ['green', area_green, cX, cY]
        list2.append('star')
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['circle'] = ['green', area_green, cX, cY]
        list2.append('circle')
    a1 = (cX, cY)
    list2.append(a1)
# red shape
list3 = []
for contour in contour_red:
    list3.append('red')
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    # compute the center of the contour
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # area of contour
    area_red = cv2.contourArea(contour)
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['triangle'] = ['red', area_red, cX, cY]
        list3.append('triangle')
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if 0.95 <= aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['square'] = ['red', area_red, cX, cY]
            list3.append('square')
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['rectangle'] = ['red', area_red, cX, cY]
            list3.append('rectangle')
    elif len(approx) == 5:
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['pentagon'] = ['red', area_red, cX, cY]
        list3.append('pentagon')
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['hexagon'] = ['red', area_red, cX, cY]
        list3.append('hexagon')
    elif len(approx) == 10:
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['star'] = ['red', area_red, cX, cY]
        list3.append('star')
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['circle'] = ['red', area_red, cX, cY]
        list3.append('circle')
    a2 = (cX, cY)
    list3.append(a2)
# blue shape
list4 = []
for contour in contour_blue:
    list4.append('blue')
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    # compute the center of the contour
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # area of contour
    area_blue = cv2.contourArea(contour)
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['triangle'] = ['blue', area_blue, cX, cY]
        list4.append('triangle')
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if 0.95 <= aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['square'] = ['blue', area_blue, cX, cY]
            list4.append('square')
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes['rectangle'] = ['blue', area_blue, cX, cY]
            list4.append('rectangle')
    elif len(approx) == 5:
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['pentagon'] = ['blue', area_blue, cX, cY]
        list4.append('pentagon')
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['hexagon'] = ['blue', area_blue, cX, cY]
        list4.append('hexagon')
    elif len(approx) == 10:
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['star'] = ['blue', area_blue, cX, cY]
        list4.append('star')
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes['circle'] = ['blue', area_blue, cX, cY]
        list4.append('circle')
    a3 = (cX, cY)
    list4.append(a3)
# print(shapes)
list5 = []
if len(list1) != 0:
    list5.append(list1)
if len(list2) != 0:
    list5.append(list2)
if len(list3) != 0:
    list5.append(list3)
if len(list4) != 0:
    list5.append(list4)

# list5 = [list1, list2, list3, list4]
print(list5)

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
