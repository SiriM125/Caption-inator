#cap_model.py

"""
Module to create and train the model to classify images 
"""
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

train_data = np.load('train_data.npy')  #load training data
test_data = np.load('test_data.npy')    #load test data
train_labels = np.load('train_labels.npy')  #load training labels
test_labels = np.load('test_labels.npy')    #load test labels

#CNN Model
model = models.Sequential() #keras Sequential model
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

#compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


#train model
model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_data=(test_data, test_labels))

#save model
model.save('trained_model')  
