import os
import cv2

datasetPath = "/home/marco/Downloads/dataset"
folder = ["train", "val", "public_test"]

for sub in folder:
      imgFolder = os.path.join(datasetPath, "images", sub)
      labelFolder = os.path.join(datasetPath, "labels", sub)

      for file in os.listdir(labelFolder):
            num = file.replace(".txt", "")
            img = cv2.imread(os.path.join(imgFolder, f"{num}.jpg"))
            hImg, wImg = img.shape[:2]
            
            with open(os.path.join(labelFolder, file), mode = "r") as f:
                  lines = f.readlines()
                  
                  for _, ln in enumerate(lines):
                        anno = ln.split()
                        obj, xNorm, yNorm, wNorm, hNorm = (float(i) for i in anno)
                        x, w, y, h = round(xNorm * wImg), round(wNorm * wImg), round(yNorm * hImg), round(hNorm * hImg)

                        topLeft, bottomRight = (x - w//2, y - h//2), (x + w//2, y + h//2)
                        img = cv2.rectangle(img, topLeft, bottomRight, (255, 255, 0), 2)

                        if obj == 0:
                              txt = "No mask"
                        elif obj == 1:
                              txt = "Mask correct"
                        else:
                              txt = "Mask incorrect"

                        cv2.putText(img, txt, bottomRight, cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 0), 1, cv2.LINE_AA)

            cv2.imwrite(os.path.join(datasetPath, "bbox", f"{sub}/{num}.jpg"), img)
