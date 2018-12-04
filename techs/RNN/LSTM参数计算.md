#  样本

shape = （302,1） ，时间步是302， 每个时间步的特征长度是 1 ，选取的 units 是 50， 中间的隐向量是 50 


## 1.  遗忘门

<div align="center"> <img src="http://p6yufwr30.bkt.clouddn.com/%E5%B0%8F%E4%B9%A6%E5%8C%A0/1528854541990.png" width="800"/> </div><br>


* Input ： $h_{t-1}$ 是上一个状态的隐向量， 长度为 50 。 $x_{t}$ 为当前的状态输入，长度为 302 ， $[h_{t-1},x_{t}]$ 的长度 为 352

* Output ： 中间隐向量的长度 50 

*  $[h_{t-1},x_{t}]$ 是 （1，51）向量， 输出 (1,50 ) 向量， 所以 $W_{f} -- (51,50)$ 矩阵； $b_f -- (1,50) $

 $$Params_f = 51*50 + 50 = 2600 $$
 
 
 ## 2. 输入门

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/raw/master/techs/Image/%E8%BE%93%E5%85%A5%E9%97%A8.png" width="800"/> </div><br

$$i^{(t)} = \sigma(W_ih^{(t-1)} + U_ix^{(t)} + b_i)$$

$$a^{(t)} =tanh(W_ah^{(t-1)} + U_ax^{(t)} + b_a)$$


 $$Params_f = 2*(352*50 + 50) = 35300 $$
 
 ## 3. 输出门
 
 <div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/raw/master/techs/Image/%E8%BE%93%E5%87%BA%E9%97%A8.png" width="800"/> </div><br>
 
 $$Params_f = 352*50 + 50 = 17650 $$
 
 ## 4. 细胞状态更新
 
 <div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E7%BB%86%E8%83%9E%E7%8A%B6%E6%80%81%E6%9B%B4%E6%96%B0.png" width="800"/> </div><br>
 
 无参数
 
 
 ## 5. 总参数
 
 $N = 4* ((input + units)* units + units) = 10400$ 
 
 
 
 <div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/techs/Image/%E6%A8%A1%E5%9E%8B%E7%BB%93%E6%9E%84.png" width="600"/> </div><br>

 
 
 
 
 
 
 
 
 
 
 
 
