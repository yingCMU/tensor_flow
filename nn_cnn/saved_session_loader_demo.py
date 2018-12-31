import tensorflow as tf


save_file = './model.ckpt'
# Remove the previous weights and bias
tf.reset_default_graph()

# Two Variables: weights and bias
# you still need to create the weights and bias Tensors in Python.
# The tf.train.Saver.restore() function loads the saved data into weights and bias.
#
# Since tf.train.Saver.restore() sets all the TensorFlow Variables,
# you don't need to call tf.global_variables_initializer().


weights = tf.Variable(tf.truncated_normal([2, 3]))
bias = tf.Variable(tf.truncated_normal([3]))
# Class used to save and/or restore Tensor Variables
saver = tf.train.Saver()

with tf.Session() as sess:
    # sess.run(tf.global_variables_initializer())
    # print('before restore bias:',sess.run(bias))
    # Load the weights and bias
    saver.restore(sess, save_file)

    # Show the values of weights and bias
    print('Weight:')
    print(sess.run(weights))
    print('Bias:')
    print(sess.run(bias))
