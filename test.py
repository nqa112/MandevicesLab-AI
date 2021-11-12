import os
import cv2

img = cv2.imread("/home/marco/Downloads/dataset/images/train/100.jpg")
hImg, wImg = img.shape[:2]

with open("/home/marco/Downloads/dataset/labels/train/100.txt", mode = "r") as f:
      lines = f.readlines()
      
      for _, ln in enumerate(lines):
            anno = ln.split()
            obj, xNorm, yNorm, wNorm, hNorm = (float(i) for i in anno)
            x, w, y, h = round(xNorm * wImg), round(wNorm * wImg), round(yNorm * hImg), round(hNorm * hImg)

            topLeft, bottomRight = (x - w//2, y - h//2), (x + w//2, y + h//2)
            img = cv2.rectangle(img, topLeft, bottomRight, (0, 255, 0), 2)

            if obj == 0:
                  txt = "No mask"
            elif obj == 1:
                  txt = "Mask correct"
            else:
                  txt = "Mask incorrect"

            cv2.putText(img, txt, topLeft, cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 255, 0))

cv2.imshow("Bounding box", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




            
