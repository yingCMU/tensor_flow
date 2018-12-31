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

## how to find a solution?
While designing the architecture, it is important to consider the following questions.

- How did I preprocess my data? How will that affect the model?
- How to choose the optimizer? Evaluate its pros and cons.
- Overfitting and Underfitting:
  - if overfitting, adding dropout or max pooling can help. You can report can describe how dropout or max pooling improved the model.
  - if underfitting, you can report how adding more convolution or fully connected layers helped.
How to decide the number and type of layers?
How to tune the hyperparameters? Sound knowledge of Linear Algebra, Probability & Statistics and Multivariate Calculus can help you a lot in narrowing down your choices.
How to train and evaluate the model? What is the metric? How do I set the benchmark?
## Project review comments:
- For developing an intuition, I think it comes down more to developing more experience on how to approach a problem.
CNNs are predominantly used for anything related to images. That's what they were created for, although there has been work to try to use them elsewhere too I believe.
- Building an architecture depends a lot on your data - If I have images of faces, that's more features than a single handwritten number, so you need a deeper model to be able to extract the features and then as you go deeper you get more features (as we saw in the lectures).
- As for tuning parameters based on results - I have been recommending students this resource to get an idea on how to analyze the results, but it then comes down to experimenting and seeing what affects what.
- I have been following one rule till now, however, and can't say it's definite but more (and good) data is better than trying to finely tune a particular model. Some form of data augmentation based on the data you have will help. Which is easier when it comes to working with images.
- I would recommend you read up on research papers if you are serious about pursuing this field (DL or ML). Or find implementations of similar projects outside of this ND so that you can learn from them and understand why something specific is done. There are too many approaches and too many parameters, and trying everything out on your own is not always feasible. So it's better to learn from others and that will help develop an intuition in the long run.
- To increase the ability of your model to generalize, good preprocessing yields impressive results.
