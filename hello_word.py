import tensorflow as tf

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

# x = tf.placeholder(tf.string)
x = tf.Variable('1')
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)
string_ph = tf.placeholder(tf.string)

hello_constant = tf.constant('Hello World!')
with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    # tf.placeholder() returns a tensor that gets its value from data passed to
    # the tf.session.run() function, allowing you to set the input right before the session runs.
    output = sess.run(string_ph, feed_dict={string_ph: 'Hello World'})
    output = sess.run(hello_constant)
    # The goal of training a neural network is to modify weights and biases to best
    # predict the labels. In order to use weights and bias, you'll need a Tensor
    # that can be modified. This leaves out tf.placeholder() and tf.constant(),
    # since those Tensors can't be modified. This is where tf.Variable class comes in.
    # output = sess.run(x)
    print(output)
