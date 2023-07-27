import pytesseract
import cv2
import numpy as np

img = cv2.imread('sample1.jpg')

#  img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
img = cv2.resize(img, None, fx=2, fy=2)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255,
                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cv2.imwrite('thresh.jpg', img)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

for psm in range(6, 13+1):
    config = '--oem 3 --psm %d' % psm
    txt = pytesseract.image_to_string(img, config=config, lang='eng')
    print(':', txt)
