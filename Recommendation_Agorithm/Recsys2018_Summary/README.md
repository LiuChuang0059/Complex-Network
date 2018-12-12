README.md


# 1. Summary

* 研究问题是否有趣，新颖

* 可解释性

* 推荐结果的公平性和准确性

<div align="center"> <img src="" width="400"/><img src="" width="400"/> </div><br>


# 2. Techs

* Topic modeling

* Causal inference  --- 因果推断

* MOnte Carlo Tree Search

* Link Prediction


-----
-----


## 1. 新问题


* 创意指数     💡💡💡

* 感兴趣指数   🌟🌟🌟

1.  系统生成新的物品 ，使得所有用户喜欢。💡💡  🌟🌟🌟

> 例如设计一款手机 ， 使得所有人都喜欢--- 覆盖所有用户群体的兴趣


*  使用变分自动编码器vae，首先将用户和物品的特征放入这个隐因子的空间里。然后使用贪婪算法，在隐因子空间中选点，然后覆盖所有的用户，最后通过decoder产生新的item。


<div align="center"> <img src="" width="600"/> </div><br>

-----


2. 交通推荐 -- 推荐**舒适**的路线   💡💡💡  🌟🌟

* 自定义舒适因子，影响路线的舒适度

*  评价标准： 50个人 调查----  类似于推荐的满意程度，，隐藏兴趣挖掘

想法💡： 兴趣指数，，提升兴趣指数


-----

3. 页面实时推荐  -- 一个页面覆盖用户感兴趣的不同分类的东西 💡  🌟🌟

* 强化学习

* 实时改变页面


<div align="center"> <img src="" width="600"/> </div><br>

-----


4.  物品的互补推荐。 💡  🌟🌟🌟

> 例如： 买了一个相机。这个时候呢，像相机套呀，镜头呀，自拍控制杆呀，镜头套呀，这些东西就可以被推荐了。
互补推荐系统会在这里面给我们推荐一些我们最可能买

💡💡💡  图书借阅的 互补推荐 + 兴趣推荐  + 最近邻的（多本参考书）

* 人们在 借阅书籍的时候 ，有收集癖好，即使不看，也愿意


<div align="center"> <img src="" width="600"/> </div><br>


-----
-----

## 2. 推荐系统的多样性


1. 算法混淆   💡  🌟🌟🌟

> 在bilibili上看了几个学习的视频。然后呢，我下一次再去这个应用程序。他就一直给我推的视频。我就没法再看其他的视频了。我就一直看学习的视频。然后他还一直推学习的视频，竟然陷入了一个恶性循环中。这样呢，推荐系统就增加了同质性，丧失了多样性。降低他的推荐效果



<div align="center"> <img src="" width="600"/> </div><br>

------

2.  Calibrated --- 按照比例推荐 💡  🌟🌟🌟

> 它是按比例推荐。也就是说用户看了99%的学习的。看了1%的娱乐的。如果是一般的推荐系统，就只给用户推荐他主要的兴趣。
而这里按比例推荐的，就是遵从以前的用户看的这个比例。也给用户推99%学习的和1%娱乐的。这样做到了多样性。

💡 💡 💡 用于 聚类后的推荐



3. 因果推理的技术解决算法混淆  💡 🌟🌟

> 为了某些商业的目的，如何增加点击率和下载量，试图改变用户本身的自然行为，所以我们看到用户点击或者是下载的时候，其实是已经受了推荐算法影响的。这个问题其实就是一个算法混淆的问题。

* 使用 强化学习，消除算法的误差

4. 社交网络的链接推荐   💡 🌟

* 通过一个弱关系的推荐还增强了推荐的多样性。

<div align="center"> <img src="" width="600"/> </div><br>


-------
------



## 3. 可解释性

1. 从评论中生成对用户行为的解释。 💡💡  🌟

> 然后这个模型引入了上下文感知扩展的概率矩阵分解,又结合从评论文当中学习的文本特征，最后预测的评级以及对评级的解释


[Why I like it Multi-task Learning for Recommendation and Explanation]()


<div align="center"> <img src="" width="600"/> </div><br>


---

2. 利用bandit对推荐的解释。 💡💡 🌟🌟🌟

> 强化学习里的两个概念探索和利用。探索呢就是把不确定用户喜不喜欢的商品推荐给用户。来探索用户到底喜欢啥。利用呢就是说从用户已知的用户喜欢的东西里找到用户最喜欢的。

[Explore,Exploit, and Explain: Personalizing Explainnable Recommendations with bandits]()



------
-----


## 4. 辅助推荐



1. 关注用户的不操作 💡 💡   🌟🌟🌟

> 将用户的不作为 分为了 7 类，将推荐问题转化为分类问题

[INterpreting User Inaction in Recommender Systems]()


---


2. 物品相似度算法与推荐质量的关系。💡  🌟 🌟🌟  ❓

* 得到了一个结论，基于内容的推荐算法，在相似度和推荐质量方面要优于基于用户行为的。

[Judging Similarity : A User-Centric Study of Related Item Reconmmendations]()


------
------



## 5. 改进算法

1. 滑动窗机制检测新数据   💡  🌟🌟🌟

* 解决了冷启动

* 利用增量的矩阵分解和主题模型，实时对新数据进行推荐

💡  滑动窗机制


[Adaptive Collaborative Topic Modeling for ONline Recommendation]


-----

2.  分类信息应用于推荐。  🌟 🌟 🌟 ✨



[Categorical-Attributes-Based Item Classification for Recommender Systems]


----

3. 单调行为链的概念   💡💡💡 🌟🌟

> 评论行为暗含着购买行为，进一步暗含着点击行为。

* 利用依赖关系进行推荐

[Item Recommendation on Monotonic Behavior Chains]()


----

4. 利用bandit来解决用户行为稀疏的问题。

> 设计了一种新的深度神经记忆增强机制，通过用户历史行为来建模用户的历史状态，从而在少量的交互中快速的学习用户对新项目的偏好。



💡  冷启动。新用户，，新项目

[Interactive Recommendation via Deep Neural Memory Augmented Contexual Bandits]()















































