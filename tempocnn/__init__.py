"""
tempo-cnn is a simple package that allows estimation of musical tempo.
"""
import logging
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()
# reduce TensorFlow chatter
tf.get_logger().setLevel(logging.ERROR)
