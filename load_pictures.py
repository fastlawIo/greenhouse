import cv2
import numpy as np
from os import path
from PIL import Image


def processing_image(image_file: str) -> Image:

    img = cv2.imread(image_file)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 130])
    upper_white = np.array([180, 110, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    #res = cv2.bitwise_and(img, img, mask=mask)
    #cv2.imshow('res', res)

    #thresh2 = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('thresh2', thresh)

    file_name = path.splitext(image_file)
    cv2.imwrite(str(file_name[0])+'_mask.jpg', thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return img

#processing_image('C:\git\plant-segmentation-my\dataset\\resources\photo_2022-02-23_15-04-44.jpg')
#processing_image('C:\git\plant-segmentation-my\dataset\\resources\photo_2022-02-23_15-04-52.jpg')
processing_image('C:\git\plant-segmentation-my\dataset\\resources\photo_2022-02-22_10-21-34.jpg')