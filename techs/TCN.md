# TCN -- 处理时间序列

# 传统的RNN +  LSTM

> 即使在理论上 LSTM 可以调整记忆门使得该被记得的东西永远留在单元里面，
但在现实里反而 TCN 可以更实在的留住长远以前的记忆，并且整个框架设计上比 LSTM 更为简单和精确


#  TCN 的 特点

* 其卷积网络层层之间是有因果关系的，意味着不会有“漏接”的历史信息或是未来数据的情况发生，即便 LSTM 它有记忆门，也无法完完全全的记得所有的历史信息，更何况要是该信息无用了就会逐渐被遗忘。

* 这个 model 的架构可以伸缩自如的调整成任何长度，并可以根据输出端需要几个接口就 mapping 成对应的样子，这点和 RNN 的框架意思相同，非常的 flexible。

* 这样的架构只能够看到“历史信息”


# TCN = 1D FCN+ casual convolutions

1.  Causal Convolutions 思维可以用来应付“不漏接”的初衷，卷积层在 t 时间的 output 只与当层和前一个层的元素做卷积，这个方法与 1989 年的 time delay neural network 类似。 

2. 1D 的 fully-convolutional network (FCN) ，让每个输出层都可以保持和输入层一样多的长宽被继续传递，使用的手法是 zero padding，和之前的 CNN architecture 建构方法如出一辙。


# TCN 结构

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/TCN%E7%BB%93%E6%9E%84.png" width="800"/> </div><br>



#  TCN 感受野 (receptive field)

##  1. CNN感受野
1. 一个感受野可以用中心位置(center location)和大小(size)来表征

> 例1. 输入特征图大小为 5*5 ，采用的卷积参数如下：卷积核大小  k=3*3 ，padding大小 p=1*1 ，步长 s=2*2 。经过一次卷积之后，得到大小为 3*3 的输出特征图（绿色）。在这个特征图上继续采用相同的卷积，得到一个 2*2 的特征图（橙色



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/CNN%E7%89%B9%E5%BE%81%E5%9B%BE.jpg" width="800"/> </div><br>

2. (右图)固定大小的CNN可视化，所有的特征图固定大小并保持与输入特征图大小一致
> 每个特征被标记在其感受野所在的中心（从而定位出感受野中心位置）。由于一个特征图中所有的特征都有相同大小的感受野，我们可以简单地在每个特征周围画出一个边界框，从而获得感受野的大小

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/CNN%E7%89%B9%E5%BE%81%E5%9B%BE2.jpg" width="800"/> </div><br>
3. 右图中，浅绿色 和浅黄色为感受野，感受野大小增加迅速，以至于第二个特征层的中心特征的感受野已经覆盖了整个输入特征图

----

## 2. 感受野计算


----

# 空洞卷积---dilated convolution

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E7%A9%BA%E6%B4%9E%E5%8D%B7%E7%A7%AF.gif" width="800"/> </div><br>



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E7%A9%BA%E6%B4%9E%E5%8D%B7%E7%A7%AF.gif" width="800"/> </div><br>


* kernel之间有间隔，，以此来增加 感受野


**空洞卷积可以应用到Seq2Seq**


------

# TCN 代码学习  

https://github.com/philipperemy/keras-tcn#table-of-contents





-------
------
# 参考


* 深度学习 + 论文详解： TCN_时间卷积网络_原理与优势---https://blog.csdn.net/Kuo_Jun_Lin/article/details/80602776


* CNN感受野----https://zhuanlan.zhihu.com/p/35708466


* 如何理解空洞卷积（dilated convolution-----https://www.zhihu.com/question/54149221
