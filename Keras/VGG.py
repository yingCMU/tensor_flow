from glob import glob
from keras.applications.vgg16 import VGG16, decode_predictions
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
# https://keras.io/applications/#vgg16
# There are two arguments to VGG16 in this example, although there could be more or less
# (check out the linked documentation to see other possible arguments).
# The first, weights='imagenet', loads the pre-trained ImageNet weights.
# This is actually the default argument per the documentation,
#  so if you don't include it, you should still be loading the ImageNet weights.
#  However, you can also specify None here to get random weights if you just want
#  the architecture of VGG16; this is not suggested here since you won't get the benefit of transfer learning.

# The argument include_top is for whether you want to include the fully-connected layer at the top of the network;
# unless you are actually trying to classify ImageNet's 1,000 classes,
# you likely want to set this to False and add your own additional layer for the output you desire.
model = VGG16(weights='imagenet', include_top=False)# without pre-trained weights: weights=None

# Pre-processing for ImageNet weights
# There is another item to consider before jumping into using an ImageNet pre-trained model.
# These networks are typically pre-trained with a specific type of pre-processing,
# so you need to make sure to use the same pre-processing steps,
# or your network's outputs will likely be erratic. VGG uses 224x224 images as input, so that's another thing to consider.
image_paths = glob('images/*.jpg')

i = 2 # Can change this to your desired image to test
img_path = image_paths[i]
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Perform inference on our pre-processed image
predictions = model.predict(x)

# Check the top 3 predictions of the model, use of decode_predictions which will map the prediction to the class name.
print('Predicted:', decode_predictions(predictions, top=3))
