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

# 4.build the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 5.compile and train the model
model.compile(optimizer='rmsprop', # good for CNNs(other options: adam, sgd)
              loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

# 6. Train the model
history = model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=64, #fasrter training
    validation_data=(X_test, y_test),
    verbose=1 #show progress bar
)

# 7 Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print("Test accuracy:", round(test_acc * 100, 2), "%")

# 8. Predict example
prediction = model.predict(X_test[:1]) # Predict the first test image
predicted_label = prediction.argmax() # Get the index of the highest probability

plt.imshow(X_test[0].reshape(28, 28), cmap='gray')
plt.title("Prediction:" + str(predicted_label))
plt.axis('off')
plt.show()

