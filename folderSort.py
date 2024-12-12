import os
import shutil

mainDirectory = "Data/"  # Base directory path
subDirectories = ["train", "validation", "test"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O",
           "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]

# Create train, validation, and test directories
for subDirectory in subDirectories:
    for letter in letters:
        dir_path = os.path.join(mainDirectory, subDirectory, letter)
        
        if not os.path.exists(dir_path):  # If path doesn't exist, create it
            os.makedirs(dir_path)

# Distribute images into train, validation, and test sets
def split_data(letter, images):
    numImg = len(images)
    # Calculate splits (limits):
    trainSplit = int(0.8 * numImg)  # (80% train)
    validationSplit = int(0.9 * numImg)  # (10% validation)
    # Test split is implicitly the remaining images  # (10% test)

    # Split the images
    trainImages = images[:trainSplit]
    validationImages = images[trainSplit:validationSplit]
    testImages = images[validationSplit:]

    # Move images to directory
    def move_images(images, destinationDirectory):
        for img in images:
            shutil.move(img, os.path.join(mainDirectory, destinationDirectory, letter))

    # Move images to respective directories
    move_images(trainImages, "train")
    move_images(validationImages, "validation")
    move_images(testImages, "test")

# Iterate over each letter and process the images
for letter in letters:
    letterPath = os.path.join(mainDirectory, letter)
    if os.path.exists(letterPath):  # Check if the letter directory exists
        # List all files in the letter directory and get their full paths
        images = [os.path.join(letterPath, img) for img in os.listdir(letterPath) 
                  
if os.path.isfile(os.path.join(letterPath, img))]
      split_data(letter, images)
      shutil.rmtree(letterPath)  # Remove the original path after moving all the images

print("Done")
