# LSTM 学习


# LSTM 数据准备输入

## 1. LSTM 输入层

```python

model = Sequential()
model.add(LSTM(32,input_shape=(50,2)))
model.add(Dense(1))
```

LSTM 输入是三维的

* 样品 ： 一个序列是一个样本。批次由一个或多个样本组成。

* 时间步 ： 一个时间步代表样本中的一个观察点。 （50个时间步长，2个特征）

* 特征 ： 一个特征是在一个时间步长的观察得到的。



```python
data= data.reshape(1,10,1)  # 每个时间步长一个样本 需要10个时间步长和1个特征。
model.add(LSTM(32,input_shape(10,1)))
```
该数据现在可以为input_shape（10，1）的LSTM的输入（X）。

----

## 2.全连接层


* A TimeDistributed wrapper layer is used around the output layer so that one value per timestep can be predicted given the full sequence provided as input.

* This requires that the LSTM hidden layer returns a sequence of values (one per timestep) rather than a single value for the whole input sequence.


## 3. Comparing Bidirectional LSTM Merge Modes

There a 4 different merge modes that can be used to combine the outcomes of the Bidirectional LSTM layers.

They are concatenation (default), multiplication, average, and sum.

```python
model.add(Bidirectional(LSTM(20, return_sequences=True), input_shape=(n_timesteps, 1), merge_mode=mode))
‘sum','ave','mul','concat'
```
* ‘sum‘: The outputs are added together.
* ‘mul‘: The outputs are multiplied together.
* ‘concat‘: The outputs are concatenated together (the default), providing double the number of outputs to the next layer.
* ‘ave‘: The average of the outputs is taken.

## 2. LSTM -keras 实现例子


[LSTM模型预测股价基于Keras](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/RNN/LSTM-keras.ipynb)

Dataset --[train](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Dataset/NSE-TATAGLOBAL.csv)---[test](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Dataset/tatatest.csv)







# 参考

* 如何为LSTM重新构建输入数据（Keras）--- https://www.jianshu.com/p/246f117af8f0

* Data and Notebook for the Stock Price Prediction Tutorial-- https://github.com/mwitiderrick/stockprice

* https://machinelearningmastery.com/develop-bidirectional-lstm-sequence-classification-python-keras/
