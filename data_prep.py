#data_prep.py
"""
Module to preprocess the image data and split into training and test data
"""
import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer


dataset_path = 'dataset'  
images = []
labels = []

#to load the images and labels separately
def load_images_and_labels(dataset_path):
    for gesture_label in os.listdir(dataset_path):
        label = int(gesture_label) 
        gesture_folder_path = os.path.join(dataset_path, gesture_label)

        for filename in os.listdir(gesture_folder_path):
            image_path = os.path.join(gesture_folder_path, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)    #grayscale conversion
            image = cv2.resize(image, (64, 64))  #resizing images
            image = image / 255.0   #normalizing images

            images.append(image)    #adding to images
            labels.append(label)    #adding to labels

load_images_and_labels(dataset_path)

#making them into numpy arrays
images = np.array(images)  
labels = np.array(labels)

#to turn labels into binary
label_binarizer = LabelBinarizer()
labels = label_binarizer.fit_transform(labels)

#split data into training and test data
train_data, test_data, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42, shuffle=True)

print("Train data shape:", train_data.shape)
print("Test data shape:", test_data.shape)
print("Train labels shape:", train_labels.shape)
print("Test labels shape:", test_labels.shape)

np.save('train_data.npy', train_data)
np.save('test_data.npy', test_data)
np.save('train_labels.npy', train_labels)
np.save('test_labels.npy', test_labels)