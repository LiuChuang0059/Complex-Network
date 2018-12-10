# Summary


# 1. 核信号的 Active曲线 --> Dose 分布曲线

> 核信号 对非均匀介质不敏感

* LSTM
* GRU
* Seq2Seq ?

----

<div align="center"> <img src="https://github.com/LiuChuang0059/ML_Project/blob/master/Project/Project_upgrade_1208/Result_summary/30%20Units-%201layer%20-%20BiGRU.png" width="1000"/> </div><br>



-----------
--------

# 2. 压强(剂量)分布重现

* 质子束打入人体后，会与人体内的原子核和电子反应，在剂量沉积区域由于能量迅速升高会有压强变化，从而诱导声波产生


* 压强(剂量)到声波分布可计算，不同介质里面振幅和相位的变化系数不一样。

* 声波信号传播 类似于 波的叠加。--折射 反射 衍射 干涉


* 传统方法， 很难获得解析形式，很难形成自动化工程。





<div align="center"> <img src="https://github.com/LiuChuang0059/ML_Project/blob/master/Picture/CT_%E5%A3%B0%E6%B3%A2%E4%BC%A0%E6%92%AD.png" width="600"/> </div><br>



<div align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/5/54/Huygens_principle.gif" width="300"/> </div><br>







------
------



# 3. 路径分析

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/Untitled%20Diagram.png" width="600"/> </div><br>


* 人体的 CT 图

* 蓝色的为 激发点， 红色的为观测点

----

1.Input ： 

* 激发点位置， 接受到波的观察点的位置，

* 节点 ----- 有不同的物理性质

* 波传输的时间
-----

2. Output：

* 确定 从激发点 到 观察点的路径


-----
3. Detail


* 节点划分 --- 网格  （或者其他）
 
 **节点对波的传输的方向(相位--角度)，传输时间有影响**

* 节点受相邻节点影响较大---- 因为波的传播选择 “最短路径“


----
----


# 4. 医学物理研究中心

1. 医学物理研究中心 -- [link](http://medphysics.whu.edu.cn/list/2.html)


2. 智慧医疗 --- [link](http://medphysics.whu.edu.cn/list/33.html)


3. 彭浩老师-- [个人主页](http://medphysics.whu.edu.cn/view/123.html) 








