#data_maker.py
"""
Module to allow users to capture image data and store it in the dataset
"""

import cv2
import os
from tkinter import Tk, Button

current_gesture_label = None

script_directory = os.path.dirname(__file__)    #directory of the file

roi_x, roi_y, roi_width, roi_height = 100, 100, 500, 500    #region of interest

#new folder if folder does not already exist for dataset
def new_gesture_folder(data_path, gesture_label):
    gesture_folder = os.path.join(data_path, "dataset", str(gesture_label))
    os.makedirs(gesture_folder, exist_ok=True)
    return gesture_folder

#setting label for each category of gestures added
def set_gesture_label(label): 
    global current_gesture_label
    current_gesture_label = label
    root.destroy() 


def launch_tkinter():
    global root

    #window
    root = Tk()
    root.title("Capture Gestures")

    #number gesture buttons
    for i in range(10):
        label = str(i)
        button = Button(root, text=label, command=lambda l=label: set_gesture_label(l))
        button.pack(side="left")

    #cancel button
    cancel_button = Button(root, text="Cancel", command=root.destroy)
    cancel_button.pack(side="left")

    root.mainloop()


def capture_gesture(data_path):
    global current_gesture_label

    launch_tkinter()

    if current_gesture_label is None:   #if no button was clicked, cancel
        return

    #calling new_gesture_folder to create a new folder if there wasn't one already
    gesture_folder = new_gesture_folder(data_path, current_gesture_label)

    
    cap = cv2.VideoCapture(0)  #turn on camera and start capturing

    capturing = True
    frame_count = 0

    while capturing:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  #to mirror the camera

        cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)   #drawing roi on screen so user knows where to gesture

        cv2.imshow("Capture Gesture", frame)
        key = cv2.waitKey(1) & 0xFF

        #on clicking 'c', the image frame inside the roi will be captured and saved to the respective folder
        if key == ord('c'):
            frame_count += 1
            roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]
            image_path = os.path.join(gesture_folder, f"image{frame_count}.png")
            cv2.imwrite(image_path, roi)
        
        #on clicking 'q' the camera will cease to capture (will turn off)
        elif key == ord('q'):
            capturing = False

    cap.release()
    cv2.destroyAllWindows()


data_path = os.path.join(script_directory)  #specifying directory such that it can be accessed on any computer
capture_gesture(data_path)