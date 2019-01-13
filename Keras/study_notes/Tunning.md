## testing
python drive.py model.h5
## Validating Your Network
In order to validate your network, you'll want to compare model performance on the training set and a validation set. The validation set should contain image and steering data that was not used for training. A rule of thumb could be to use 80% of your data for training and 20% for validation or 70% and 30%. Be sure to randomly shuffle the data before splitting into training and validation sets.

If model predictions are poor on both the training and validation set (for example, mean squared error is high on both), then this is evidence of underfitting. Possible solutions could be to

- increase the number of epochs
- add more convolutions to the network.
When the model predicts well on the training set but poorly on the validation set (for example, low mean squared error for training set, high mean squared error for validation set), this is evidence of overfitting. If the model is overfitting, a few ideas could be to

- use dropout or pooling layers
- use fewer convolution or fewer fully connected layers
- collect more data or further augment the data set
Ideally, the model will make good predictions on both the training and validation sets. The implication is that when the network sees an image, it can successfully predict what angle was being driven at that moment.

## Data preprocessing
Lambda layers(https://keras.io/layers/core/#lambda) lambda layers can be used to create arbitrary functions that operate on each image as it passes through the layer. (normalization)
## More networks
Try more powerfull networks
## Data augmentation
1. more data to train the network
2. training data is more comprehensive
for example, A effective technique for helping with the left turn bias involves flipping images and taking the opposite sign of the steering measurement. For example:
## using multiple cameras
1. there is simply more data
2. it will teach the car to pull back to center when it is drifting
So in a real car, we’ll have multiple cameras on the vehicle, and we’ll map recovery paths from each camera. For example, if you train the model to associate a given image from the center camera with a left turn, then you could also train the model to associate the corresponding image from the left camera with a somewhat softer left turn. And you could train the model to associate the corresponding image from the right camera with an even harder left turn.
[paper](http://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf)


steps:
1. First train a model with easy network, one flattern layer: car is circling around all the time, barly move
6428/6428 [==============================] - 5s - loss: 20688658.5851 - val_loss: 80256.2745
Epoch 2/7
6428/6428 [==============================] - 5s - loss: 117490.2840 - val_loss: 10319.2003
Epoch 3/7
6428/6428 [==============================] - 5s - loss: 4566.0299 - val_loss: 3351.1434
Epoch 4/7
6428/6428 [==============================] - 5s - loss: 3044.8197 - val_loss: 2790.9011
Epoch 5/7
6428/6428 [==============================] - 5s - loss: 2602.0454 - val_loss: 2944.8986
Epoch 6/7
6428/6428 [==============================] - 5s - loss: 2272.7446 - val_loss: 2542.3872
Epoch 7/7
6428/6428 [==============================] - 5s - loss: 1980.2080 - val_loss: 2336.9403
2. Run autonomous driving with network to confirm it is working
3. normalize the image pixel: after this car already driving in track, out of track sometimes
6428/6428 [==============================] - 6s - loss: 2.4140 - val_loss: 0.2066
Epoch 2/7
6428/6428 [==============================] - 5s - loss: 0.1823 - val_loss: 0.0924
Epoch 3/7
6428/6428 [==============================] - 5s - loss: 0.0649 - val_loss: 0.0459
Epoch 4/7
6428/6428 [==============================] - 5s - loss: 0.0404 - val_loss: 0.0463
Epoch 5/7
6428/6428 [==============================] - 5s - loss: 0.0321 - val_loss: 0.0681
Epoch 6/7
6428/6428 [==============================] - 5s - loss: 0.0328 - val_loss: 0.0649
Epoch 7/7
6428/6428 [==============================] - 5s - loss: 0.0327 - val_loss: 0.0397
4. apply letnet to increase accuracy
6428/6428 [==============================] - 17s - loss: 5.9959 - val_loss: 0.0198
Epoch 2/7
6428/6428 [==============================] - 14s - loss: 0.0212 - val_loss: 0.0173
Epoch 3/7
6428/6428 [==============================] - 14s - loss: 0.0159 - val_loss: 0.0175
Epoch 4/7
6428/6428 [==============================] - 14s - loss: 0.0151 - val_loss: 0.0165
Epoch 5/7
6428/6428 [==============================] - 14s - loss: 0.0144 - val_loss: 0.0158
Epoch 6/7
6428/6428 [==============================] - 14s - loss: 0.0136 - val_loss: 0.0152
Epoch 7/7
6428/6428 [==============================] - 14s - loss: 0.0129 - val_loss: 0.0146
5. data augmentation: flip images
12857/12857 [==============================] - 37s - loss: 4.6942 - val_loss: 0.0178
Epoch 2/7
12857/12857 [==============================] - 34s - loss: 0.0162 - val_loss: 0.0154
Epoch 3/7
12857/12857 [==============================] - 34s - loss: 0.0153 - val_loss: 0.0149
Epoch 4/7
12857/12857 [==============================] - 34s - loss: 0.0146 - val_loss: 0.0141
Epoch 5/7
12857/12857 [==============================] - 34s - loss: 0.0128 - val_loss: 0.0130
Epoch 6/7
12857/12857 [==============================] - 34s - loss: 0.0110 - val_loss: 0.0127
Epoch 7/7
12857/12857 [==============================] - 34s - loss: 0.0101 - val_loss: 0.0131
