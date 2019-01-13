## concept
As humans, how do we classify the following image of a dog as a Golden Retrieve?
identify certain parts of the dog, such as the nose, the eyes, and the fur. We essentially break up the image into smaller pieces, recognize the smaller pieces, and then combine those pieces to get an idea of the overall dog.
In our case, the levels in the hierarchy are:

- Simple shapes, like ovals and dark circles
- Complex objects (combinations of simple shapes), like eyes, nose, and fur
- The dog as a whole (a combination of complex objects)

With deep learning, we don't actually program the CNN to recognize these specific features. Rather, the CNN learns on its own to recognize such objects through forward propagation and backpropagation!

It's amazing how well a CNN can learn to classify images, even though we never program the CNN with information about specific features to look for.

What's important here is that we are grouping together adjacent pixels and treating them as a collective.
In a normal, non-convolutional neural network, we would have ignored this adjacency. In a normal network, we would have connected every pixel in the input image to a neuron in the next layer. In doing so, we would not have taken advantage of the fact that pixels in an image are close together for a reason and have special meaning.By taking advantage of this local structure, our CNN learns to classify local patterns, like shapes and objects, in an image.
## bias - variance
The bias–variance dilemma or problem is the conflict in trying to simultaneously minimize these two sources of error that prevent supervised learning algorithms from generalizing beyond their training set:[citation needed]

The bias is an error from erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss the relevant relations between features and target outputs (underfitting).
The variance is an error from sensitivity to small fluctuations in the training set. High variance can cause an algorithm to model the random noise in the training data, rather than the intended outputs (overfitting).
## Filter Depth
It's common to have more than one filter. Different filters pick up different qualities of a patch. For example, one filter might look for a particular color, while another might look for a kind of object of a specific shape. The amount of filters in a convolutional layer is called the filter depth.
## How many neurons does each patch connect to?
- Choosing a filter depth of k connects each patch to k neurons in the next layer.
That’s dependent on our filter depth. If we have a depth of k, we connect each patch of pixels to k neurons in the next layer. This gives us the height of k in the next layer, as shown below. In practice, k is a hyperparameter we tune, and most CNNs tend to pick the same starting values.
## each neuron
But why connect a single patch to multiple neurons in the next layer? Isn’t one neuron good enough?
Multiple neurons can be useful because a patch can have multiple interesting characteristics that we want to capture.
For example, one patch might include some white teeth, some blonde whiskers, and part of a red tongue. In that case, we might want a filter depth of at least three.
Remember that the CNN isn't "programmed" to look for certain characteristics. Rather, it learns on its own which characteristics to notice.

## width, height, depth, padding? [link](https://classroom.udacity.com/nanodegrees/nd013/parts/edf28735-efc1-4b99-8fbb-ba9c432239c8/modules/6b6c37bc-13a5-47c7-88ed-eb1fce9789a0/lessons/0fb1d383-484e-4c49-a0e4-03922c1416d6/concepts/64217999280923)
depends on padding : same padding or valid padding
with valid padding: the width and height of each subsequent layer
In an ideal world, we'd be able to maintain the same width and height across layers so that we can continue to add layers without worrying about the dimensionality shrinking and so that we have consistency. How might we achieve this? One way is to simply add a border of 0s to our original 5x5 image. You can see what this looks like in the below image.

Given:
- our input layer has a width of W and a height of H
- our convolutional layer has a filter size F (F*F patch)
- we have a stride of S
- a padding of P
- and the number of filters K(depth),
the following formula gives us the width of the next layer: W_out =[ (W−F+2P)/S] + 1.

The output height would be H_out = [(H-F+2P)/S] + 1.

And the output depth would be equal to the number of filters D_out = K.

The output volume would be W_out * H_out * D_out.

## sharing parameters
sharing parameters not only helps us with translation invariance, but also gives us a smaller, more scalable model.

## TensorFlow padding
in TensorFlow, read this [document](https://www.tensorflow.org/api_guides/python/nn#Convolution).

In summary TensorFlow uses the following equation for 'SAME' vs 'VALID'

SAME Padding, the output height and width are computed as:

out_height = ceil(float(in_height) / float(strides[1]))

out_width = ceil(float(in_width) / float(strides[2]))

VALID Padding, the output height and width are computed as:

out_height = ceil(float(in_height - filter_height + 1) / float(strides[1]))

out_width = ceil(float(in_width - filter_width + 1) / float(strides[2]))
## pooling
pooling decrease the size of the output and prevent overfitting. Reducing overfitting is a consequence of the reducing the output size, which in turn, reduces the number of parameters in future layers.
the benefit of the max pooling operation is to reduce the size of the input, and allow the neural network to focus on only the most important elements. Max pooling does this by only retaining the maximum value for each filtered area, and removing the remaining values.
Recently, pooling layers have fallen out of favor. Some reasons are:

Recent datasets are so big and complex we're more concerned about underfitting.
Dropout is a much better regularizer.
Pooling results in a loss of information. Think about the max pooling operation as an example. We only keep the largest of n numbers, thereby disregarding n-1 numbers completely.
