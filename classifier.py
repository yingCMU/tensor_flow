import numpy as np
import tensorflow as tf


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)
x = tf.nn.softmax([2.0, 1.0, 0.2])
logits = [3.0, 1.0, 0.2]
print(softmax(logits))
