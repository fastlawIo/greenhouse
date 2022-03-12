import cv2
from os import path
from PIL import Image


def processing_image(image_file: str) -> Image:

    img = cv2.imread(image_file)
    blue, green, red = cv2.split(img)
    #cv2.imshow('green', green)

    blurred = cv2.GaussianBlur(green, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 355, 5)
    #cv2.imshow("Gaussian Adaptive Thresholding", thresh)
    file_name = path.splitext(image_file)
    cv2.imwrite(str(file_name[0])+'_mask.jpg', thresh)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return img

processing_image('C:\git\plant-segmentation-my\dataset\\resources\photo_2022-02-23_15-04-49.jpg')