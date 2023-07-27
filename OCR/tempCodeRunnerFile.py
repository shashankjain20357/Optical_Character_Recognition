    config = '--oem 3 --psm %d' % psm
    txt = pytesseract.image_to_string(img, config=config, lang='eng')
    print(':', txt)
