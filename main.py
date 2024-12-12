import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import random

cap = cv2.VideoCapture(0)  # Initialise video capture
detector = HandDetector(maxHands=1)  # Initialise HandDetector object
classifier = Classifier("Model/model.h5", "Model/labels.txt")

# Constants
offset = 20  # Expand bounding box
imgSize = 300  # Image dimensions

# Words
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O",
          "P", "Q", "R", "S", "T", "U", "V", "W",
          "X", "Y"]
wordsFile = "words.txt"

modelAccuracy = 0
currentWordIndex = 0
currentLetterIndex = 0
instructionSetConstant = 0

# Functions
def get_prediction(imgWhite):  # Retrieve model prediction, and index
    modelPrediction, modelIndex = classifier.getPrediction(imgWhite)
    return modelPrediction, modelIndex

def words_list(wordsFile):  # Put words into a List
    wordsList = []
    with open(wordsFile) as file:
        for line in file:
            wordsList.append(line.strip())
    return wordsList

def last_word(currentWordIndex, words):
    if currentWordIndex == len(words):  # Check if there are no words left
        currentWordIndex = 0  # Go back to initial word
    return currentWordIndex

while True:
    success, img = cap.read()  # Capture frame from camera
    imgOutput = img.copy()  # Main display
    hands, img = detector.findHands(img)  # Detect hands and annotate the frame
    
    # ASL Setup
    words = words_list(wordsFile)  # Place all words into a list
    currentWord = list(words[currentWordIndex])  # Split currentWord into individual letters
    currentLetter = currentWord[currentLetterIndex]
    
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # Getting bounding box information
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255  # Image background
    
        imgCropShape = imgCrop.shape
    
        # Image fitting
        aspectRatio = h / w
    
        if (0 < (x - offset) < 320) and ((y - offset) > 0):  # Prevents error when x/y coordinates are negative
    
            # Height is greater
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))  # Resize imgCrop
                # imgResizeShape = imgResize.shape  # Retrieve shape of imgResize
                wGap = math.ceil((imgSize - wCal) / 2)  # Used to centre imgCrop
                imgWhite[:, wGap:wCal + wGap] = imgResize
                prediction, index = get_prediction(imgWhite)
    
                # Bounding box
                cv2.rectangle(imgOutput, (x - offset - 2, y - offset - 30), (x + w + 22, y - offset), (255, 0, 255), cv2.FILLED)
                cv2.putText(imgOutput, labels[index], (x - 17, y - 23), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 3)
    
            # Width is greater
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))  # Resize imgCrop
                # imgResizeShape = imgResize.shape  # Retrieve shape of imgResize
                hGap = math.ceil((imgSize - hCal) / 2)  # Used to centre imgCrop
                imgWhite[hGap:hCal + hGap, :] = imgResize
                prediction, index = get_prediction(imgWhite)
    
                # Bounding box
                cv2.rectangle(imgOutput, (x - offset - 2, y - offset - 30), (x + w + 22, y - offset), (255, 0, 255), cv2.FILLED)
                cv2.putText(imgOutput, labels[index], (x - 17, y - 23), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 3)

            modelAccuracy = prediction[index]

          print(prediction[index], labels[index])

          # ASL Alphabet Learning
          letter = labels[index]  # Model letter prediction
          
          print(words[currentWordIndex], currentWordIndex)
          print(letter, currentLetter, currentLetterIndex)
          
          if currentLetter == letter:  # Check if model's prediction matches with currentLetter
              if currentLetterIndex >= (len(currentWord) - 1):  # Check if currentLetter reaches end of currentWord
                  currentWordIndex += 1  # Move onto next word in the list
                  currentLetterIndex = 0  # First letter of new word
                  currentWordIndex = last_word(currentWordIndex, words)
              else:
                  currentLetterIndex += 1  # Move onto next letter in currentWord
          
          if ((x - offset) > 320) or ((x - offset) < 0) or ((y - offset) < 0):  # Hand is not visible
              modelAccuracy = 0
    else:
        modelAccuracy = 0

# Model Accuracy
cv2.putText(imgOutput, str(modelAccuracy * 100)[:4] + "%", (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

# GUI
cv2.rectangle(imgOutput, (400, 0), (1000, 1000), (179, 227, 255), cv2.FILLED)

# Background
cv2.putText(imgOutput, currentLetter, (485, 153), cv2.FONT_HERSHEY_PLAIN, 7, (146, 32, 117), 7)  # currentLetter
cv2.putText(imgOutput, words[currentWordIndex], (419, 280), cv2.FONT_HERSHEY_PLAIN, 4, (146, 32, 117), 4) # currentWord
# Skip Instructions
cv2.putText(imgOutput, "Press (L) to move", (444, 175), cv2.FONT_HERSHEY_PLAIN, 1, (51, 3, 41), 1)
cv2.putText(imgOutput, "onto next letter.", (450, 195), cv2.FONT_HERSHEY_PLAIN, 1, (51, 3, 41), 1)
cv2.putText(imgOutput, "Press (W) to move", (440, 330), cv2.FONT_HERSHEY_PLAIN, 1, (51, 3, 41), 1)
cv2.putText(imgOutput, "onto next word.", (450, 350), cv2.FONT_HERSHEY_PLAIN, 1, (51, 3, 41), 1)

# Instructions
if len(hands) == 0 and instructionSetConstant == 0:  # Display initial message
    cv2.putText(imgOutput, "Place hand in front of", (425, 415), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    cv2.putText(imgOutput, "camera to begin.", (450, 435), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
elif len(hands) == 0:  # Display message if no hands are detected
    cv2.putText(imgOutput, "Place hand in front", (434, 415), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    cv2.putText(imgOutput, "of camera.", (475, 435), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
elif hands:
    instructionSetConstant = 1  # Change instructionSetConstant so that initial message can no longer be displayed
    hand = hands[0]
    x, y, w, h = hand['bbox']  # Getting bounding box information
    if (x - offset) > 320:  # Inform user to move hand to the left
        cv2.putText(imgOutput, "Move hand on the left", (425, 415), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
        cv2.putText(imgOutput, "hand side of the screen.", (415, 435), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    prediction, index = get_prediction(imgWhite)
    if currentLetter == labels[index]:
        randomMessage = random.randint(0, 1)  # Display random message
        if randomMessage == 1:
            cv2.putText(imgOutput, "Well Done!", (477, 425), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
        else:
            cv2.putText(imgOutput, "Correct!", (480, 425), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

cv2.imshow("Fingerspelling Recognition Software", imgOutput)

key = cv2.waitKey(1)

# Skip Letter
if key == ord("l"):
    print(currentLetter, "is skipped.")
    if currentLetterIndex >= (len(currentWord) - 1):  # Check if currentLetter reaches end of currentWord
        currentWordIndex += 1  # Move onto next word in the list
        currentLetterIndex = 0  # First letter of new word
        currentWordIndex = last_word(currentWordIndex, words)
    else:
        currentLetterIndex += 1  # Increment Letter

# Skip Word
if key == ord("w"):
    print(words[currentWordIndex], "is skipped.")
    currentLetterIndex = 0  # First letter of new word
    currentWordIndex = last_word(currentWordIndex + 1, words)
