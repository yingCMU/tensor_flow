# https://keras.io/layers/convolutional/#cropping2d
# Keras provides the Cropping2D layer for image cropping within the model. This is relatively fast, because the model is parallelized on the GPU, so many images are cropped simultaneously.
#
# By contrast, image cropping outside the model on the CPU is relatively slow.
#
# Also, by adding the cropping layer, the model will automatically crop the input images when making predictions in drive.py.
#
# The Cropping2D layer might be useful for choosing an area of interest that excludes the sky and/or the hood of the car.
from keras.models import Sequential, Model
from keras.layers import Cropping2D
import cv2

# set up cropping2D layer
model = Sequential()
# cropping:
# 50 rows pixels from the top of the image
# 20 rows pixels from the bottom of the image
# 0 columns of pixels from the left of the image
# 0 columns of pixels from the right of the image
model.add(Cropping2D(cropping=((50,20), (0,0)), input_shape=(3,160,320)))
#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
	for pe in p:
	    if pe == Z:
	        q.append(pHit * pe)
	    else:
	        q.append(pMiss * pe)
    return q

print sense(p,Z)
