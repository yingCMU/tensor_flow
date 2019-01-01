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
6. example project: https://github.com/Goddard/udacity-traffic-sign-classifier/blob/master/writeup_template.md
https://github.com/jeremy-shannon/CarND-Traffic-Sign-Classifier-Project/blob/master/Traffic_Sign_Classifier.md
7. read project review: https://review.udacity.com/?utm_campaign=ret_000_auto_ndxxx_submission-reviewed&utm_source=blueshift&utm_medium=email&utm_content=reviewsapp-submission-reviewed&bsft_clkid=209c66f2-dc06-4ef1-a830-346bafff2a3d&bsft_uid=9c32c00f-8931-4ea3-a506-96f58a2e8d30&bsft_mid=d547cebd-7db1-4ccb-852f-02efb4c2f691&bsft_eid=6f154690-7543-4582-9be7-e397af208dbd&bsft_txnid=356f86ed-1ded-42ba-8f02-8057ef323e89#!/reviews/1642072
8. In order to further improve this work, you can try visualizing the model architecture using TensorBoard(https://www.tensorflow.org/guide/graph_viz)
9. read 99.1% [accuracy](https://medium.com/@vivek.yadav/improved-performance-of-deep-learning-neural-network-models-on-traffic-sign-classification-using-6355346da2dc)
10. read parameter [tuning](http://cs231n.github.io/neural-networks-3/#baby)
11. Adam Optimizer: [Link](http://ruder.io/optimizing-gradient-descent/index.html#adam)
Choosing the batch_size of Stochastic Gradient Descent: [Link](https://stats.stackexchange.com/questions/140811/how-large-should-the-batch-size-be-for-stochastic-gradient-descent)
12. [Traffic Signs Color Detection andSegmentation in Poor Light Conditions](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.5021&rep=rep1&type=pdf)
13. transfer learning, how?
