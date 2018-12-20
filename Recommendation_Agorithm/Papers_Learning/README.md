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
-----

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





































