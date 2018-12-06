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

### 2. CT 图探测信号 -----> 一维剂量分布



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
-----


# 2. 开题摘要 --- CT 图探测信号 -----> 一维剂量分布

题目： 基于神经网络学习方法的质子治疗剂量分布预测

### 1. 目的：
质子治疗是其中一种利用质子束来照射患病的组织的粒子治疗，最常用于治疗癌症。 本文提出一种基于机器学习的方法，快速准确的在基于CT的异构组织中重建剂量分布。用以新患者的计划剂量学特性预测。

### 2. 方法：
收集至少200组不同入射能量，和不同入射方向下，探测器探测的声波波形，以及对应的计算所得的剂量分布。训练基于循环神经网络(RNN)，混合其他的神经网络的模型，建立声波波形信号和对应剂量分布之间的关联。

----



Title: Prediction of  dose distribution in proton therapy based on neural network learning

1. Purpose:
Proton therapy is one of the particle treatments that uses beams of protons to illuminate diseased tissue and is most commonly used to treat cancer. In this paper, we propose a machine learning-based method to rapidly and accurately reconstruct dose distribution in CT-based heterogeneous tissues for clinical prediction of the dosimetric features. 


2. Methods :
At least 200 groups of acoustic wave waveforms detected by the detector and corresponding calculated dose distributions at different incident energies and different incident directions need to be collected. To establish the relationship between the acoustic waveform signal and the corresponding dose distribution, a model which is based on the recurrent neural network (RNN) is trained with 190 randomly selected cases and verified in 10 cases.

-----



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 





