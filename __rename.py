import tensorflow as tf

# Check TensorFlow version
print(tf.__version__)

# Simple computation
hello = tf.constant('Hello, TensorFlow!')
tf.print(hello)