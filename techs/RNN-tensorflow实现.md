#  RNN Tensorflow 实现

## 1. 单步RUN-- RNUCell

### 1. j简介
> This module provides a number of basic commonly used RNN cells, such as LSTM
(Long Short Term Memory) or GRU (Gated Recurrent Unit), and a number of
operators that allow adding dropouts, projections, or embeddings for inputs.
Constructing multi-layer cells is supported by the class `MultiRNNCell`, or by
calling the `rnn` ops several times.

* 每个RNNCell都有一个call方法，使用方式是：(output, next_state) = call(input, state)。


* 有一个初始状态h0，还有输入x1，调用call(x1, h0)后就可以得到(output1, h1)：


* 再调用一次call(x2, h1)就可以得到(output2, h2)：

> 每调用一次RNNCell的call方法，就相当于在时间上“推进了一步”，这就是RNNCell的基本功能。


### 2. 分类

1. class RNNCell(base_layer.Layer)

2. class BasicRNNCell(RNNCell):
```python

"""The most basic RNN cell.
  Args:
    num_units: int, The number of units in the RNN cell.
    activation: Nonlinearity to use.  Default: `tanh`.
    reuse: (optional) Python boolean describing whether to reuse variables
     in an existing scope.  If not `True`, and the existing scope already has
     the given variables, an error is raised.
  """

  def __init__(self, num_units, activation=None, reuse=None):
    super(BasicRNNCell, self).__init__(_reuse=reuse)
    self._num_units = num_units
    self._activation = activation or math_ops.tanh
```

3. class GRUCell(RNNCell):
  Gated Recurrent Unit cell (cf. http://arxiv.org/abs/1406.1078).

4. class BasicLSTMCell(RNNCell):
>  For advanced models, please use the full @{tf.nn.rnn_cell.LSTMCell}
  that follows
  
  
  5. class MultiRNNCell(RNNCell):
```python

 def __init__(self, cells, state_is_tuple=True):
    """Create a RNN cell composed sequentially of a number of RNNCells.
    Args:
      cells: list of RNNCells that will be composed in this order.
      state_is_tuple: If True, accepted and returned states are n-tuples, where
        `n = len(cells)`.  If False, the states are all
        concatenated along the column axis.  This latter behavior will soon be
        deprecated.
    Raises:
      ValueError: if cells is empty (not allowed), or at least one of the cells
        returns a state tuple but the flag `state_is_tuple` is `False`.
    """
 ```
  
## 3. 类属性

* state_size : 隐层的大小
* output_size : 输出的大小

通常是将一个batch送入模型计算，设输入数据的形状为(batch_size, input_size)，
那么计算时得到的隐层状态就是(batch_size, state_size)，输出就是(batch_size, output_size)。

## 4.

* 学习单步的RNN：RNNCell

* 学习如何一次执行多步：tf.nn.dynamic_rnn


* 学习如何堆叠RNNCell：MultiRNNCell


[详见link](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Tensorflow%E5%9F%BA%E7%A1%80%E5%AD%A6%E4%B9%A0.ipynb)

## 5. 数据集准备



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E5%88%86%E5%89%B2%E6%95%B0%E6%8D%AE%E9%9B%86.png" width="600"/> </div><br>




* 假如我们目前手里有一个序列1-12，
* 在LSTM中，batch_size意味着每次向网络输入多少个样本，在上图中，当我们设置batch_size=2时，我们会将整个序列划分为6个batch，每个batch中有两个数字。
> 关于batch-size https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network

* 然而由于RNN中存在着“记忆”，也就是循环。事实上一个循环神经网络能够被看做是多个相同神经网络的叠加，在这个系统中，每一个网络都会传递信息给下一个。上面的图中，我们可以看到整个RNN网络由三个相同的神经网络单元叠加起来的序列。那么在这里就有了第二个概念sequence_length（也叫steps），中文叫序列长度。上图中序列长度是3，可以看到将三个字符作为了一个序列。

* 定义一个batch中的序列个数为N（即batch_size），定义单个序列长度为M（也就是我们的num_steps）。那么实际上我们每个batch是一个N \times M的数组，相当于我们的每个batch中有N\times M个字符。在上图中，当我们设置N=2， M=3时，我们可以得到每个batch的大小为2 x 3 = 6个字符，整个序列可以被分割成12 / 6 = 2个batch。

-------







# 参考

* rnn_cell_impl.py---源码-----https://github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/rnn_cell_impl.py

* TensorFlow中RNN实现的正确打开方式---https://zhuanlan.zhihu.com/p/28196873

* https://zhuanlan.zhihu.com/p/27087310



