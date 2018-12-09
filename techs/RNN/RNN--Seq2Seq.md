#  编码-解码模型



> The main idea behind this is that it contains an encoder RNN (LSTM) and a decoder rnn. One to ‘understand’ the input sequence and the decoder to ‘decode’ the ‘thought vector’ and construct an output sequence.


> Encoder 与Decoder 不一定都只有RNN，可以让CNN 与RNN 一起当Encoder，负责将影像编码成向量，而Decoder 根据这个向量来生成描述，这样就能让机器描述图片中发生了什么：


# 1. 模型

### 1. Encoder-Decoder结构先将输入数据编码成一个上下文向量c：

1. 最简单的方法就是把Encoder的最后一个隐状态赋值给c

2. 还可以对最后的隐状态做一个变换得到c，

3.  也可以对所有的隐状态做变换

### 2. 拿到c之后，就用另一个RNN网络对其进行解码

* c当做之前的初始状态h0输入到Decoder

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/Seq2Seq%E6%A8%A1%E5%9E%8B1.jpg" width="400"/> </div><br>

* c当做每一步的输入：



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/Seq2Seq%E6%A8%A1%E5%9E%8B2.jpg" width="400"/> </div><br>

-----
-----

# 2. 优缺点
### 1. Pros：
* 输入输出长度不一定相同

* 叠加其他的 CNN 进行编码


### 2. 缺点：

* 编码器 RNN 输出的上下文 C 的维度太小而难以适当地概括一个长序列

### 3. 改进：
* 引入将序列 C 的元素和输出序列的元素相关联的 注意力机制(attention mechanism)

-----
-----

# 3. Attention机制
**Attention机制通过在每个时间输入不同的c来解决这个问题**

> 每一个c会自动去选取与当前所要输出的y最合适的上下文信息。具体我们用 $a_{ij}$ 衡量Encoder中第j阶段的hj和解码时第i阶段的相关性，最终Decoder中第i阶段的输入的上下文信息 c_i 就来自于所有 h_j 对 a_{ij} 的加权和

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6.jpg" width="400"/> </div><br>

1. $a_{ij}$ 的计算

实际和Decoder的第i-1阶段的隐状态、Encoder第j个阶段的隐状态有关。

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/a%E7%9A%84%E8%AE%A1%E7%AE%97.jpg" width="400"/> </div><br>

------
------

# 4. 图解

![](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN_1.gif)


![](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/seq2seq_4.gif)


![](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/seq2seq_5.gif)

![](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/seq2seq_6.gif)

![](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/seq2seq_7.gif)


![](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/attention_process.gif)


![](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/attention_tensor_dance.gif)


![]()

------
-----
# 参考


* 深度学习---Ian Goodfellow and Yoshua Bengio and Aaron Courville

* 完全图解RNN、RNN变体、Seq2Seq、Attention机制--https://zhuanlan.zhihu.com/p/28196873

*  图解---https://zhuanlan.zhihu.com/p/40920384


* rnn_cell_impl.py---源码-----https://github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/rnn_cell_impl.py

* 动态图解 Seq2Seq-- https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/

* Attention机制详解（一）——Seq2Seq中的Attention ---https://zhuanlan.zhihu.com/p/47063917



