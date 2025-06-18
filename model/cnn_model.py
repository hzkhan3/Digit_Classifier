import tensorflow
from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras import layers

def create_model():
    # Create the model architecture
    network = models.Sequential()
    network.add(layers.Dense(512, activation="relu", input_shape = (28*28, )))
    network.add(layers.Dense(10, activation = "softmax"))

    return network



