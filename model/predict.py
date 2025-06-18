from train_model import train_model
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

def predict_digit(image):
    # Extract file extension from the input path
    filename, file_extension = os.path.splitext(image)
    image_extension = [".jpeg", "jpeg", ".png"]
    
    # Check if the image file has the supported extensions
    if file_extension in image_extension:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        print("File type not accepted")

    # Resize the image to be 28 x 28 pixels for the CNN
    image = cv2.resize(image, (28, 28))

    # Invert the colors so that it is white on black background
    image = 255 - image

    # Normalize the image
    image =  image.astype('float32') / 255

    # Reshape the image in the correct format for the model
    image = image.reshape(1, (28*28))

    # Load the model
    loaded_model = load_model("cnn_model.keras")

    # Predict the digit
    prediction = loaded_model.predict(image)

    # Extract the predicted digit and the confidence 
    predicted_digit = np.argmax(prediction)
    confidence = round(float(np.max(prediction)) * 100, 2)

    return predicted_digit, confidence



