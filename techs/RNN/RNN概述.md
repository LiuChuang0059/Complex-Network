# 1. Sequence to Sequence 
> The main idea behind this is that it contains an encoder RNN (LSTM) and a decoder rnn. 
> One to ‘understand’ the input sequence and the decoder to ‘decode’ the ‘thought vector’ and construct an output sequence.

* Encoder 与Decoder 不一定都只有RNN，可以让CNN 与RNN 一起当Encoder，负责将影像编码成向量，而Decoder 根据这个向量来生成描述，这样就能让机器描述图片中发生了什么：



# 循环神经网络 -- Recurrent neural network

* RNN多种类型

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E7%B1%BB%E5%9E%8B.png" width="800"/> </div><br>

# 1. define 
1. 用于处理序列数据的神经网络

2. 时间步索引不必是字面上现实世界中流逝的时间。有时，它仅表示序列中的位置。 RNN 也可以应用于跨越两个维度的空间数据(如图像)。

3. 循环神经网络使用式

$h(t) =f(h(t−1),x(t);θ)$

4. RNN 典型结构 
<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E5%85%B8%E5%9E%8B%E7%BB%93%E6%9E%84.png" width="800"/> </div><br>

* 左面是回路图，
* 右边是展开图： 其中每一个组件由许多不同的变量表 示，每个时间步一个变量，表示在该时间点组件的状态

5. 展开的循环架构 分解为函数的循环使用

Pros：
 * 无论序列的长度，学成的模型始终具有相同的输入大小，因为它指定的是从一 种状态到另一种状态的转移，而不是在可变长度的历史状态上操作。
 * 我们可以在每个时间步使用相同参数的相同转移函数 f
 
 学习在所有时间步和所有序列长度上操作单一的模型 f 是可能的， 而不需要在所有可能时间步学习独立的模型 g(t)。
 
 学习单一的共享模型允许泛化到 没有见过的序列长度(没有出现在训练集中)，并且估计模型所需的训练样本远远少 于不带参数共享的模型。


-----
-----

# 2. 设计 循环神经网络

### 0. 设计模式

1. 每个时间步都有输出，并且隐藏单元之间有循环连接的循环网络


<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E6%A8%A1%E5%BC%8F1.png" width="600"/> </div><br>
* 选择将想要的任何信息 放入隐藏表示h ， 并传递到未来

2. 每个时间步都产生一个输出，只有当前时刻的输出到下个时刻的隐藏单元之间
有循环连接的循环网络


<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E6%A8%A1%E5%BC%8F2.png" width="600"/> </div><br>

*  将特定的输出值传播到未来，缺乏一些关键信息（因为输出单元明确地训练成匹配训练集的目标，它 们不太能捕获关于过去输入历史的必要信息）---更容易训练

3.  隐藏单元之间存在循环连接，但读取整个序列后产生单个输出的循环网络

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E6%A8%A1%E5%BC%8F3.png" width="600"/> </div><br>

* 网络可以用于概括序列并产生用于进一步处理的固定大小的表示。在结束处可能存在目标(如此处所示)，或者通过更 下游模块的反向传播来获得输出 o(t) 上的梯度。


-----

### 1.导师驱动过程（teacher forcing）和输出循环网络

1. 因为训练集提供输出的理想值，所以 没有必要先计算前一时刻的输出。在时刻 t + 1 接收 真实值 y(t) 作为输入
因此训 练可以并行化，即在各时刻 t 分别计算梯度


2. 缺点：

* 训练期间该网络看到的输入与测试时看到的会有很大的不同 


<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E5%AF%BC%E5%B8%88%E9%A9%B1%E5%8A%A8%E8%BF%87%E7%A8%8B.png" width="400"/> </div><br>

* 改善：随意选择生成值或真实的数据值作为输入以减小训练时和测试时看到的输入 之间的差别。这种方法利用了课程学习策略，逐步使用更多生成值作为输入。

-------

### 2. 通过时间反向传播(back-propagation through time, BPTT)---计算神经网络梯度

* 与 x 序列配对的 y 的总损失就是所有时间步的损失之和

* 梯度计算涉及执行 一次前向传播，接着是由右到左的反向传播。
* 运行时间是 O(τ)，并且不能通过并行化来降低，因为前向传播图是固有循序的; 每个时间步只能一前一后地计算。
* 前向传播中的各个状态必须保存，直到它们反向 传播中被再次使用，因此内存代价也是 O(τ)

------

### 3. 基于上下文的 RNN 序列建模


1. 当 x 是一个固定大小的向量时，我们可以简 单地将其看作产生 y 序列 RNN 的额外输

* 在每一个时刻作为一个额外的输入

* 作为初始状态

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E4%BD%9C%E4%B8%BA%E9%A2%9D%E5%A4%96%E7%9A%84%E8%BE%93%E5%85%A5.png" width="800"/> </div><br>

* 将固定长度的向量 x 映射到序列 Y 上分布的 RNN。🌟

这类 RNN 适用于很多任务如图注， 其中单个图像作为模型的输入，然后产生描述图像的词序列。观察到的输出序列的每个元素 y(t) 同时用作输入(对于当前时间步)和训练期间的目标(对于前一时间步)。




2. RNN 可以接收向量序列 x(t) 作为输入
<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E6%8E%A5%E6%94%B6%E5%90%91%E9%87%8F%E8%BE%93%E5%85%A5.png" width="800"/> </div><br>

* 我们可以在时刻 t 的输出到时刻 t + 1 的隐藏单元添加连接


对比 图 10.3 ，此 RNN 包含从前一个输出到当前状态的连接。
这些连接允许此RNN对给定 x 的序列后 相同长度的 y 序列上的任意分布建模。
图 10.3 的 RNN 仅能表示在给定 x 值的情况下，y 值彼此 条件独立的分布。


------
------

# 3. 双向 RNN 
> 在许多应用中，我们要输出的 y(t) 的预测可能依赖于整个输入序列。例 如，在语音识别中，由于协同发音，当前声音作为音素的正确解释可能取决于未来 几个音素，甚至潜在的可能取决于未来的几个词

1. 双向 RNN 结合时间上从序列起点开始移动的 RNN 和另一个时间上 从序列末尾开始移动的 RNN

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E5%8F%8C%E5%90%91RNN.png" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E5%8F%8C%E5%90%91RNN.png" width="600"/> </div><br>

**2维输入--- 四个RNN组成，那在 2 维网格每个点 (i, j) 的输出 out 就能计算一个能捕捉到大多局部信息但仍依 赖于长期输入的表示** 🌟

-------
-----
# 4. 基于编码-解码的序列到序列架构
1. 想法：

(1) 编码 器(encoder)或读取器(reader) 或输入 (input) RNN 处理输入序列。编码器输出 上下文 C(通常是最终隐藏状态的简单函数)。

(2)解码器(decoder)或写入器 (writer) 或输出 (output) RNN 则以固定长度的向量为条件产生输出 序列 Y = (y(1),...,y(ny))


2. Pros：

创新之处在于长 度 nx 和 ny 可以彼此不同

3. 不足：

编码器 RNN 输出的上下文 C 的维度太小而难以适 当地概括一个长序列

4. 改进：

引入将序列 C 的元素和输出序列的元素相关联的 注意力机制(attention mechanism)

----
-----



# 5. 深度循环网络


1. 大多数的 RNN

* 从输入到隐藏状态，

* 从前一隐藏状态到下一隐藏状态

* 从隐藏状态到输出

每一块对应一个浅变换--深度 MLP 内单个层来表示的变换



2. RNN 状态分为多层


<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E6%B7%B1%E5%BA%A6RNN.png" width="600"/> </div><br>


* a : 隐藏循环状态可 以被分解为具有层次的组

* b:  可以向输入到隐藏，隐藏到隐藏以及隐藏到输出的部分引入更深的 计算 (如 MLP)。这可以延长链接不同时间步的最短路径

* c: 可以引入跳跃连接来缓解路径延长 的效应。


-------
------

# 6. 递归神经网络

> 递归神经网络代表循环网络的另一个扩展，它被构造为深的树状结构而不是 RNN 的链状结构，因此是不同类型的计算图。

pros:
对于具有相同长度 τ 的序列，深度(通过非线性 操作的组合数量来衡量)可以急剧地从 τ 减小为 O(logτ)

-----
-----

# 7. 梯度消失或者爆炸

1. 循环网络涉及相同函数的多次组合，每个时间步一次。这些组合可以导致极端 非线性行为
<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E9%9D%9E%E7%BA%BF%E6%80%A7.png" width="400"/> </div><br>

* 在标量情况下，多次乘一个权重 w。该乘积wt 消失还是爆炸取决于 w 的幅值

* 循环神经网络所使用的函数组合有点像矩阵乘法
特征值提升到 t 次后，导致幅值不到一的特征值衰减到零，而幅值大于一的就会激增。任何不与最大特征向量对齐的 h(0) 的部分将最终被丢弃


增加了需要捕获的依赖关系的跨度， 基于梯度的优化变得越来越困难，SGD 在长度仅为 10 或 20 的序列上成功训练传 统 RNN 的概率迅速变为 0。



-------
------

# 8. 回声状态网络 echo state network
> 储层计算循环网络:将任意长度 的序列(到时刻 t 的输入历史)映射为一个长度固定的向量(循环状态 h(t))，之后 可以施加一个线性预测算子(通常是一个线性回归

回声状态网络的策略是简单地固定权重使其具有一定的谱半径如 3，其中信息通过时间前向传播，但会由于饱和非线性单元(如 tanh)的稳定作用而不会爆炸。



# 9. 渗漏单元和其他多时间尺度的策略

> 使模型的某些部 分在细粒度时间尺度上操作并能处理小细节，而其他部分在粗时间尺度上操作并能 把遥远过去的信息更有效地传递过来

1. 时间维度的跳跃链接
> 增加从遥远过去的变量到目前变量的直接连接是得到粗时间尺度的一种方法


2. 渗漏单元和一些列不同时间尺度 
> 对某些 v 值应用更新 μ(t) ← αμ(t−1) + (1 − α)v(t) 累积一个滑动平均值 μ(t)， 其中 α 是一个从 μ(t−1) 到 μ(t) 线性自连接的例子。
当 α 接近 1 时，滑动平均值能记 住过去很长一段时间的信息，而当 α 接近 0，关于过去的信息被迅速丢弃。线性自连 接的隐藏单元可以模拟滑动平均的行为。
这种隐藏单元称为 渗漏单元(leaky unit)。

* 使用权重接近 1 的线性自连接是确保该单元可以访问过去值的不同方式。线性自连接通过 调节实值 α 更平滑灵活地调整这种效果，而不是调整整数值的跳跃长度。

3. 删除连接

> 主动删除长度 为一的连接并用更长的连接替换它们,收到这种新连接的单元，可以学习在长时间 尺度上运作，但也可以选择专注于自己其他的短期连接

-----
----

# 10. 门控 RNN 
> 渗漏单元通过手动选择常量的连接权重或参数化的连接权重来 达到这一目的。
门控 RNN 将其推广为在每个时间步都可能改变的连接权重。


## 1. LSTM 

### 1. 简述

1. 引入自循环的巧妙构思，以产生梯度长时间持续流动的路径

2. 使自循环的权重视上下文而定，而不是固定的


* LSTM 块



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/LSTM%E5%9D%97.png" width="600"/> </div><br>


* LSTM 循 环网络除了外部的 RNN 循环外，还具有内部的 “LSTM 细胞’’ 循环(自环)

* 每个单元有相同的输入和输出，但也有更多的参数和控制信息流动的门控单元系统

* 最重要的组成部分是状态单元 s(t)，类似于渗透单元的线性自环，。然而，此处自环的权重(或相关联的时间常数)由 遗忘门 (forget gate) f(t) 控制

----
### 2. 从RNN到LSTM

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E6%A8%A1%E5%BC%8F1.png" width="600"/> </div><br>

* 如果我们略去每层都有的o(t),L(t),y(t)，则RNN的模型可以简化成如下图的形式

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/RNN%E7%AE%80%E5%8C%96%E6%A8%A1%E5%9E%8B.png" width="600"/> </div><br>

* 隐藏状态h(t)由x(t)和h(t−1)得到。得到h(t)后一方面用于当前层的模型损失计算，另一方面用于计算下一层的h(t+1)。

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/LSTM%E7%BB%93%E6%9E%84%E5%9B%BE.png" width="800"/> </div><br>


### 3. LSTM 模型结构解析
##### 1. 细胞状态
<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E7%BB%86%E8%83%9E%E7%8A%B6%E6%80%81.png" width="600"/> </div><br>

##### 2. 遗忘门 ---- 一定的概率控制是否遗忘上一层的隐藏细胞状态

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E9%81%97%E5%BF%98%E9%97%A8.png" width="600"/> </div><br>


* 输入的有上一序列的隐藏状态h(t−1)和本序列数据x(t)，通过一个激活函数，一般是sigmoid，得到遗忘门的输出f(t)

* sigmoid-- 输出在[0,1] 之间， 输出代表遗忘上一层隐藏细胞状态的概率


##### 3. LSTM -输入门
<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E8%BE%93%E5%85%A5%E9%97%A8.png" width="600"/> </div><br>

* 一部分使用了sigmoid激活函数，输出为i(t）
$$i^{(t)} = \sigma(W_ih^{(t-1)} + U_ix^{(t)} + b_i)$$
*  另一部分使用了tanh激活函数，输出为a(t)
$$a^{(t)} =tanh(W_ah^{(t-1)} + U_ax^{(t)} + b_a)$$

*  i(t) 和 a(t) 相乘更新细胞状态


##### 4. LSTM 细胞状态更新


<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E7%BB%86%E8%83%9E%E7%8A%B6%E6%80%81%E6%9B%B4%E6%96%B0.png" width="600"/> </div><br>


细胞状态C(t)由两部分组成，第一部分是C(t−1)和遗忘门输出f(t)的乘积，第二部分是输入门的i(t)和a(t)的乘积，即：

$$C^{(t)} = C^{(t-1)} \odot f^{(t)} + i^{(t)} \odot a^{(t)}$$


##### 5. 输出门

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E8%BE%93%E5%87%BA%E9%97%A8.png" width="600"/> </div><br>

藏状态h(t)的更新由两部分组成，第一部分是o(t), 它由上一序列的隐藏状态h(t−1)和本序列数据x(t)，以及激活函数sigmoid得到，第二部分由隐藏状态C(t)和tanh激活函数组成, 

$$o^{(t)} = \sigma(W_oh^{(t-1)} + U_ox^{(t)} + b_o)$$
$$h^{(t)} = o^{(t)} \odot tanh(C^{(t)})$$













------





## 2. GRU--- 门控循环单元







----
-----









# 参考资料

* 深度学习---Ian Goodfellow and Yoshua Bengio and Aaron Courville

* https://www.cnblogs.com/pinard/p/6519110.html

* Andrew Ng


































