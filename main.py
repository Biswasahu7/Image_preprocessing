# import easyocr
# reader = easyocr.Reader(['en'])
# result = reader.readtext("/home/vert/Documents/Croped_Code_Image_OpencvMo/image_289.jpg")
# print(result)

# a = [1,2,3,1,2,2]
# allcode = ['7121105133521', '7121105133521', '112110533521', '1721105133521', '712110533521', '12110533521','112110533521','112110533521','112110533521','112110533521']
# maxcode = max(allcode, key=allcode.count)
# print(maxcode)

# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import pandas as pd
from matplotlib import pyplot as plt

from PIL import Image
import numpy as np
import easyocr
import cv2
import pytesseract as tess
reader = easyocr.Reader(['en'])

# load the example image
# image = cv2.imread("/home/vert/Documents/Croped_Code_Image_OpencvMo/image_3.jpg")
# print(pytesseract.image_to_string(Image.open('/home/vert/Documents/Croped_Code_Image_OpencvMo/image_47.jpg')))
# print(pytesseract.image_to_string(Image.open('/home/vert/Documents/Croped_Code_Image_OpencvMo/image_3.jpg'), lang='fra'))

# kernal = np.ones((2,2),np.uint8)
# erosion =  cv2.erode(image,kernal,iterations=1)

# Something we got


# kernal = np.ones((6,6),np.uint8)
# closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE, kernal)

# result = reader.readtext(image)
# result1 = reader.readtext(closing)
# print("Original Image OCR Result-{}".format(result))
# print("Edited Image OCR Result-{}".format(dilation))

#22131727195
# cv2.imshow("Original image", image)
# cv2.imshow("Edited image", dilation)
# cv2.waitKey(0)
#
# # result = reader.readtext(image)
# print(result)

# This function we will pass our OCR result.
def pro(result):
    # print(result)
    print("Length of code - {}".format(len(result)))

    if result == "":
        print("Blank OCR Result")
        # logger.info("Blank OCR Result came for EasyOCR")

    else:
        code1 = []
        codelist=[]
        code = []
        
        # Checking result length
        if len(result) == 2:

            for z in result:
                # print(z)
                code1.append(z)

            # Take the proper number index from the list...
            A = str(code1[0][1]) + str(code1[1][1])
            # print("code3-{}".format(code1))
            # print(code1[2])

            # Replace the special character to 1...
            a = A.replace('|', '1')
            b = a.replace('/', '1')
            c = b.replace('!', '1')
            d = c.replace('(', '1')
            e = d.replace(')', '1')
            f = e.replace('S', '5')
            g = f.replace('&', 'x')
            h = g.replace('%', 'x')
            i = h.replace('^', '1')
            j = i.replace('p', 'B')
            k = j.replace('$', '9')
            l = k.replace('[', '1')
            m = l.replace('@', '2')
            n = m.replace('I', '1')
            o = n.replace('i', '1')
            p = o.replace('g', '9')
            q = p.replace('e', '2')
            r = q.replace('}', '1')
            s = r.replace(']', '1')
            t = s.replace('l', '1')
            u = t.replace('o', '0')
            v = u.replace('G', '6')
            w = v.replace('+', '0')
            x = w.replace('A','4')
            y = x.replace('u', '0')
            z = y.replace('{', '1')
            a1 = z.replace('x', '6')
            a3 = a1.replace('Q', '0')
            a2 = a3.replace('C', '0')
            result1 = a2.replace('?', '2')
            # print("result1-{}".format(result1+result1))

            finalcode = result1
            # logger.info("All special character has been removed")

            # # Appending final code result to codelist variable...
            codelist.append(finalcode)

            # Converting list to string for mapping with IR data...
            code = ''.join(codelist)

        elif len(result) == 3:

            # print(result)
            # print("code length is more then 1")

            for z in result:
                # print(z)
                code1.append(z)
                # code2.append(z)
                # code3.append(z)
            # print("code3-{}".format(code3))

            # print(result)

            # Take the proper number index from the list...
            # A = str(code1[0][1]) + str(code1[1][1]) + str(code1[2][1])
            A = str(code1[1][1]) + str(code1[2][1])
            # print("code3-{}".format(code1))
            # print(code1[2])

            # Replace the special character to 1...
            a = A.replace('|', '1')
            b = a.replace('/', '1')
            c = b.replace('!', '1')
            d = c.replace('(', '1')
            e = d.replace(')', '1')
            f = e.replace('S', '5')
            g = f.replace('&', 'x')
            h = g.replace('%', 'x')
            i = h.replace('^', '1')
            j = i.replace('p', 'B')
            k = j.replace('$', '9')
            l = k.replace('[', '1')
            m = l.replace('@', '2')
            n = m.replace('I', '1')
            o = n.replace('i', '1')
            p = o.replace('g', '9')
            q = p.replace('e', '2')
            r = q.replace('}', '1')
            s = r.replace(']', '1')
            t = s.replace('l', '1')
            u = t.replace('o', '0')
            v = u.replace('G', '6')
            w = v.replace('+', '0')
            x = w.replace('A','4')
            y = x.replace('u', '0')
            z = y.replace('{', '1')
            a1 = z.replace('x', '6')
            a3 = a1.replace('Q', '0')
            a2 = a3.replace('C', '0')
            result1 = a2.replace('?', '2')
            # print("result1-{}".format(result1+result1))

            finalcode = result1
            # logger.info("All special character has been removed")

            # # Appending final code result to codelist variable...
            codelist.append(finalcode)

            # Converting list to string for mapping with IR data...
            code = ''.join(codelist)

            # print("Dilation OCR Result -{}".format(code))

        else:

            for z in result:
                # print(result)
                # Take the proper number index from the list...
                A = str(z[1])
                # print(A)

                # Replace the special character to 1...
                a = A.replace('|', '1')
                b = a.replace('/', '1')
                c = b.replace('!', '1')
                d = c.replace('(', '1')
                e = d.replace(')', '1')
                f = e.replace('S', '5')
                g = f.replace('&', 'x')
                h = g.replace('%', 'x')
                i = h.replace('^', '1')
                j = i.replace('p', 'B')
                k = j.replace('$', '9')
                l = k.replace('[', '1')
                m = l.replace('@', '2')
                n = m.replace('I', '1')
                o = n.replace('i', '1')
                p = o.replace('g', '9')
                q = p.replace('e', '2')
                r = q.replace('}', '1')
                s = r.replace(']', '1')
                t = s.replace('l', '1')
                u = t.replace('o', '0')
                v = u.replace('G', '6')
                w = v.replace('+', '0')
                x = w.replace('A', '4')
                y = x.replace('u', '0')
                z = y.replace('{', '1')
                a1 = z.replace('x', '6')
                a3 = a1.replace('Q', '0')
                a2 = a3.replace('C', '0')
                result1 = a2.replace('?', '2')
                # print("result1-{}".format(result1+result1))

                finalcode = result1
                # logger.info("All special character has been removed")

                # # Appending final code result to codelist variable...
                codelist.append(finalcode)

                # Converting list to string for mapping with IR data...
                code = ''.join(codelist)
                # print("Dilation OCR Result-{}".format(code))

    return code

# image processing
image = cv2.imread("/home/vert/Documents/Refer_Images/image_73823.jpg")
# image = cv2.imread("/home/vert/Documents/Croped_Code_Image_OpencvMo/image_810.jpg")


# For image process we need to assign kernal size.(As per your requied we can change and wathch your result)
kernal = np.ones((5,5),np.uint8)

# convert image to dialation.
dilation_image = cv2.dilate(image,kernal,iterations=1)

# Convert image into closing (If any blank is there between letter)
closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernal)
erode=cv2.erode(closing_image,kerne.l=kernal)

# Calling above function and passig image into easyocr to extract number form image.
result = pro(reader.readtext(image))
result1 = pro(reader.readtext(dilation_image))
result2 = pro(reader.readtext(closing_image))

# Print result
print("Normal Image result-{}".format(result))
print("closing OCR result-{}".format(result2))

# Display your image
cv2.imshow("Image", closing_image)
cv2.waitKey(0)
#.

# Pytesseract
# text = tess.image_to_string(image)
# text1=tess.image_to_string(dilation)

# print("pytesseract result - {} \n {}".format(text,text1))
# print("*"*22)
# print("Easy ocr result-{} \n {}".format(result,result1))
