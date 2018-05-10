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

### 다음과 같이 변수 스코프를 줄 수도 있다.
```python
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
```
![img](https://github.com/jis1218/Tensorboard-practice/blob/master/img/img2.PNG)


### TensorBoard 사용법
##### 1. TF 그래프에서 어떤 tensor를 사용할 것인지 정한다.
```python
w2_hist = tf.summary.histogram("weights2", W2)
cost_summ = tf.summary.scalar("cost", cost)
```

##### 2. 모든 summary(위의 w2_hist, cost_summ)을 합쳐준다.
```python
summary = tf.summary.merge_all()
```

##### 3. summary를 어느 파일 경로에 저장할 것인지 정한다. 그 후 그래프를 넣어준다.
```python
writer - tf.summary.FileWriter(....)
writer.add_graph(sess.graph)
```

##### 4. summary를 실행시켜준다.
```python
s, _ = sess.run([summary, optimizer], feed_dict=feed_dict)
writer, add_summary(s, global_step=global_step)
```

##### 5. TensorBoard를 실행시킨다.


### 하나의 모델인데 다른 파라미터로 비교해보고 싶은 경우(learning rate을 다르게 줄 경우)
> ##### 파일 디렉토리를 다르게 하면 된다.
> ##### 하나는 /logs/abc
> ##### 다른 하나는 /logs/def
> ##### 라고 한다면 -logdir=./logs 라고 하면 하위 디렉토리인 두개를 비교할 수가 있다.



