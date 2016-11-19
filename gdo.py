# coding:utf-8

import tensorflow as tf
import numpy as np


# 区間(0, 100)において y = 2x + 20上の点にy軸方向に-10～10の誤差を
# ランダムに加えたものをサンプルとする 

sampX = np.linspace(0., 100., 101., dtype='float32')
randerr = (np.random.rand(101) - 0.5) * 2
Y = (2 * sampX) + 20 
sampY = Y + randerr

# サンプルのy成分を説明する一次関数を最適化していくにあたって
# 関数の傾きの初期値として右端の点と左端の点を結んだ直線の傾き
# y切片の初期値として左端の点のy成分を選ぶ

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