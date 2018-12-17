[md guide](https://guides.github.com/features/mastering-markdown/)
##  backprop
1. each backprop step takes 2X memory as forwardprop, why?
## architecture
2. make hidden layer wider vs make deeper layer
  1. you can get much more performance using less parameters by going deeper rather than wider
  2.lots of phenomena tend to have a hierarchical structure, as a result, the model has easier time learning then.  e.g image processing line edges->part shapes -> objects
## Save and Restore TensorFlow Models
save any tf.Variable to your file system.

## regularization
1. skinny jeans problem, why?
  network that is just right size for the data is very hard to optimize, so instead train networks that are way to big for data
  and then try our best to prevent them from overfitting
2. how to prevent overfitting
  1. early termination: look at the performance of validation set and stop training(reach the point of overfitting) as soon as it stops improving
  2. regularization
  apply artificial constraints on your network, implicitly reduce the number of free parameters (make the skinny jeans right to fit in)
  L2 regularization: add another term to the loss to penalize large weights ... + 1/2 ||w||^2, derivative is just w
  3. dropout
  Dropout is a regularization technique for reducing overfitting. The technique temporarily drops units (artificial neurons) from the network, along with all of those units' incoming and outgoing connections. [paper](http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf)
