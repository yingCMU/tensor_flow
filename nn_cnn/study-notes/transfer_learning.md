Transfer learning involves taking a pre-trained neural network and adapting the neural network to a new, different data set.
[link](https://classroom.udacity.com/nanodegrees/nd013/parts/edf28735-efc1-4b99-8fbb-ba9c432239c8/modules/6b6c37bc-13a5-47c7-88ed-eb1fce9789a0/lessons/818a5b8e-44b3-42f9-9921-e0e0e49f104e/concepts/10489223-72fa-4393-848b-f882ba3cf7f9)
Depending on both:
1. the size of the new data set, and
2. the similarity of the new data set to the original data set
(A large data set might have one million images. A small data could have two-thousand images. The dividing line between a large data set and small data set is somewhat subjective. Overfitting is a concern when using transfer learning with a small data set.

Images of dogs and images of wolves would be considered similar; the images would share common characteristics. A data set of flower images would be different from a data set of dog images.)
the approach for using transfer learning will be different. There are four main cases.
Each of the four transfer learning cases has its own approach.
- Case 1: Small Data Set, Similar Data
If the new data set is small and similar to the original training data:

slice off the end of the neural network
add a new fully connected layer that matches the number of classes in the new data set
randomize the weights of the new fully connected layer; freeze all the weights from the pre-trained network
train the network to update the weights of the new fully connected layer
To avoid overfitting on the small data set, the weights of the original network will be held constant rather than re-training the weights.

Since the data sets are similar, images from each data set will have similar higher level features. Therefore most or all of the pre-trained neural network layers already contain relevant information about the new data set and should be kept.
- Case 2: Small Data Set, Different Data
If the new data set is small and different from the original training data:

slice off most of the pre-trained layers near the beginning of the network
add to the remaining pre-trained layers a new fully connected layer that matches the number of classes in the new data set
randomize the weights of the new fully connected layer; freeze all the weights from the pre-trained network
train the network to update the weights of the new fully connected layer
Because the data set is small, overfitting is still a concern. To combat overfitting, the weights of the original neural network will be held constant, like in the first case.

But the original training set and the new data set do not share higher level features. In this case, the new network will only use the layers containing lower level features.
- Case 3: Large Data Set, Similar Data
If the new data set is large and similar to the original training data:

remove the last fully connected layer and replace with a layer matching the number of classes in the new data set
randomly initialize the weights in the new fully connected layer
initialize the rest of the weights using the pre-trained weights
re-train the entire neural network
Overfitting is not as much of a concern when training on a large data set; therefore, you can re-train all of the weights.

Because the original training set and the new data set share higher level features, the entire neural network is used as well.
- Case 4: Large Data Set, Different Data
If the new data set is large and different from the original training data:

remove the last fully connected layer and replace with a layer matching the number of classes in the new data set
retrain the network from scratch with randomly initialized weights
alternatively, you could just use the same strategy as the "large and similar" data case
Even though the data set is different from the training data, initializing the weights from the pre-trained network might make training faster. So this case is exactly the same as the case with a large, similar data set.

If using the pre-trained network as a starting point does not produce a successful model, another option is to randomly initialize the convolutional neural network weights and train the network from scratch.

| Network      | Error %   |
| ----------- | ----------- |
| Winner of ImageNet| 26%      |
| AlexNet   | 15%        |
| VGG   | 7.3%        |
| GoogleNet   | 6.7%        |

## transfer learning from ImageNet(object detection and localization)
Pre-training a network with the ImageNet dataset is a very common way to get a strong neural network that can be used for transfer learning. With recent versions of Keras, you can easily import a pre-trained network by using the [Keras Applications models](https://keras.io/applications/)
## AlexNet
AlexNet Architecture - very complex and not every feature is necessary, but best understood and most widely used neural network
AlexNet puts the network on two GPUs, which allows for building a larger network. Although most of the calculations are done in parallel, the GPUs communicate with each other in certain layers. The original [research paper](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) on AlexNet said that parallelizing the network decreased the classification error rate by 1.7% when compared to a neural network that used half as many neurons on one GPU.
##  [VGG paper](https://arxiv.org/pdf/1409.1556.pdf)
in Keras, There are actually two versions of VGG, VGG16 and VGG19 (where the numbers denote the number of layers included in each respective model)
## [GoogLeNet/Inception paper](https://arxiv.org/pdf/1409.4842.pdf)
