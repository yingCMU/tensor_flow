import tensorflow as tf
# keep_prob allows you to adjust the number of units to drop. In order to compensate for dropped units, tf.nn.dropout() multiplies all units that are kept (i.e. not dropped) by 1/keep_prob.
#
# During training, a good starting value for keep_prob is 0.5.
#
# During testing, use a keep_prob value of 1.0 to keep all units and maximize the power of the model.
#You should only drop units while training the model. During validation or testing, you should keep all of the units to maximize accuracy
keep_prob = tf.placeholder(tf.float32) # probability to keep units

hidden_layer = tf.add(tf.matmul(features, weights[0]), biases[0])
hidden_layer = tf.nn.relu(hidden_layer)
hidden_layer = tf.nn.dropout(hidden_layer, keep_prob)

logits = tf.add(tf.matmul(hidden_layer, weights[1]), biases[1]
