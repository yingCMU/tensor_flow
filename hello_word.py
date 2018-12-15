import tensorflow as tf

    # 1. use placeholder with feed_dict, input is passed only once and can't be modified
    # 2. use variable, don't use feed_dict, variable need to be initialized first

hello_constant = tf.constant('Hello World!')

# x = tf.placeholder(tf.string)
x = tf.Variable('1')
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)
string_ph = tf.placeholder(tf.string)

hello_constant = tf.constant('Hello World!')
with tf.Session() as sess:
    # sess.run(tf.global_variables_initializer())
    #--- constant ----
    output = sess.run(hello_constant)
    #--- placeholder ----
    # tf.placeholder() returns a tensor that gets its value from data passed to
    # the tf.session.run() function, allowing you to set the input right before the session runs.
    output = sess.run(string_ph, feed_dict={string_ph: 'Hello World'})
    #--- Variable ----
    # The goal of training a neural network is to modify weights and biases to best
    # predict the labels. In order to use weights and bias, you'll need a Tensor
    # that can be modified. This leaves out tf.placeholder() and tf.constant(),
    # since those Tensors can't be modified. This is where tf.Variable class comes in.
    # The tf.Variable class creates a tensor with an initial value that can be modified,
    # much like a normal Python variable. This tensor stores its state in the session,
    # so you must initialize the state of the tensor manually using  tf.global_variables_initializer().
    # Using the tf.Variable class allows us to change the weights and bias, but an initial value needs to be chosen.
    # Initializing the weights with random numbers from a normal distribution is good practice.
    # Randomizing the weights helps the model from becoming stuck in the same place every time you train it.
    # Similarly, choosing weights from a normal distribution prevents any one weight from overwhelming other weights.
    # You'll use the tf.truncated_normal() function to generate random numbers from a normal distribution.
    # Since the weights are already helping prevent the model from getting stuck,
    # you don't need to randomize the bias. Let's use the simplest solution, setting the bias to 0.
    # output = sess.run(x)
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    print(output)
