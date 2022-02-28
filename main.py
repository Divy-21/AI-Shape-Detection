import PIL
import tkinter
import cv2
import numpy as np
from matplotlib import pyplot as plt

from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
# image prompt
def select_image():
 path = filedialog.askopenfilename()
 img = cv2.imread(path)
 imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
 contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#shape detections
 cv2.imshow("img", img)
 for contour in contours:
     approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
     cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
     x = approx.ravel()[0]
     y = approx.ravel()[1] - 5
     if len(approx) == 3:
         cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
     elif len(approx) == 4:
         x1 ,y1, w, h = cv2.boundingRect(approx)
         aspectRatio = float(w)/h
         print(aspectRatio)
         if aspectRatio >= 0.95 and aspectRatio <= 1.05:
           cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
         else:
           cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
     elif len(approx) == 5:
         cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
     elif len(approx) == 10:
         cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
     elif len(approx) == 7:
         cv2.putText(img, "Heptagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
     elif len(approx) == 6:
         cv2.putText(img, "Hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
     elif len(approx) == 10:
         cv2.putText(img, "Decagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
     else:
         cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

 cv2.imshow(path, img)

#gui code
root = Tk()
root.title('Shape Detection')
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="100", pady="100")
root.mainloop()

		
