# Tensorflow 使用

# 坑
1. 
```python
output, h1 = cell.call(inputs, h0) #调用call函数

Error ：AttributeError: 'BasicRNNCell' object has no attribute '_kernel'

改正：output, h1 = cell.__call__(inputs, h0) #调用call函数
```
----
2. 
```python

def call(self, inputs, state):
    """Most basic RNN: output = new_state = act(W * input + U * state + B)."""
    output = self._activation(_linear([inputs, state], self._num_units, True))
    return output, output
```

> 在BasicRNNCell中，output其实和隐状态的值是一样的。因此，我们还需要额外对输出定义新的变换，才能得到图中真正的输出y。由于output和隐状态是一回事，所以在BasicRNNCell中，state_size永远等于output_size。TensorFlow是出于尽量精简的目的来定义BasicRNNCell的，所以省略了输出参数，

-----
```python
if self._state_is_tuple:
  new_state = LSTMStateTuple(new_c, new_h)
else:
  new_state = array_ops.concat([new_c, new_h], 1)
return new_h, new_state

```
> 返回的隐状态是new_c和new_h的组合，而output就是单独的new_h。如果我们处理的是分类问题，那么我们还需要对new_h添加单独的Softmax层才能得到最后的分类概率输出
3. 

# 

## 1. tf.dynamic_rnn

> 假设你的RNN的输入input是[2,20,128]，其中2是batch_size,20是文本最大长度，128是embedding_size，
可以看出，有两个example，我们假设第二个文本长度只有13，剩下的7个是使用0-padding方法填充的。
dynamic返回的是两个参数：outputs,last_states，其中outputs是[2,20,128]，也就是每一个迭代隐状态的输出,
last_states是由(c,h)组成的tuple，均为[batch,128]。

> 到这里并没有什么不同，但是dynamic有个参数：sequence_length，这个参数用来指定每个example的长度，比如上面的例子中，我们令 sequence_length为[20,13]，表示第一个example有效长度为20，第二个example有效长度为13，当我们传入这个参数的时候，对于第二个example，TensorFlow对于13以后的padding就不计算了，其last_states将重复第13步的last_states直至第20步，而outputs中超过13步的结果将会被置零。









# 参考

*  tf.dynamic_rnn使用---https://blog.csdn.net/u010223750/article/details/71079036
