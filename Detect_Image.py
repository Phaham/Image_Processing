# current code ->

import cv2
import numpy as np
import os


def color_difference(color1, color2):
    return sum([abs(component1 - component2) for component1, component2 in zip(color1, color2)])


def detect_shapes(img):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a nested list
    containing details of colored (non-white) shapes in that image
    Input Arguments:
    ---
    `img` :	[ numpy array ]
            numpy array of image returned by cv2 library
    Returns:
    ---
    `detected_shapes` : [ list ]
            nested list containing details of colored (non-white)
            shapes present in image

    Example call:
    ---
    shapes = detect_shapes(img)
    """
    detected_shapes = []

    ##############	ADD YOUR CODE HERE	##############
    TARGET_COLORS = {"Red": (0, 0, 255), "Orange": (0, 160, 255), "Green": (0, 255, 0), "Blue": (255, 0, 0)}

    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thrash = cv2.threshold(imgGry, 240, 255, cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5

        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if aspectRatio >= 0.95 and aspectRatio < 1.05:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif len(approx) == 5:
            shape = "Pentagon"
        else:
            shape = "Circle"

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        my_color = np.array(cv2.mean(img[y:y + h, x:x + w])).astype(np.uint8)[:-1]
        differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in
                       TARGET_COLORS.items()]
        differences.sort()
        my_color_name = differences[0][1]
        detected_shapes.append([my_color_name, shape, (cX,cY)])

    ##################################################

    return detected_shapes


def get_labeled_image(img, detected_shapes):
    ######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########
    """
    Purpose:
    ---
    This function takes the image and the detected shapes list as an argument
    and returns a labelled image
    Input Arguments:
    ---
    `img` :	[ numpy array ]
            numpy array of image returned by cv2 library
    `detected_shapes` : [ list ]
            nested list containing details of colored (non-white)
            shapes present in image
    Returns:
    ---
    `img` :	[ numpy array ]
            labelled image

    Example call:
    ---
    img = get_labeled_image(img, detected_shapes)
    """
    ######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########

    for detected in detected_shapes:
        colour = detected[0]
        shape = detected[1]
        coordinates = detected[2]
        cv2.putText(img, str((colour, shape)), coordinates, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    return img


if __name__ == '__main__':

    # path directory of images in 'test_images' folder
    img_dir_path = 'test_images/'

    # path to 'test_image_1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'

    # read image using opencv
    img = cv2.imread(img_file_path)

    print('\n============================================')
    print('\nFor test_image_' + str(file_num) + '.png')

    # detect shape properties from image
    detected_shapes = detect_shapes(img)
    print(detected_shapes)

    # display image with labeled shapes
    img = get_labeled_image(img, detected_shapes)
    cv2.imshow("labeled_image", img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')

    if choice == 'y':

        for file_num in range(1, 15):
            # path to test image file
            img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'

            # read image using opencv
            img = cv2.imread(img_file_path)

            print('\n============================================')
            print('\nFor test_image_' + str(file_num) + '.png')

            # detect shape properties from image
            detected_shapes = detect_shapes(img)
            print(detected_shapes)

            # display image with labeled shapes
            img = get_labeled_image(img, detected_shapes)
            cv2.imshow("labeled_image", img)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
