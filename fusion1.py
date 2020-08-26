from PIL import Image
import numpy as np
import codecs
import pytesseract
import cv2
#upscaling
casemod_path="casemod/casemod2.png"
im = Image.open("images/10.png")
im.save(casemod_path, dpi=(300,300))
##############################
#grayscaling
image = cv2.imread(casemod_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(casemod_path,gray)
################################
#thresholding(adaptive_gaus)
image1 = cv2.imread(casemod_path)  
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 199, 5)
 
#thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                         cv2.THRESH_BINARY, 199, 5)  
#cv2.imshow('Adaptive Mean', thresh1)
#cv2.imshow('Adaptive Gaussian', thresh2)
cv2.imwrite(casemod_path,thresh1)
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()
################################################################
    ################################################
#OCR part
def ocr_core(img):
    text = pytesseract.image_to_string(Image.open(img),lang="tamil7")
    return text
img=casemod_path
print(ocr_core(img))
f=codecs.open("result/10.txt","w","utf-8")
f.write(ocr_core(img))
f.close()


