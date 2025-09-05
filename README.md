_Real-time ASL fingerspelling recognition and interactive learning tool._

This software uses a webcam to detect and classify American Sign Language (ASL) fingerspelling gestures in real time. It provides an interactive learning environment where users can practise spelling words and receive instant feedback. The system is built using Python, OpenCV, TensorFlow, and CVZone for hand tracking and classification.

---

###🔬 Brief Project Flow 📝
The system captures hand gestures via webcam, processes the images, and uses a trained convolutional neural network (CNN) to classify the ASL letter. The GUI provides real-time feedback, instructional messages, and a structured learning experience.

---

📸 Dataset Collection
1. Data Capture:
  * Used a custom Python script (dataCollection.py) to capture hand images for each ASL letter (excluding J and Z due to movement requirements).
  * Images were cropped, resized to 300x300 pixels, and centered on a white background.
  * 300 images per letter were collected (total 7,200 images).
3. Data Splitting:
  * Dataset split into 80% training, 10% validation, and 10% test sets using a custom sorting script (folderSort.py).
