# Sign Language Fingerspelling Recognition System

A simple, camera-based ASL fingerspelling recognition and learning environment.  
This repo contains data collection helpers, a dataset organiser, a training script for a CNN classifier, and a lightweight real-time app that detects a hand, draws a bounding box, and shows the predicted letter with a confidence score.

---

## Brief Project Flow - TL;DR
- Capture many labelled images of your hand using `dataCollection.py` (300 images per letter by default). Images are saved as 300×300 jpgs.  
- Run `folderSort.py` to split the collected images into `train/`, `validation/` and `test/` using an 80/10/10 split.  
- Train a CNN classifier using `trainClassifier.py` (Keras `ImageDataGenerator` for augmentation + training). Produces `model.h5`.  
- Run `main.py` to start the live recognition GUI. The app uses a hand detector to localise the hand, crops and normalises the hand image, gets a prediction from the classifier, then draws the bounding box, label and confidence on the frame.

<img width="956" height="763" alt="Image" src="https://github.com/user-attachments/assets/d19e8bef-a306-403c-ab53-2e465931ed28" />

## Dataset & Collection Notes
- `dataCollection.py` captures images from a webcam. Press `s` to save a labelled image and `r` to advance to the next letter folder. Default target is **300 images per letter** saved to `Data/<LETTER>/`.  
- `folderSort.py` moves images into `Data/train/<LETTER>/`, `Data/validation/<LETTER>/` and `Data/test/<LETTER>/` using an 80/10/10 split (for example 240 train / 30 val / 30 test per letter at 300 images per letter).

## Data Processing & Model Summary
- Input flow: capture frame -> detect hand -> crop to bounding box -> resize to classifier input size (300×300) -> classifier predicts letter + confidence -> overlay results on GUI.  
- Training uses `tensorflow.keras.preprocessing.image.ImageDataGenerator` with augmentation (rotation, shifts, shear, zoom, horizontal flip) and rescales to [0,1]. Target size is 300×300.  
- The trained model is saved as `model.h5`. `labels.txt` and `words.txt` support mapping and practice words.

## Tests & success criteria
- System tested across common scenarios. Most static letters are correctly classified in controlled lighting. 
- The app is tolerant of moderate motion blur and handles multiple hands by selecting the strongest detection.

## Known Limitations
- Letters that require motion, such as `J` and `Z`, are not reliably classified by a static-image classifier. These are currently exceptions.
- Project focuses on ASL fingerspelling only and does not attempt full sign language recognition. Full sign recognition requires facial expression and body modelling plus much more data.
- Accuracy is sensitive to lighting, background and hand distance to the camera. See the documentation for suggested thresholds and workarounds.

## Future work ideas
- Add temporal modelling to handle motion letters `J` and `Z`.
- Integrate a continuous decoder so full words and phrases can be detected instead of single letters
- Build a plugin for web conferencing to offer live translation in meetings, subject to privacy considerations.
