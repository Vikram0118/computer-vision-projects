import cv2
from fpdf import FPDF
import os

cap = cv2.VideoCapture("./video.mp4")

time_skips = float(1000) 
count = 0
success,image = cap.read()
while success:
    name = './images/frame' + str(count) + '.jpg'
    cv2.imwrite(name, image)     
    cap.set(cv2.CAP_PROP_POS_MSEC,(count*time_skips))    
    success,image = cap.read()
    count += 1
cap.release()


pdf=FPDF()
pdf.set_auto_page_break(0)
img_list=[x for x in os.listdir("./images")]
for img in img_list:
    pdf.add_page()
    image="./images/"+img
    pdf.image(image,w=150,h=260)
pdf.output("images.pdf")







