# coding: utf-8
'''
Created on 2018. 4. 24.

@author: Insup Jung
'''

import tensorflow as tf
from tensorflow.contrib.factorization.examples.mnist import fill_feed_dict

if __name__ == '__main__':
    
    
    with tf.name_scope("MyOperationGroup"):
        with tf.name_scope("Scope_A"):            
            a = tf.add(1, 2)
            b = tf.multiply(a, 3) #곱하는 함수 tf.mat_mul은 matrix multiply이다.       
            c = tf.add(4, 5)
            d = tf.multiply(c, 6)
        
        with tf.name_scope("Scope_B"):
            e = tf.multiply(4, 5)
            f = tf.div(c, 6)
            g = tf.add(b, d)
            h = tf.multiply(g, f)
    
    with tf.name_scope("Scope_C"):    
        k = tf.placeholder(tf.float32)
        l = tf.placeholder(tf.float32)
        m = tf.add(k, l)
        
    with tf.Session() as sess:
        writer = tf.summary.FileWriter("board", sess.graph)
        print (sess.run(h))
        
        print(sess.run(m, feed_dict={k : 1, l : 3}))   
    
    pass