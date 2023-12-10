# Hand Gesture Recognition

## Files and Directories
- **data_maker.py**: Allows users to capture image data and store it in the dataset
- **data_prep.py**: Preprocesses the image data for the CNN model and split into training and test data
- **cap_model.py**: Contains the CNN model
- **caption_maker.py**: Uses the trained model to perform real-time hand gesture recognition and captioning.
- **trained_model/**: Directory containing the trained CNN model.
- **dataset/**: Directory containing the captured hand gesture images.

## Getting Started
### Option 1: Direct Hand Gesture Recognition

Directly run caption_maker.py.
    
    python caption_maker.py

This uses the given trained_model that was trained using dataset: https://www.kaggle.com/datasets/muhammadkhalid/sign-language-for-numbers
as well as images captured by author (me). 

Make gestures inside the region of interest (green box) to view the gesture recognition and captioning at work!

### Option 2: Capture your own dataset

Run data_maker.py
    
    python data_maker.py

- Press a button 0-9 to capture that gesture.
- Make gesture inside the region of interest (green box)
- Press 'c' on keyboard to capture the image. 
- Ensure to capture several images in each number category to get a varied dataset
- Press 'q' to quit the window.
- Rerun data_maker.py to choose another gesture number to capture

###
Optional:
-----
If you want to increase the size of dataset 
- First delete the already existing dataset folder if there is any in your project folder. 
- Then download the dataset from https://www.kaggle.com/datasets/muhammadkhalid/sign-language-for-numbers to your project directory. 
- Change the name from "Sign Language for Numbers" to "dataset"
- Delete the "unknown" folder inside the dataset folder. 
- Now your captured images will add onto the existing dataset.
-----

###

Run data_prep.py

    python data_prep.py

This will preprocess the data and split it into training and testing datasets.

**Delete the given trained_model folder.**

Run cap_model.py

    python cap_model.py

This will create the new trained_model using the dataset captured

Run caption_maker.py

    python caption_maker.py

Make gestures inside the region of interest (green box) to view the gesture recognition and captioning at work!
