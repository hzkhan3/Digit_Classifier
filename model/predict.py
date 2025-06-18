from train_model import train_model
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from PIL import Image, ImageOps
import os

def predict_digit(image):
    # Check if the image is a pillow image
    if not isinstance(image, Image.Image):
        raise ValueError("Input must be a PIL Image")
    
    # Convert to grayscale
    image = ImageOps.grayscale(image)

    # Resize to 28x28
    image = image.resize((28, 28))

    # Invert the image (white digit on black background)
    image = ImageOps.invert(image)

    # Convert to NumPy array and normalize
    image = np.array(image).astype('float32') / 255.0

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



