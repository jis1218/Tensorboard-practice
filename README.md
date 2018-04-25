# 텐서보드를 이용해 graph 시각화 하기
### 간단한 코드를 시각화 해보자
```python
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
```

![img](https://github.com/jis1218/Tensorboard-practice/blob/master/img/img1.PNG)


