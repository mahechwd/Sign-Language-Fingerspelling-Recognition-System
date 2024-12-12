import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)  # Initialise video capture
detector = HandDetector(maxHands=1)  # Initialise HandDetector object

# Constants
offset = 20  # Expand bounding box
imgSize = 300  # Image dimensions
maxImg = 300  # Maximum number of images
counter = 0

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O",
           "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
letters_index = 0

while True:
    success, img = cap.read()  # Capture frame from camera
    hands, img = detector.findHands(img)  # Detect hands and annotate the frame

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # Getting bounding box information
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255  # Image background

        imgCropShape = imgCrop.shape

        # Image fitting
        aspectRatio = h / w

        # Height is greater
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            #imgResizeShape = imgResize.shape  # Retrieve shape of imgResize
            wGap = math.ceil((imgSize - wCal) / 2)  # Used to centre imgCrop
            imgWhite[:, wGap:wCal+wGap] = imgResize

        # Width is greater
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgWhite[:, wGap:wCal+wGap] = imgResize
            #imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)  # Used to centre imgCrop
            imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

cv2.imshow("Image", img)

key = cv2.waitKey(1)

if key == ord("s"):  # Save imgWhite
    counter += 1  # Increment number of images taken
    if counter > maxImg:
        print((counter % maxImg), "Press R for next letter.")  # maxImg reached
    else:
        folder = "Data/" + letters[letters_index]  # Current directory
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)  # Save imgWhite
        print(letters[letters_index], counter)  # Current letter

if key == ord("r"):  # Change folder
    counter = 0  # Reset number of images taken
    letters_index += 1  # Move onto next letter
    print("Folder changed to", letters[letters_index])
