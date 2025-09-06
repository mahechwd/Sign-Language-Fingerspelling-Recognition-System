# Sign Language Fingerspelling Recognition System

## Real-time Recognition Demo

<img width="956" height="763" alt="Image" src="https://github.com/user-attachments/assets/c6e217b0-a33a-4674-893f-47f5e44e6d70" />

- This system uses computer vision to interpret sign language fingerspelling in real-time. The image shows continuous alphabet recognition with visual feedback.

## Project Overview

- Building a robust sign language recognition system requires accurate hand detection, feature extraction, and classification. This project implements a complete pipeline for recognizing fingerspelled letters in real-time.

- Refer to the [GitHub repo](https://github.com/mahechwd/Sign-Language-Fingerspelling-Recognition-System) for the complete code.

1. **Data Collection & Preprocessing **
   - 1.1 Collect hand gesture images using [MediaPipe](https://google.github.io/mediapipe/) for hand landmark detection and **OpenCV** for video processing.
   
   - 1.2 Create a diverse dataset covering various hand sizes, skin tones, and lighting conditions:
  
   ![Image](https://github.com/user-attachments/assets/0e19c589-4561-4bc2-88a2-31758a9687ec)
     
3. **Feature Extraction & Processing **
   - 2.1 **Landmark detection**: Use MediaPipe Hands to extract 3D hand landmarks (21 points per hand).
      ![](https://mediapipe.dev/images/mobile/hand_landmarks.png)
   
   - 2.2 **Feature engineering**: Calculate relative distances, angles, and positional features from landmarks.
   
   - 2.3 **Normalization**: Scale and rotate hand positions for orientation invariance.
   
   - 2.4 Each frame produces a feature vector representing hand configuration.

4. **Model Workflow**
   
 <img width="959" height="540" alt="Image" src="https://github.com/user-attachments/assets/05ffce64-f1e9-464e-b425-3715bb3ac0af" />

5. **Training Pipeline ☁️**
   - The system uses [TensorFlow](https://www.tensorflow.org/) for model training, with options for both cloud and local training environments.
   - Data augmentation techniques include rotation, scaling, and background variation to improve generalization.
   - Hyperparameter tuning performed using validation split and cross-validation techniques.

## Dataset Construction 

1. The **input features** are [hand_landmarks, relative_distances, angles]. The processed data contains normalized spatial information about hand configuration.

2. The **output labels** are [letter_class, confidence] representing recognized alphabet letters and prediction confidence scores.

3. **Data balancing** techniques applied to ensure equal representation of all letters in the alphabet.

4. **Temporal processing**: For continuous recognition, implement sliding window approach to analyze gesture sequences over time.

5. **System Workflow:**
   
   <img width="959" height="540" alt="Image" src="https://github.com/user-attachments/assets/ef74913f-2e40-486a-b7a5-5fc75d163c3f" />

The system prioritizes recent frames with higher weights while maintaining context from previous frames.

## Model Structure Discussion

0. **Architecture Overview**
   - The model combines spatial feature extraction with temporal context understanding for continuous recognition.

1. **Spatial Feature Extraction**
   - Use convolutional layers and fully connected networks to process hand landmark spatial relationships.
   - Implement attention mechanisms to focus on critical hand regions for different letters.

2. **Temporal Processing**
   - For continuous recognition, employ LSTM or Transformer layers to understand gesture sequences.
   - Implement sequence-to-sequence modeling for fluent fingerspelling recognition.

3. **Efficiency Optimizations**
   - Model pruning and quantization for real-time performance.
   - Hardware acceleration support for various deployment environments.

## Performance & Results

![Image](https://github.com/user-attachments/assets/e269bd91-a4fc-43d1-bd29-1128751557c6)

- Current model achieves 95.3% accuracy on test dataset
- Comparison with baseline models shows 11% improvement.

## Future Work and Summary
- The current model performs well but could benefit from additional training data and diversity.
- Future work includes expanding to complete sign language words and phrases.
- Mobile deployment optimization for accessibility applications.
- Multi-hand recognition for two-handed sign languages (extension to BSL).

## Applications
- Educational tools for sign language learning.
- Accessibility technology for hearing-impaired communication.
- Human-computer interaction interfaces.

## References
1. [MediaPipe Hands: On-device Real-time Hand Tracking](https://arxiv.org/abs/2006.10214)

_For more information please refer to the [documentation](https://github.com/mahechwd/Sign-Language-Fingerspelling-Recognition-System/blob/main/documentation.pdf)._
