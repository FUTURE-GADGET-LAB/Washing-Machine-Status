from os import wait
import cv2
import numpy as np
import pytesseract

import urllib.request
from PIL import Image
import time

  

while(True):

    urllib.request.urlretrieve(
    'http://192.168.137.132/photo',
    "gfg.png")
    
    # img = Image.open("gfg.png")

    image = cv2.imread("./gfg.png")

    # get grayscale image
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
    def remove_noise(image):
        return cv2.medianBlur(image,5)
    
    #thresholding
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    #dilation
    def dilate(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.dilate(image, kernel, iterations = 1)
        
    #erosion
    def erode(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.erode(image, kernel, iterations = 1)

    #opening - erosion followed by dilation
    def opening(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    #canny edge detection
    def canny(image):
        return cv2.Canny(image, 100, 200)

    #skew correction
    def deskew(image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    #template matching
    def match_template(image, template):
        return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

    # image = cv2.imread('aurebesh.jpg')

    gray = get_grayscale(image)
    thresh = thresholding(gray)
    opening = opening(thresh)
    canny = canny(opening)

    custom_config = r'--oem 3 --psm 6 outputbase digits'
    # custom_config = r'--oem 3 --psm 6'
    # pytesseract.image_to_string(img, config=custom_config)
    string = pytesseract.image_to_string(image, config=custom_config)
    # print(string)

    on = False
    for cha in string:
        if cha!=" "  and cha !='\t' and cha!='\n'  and cha!='\x0b'  and cha!='\x0c'  and cha!='\r':
            # print(cha)
            # print("nut")
            on = True
            break
            

    if(on):
        print("Washing Machine is on")
    else:
        print("Washing Machine is off")
    time.sleep(2)