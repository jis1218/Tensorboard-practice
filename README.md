# 텐서보드를 이용해 graph 시각화 하기
### 간단한 코드를 시각화 해보자 - Tensorflow가 어떤 식으로 동작하는지 가늠할 수가 있다.
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

### cmd 창에서 텐서보드를 실행할 때는 다음과 같이 해준다.
##### tensorboard --logdir=(데이터 들어있는 폴더)/

