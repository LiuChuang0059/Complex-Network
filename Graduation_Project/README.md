# 毕业设计


#  1. 研究方向


## 1 目前工作

### 1. activity 曲线 ---->  dose 曲线

* RNN + LSTM
* RNN + GRU
* RNN + BiLSTM
* Seq2Seq 

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/3000-50-1.png" width="800"/> </div><br>

---------

### 2. CT 图探测信号 -----> 布拉格峰位置



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/CT%E5%9B%BE.png" width="400"/> </div><br>

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/CT%E5%9B%BE2.png" width="400"/> </div><br>

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/CT%E5%9B%BE3.png" width="400"/> </div><br>


---------


### 3.  LDA + RNN  推荐系统



----------
----------

## 2. 想法 💡

### 1.  确定经过的节点路径 --- 医学物理

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/Untitled%20Diagram.png" width="600"/> </div><br>

* 人体的 CT 图

* 蓝色的为 激发点， 红色的为观测点

* 每个点 有不同的物理性质

* 确定 从激发点 到 观察点的路径


------

### 2. 天文数据处理 --- 类似于 CT图 探测信号

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/%E5%A4%A9%E6%96%87%E9%A2%91%E8%B0%B1%E5%9B%BE.png" width="600"/> </div><br>

> LAMOST数据集中的每一条光谱提供了3690-9100埃的波长范围内的一系列辐射强度值。光谱自动分类就是要从上千维的光谱数据中选择和提取对分类识别最有效的特征来构建特征空间 ，并运用算法对各种天体进行区分。----- [阿里云天池大赛2018](https://tianchi.aliyun.com/competition/information.htm?spm=5176.11165320.5678.2.1c1b21e1sp8ntD&raceId=231646)


> 模板匹配、支持向量机、近邻方法、神经网络、概率神经网络、径向基神经网络、小波变换、主分量分析、小波分析、最小距离方法等。其中神经网络和主分量分析是应用最为广泛和深入的方法

* 1.CNN  

* 2.主动学习--active learning

> 数据标注代价高昂，我们也面临着如何以最少量的样本，来获得最有效学习模型的问题. 迭代地从未标注数据里面挑选出一部分重要数据去标注，从而获得更多有标记数据。所以主动学习的目标是希望用最小标注代价获得最好的学习模




*  数据公开，数据集多
*  数据量大，较复杂



------

### 3. 图片推断生成

1. 一系列星空图 ，推断未来的星空图 ---- 数据多，意义不大

2. 癌变的CT 图 ，推断未来的癌变图  ---- 数据少，需要较高精度，和一定可解释性

* 1.  提取特征 ， 特征和相应的图像训练gan模型

* 2.  特征使用RNN ， 预测未来的 特征

* 3.  未来特征 生成星空图像


----------

 
### 4. 质心 -- 节点 



<div align="center"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR2vV9Mx9Xl-6RYp2ZSN-mopLarrRJF6sh8jmr2q2UXS1jhNkQzg" width="400"/> </div><br>


1. 节点的重要性衡量：

距离 + 度


2. 社区的描述

* 质心 ： 质点组的质量 全部集中在质心

* 质点的运动 = 质心的运动 + 质点相对与质心的yundong

* 作用于各个质点的外力，相当于作用于质心

* 质点有进一步的动力学特征


 
 ----------
 
 
### 5. 复杂电路 --- 环状网络


<div align="center"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLPmTtPRwzCWmS9DQuWDf_Oy6yv2JXipSIl4Ddy8AtSD3VG33_KA" width="400"/> </div><br>


* 基尔霍夫方程组

节点的电流方程组 ： 汇流于节点的电流为 0

回路电压方程组 ： 沿着回路一周，电势的数值不变


* 考虑

电源 对应传播源

加入电容 电感 ---交流电路

电感： 阻高频，通低频

电容： 阻低频，通高频
 
 
 
 --------
 
 ### 6. k - 核  ----- 等势面 or  原子跃迁轨道
 
 
 <div align="center"> <img src="https://gss0.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/b2de9c82d158ccbf5ab7f1791bd8bc3eb135416d.jpg" width="600"/> </div><br>
 
 <div align="center"> <img src="http://pgyw.gxkjwx.com:82/DRCNet.Mirror.Documents.Web/docImage.aspx?ImageID=2657491" width="600"/> </div><br>
 
 <div align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Bohr_atom_model.svg/250px-Bohr_atom_model.svg.png" width="600"/> </div><br>
 
 
 
 * 等势面 密集的地方场强大，稀疏的地方 场强小
 
 * 能级图：  离散 
 
 -------
 
 ### 7.  人类运动 ----- 电子的准经典运动
 
 电子在外力的作用下运动 ： 即受到晶体的周期性势场的作用，也收到外力的作用 --- 准经典运动
 
 周期性 ：上班 --- 外力 ：节假日
 
 
 ### 8. 多体 
 
 1. 力学中：  至多 三体问题 + 限制条件
  
  
 2.  固体物理中解决多体问题： 
 
 晶体中的多电子问题简化为一个 在所有晶格离子 的周期场V 以及其他的电子的平均场中运动的单电子问题
 
 可以 进一步考虑 电子之间的交互关联作用
 
 
 
 
 
 
 
 
 
 
 





