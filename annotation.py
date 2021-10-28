import os
import json
import cv2

IM_SIZE = 500  # resize all images to 500x500
outputNumber = 1
jsonPath = r'/home/marco/Assignment_2/annotated_json'
imgPath = r'/home/marco/Assignment_2/images_input'

for files in os.listdir(jsonPath):
    f = open(os.path.join(jsonPath, files))
    data = json.load(f)

    for idx in data['shapes']:  # take 'points' field 1-by-1 in 'shapes' field
        points = idx['points']

        x1 = int((points[0])[0])  # coordinate axes of annotated images
        y1 = int((points[0])[1])
        x2 = int((points[1])[0])
        y2 = int((points[1])[1])

        img = cv2.imread(r'/home/marco/Assignment_2' + data['imagePath'].replace('..', ''))  # from annotated json file, take the following image file
        cropImg = img[y1:y2, x1:x2]  # axes are INVERTED

        # resize and check broken images
        try:
            resize = cv2.resize(cropImg, (IM_SIZE, IM_SIZE))
        except:
            print(r'/home/marco/Assignment_2' + data['imagePath'].replace('..', ''))

        # resize = cv2.resize(cropImg, (IM_SIZE, IM_SIZE))
        cv2.imwrite(r'/home/marco/Assignment_2/annotated_input/' + 'corgi%d.jpg' % outputNumber, resize)
        outputNumber += 1