#   相关文献阅读

# 1. Deep Learning based Recommender System: A Survey and New Perspectives -- 2017

* Deep learning is able to effectively capture the non-linear and non-trivial user-item relationships, and enable the codification of more complex abstractions as data representations in the higher layers. Furthermore, it catches the intricate relationships within the data itself, from abundant accessible data sources such as contextual, textual and visual information.

### 1. Multilayer Perceptron based Recommender System


##### 1. 传统的 矩阵分解

* MF模型是用户和项目的潜在因素的双向互动，它假设潜在空间的每一维都是相互独立的并且用相同的权重将它们线性结合。因此，MF可视为隐向量（latent factor）的线性模型。



* 使用一个简单的和固定的内积，来估计在低维潜在空间中用户-项目的复杂交互，从而所可能造成的限制


##### 2. NCF 模型--- NLP

* 用户和商品 分别 embedding 生成向量

* concat 两个向量

* 输入 多层神经网络

* 目标函数  ： 将 yui 的值作为一个标签——1表示项目 i 和用户 u 相关，否则为0。这样，预测分数 ŷ ui 就代表了项目 i 和用户 u 相关的可能性大小。因此，我们需要将网络输出限制到[0，1]的范围内。



##### 3. wide and deeplearning  ----> Deep FM

* DeepFM包含两部分：神经网络部分与因子分解机部分，分别负责低阶特征的提取和高阶特征的提取。这两部分共享同样的输入,




-------


### 2. Autoencoder based Recommender System

##### 1. AutoRec

* I-AutoRec performs better than U-AutoRec, which may be due to the higher variance of user partial observed vectors.
* Different combination of activation functions f (·) and д(·) will influence the performance considerably.
* Increasing the hidden unit size moderately will improve the result as expanding the hidden layer dimensionality gives AutoRec more capacity to model the characteristics of the input.
* Adding more layers to formulate a deep network further improves the performance.


##### 2. CFN -- Collaborative Filtering Neural network

* 加入了去噪声的机制， 模型更加鲁棒
* 加入 side-information ： 例如 个人信息，商品描述


##### 3. CDAE(Collaborative Denoising Auto-Encoder) --- ranking Prediciton

* Parameters are learned by minimizing the reconstruction error:

* 加入负样本，在隐式反馈中， 加快计算速度，减少计算的复杂度。

[YaoWu,ChristopherDuBois,AliceXZheng,andMartinEster.2016.Collaborativedenoisingauto-encodersfortop-nrecommender
systems. In Proceedings of the Ninth ACM International Conference on Web Search and Data Mining. ACM, 153–162.]()



-----

### 3. Convolutional Neural Network based Recommender System

##### 1. BCNN



##### 2. ABCNN(Attention based CNN.)




----


### 4. Recurrent Neural Network based Recommender System

##### 1. Session-based recommendation

> 服务端为特定的对象创建了特定的Session，用于标识这个对象，并且跟踪用户的浏览点击行为。我们这里可以将其理解为具有时序关系的一些记录序列。


* 基于内容的推荐算法和协同过滤推荐算法（model-based、memory-based）在刻画序列数据中存在缺陷：每个item相互独立，不能建模session中item的连续偏好信息。

* 1. item-to-item recommendation approach (Sarwar et al.,2001; Linden et al., 2003) : 采用session中item间的相似性预测下一个item。缺点：只考虑了最后一次的click 的item相似性， 忽视了前面的的clicks, 没有考虑整个序列信息。

* 2. Markov decision Processes （MDPs）（Shani et al., 2002）：马尔科夫决策过程，用四元组<S,A, P, R>（S: 状态, A: 动作, P: 转移概率, R: 奖励函数）刻画序列信息，通过状态转移概率的计算点击下一个动作：即点击item的概率。缺点：状态的数量巨大，会随问题维度指数增加。




-------------
------------

# 2.  Session-based recommendations with recurrent neural networks. (ICLR 2016)

### 1. 模型(GRU4REC)架构（如下图）

* 模型输入: session 中的点击序列, x = [x_{1},x_{2}...x_{r-1},x_{r}] , 1 ≤ r < n，通过one hot encoding 编码，通过embedding层压缩为低维连续向量作为 GRU 的输入。

* 模型输出:每一个item 被点击的预测概率， y =M(x), where y = [y_{1},y_{2}...y_{m}]


### 2. Training data sample：

* 因为item的维度非常高，item数量过大的概率会导致计算量庞大，所以只选取当前的正样本（即下一个点击的item）加上随机抽取的负样本。论文采用了取巧的方法来减少采样需要的计算量，即选取了同一个mini-batch 中其他sequence下一个点击的item作为负样本，用这些正负样本来训练整个神经网络。


### 3. 损失函数

* Pairwise ranking，即正样本的loss要低于负样本。本文使用了两种基于Pairwise ranking的loss function：

	* BPR：一种矩阵分解法，

	* TOP1：一种正则估计



-----------
----------

# 3. Incorporating Dwell Time in Session-Based Recommendations with Recurrent Neural Networks. (RecSys 2017)

**用户在session中的item停留时间越长，越感兴趣**


* 每个item 按照单位时间划分成 d_{t_{i}}/t+1个时间片



-------
--------

# 4. Improved Recurrent Neural Networks for Session-based Recommendations. (DLRS 2016)

### 1.  Data augmentation（数据增强）

* 给定一个session的输入序列 [x_{1},x_{2}...x_{n}] , 可以产生多条训练数据，如（ [x_{1},V(x_{2})], [x_{1},x_{2}, V(x_{3})] ）如下图，可以增加训练数据。此外，用户可能出现误点击的，用dropout 的方式来泛化数据，可以增强训练的鲁棒性。


### 2. Model pre-training

* 在推荐中，对于user和item更新都很快的推荐场景，最近的信息更为重要，文本提出先利用历史所有数据预训练出一个模型，然后只选取最近的数据，以预训练得到的模型权重作为初始化参数，再训练一个最终模型。


### 3. Output embedding

* 直接预测 item 的 embedding 向量。使预测结果更具有泛化意义，相当于预测了用户 embedding后的语义空间中兴趣表示，训练时定义的loss为输出层与该样本在embedding层的cosine相似度。



------
------






















