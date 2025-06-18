import tensorflow
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras import models, layers
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib as plt
from cnn_model import create_model

def train_model():
    # Load the data
    (train_image, train_label), (test_image, test_label) = mnist.load_data()

    # Normalize the images
    train_image = train_image.reshape((60000, 28*28))
    train_image = train_image.astype('float32') / 255
    
    test_image = test_image.reshape((10000, 28*28))
    test_image = test_image.astype('float32') / 255
    
    # Initialize the network
    network = create_model()
    network.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    
    # Encode the labels into categoricals
    train_label = to_categorical(train_label)
    test_label = to_categorical(test_label)

    # Train the model
    network.fit(train_image, train_label, epochs=5, batch_size = 32)

    # Test it on the test images
    test_loss, test_acc = network.evaluate(test_image, test_label)
    print('test_acc:', test_acc)

    # Save the model
    network.save("cnn_model.keras")

def main():
    train_model()

if __name__ == '__main__':
    main()
    

