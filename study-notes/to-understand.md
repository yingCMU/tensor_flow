1. How many unique classes/labels there are in the dataset.
used np.unique(y_train).shape
[list of signs](https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project/blob/master/signnames.csv)
2. preprocessing
   why normalization?normalized the image because it converges much faster with feature scaling than without it.
   Minimally, the image data should be normalized so that the data has mean zero and equal variance. For image data, (pixel - 128)/ 128 is a quick way to approximately normalize the data and can be used in this project.
3. how visualization layer works, how does that evaluate to input image
4. [Adam Optimization Algorithm for Deep Learning](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/)
5 difference between softmax_logits = tf.nn.softmax(logits)
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=one_hot_y, logits=logits)
