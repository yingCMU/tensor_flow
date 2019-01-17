# **Behavioral Cloning**
---
**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./arch.png "Model Visualization"
[image2]: ./center_2019_01_01_03_46_20_422.jpg "Center Image"
[image3]: ./left_2019_01_01_03_46_20_422.jpg "Recovery Image (left)"
[image4]: ./right_2019_01_01_03_46_20_422.jpg "Recovery Image (right)"
[image5]: ./original.png "Original Image"
[image6]: ./flipped.png "Flipped Image"
[image7]: ./history.png "Flipped Image"


## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. Solution Design Approach
1. Starting from applying leNet architecture to training data, I got the following accuracy:
 train loss: 0.0129 - val_loss: 0.0146
The autonomous car turns out to keep turning left and drive out of track.
2. Then I used image flipping to augment training data to fix left bias and got following accuracy:
train loss: 0.0101 - val_loss: 0.0131
The autonomous car does not pull left out of track, but turns out to fail to turn left in big curves.
3. I also used image cropping to remove top 70 pixels (sky and trees) and bottom 25 pixels (hood of car), accuracy:
train loss: 0.0114 - val_loss: 0.0119
4. I added a dropout layer(0.25 drop out) before first max pooling layer
and it didn't change accuracy much:
train loss: 0.0096 - val_loss: 0.0114
The autonomous car still drive out of track.
5. Then I decided to apply the model from [Nvidia paper](http://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) with 0.25 dropout layer, accuracy:
train loss: 0.0077 - val_loss: 0.0116
6. Train loss is much better than validation loss, which signals overfitting, so I increased dropout rate to 0.5 to reduce overfitting, got accuracy:
train loss: 0.0083 - val_loss: 0.0108
The simulation is running much better, but still fell out of track in bigger curves.
7. To teach car to learn how to recover, I decided to use left and right camera images. Train and validation error turns higher which is expected with bigger data set but the autonomous car is not falling out of track any more.
8. I added generator to reduce memory usage, but it turns out to be much slower (~2500s) than without generator

#### 2. Final Model Architecture
Preprocessing:
1. Image normalization: (x / 255.0) - 0.5
2. cropping: (70, 25), (0, 0)
Data augmentation:
1. flip image

The final model architecture (model.py lines 73-84) consisted of a convolution neural network with the following layers and layer sizes:
Convolution: 5x5, filter: 24, strides: 2x2, activation: ELU
Convolution: 5x5, filter: 36, strides: 2x2, activation: ELU
Convolution: 5x5, filter: 48, strides: 2x2, activation: ELU
Convolution: 3x3, filter: 64, strides: 1x1, activation: ELU
Convolution: 3x3, filter: 64, strides: 1x1, activation: ELU
Drop out (0.5)
Flattern
Fully connected: neurons: 100, activation: ELU
Fully connected: neurons: 50, activation: ELU
Fully connected: neurons: 10, activation: ELU
Fully connected: neurons: 1 (output)
Here is a visualization of the architecture:

![alt text][image1]

#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text][image2]

To teach the vehicle to learn recover from the side of road back to center, I use both left and right camera image with correction angles:
left image: steer angle + 0.2
right image: steer angle - 0.2

![alt text][image3]
![alt text][image4]

To augment the data sat, I also flipped images and angles thinking that this would reduce left bias and teach the vechile to learn generalized driving. For example, here is an image that has then been flipped:

![alt text][image5]
![alt text][image6]

After the collection process, I then preprocessed this data by normalization and cropping unnecessary image parts (like sky , trees and car hood)
I finally randomly shuffled the data set and put 20% of the data into a validation set.
I used this training data for training the model. The validation set helped determine if the model was over or under fitting.
I chose batch size of 128 (same as previous project)
The ideal number of epochs was 7 as evidenced by overfitting over 7 (validation loss increasing while train loss dropping).
I used an adam optimizer so that manually training the learning rate wasn't necessary.
The following shows loss in training process:
![alt text][image7]
