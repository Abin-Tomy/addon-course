import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# 1.load dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2.normalize data(scale pixel values to [0, 1])
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# 3.Reshape data (CNN expects 3D input: height, width, channels)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
