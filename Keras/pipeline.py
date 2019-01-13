from keras.models import Sequential, Model
from keras.layers import Lambda
# <!-- In Keras, lambda layers can be used to create arbitrary functions that operate on each image as it passes through the layer.
#
# In this project, a lambda layer is a convenient way to parallelize image normalization. The lambda layer will also ensure that the model will normalize input images when making predictions in drive.p -->
# set up lambda layer
model = Sequential()
model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160,320,3)))
...
