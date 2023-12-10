#caption_maker.py

"""
Module to use the trained model to perform real-time hand gesture recognition and captioning. 
"""
import cv2 
import numpy as np
from tensorflow.keras.models import load_model
import os

script_directory = os.path.dirname(__file__)

model_path = os.path.join(script_directory, "trained_model")
model = load_model(model_path)  #load model

category_digit = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}   #specify which category is for which digit

cap = cv2.VideoCapture(0)   #camera on

#roi specification
roi_margin = 30
roi_x, roi_y, roi_width, roi_height = 100, 100, 500, 500

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)  #to mirror the camera

    roi = frame[roi_y - roi_margin:roi_height + roi_margin, roi_x - roi_margin:roi_width + roi_margin]

    roi = cv2.resize(roi, (64, 64)) #resizing images

    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)    #converting to grayscale
    normalized_roi = roi_gray / 255.0   #normalizing pixels
    input_roi = normalized_roi.reshape(-1, 64, 64, 1)
    prediction = model.predict(input_roi)   #using model to predict number

    predicted_class = np.argmax(prediction)
    predicted_digit = category_digit[predicted_class]

    cv2.putText(frame, f"Caption: {predicted_digit}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)    #captioning
    cv2.rectangle(frame, (roi_x - roi_margin, roi_y - roi_margin), (roi_x + roi_width + roi_margin, roi_y + roi_height + roi_margin), (0, 255, 0), 2)
    cv2.imshow('Hand Gesture Recognition', frame)

    #on clicking 'q' the window will close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
