# coding: utf-8
'''
Created on 2018. 4. 24.

@author: Insup Jung
'''

import tensorflow as tf

if __name__ == '__main__':
    
    a = tf.add(1, 2)
    b = tf.multiply(a, 3) #곱하는 함수 tf.mat_mul은 matrix multiply이다.
    c = tf.add(4, 5)
    d = tf.multiply(c, 6)
    e = tf.multiply(4, 5)
    f = tf.div(c, 6)
    g = tf.add(b, d)
    h = tf.multiply(g, f)
    
    with tf.Session() as sess:
        writer = tf.summary.FileWriter("board", sess.graph)
        print (sess.run(h))   
    
    pass