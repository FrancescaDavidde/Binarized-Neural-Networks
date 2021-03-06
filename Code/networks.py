import tensorflow as tf
import layers

# CREAZIONE DELLE 4 RETI (2+2)
# GET NETWORK PER TRAINING

#---CIFAR 10---# (A)

# NB per cifar avremo CONVOLUTIONAL NEURAL NETWORK

# BNN with SIGN FUNCTION
# original batch normalization and vanilla adam

def binary_cifar10(input, training=True):
	out = layers.binaryConv2d(input, 128, [3,3], [1,1], padding='VALID', binarize_input=False, name='bc_conv2d_1')
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 128, [3,3], [1,1], padding='SAME',  name='bnn_conv2d_1')
	out = tf.layers.max_pooling2d(out, [2,2], [2,2])
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 256, [3,3], [1,1], padding='SAME', name='bnn_conv2d_2')
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 256, [3,3], [1,1], padding='SAME',  name='bnn_conv2d_3')
	out = tf.layers.max_pooling2d(out, [2,2], [2,2])
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 512, [3,3], [1,1], padding='SAME',  name='bnn_conv2d_4')
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 512, [3,3], [1,1], padding='SAME',  name='bnn_conv2d_5')
	out = tf.layers.max_pooling2d(out, [2,2], [2,2])
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryDense(out, 1024,  name='binary_dense_1')
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryDense(out, 1024,  name='binary_dense_2')
	out = tf.layers.batch_normalization(out, training=training)
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryDense(out, 10, name='binary_dense_3')
	output = tf.layers.batch_normalization(out, training=training)
	
	return input, output
	
# BNN with SIGN FUNCTION 
# shift based batch normalization ---> spatial_shift_batch_norm quando ?? ancora conv2d, poi diventa shift_batch_norm
# shift based adam opt.

def binary_cifar10_sbn(input, training=True):
	out = layers.binaryConv2d(input, 128, [3,3], [1,1], padding='VALID',  binarize_input=False, name='bc_conv2d_1')
	out = layers.spatial_shift_batch_norm(out, training=training, name='shift_batch_norm_1')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 128, [3,3], [1,1], padding='SAME',  name='bnn_conv2d_1')
	out = tf.layers.max_pooling2d(out, [2,2], [2,2])
	out = layers.spatial_shift_batch_norm(out, training=training, name='shift_batch_norm_2')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 256, [3,3], [1,1], padding='SAME',  name='bnn_conv2d_2')
	out = layers.spatial_shift_batch_norm(out, training=training, name='shift_batch_norm_3')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 256, [3,3], [1,1], padding='SAME',  name='bnn_conv2d_3')
	out = tf.layers.max_pooling2d(out, [2,2], [2,2])
	out = layers.spatial_shift_batch_norm(out, training=training, name='shift_batch_norm_4')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 512, [3,3], [1,1], padding='SAME', name='bnn_conv2d_4')
	out = layers.spatial_shift_batch_norm(out, training=training, name='shift_batch_norm_5')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryConv2d(out, 512, [3,3], [1,1], padding='SAME', name='bnn_conv2d_5')
	out = tf.layers.max_pooling2d(out, [2,2], [2,2])
	out = layers.spatial_shift_batch_norm(out, training=training, name='shift_batch_norm_6')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryDense(out, 1024,  name='binary_dense_1')
	out = layers.shift_batch_norm(out, training=training, name='shift_batch_norm_7')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryDense(out, 1024, name='binary_dense_2')
	out = layers.shift_batch_norm(out, training=training, name='shift_batch_norm_8')
	out = tf.clip_by_value(out, -1, 1)

	out = layers.binaryDense(out, 10, name='binary_dense_3')
	output = layers.shift_batch_norm(out, training=training, name='shift_batch_norm_9')
	
	return input, output

# ---MNIST---#	(B)

# NB per mnist avremo una MLP
	
# BNN with SIGN FUNCTION FROM BINARIZE(X) function
# original batch normalization and vanilla adam

def binary_mnist(input, training=True):
	fc1 = layers.binaryDense(input, 784, activation=None, name="binarydense1", binarize_input=False)
	bn1 = tf.layers.batch_normalization(fc1, training=training)
	ac1 = tf.clip_by_value(bn1, -1, 1)

	fc2 = layers.binaryDense(ac1, 2048, activation=None, name="binarydense2")
	bn2 = tf.layers.batch_normalization(fc2, training=training)
	ac2 = tf.clip_by_value(bn2, -1, 1)

	fc3 = layers.binaryDense(ac2, 2048, activation=None, name="binarydense3")
	bn3 = tf.layers.batch_normalization(fc3, training=training)
	ac3 = tf.clip_by_value(bn3, -1, 1)

	fc4 = layers.binaryDense(ac3, 10, activation=None, name="binarydense4")
	output =  tf.layers.batch_normalization(fc4, training=training)
	
	return input, output

# BNN with SIGN FUNCTION FROM BINARIZE(X) function
# shift based batch normalization  ----> layers.shift_batch_norm
# shift based adam opt.
	
def binary_mnist_sbn(input, training=True):
	fc1 = layers.binaryDense(input, 784, activation=None, name="binarydense1", binarize_input=False)
	bn1 = layers.shift_batch_norm(fc1, training=training, name="batch_norm1")
	ac1 = tf.clip_by_value(bn1, -1, 1)

	fc2 = layers.binaryDense(ac1, 2048, activation=None, name="binarydense2")
	bn2 = layers.shift_batch_norm(fc2, training=training, name="batch_norm2")
	ac2 = tf.clip_by_value(bn2, -1, 1)

	fc3 = layers.binaryDense(ac2, 2048, activation=None, name="binarydense3")
	bn3 = layers.shift_batch_norm(fc3, training=training, name="batch_norm3")
	ac3 = tf.clip_by_value(bn3, -1, 1)

	fc4 = layers.binaryDense(ac3, 10, activation=None, name="binarydense4")
	output = layers.shift_batch_norm(fc4, training=training, name="batch_norm4")
	
	return input, output

# scelta network adatta

def get_network(type, dataset, *args, **kargs):

	if dataset == 'mnist':
		if type == 'binary':
			return binary_mnist(*args, **kargs)
		if type == 'binary_sbn':
			return binary_mnist_sbn(*args, **kargs)
	
	if dataset == 'cifar10':
		if type == 'binary':
			return binary_cifar10(*args, **kargs)
		if type == 'binary_sbn':
			return binary_cifar10_sbn(*args, **kargs)
	
	return None
	

		
