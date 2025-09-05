# Sign Language Fingerspelling Recognition System 🤟📷

*Real-time ASL fingerspelling recognition and interactive learning tool*

This software uses a webcam to detect and classify American Sign Language (ASL) fingerspelling gestures in real time. It provides an interactive learning environment where users can practise spelling words and receive instant feedback. The system is built using Python, OpenCV, TensorFlow, and CVZone for hand tracking and classification.

---

## 🔬 Brief Project Flow 📝

The system captures hand gestures via webcam, processes the images, and uses a trained convolutional neural network (CNN) to classify the ASL letter. The GUI provides real-time feedback, instructional messages, and a structured learning experience.

---

## 📸 Dataset Collection

1. **Data Capture**:
   - Used a custom Python script (`dataCollection.py`) to capture hand images for each ASL letter (excluding J and Z due to movement requirements)
   - Images were cropped, resized to 300x300 pixels, and centered on a white background
   - 300 images per letter were collected (total 7,200 images)

2. **Data Splitting**:
   - Dataset split into 80% training, 10% validation, and 10% test sets using a custom sorting script (`folderSort.py`)

---

## 🧠 Model Training

- **Architecture**: CNN with Conv2D, MaxPooling2D, Flatten, Dense, and Dropout layers
- **Training**: Used TensorFlow/Keras with data augmentation (rotation, shifts, shear, zoom, flip)
- **Performance**: Achieved **95.33% test accuracy** after hyperparameter tuning and dataset refinement
- **Output**: Model saved as `model.h5` for real-time inference

---

## 🖥️ GUI and Interactive Learning

- **Real-Time Feedback**: Displays recognised letter, accuracy percentage, and instructional messages
- **Word Practice**: Users spell words from a predefined list (`words.txt`), progressing letter-by-letter
- **Skip Functionality**: Press `L` to skip a letter, `W` to skip a word
- **GUI Design**: Clean interface with colour-coded elements (HEX: #FFE3B3 background, #752092 text)
- **Instructions**: Contextual prompts guide hand placement and provide positive reinforcement

---

## 🛠️ Technical Setup

- **Languages**: Python 3.9
- **Libraries**: OpenCV, CVZone, MediaPipe, TensorFlow, NumPy
- **Hardware**: Webcam (720p+), Windows 10/11, Intel Core i3+
- **Key Files**:
  - `main.py` – Main application
  - `trainClassifier.py` – Model training
  - `dataCollection.py` – Image capture
  - `folderSort.py` – Dataset organisation

---

## ✅ Features

- Real-time hand detection and bounding box tracking
- Live accuracy feedback and letter prediction
- Interactive word-based learning with skip options
- Customisable word list via `words.txt`
- Responsive GUI with instructional messages

---

## 📚 References

- Inspired by existing solutions like [fingerspelling.xyz](https://fingerspelling.xyz)
- Uses CVZone HandTracker and Classifier modules
- Built with TensorFlow for CNN-based classification

---

## 🔮 Future Improvements

- Support for dynamic signs (e.g., J, Z)
- Multi-hand detection
- Integration with video conferencing tools
- Expanded sign language support (BSL, ISL, etc.)

---

*This project was developed as part of the OCR A-Level Computer Science NEA.*
*Refer to the full documentation above for detailed analysis, design, and testing.*
