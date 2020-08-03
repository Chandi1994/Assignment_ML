# -*- coding: utf-8 -*-
"""1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q6patYZg4ZNSWPkoCn4oZzJRhGy74zjc

# Import Libraries
"""

from keras import models, layers
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import numpy as np

"""# Loading dataset"""

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train.shape, x_test.shape

_, ax = plt.subplots(1, 20, figsize=(10,10))

for i in range(0, 20):
    ax[i].axis('off')
    ax[i].imshow(x_train[i], cmap=plt.cm.binary)

"""# Data Preprocessing"""

# reshape dataset to have a single channel
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

#target values
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# convert from integers to floats
x_train= x_train.astype('float32')
x_test= x_test.astype('float32')

# rescale pixel values from range [0, 255] to [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

"""# Build the neural network"""

# Building the model
model = models.Sequential()

# 3 convolutional layers
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# 1 hidden layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

# The output layer with 10 neurons, for 10 classes
model.add(layers.Dense(10, activation='softmax'))

# Compiling the model using some basic parameters
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=64)

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Accuracy:', test_acc)
print('Loss: ', test_loss)

model.summary()