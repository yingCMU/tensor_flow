[md guide](https://guides.github.com/features/mastering-markdown/)
##  backprop
1. each backprop step takes 2X memory as forwardprop, why?
## architecture
2. make hidden layer wider vs make deeper layer
  1. you can get much more performance using less parameters by going deeper rather than wider
  2.lots of phenomena tend to have a hierarchical structure, as a result, the model has easier time learning then.  e.g image processing line edges->part shapes -> objects
## Save and Restore TensorFlow Models
save any tf.Variable to your file system.
## feature scaling/ data normalization
1. Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work properly without normalization. For example, the majority of classifiers calculate the distance between two points by the Euclidean distance. If one of the features has a broad range of values, the distance will be governed by this particular feature. Therefore, the range of all features should be normalized so that each feature contributes approximately proportionately to the final distance.
2. Another reason why feature scaling is applied is that gradient descent converges much faster with feature scaling than without it.[Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167.pdf)
### methods
## regularization
1. skinny jeans problem, why?
  network that is just right size for the data is very hard to optimize, so instead train networks that are way to big for data
  and then try our best to prevent them from overfitting
### overfitting
[The problem of overfitting](https://pdfs.semanticscholar.org/f65e/e7b52912f8485dc0411a40ccebf5f3f2afef.pdf)
Overfitting is especially likely in cases where learning was performed too long or where training examples are rare, causing the learner to adjust to very specific random features of the training data, that have no causal relation to the target function.
### Regularization
Regularization can be motivated as a technique to improve the generalizability of a learned model.
Typically in learning problems, only a subset of input data and labels are available, measured with some noise. Therefore, the expected error is unmeasurable, and the best surrogate available is the empirical error over the {\displaystyle N} N available samples. Without bounds on the complexity of the function space available, a model will be learned that incurs zero loss on the surrogate empirical error. If measurements (e.g. of {\displaystyle x_{i}} x_{i}) were made with noise, this model may suffer from overfitting and display poor expected error. Regularization introduces a penalty for exploring certain regions of the function space used to build the model, which can improve generalization.

Generally, a learning algorithm is said to overfit relative to a simpler one if it is more accurate in fitting known data (hindsight) but less accurate in predicting new data (foresight). One can intuitively understand overfitting from the fact that information from all past experience can be divided into two groups: information that is relevant for the future and irrelevant information ("noise"). Everything else being equal, the more difficult a criterion is to predict (i.e., the higher its uncertainty), the more noise exists in past information that needs to be ignored. The problem is determining which part to ignore. A learning algorithm that can reduce the chance of fitting noise is called "robust."

 R(f) is typically chosen to impose a penalty on the complexity of f
  {\displaystyle \lambda } \lambda  is a parameter which controls the importance of the regularization term
  1. early termination: look at the performance of validation set and stop training(reach the point of overfitting) as soon as it stops improving
  2. regularization
  apply artificial constraints on your network, implicitly reduce the number of free parameters (make the skinny jeans right to fit in)
  L2 regularization: add another term to the loss to penalize large weights ... + 1/2 ||w||^2, derivative is just w
  3. dropout
  Dropout is a regularization technique for reducing overfitting. The technique temporarily drops units (artificial neurons) from the network, along with all of those units' incoming and outgoing connections. [paper](http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf)
### dropout
1. [Improving neural networks by preventing co-adaptation of feature detectors](https://arxiv.org/pdf/1207.0580.pdf)
2. [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](http://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)
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
