import cv2
from PIL import Image
import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# img1 = Image.open('sample1.jpg')
# img2 = Image.open('sample2.jpg')
# img3 = Image.open('sample3.png')
# text1 = tess.image_to_string(img1)
# text2 = tess.image_to_string(img2)
# text3 = tess.image_to_string(img3)
# print(text1)
# print(text2)
# print(text3)

camera = cv2.VideoCapture(0)

while True:
    _, img = camera.read()
    cv2.imshow('Text detection', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite('test1.jpg', img)
        break
camera.release()
cv2.destroyAllWindows()


def tesseract():
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    Imagepath = 'test1.jpg'
    i = Image.open('test1.jpg')
    text = tess.image_to_string(i)
    print(text[:-1])


tesseract()
