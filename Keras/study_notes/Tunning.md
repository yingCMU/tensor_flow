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

## Cropping Images in Keras(avoid distraction)
he cameras in the simulator capture 160 pixel by 320 pixel images.

Not all of these pixels contain useful information, however. In the image above, the top portion of the image captures trees and hills and sky, and the bottom portion of the image captures the hood of the car.

Your model might train faster if you crop each image to focus on only the portion of the image that is useful for predicting a steering angle.
## collecting more data
### Recovery Laps
If you drive and record normal laps around the track, even if you record a lot of them, it might not be enough to train your model to drive properly.

Here’s the problem: if your training data is all focused on driving down the middle of the road, your model won’t ever learn what to do if it gets off to the side of the road. And probably when you run your model to predict steering measurements, things won’t go perfectly and the car will wander off to the side of the road at some point.

So you need to teach the car what to do when it’s off on the side of the road.

One approach might be to constantly wander off to the side of the road and then steer back to the middle.

A better approach is to only record data when the car is driving from the side of the road back toward the center line.

So as the human driver, you’re still weaving back and forth between the middle of the road and the shoulder, but you need to turn off data recording when you weave out to the side, and turn it back on when you steer back to the middle.
### Driving Counter-Clockwise
Track one has a left turn bias. If you only drive around the first track in a clock-wise direction, the data will be biased towards left turns. One way to combat the bias is to turn the car around and record counter-clockwise laps around the track. Driving counter-clockwise is also like giving the model a new track to learn from, so the model will generalize better.

### Using Both Tracks
If you end up using data from only track one, the convolutional neural network could essentially memorize the track. Consider using data from both track one and track two to make a more generalized model.

### Collecting Enough Data
How do you know when you have collected enough data? Machine learning involves trying out ideas and testing them to see if they work. If the model is over or underfitting, then try to figure out why and adjust accordingly.

Since this model outputs a single continuous numeric value, one appropriate error metric would be mean squared error. If the mean squared error is high on both a training and validation set, the model is underfitting. If the mean squared error is low on a training set but high on a validation set, the model is overfitting. Collecting more data can help improve a model when the model is overfitting.

What if the model has a low mean squared error on both the training and validation sets, but the car is falling off the track?

Try to figure out the cases where the vehicle is falling off the track. Does it occur only on turns? Then maybe it's important to collect more turning data. The vehicle's driving behavior is only as good as the behavior of the driver who provided the data.

Here are some general guidelines for data collection:

two or three laps of center lane driving
one lap of recovery driving from the sides
one lap focusing on driving smoothly around curves


write-up steps:
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
6. cropping images: remove top 70 (tree, sky) and bottom 25 (car)
12857/12857 [==============================] - 23s - loss: 0.6066 - val_loss: 0.0155
Epoch 2/7
12857/12857 [==============================] - 17s - loss: 0.0151 - val_loss: 0.0145
Epoch 3/7
12857/12857 [==============================] - 17s - loss: 0.0143 - val_loss: 0.0137
Epoch 4/7
12857/12857 [==============================] - 17s - loss: 0.0136 - val_loss: 0.0131
Epoch 5/7
12857/12857 [==============================] - 18s - loss: 0.0128 - val_loss: 0.0126
Epoch 6/7
12857/12857 [==============================] - 17s - loss: 0.0121 - val_loss: 0.0122
Epoch 7/7
12857/12857 [==============================] - 17s - loss: 0.0114 - val_loss: 0.0119
7. use dropout:
 [first dropout layer(before maxpooling):
12857/12857 [==============================] - 20s - loss: 0.3226 - val_loss: 0.0161
Epoch 2/7
12857/12857 [==============================] - 18s - loss: 0.0149 - val_loss: 0.0151
Epoch 3/7
12857/12857 [==============================] - 18s - loss: 0.0134 - val_loss: 0.0139
Epoch 4/7
12857/12857 [==============================] - 19s - loss: 0.0122 - val_loss: 0.0130
Epoch 5/7
12857/12857 [==============================] - 18s - loss: 0.0113 - val_loss: 0.0124
Epoch 6/7
12857/12857 [==============================] - 18s - loss: 0.0105 - val_loss: 0.0119
Epoch 7/7
12857/12857 [==============================] - 18s - loss: 0.0099 - val_loss: 0.0118
[2nd run]:
12857/12857 [==============================] - 21s - loss: 0.0892 - val_loss: 0.0139
Epoch 2/7
12857/12857 [==============================] - 19s - loss: 0.0120 - val_loss: 0.0120
Epoch 3/7
12857/12857 [==============================] - 19s - loss: 0.0108 - val_loss: 0.0114
Epoch 4/7
12857/12857 [==============================] - 19s - loss: 0.0103 - val_loss: 0.0113
Epoch 5/7
12857/12857 [==============================] - 19s - loss: 0.0099 - val_loss: 0.0115
Epoch 6/7
12857/12857 [==============================] - 18s - loss: 0.0097 - val_loss: 0.0117
Epoch 7/7
12857/12857 [==============================] - 19s - loss: 0.0096 - val_loss: 0.0114
(first dropout layer(after ma pooling))
12857/12857 [==============================] - 20s - loss: 0.5994 - val_loss: 0.0164
Epoch 2/7
12857/12857 [==============================] - 18s - loss: 0.0148 - val_loss: 0.0152
Epoch 3/7
12857/12857 [==============================] - 18s - loss: 0.0136 - val_loss: 0.0145
Epoch 4/7
12857/12857 [==============================] - 18s - loss: 0.0127 - val_loss: 0.0139
Epoch 5/7
12857/12857 [==============================] - 18s - loss: 0.0118 - val_loss: 0.0135
Epoch 6/7
12857/12857 [==============================] - 18s - loss: 0.0112 - val_loss: 0.0131
Epoch 7/7
12857/12857 [==============================] - 17s - loss: 0.0107 - val_loss: 0.0129

(add 2nd dropout layer(50%) after flattern)
12857/12857 [==============================] - 21s - loss: 0.0447 - val_loss: 0.0161
Epoch 2/7
12857/12857 [==============================] - 19s - loss: 0.0144 - val_loss: 0.0138
Epoch 3/7
12857/12857 [==============================] - 18s - loss: 0.0117 - val_loss: 0.0120
Epoch 4/7
12857/12857 [==============================] - 19s - loss: 0.0109 - val_loss: 0.0122
Epoch 5/7
12857/12857 [==============================] - 19s - loss: 0.0106 - val_loss: 0.0112
Epoch 6/7
12857/12857 [==============================] - 19s - loss: 0.0105 - val_loss: 0.0116
Epoch 7/7
12857/12857 [==============================] - 19s - loss: 0.0103 - val_loss: 0.0118
(change 2nd dropout layer to 25%)
12857/12857 [==============================] - 21s - loss: 0.1763 - val_loss: 0.0153
Epoch 2/7
12857/12857 [==============================] - 19s - loss: 0.0141 - val_loss: 0.0139
Epoch 3/7
12857/12857 [==============================] - 19s - loss: 0.0125 - val_loss: 0.0128
Epoch 4/7
12857/12857 [==============================] - 19s - loss: 0.0112 - val_loss: 0.0120
Epoch 5/7
12857/12857 [==============================] - 19s - loss: 0.0106 - val_loss: 0.0118
Epoch 6/7
12857/12857 [==============================] - 19s - loss: 0.0103 - val_loss: 0.0115
Epoch 7/7
12857/12857 [==============================] - 19s - loss: 0.0101 - val_loss: 0.0117
7. even more powerful network by Nvidia to pass the bridge
with 0.25 dropout: overfitting  

12857/12857 [==============================] - 20s - loss: 0.0202 - val_loss: 0.0110
Epoch 2/7
12857/12857 [==============================] - 16s - loss: 0.0113 - val_loss: 0.0103
Epoch 3/7
12857/12857 [==============================] - 16s - loss: 0.0103 - val_loss: 0.0107
Epoch 4/7
12857/12857 [==============================] - 16s - loss: 0.0095 - val_loss: 0.0110
Epoch 5/7
12857/12857 [==============================] - 16s - loss: 0.0089 - val_loss: 0.0111
Epoch 6/7
12857/12857 [==============================] - 16s - loss: 0.0082 - val_loss: 0.0117
Epoch 7/7
12857/12857 [==============================] - 16s - loss: 0.0077 - val_loss: 0.0116

With 0.5 dropout: better

12857/12857 [==============================] - 18s - loss: 0.0158 - val_loss: 0.0114
Epoch 2/7
12857/12857 [==============================] - 16s - loss: 0.0109 - val_loss: 0.0107
Epoch 3/7
12857/12857 [==============================] - 16s - loss: 0.0100 - val_loss: 0.0108
Epoch 4/7
12857/12857 [==============================] - 16s - loss: 0.0095 - val_loss: 0.0107
Epoch 5/7
12857/12857 [==============================] - 16s - loss: 0.0091 - val_loss: 0.0103
Epoch 6/7
12857/12857 [==============================] - 16s - loss: 0.0088 - val_loss: 0.0113
Epoch 7/7
12857/12857 [==============================] - 16s - loss: 0.0083 - val_loss: 0.0108

with 0.5 dropout (2nd run):
12857/12857 [==============================] - 18s - loss: 0.0176 - val_loss: 0.0109
Epoch 2/7
12857/12857 [==============================] - 17s - loss: 0.0113 - val_loss: 0.0113
Epoch 3/7
12857/12857 [==============================] - 16s - loss: 0.0103 - val_loss: 0.0105
Epoch 4/7
12857/12857 [==============================] - 16s - loss: 0.0096 - val_loss: 0.0112
Epoch 5/7
12857/12857 [==============================] - 16s - loss: 0.0093 - val_loss: 0.0113
Epoch 6/7
12857/12857 [==============================] - 16s - loss: 0.0086 - val_loss: 0.0115
Epoch 7/7
12857/12857 [==============================] - 16s - loss: 0.0081 - val_loss: 0.0115

result is there is still sometimes of the track, especiially after crossing bridge

8. collect more data: second lap
 - Using the left/right images is useful to train the recovery driving scenario.
error is higher but car on track, yeah
-lenet: still off track
TODO:
2. The code in model.py uses a Python generator
4. Have the model parameters been tuned appropriately: Learning rate parameters are chosen with explanation, or an Adam optimizer is used.
5. Is the training data chosen appropriately? Training data has been chosen to induce the desired behavior in the simulation (i.e. keeping the car on the track).
6. Is the solution design documented?
  - The README thoroughly discusses the approach taken for deriving and designing a model architecture fit for solving the given problem
  - The README provides sufficient details of the characteristics and qualities of the architecture, such as the type of model used, the number of layers, the size of each layer. Visualizations emphasizing particular qualities of the architecture are encouraged. Here is one such tool for visualization.
  - The README describes how the model was trained and what the characteristics of the dataset are. Information such as how the dataset was generated and examples of images from the dataset must be included.
7. No tire may leave the drivable portion of the track surface. The car may not pop up onto ledges or roll over any surfaces that would otherwise be considered unsafe (if humans were in the vehicle).
