# 推荐算法 

## 0. 典型的推荐算法

* 协同过滤
* GBDT --深度学习
* Factorization Machine ---深度学习

* DNN

* Logistic Regression

----
* 深度学习;
• 社会化推荐;
• 学习排序;
• 多臂Bandit(探索/利用);
• 张量因子分解和因子分解(情境感知的推荐)

------
------


## 1. 开源工具

* 用户不多， 慎用 分布式版本

### 1. 内容分析
<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/Image/%E5%BC%80%E6%BA%90-%E5%86%85%E5%AE%B9%E5%88%86%E6%9E%90%E3%80%81.png" width="600"/> </div><br>


* FasText 还提供分类功能，效果几乎等同于CNN ，效率和线性模型一样


* 主题模型还有 百度的 Familia 

* 嵌入 还有 FAIR 的starspace 


### 2.  协同过滤和矩阵分解

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/Image/%E5%BC%80%E6%BA%90-%E5%8D%8F%E5%90%8C%E8%BF%87%E6%BB%A4%2B%E7%9F%A9%E9%98%B5%E5%88%86%E8%A7%A3.png" width="600"/> </div><br>



### 3. 模型融合

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/Image/%E5%BC%80%E6%BA%90-%E6%B7%B7%E5%90%88%E6%A8%A1%E5%9E%8B.png" width="600"/> </div><br>



#### 4. 完整项目推荐

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/Image/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE-%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F.png" width="600"/> </div><br>


------
------
## 2. 业界个性化推荐系统

### 1. 今日头条的推荐系统

#### 1. 推荐系统，如果用形式化的方式去描述实际上是拟合一个用户对内容满意度的函数，这个函数需要输入三个维度的变量。

* 第一个维度是内容

* 第二个维度是用户特征

* 第三个维度是环境特征


#### 2. 隐形语义特征 --- 语义标签

#### 3. 层次化文本分类算法
元分类器类型  ---  SVM ； SVM + CNN ； SVM+ CNN+ RNN

-----
### 2.  淘宝推荐系统
-----

### 3. 豆瓣

> 即选择多样、口味很重要、单位成本不重要，同时能够广泛传播 (InformationCascade)的产品；接着在对真实的数据集进行定量分析后，进一步得出，应该是条目增长相对稳定、能够快速获得用户反馈，数据稀疏性与条目多样性、时效性比较平衡的产品，才是适合推荐的产品。
其次，豆瓣网的推荐引擎面对高成长性的挑战，通过降低存储空间，近似算法与分布式计算的设计，来实现对基于用户的协同过滤推荐系统的线性扩展。
> 括倾向于给出平庸的推荐，有信息无结构，以及缺乏对用户的持续关注等黑盒推荐问题。豆瓣提出了分为 Prediction，Forecasting，Recommendation 三个阶段的下一代推荐系统，并探讨了一种下一代推荐引擎的构想——基于用户行为模型的、有记忆的、可进化的系统。


### 4. Hulu的个性化推荐
* 它包含了基于物品的协同过滤机制，基于内容的推荐，基于人口统计的推荐，从用户行为中提炼出来的主题模型，以及根据用户反馈信息对推荐系统的优化



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/%E5%9B%BE%E4%B9%A6%E8%AF%84%E5%88%86%E7%9F%A9%E9%98%B5.png" width="400"/> </div><br>

--------

### 5. YouTube视频推荐
[link](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0--%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F.md)

-----

### 6.  Spotify 推荐模型
[link](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0--%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F.md)





------
------

## 3. 个性化推荐算法

<div align="center"> <img src=https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F%E7%AE%97%E6%B3%95.png" width="600"/> </div><br>


### 1. 基于人口统计学的推荐 ---- Demographic-based Recommendation

>  简单的额根据系统用户的基本信息 发现用户的相关程度， 后将相似用户喜爱的其他物品推荐给当前用户
  *  优点(Pros)： 简单，不使用当前用户对物品的喜好历史数据，所以对于新用户来讲没有“冷启动（Cold Start）”的问题。
  * 缺点(Cons)：  分类粗糙， 用户信息涉密
  
-----

### 2. 基于内容的推荐(Content-Based Recommendation) --- [详述link](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/%E5%86%85%E5%AE%B9%E6%8E%A8%E8%8D%90.md)

> 针对文章本身抽取一些tag作为该文章的关键词，继而可以通过这些tag来评价两篇文章的相似度。 推荐相似的物品
  * 优点： 不需要用户数据 ；； 不存在过度推荐热门，不存在冷启动问题
  
  * 缺点：缺点在于抽取的特征既要保证准确性又要具有一定的实际意义，否则很难保证推荐结果的相关性

> 基于内容的推荐中，假设可以获取到 item 的描述信息， 并将其作为 item 的特征向量(例如标题、年份、描述)。这些特征向量 被用于创建一个反映用户偏好的模型。各种信息检索(例如 TF-IDF)和 机器学习技术(例如朴素贝叶斯、支持向量机、决策树等)可被用于创建 用户模型，从而为用户产生推荐。

1.  如图1，是评分矩阵、
2. 首先，基于书籍的内容（标题，高频词汇，作者等等特征）--转化成向量， 计算书籍之间的相似度 
3. 我们选取一个用 户此前评分过的书籍，并推荐与它们最相似的书籍。（类似于协同过滤法）

-------

### 3. 基于关联规则的推荐
>  挖掘出关联规则，也就是那些同时被很多用户购买的物品集合，这些集合内的物品可以相互进行推


* 优点： 推荐系统一般转化率较高

* 缺点： 计算量较大，但是可以离线计算，因此影响不大。；； 由于采用用户数据，不可避免的存在冷启动和稀疏性问题；；存在热门项目容易被过度推荐的问题


**相当于整合了优点，规避 缺点**
-------------


### 4. 基于协同过滤的推荐(CF)---[详述 link](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/%E8%BF%91%E9%82%BB%E6%8E%A8%E8%8D%90-%E5%8D%8F%E5%90%8C%E8%BF%87%E6%BB%A4.md)

#### 1. 基于用户的协同过滤推荐

> 根据所有用户对物品或者信息的偏好（评分），发现与当前用户口味和偏好相似的“邻居”用户群

* 优点： 因此可以发现用户的潜在兴趣，

* 缺点： 缺点在于一般的Web系统中，用户的增长速度都远远大于物品的增长速度，因此其计算量的增长巨大

1. 使用包含了 用户喜好项的向量(或数组)代表每一个用户，之后使用余弦相似性，构成一个相似矩阵
2. 第一个用户，为他们生成一些推荐。首先，我们找到了与第一个用户最相 似的另一用户，删除用户已经评价过的书籍，给最相似用户正在阅读的书 籍加权，然后计算出总



------

#### 2.  基于物品（项）的协同过滤--   

**有一些类似于基于物品的协同过滤**

> 它使用所有用户对物品或者信息的偏好（评分），发现物品和物品之间的相似度，然后根据用户的历史偏好信息，将类似的物品推荐给用户

* 缺点
  * 方法的核心是基于历史数据，所以对新物品和新用户都有“冷启动”的问题。
  * 推荐的效果依赖于用户历史偏好数据的多少和准确性。
  * 由于以历史数据为基础，抓取和建模用户的偏好后，很难修改或者根据用户的使用演变，从而导致这个方法不够灵活。

1. 使用评 价过一本书的用户向量(或数组)表示这本图书，并比较他们的余弦相似性函数--获得相似性矩阵
2. 为用户进行推荐。我们选取他们评价过的图书，找出与他们最相似的前两本 书，进行加权，然后推荐给用户加权分最高且他没有读过的书
> 该用户 看过的书籍 每一本都有两本相近的书籍 使用看过的书籍的分数✖️ 相似性系数 加权求和，最大的 没读过的，作为推荐

------

#### 3. 基于矩阵分解 ----- 贝叶斯 聚类分析 分类回归 首先玻尔兹曼

1. 矩阵因子分解 将项和用户转化为了 相同的潜在空间-----代表了用户和项之间的潜在相互作用


2. 矩阵分解背后的原理是潜在特征代表了用户如何给项进行评分

----

#### 4.   2007 ProgressPrize of Netflix

1. SVD 

 * 使用随机梯度下降 迭代 近似计算 SVD
 * 使用 SVD分解 用户的特征向量，以及 项的特征向量
 
 

2. RBM ---  Restricted Boltzmann Machines
 * 　RBM可以看做是一个编码解码的过程，从可见层到隐藏层就是编码，而反过来从隐藏层到可见层就是解码
 *  把每个用户对各个物品的评分做为可见层神经元的输入，然后有多少个用户就有了多少个训练样本
 * 对于可见层输入的训练样本和随机初始化的W,a,我们可以用上面的sigmoid激活函数得到隐藏层的神经元的0,1值，这就是编码。然后反过来从隐藏层的神经元值和W,b可以得到可见层输出，这就是解码
 
 * 即上面的对数似然损失函数尽可能小。按照这个损失函数，我们通过迭代优化得到W,a,b，

 *  然后对于某个用于那些没有评分的物品 --我们用解码的过程可以得到一个预测评分，取最高的若干评分对应物品即可做用户物品推荐了。


#### 5. Clustering

1. cluster users and compute per-cluster “typical” preferences

2. Users receive recommendations computed at the cluster level


3. Clustering techs

* k-means and all its variations

* Locality- sensitive- Hashing

* Affinity Propagation

* Spectral Clustering

* LDA

* Non-parametric Bayesian Clustering 
 




### 5. 混合推荐算法


* 不同的推荐方式进行组合----加权 或者 梯度boosted决策树



<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/%E6%B7%B7%E5%90%88%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F.png" width="400"/> </div><br>


<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/%E5%9B%9B%E7%A7%8D%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F.png" width="800"/> </div><br>

----------------

## 4. Index
### 1. ranking ---[详述 link](https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Recommendation_Agorithm/%E6%8E%92%E8%A1%8C%E6%A6%9C.md)
 
 -----
 ### 2 Similarity
 
 **The final concept of “similarity” responds to what users vote
as similar**
 
 * some MAB explore/exploit approach
 
 -----

 ### 3. Deep Learning
 
 * Deep Learning for Collaborative Filtering 
 
  * Reccurrent Network
  
 * Content-basede  
  * CNN
  * Training the deep neural network to predict 40 latent factors
coming from Spotify’s CF solution
 
-----
### 4.  Social and Trust-based recommenders

* 社交推荐
* 评估人和人之间的信任度


----
### 5. 页面优化

*  User Attention Modeling

>  From “Modeling User Attention and Interaction on the Web” 2014 - PhD Thesis by Dmitry Lagun (Emory U.)

---

### 6. EE 问题

* Multi-armed bandit problem, K-armed bandit problem, MAB

 * Thompson采样
 > 假设每个臂是否产生收益，其背后有一个概率分布，产生收益的概率为p;我们不断地试验，去估计出一个置信度较高的*概率p的概率分布*就能近似解决这个问题了。
怎么能估计概率p的概率分布呢？ 答案是假设概率p的概率分布符合beta(wins, lose)分布，它有两个参数: wins, lose。每个臂都维护一个beta分布的参数。每次试验后，选中一个臂，摇一下，有收益则该臂的wins增加1，否则该臂的lose增加1。每次选择臂的方式是：用每个臂现有的beta分布产生一个随机数b，选择所有臂产生的随机数中最大的那个臂去摇

 * UCB算法
 > 先对每一个臂都试一遍,之后，每次选择以下值最大的那个臂


-----
------
## 5.  长尾理论---推荐算法

<div align="center"> <img src="https://github.com/LiuChuang0059/ComplexNetwork-DataMining/blob/master/Image/%E9%95%BF%E5%B0%BE%E7%90%86%E8%AE%BA.png" width="400"/> </div><br>

> 在互联网时代由于 网络技术能以很低的成本让人们去获得更多的信息和选择，在很多网站内有越来越多的原先被“遗忘”的非最热门的事物重新被人们关注起来。事
实上，每一个人的品味和偏好都并非和主流人群完全一致。


* 长尾理论作为一种新的经济模式，被成功的应用于网络经济领域。而 对长尾资源的盘活和利用，恰恰是推荐系统所擅长的，因为用户对长尾内 容通常是陌生的，无法主动搜索，唯有通过推荐的方式，引起用户的注意， 发掘出用户的兴趣，帮助用户做出最终的选择。

* 只依赖最热门内容的另一个不易察觉的危险是潜在用户的流失:因为 只依赖爆款虽然能吸引一批用户(简称 A 类用户)，但同时也悄悄排斥了 对这些热门内容并不感冒的用户(简称 B 类用户)，按照长尾理论，B 类
用户的数量并不少，并且随时间推移 A 类用户会逐步转变为 B 类用户(因 为人们都是喜新厌旧的)，所以依靠推荐系统来充分满足用户个性化、差 异化的需求，让长尾内容在合适的时机来曝光，维护企业健康的生态，才 能让企业的运转更稳定，波动更小。


-------
------

## 6. 评价方法
推荐系统的评价面要宽泛的多，往往推荐结果的数量要多很多，出现 的位置、场景也非常复杂，从量化角度来看，当应用于 Top-N 结果推荐时， MAP(Mean Average Precison)或CTR(Click Through Rate，计算广告 中常用)是普遍的计量方法;当用于评分预测问题时，RMSE(Root Mean Squared Error)或 MAE(Mean Absolute Error)是常见量化方法。
由于推荐系统和实际业务绑定更为紧密，从业务角度也有很多侧面评 价方法，根据不同的业务形态，有不同的方法，例如带来的增量点击，推 荐成功数，成交转化提升量，用户延长的停留时间等指标





------
-------
# 参考
* 推荐算法总结-----https://www.jianshu.com/p/af93e2ff2f83

* 今日头条推荐系统架构-----https://36kr.com/p/5114077.html

* 《推荐系统-理论篇》---InfoQ

* RBM 详解---(https://www.cnblogs.com/pinard/p/6530523.html)


* 专治选择困难症——bandit算法----刑无刀----https://zhuanlan.zhihu.com/p/21388070


* 极客时间 --- 刑无刀
