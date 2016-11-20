# coding:utf-8

import tensorflow as tf
import numpy as np


# ���(0, 100)�ɂ����� y = 2x + 20��̓_��y��������-10�`10�̌덷��
# �����_���ɉ��������̂��T���v���Ƃ��� 

sampX = np.linspace(0., 100., 101., dtype='float32')
randerr = (np.random.rand(101) - 0.5) * 2
Y = (2 * sampX) + 20 
sampY = Y + randerr

# �T���v����y�������������ꎟ�֐����œK�����Ă����ɂ�������
# �֐��̌X���̏����l�Ƃ��ĉE�[�̓_�ƍ��[�̓_�����񂾒����̌X��
# y�ؕЂ̏����l�Ƃ��č��[�̓_��y������I��

a = tf.Variable(tf.to_float((sampY[100]-sampY[0])/(sampX[100]-sampX[0])), name="slope")
b = tf.Variable(tf.to_float(sampY[0]), name="y-intercept")

x = tf.placeholder(tf.float32, shape=[101])
y = tf.placeholder(tf.float32, shape=[101])



ymodel = tf.add(tf.mul(a, x), b)
MSE = tf.reduce_mean(tf.pow((ymodel - y), 2))
optimize = tf.train.GradientDescentOptimizer(0.00015).minimize(MSE)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    
    for i in range(50001):
        sess.run(optimize, feed_dict={x:sampX, y:sampY})
        if i % 5000  == 0:
            print '\nStep %d' % i
            print 'Slope = %f, Y-intercept = %f' % (sess.run(a), sess.run(b))