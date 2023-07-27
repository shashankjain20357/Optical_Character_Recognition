import cv2
from PIL import Image
import pytesseract as tess
import numpy as np

# import cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
# img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
# img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
# img = cv2.GaussianBlur(img, (1, 1), 0)

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
img1 = np.array(Image.open('sample1.jpg'))
img2 = np.array(Image.open('sample2.jpg'))
# img3 = Image.open('sample3.png')
text1 = tess.image_to_string(img1)
text2 = tess.image_to_string(img2)
# text3 = tess.image_to_string(img3)
print(text1)
print(text2)
# print(text3)
