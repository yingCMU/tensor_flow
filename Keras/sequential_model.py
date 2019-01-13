from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten

# https://keras.io/getting-started/sequential-model-guide/
# https://keras.io/models/sequential/
# https://github.com/keras-team/keras/blob/master/examples/mnist_mlp.py
# Layers
# A Keras layer is just like a neural network layer. There are fully connected layers, max pool layers, and activation layers.
# You can add a layer to the model using the model's add() function. For example, a simple model would look like this:
# a wrapper for the neural network model. It provides common functions like fit(), evaluate(), and compile().
# Create the Sequential model
# Create the Sequential model
model = Sequential()

#1st Layer - Add a flatten layer
# Keras will automatically infer the shape of all layers after the first layer. This means you only have to set the input dimensions for the first layer.
#sets the input dimension to (32, 32, 3) and output dimension to (3072=32 x 32 x 3)
model.add(Flatten(input_shape=(32, 32, 3)))

#2nd Layer - Add a fully connected layer
#takes in the output of the first layer and sets the output dimensions to (100)
model.add(Dense(100))

#3rd Layer - Add a ReLU activation layer
model.add(Activation('relu'))

#4th Layer - Add a fully connected layer
model.add(Dense(60))

#5th Layer - Add a ReLU activation layer
model.add(Activation('relu'))


model.compile(loss = 'mse', optimizer = 'adam')
model.fit(X_train, y_train, validation_split= 0.2, shuffle = true)
model.save('model.h5')
