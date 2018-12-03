# 毕业设计


##  1. 研究方向--- 物理相关


### 1. 天文学数据处理


*  数据 公开，数据集多
*  数据量大，较复杂

0. 数据集  

* [SDSS 数据集](http://www.astroml.org/user_guide/datasets.html#)

> SDSS, a decade-plus photometric and spectroscopic survey at the Apache Point Observatory in New Mexico. The survey obtained photometry for hundreds of millions of stars, quasars, and galaxies, and spectra for several million of these objects. In addition, the second phase of the survey performed repeated imaging over a small portion of the sky, called Stripe 82, enabling the study of the time-variation of many objects.





-----------


1. 光谱的自动分类
> 天体光谱是确定天体的物质结构、性质和化学组成成分的重要手段。

> LAMOST数据集中的每一条光谱提供了3690-9100埃的波长范围内的一系列辐射强度值。光谱自动分类就是要从上千维的光谱数据中选择和提取对分类识别最有效的特征来构建特征空间 ，并运用算法对各种天体进行区分。----- [阿里云天池大赛2018](https://tianchi.aliyun.com/competition/information.htm?spm=5176.11165320.5678.2.1c1b21e1sp8ntD&raceId=231646)

相关工作：

> 模板匹配、支持向量机、近邻方法、神经网络、概率神经网络、径向基神经网络、小波变换、主分量分析、小波分析、最小距离方法等。其中神经网络和主分量分析是应用最为广泛和深入的方法

* 1.CNN  



* 2.主动学习--active learning
> 数据标注代价高昂，我们也面临着如何以最少量的样本，来获得最有效学习模型的问题. 迭代地从未标注数据里面挑选出一部分重要数据去标注，从而获得更多有标记数据。所以主动学习的目标是希望用最小标注代价获得最好的学习模

**样本选择**

* informative instance

* representative instance

sourse

* [Multiclass Active Learning Algorithms with Application in Astronomy.](https://github.com/chengsoonong/mclass-sky)
* [recent progress on active learning](https://www.jiqizhixin.com/articles/2018-06-20-14)
* [主动学习-Active Learning：如何减少标注代价](https://zhuanlan.zhihu.com/p/39367595)


-------------


2. 图片分类问题

相关工作

[How Machine Vision Is Reinventing the Study of Galaxies](https://www.technologyreview.com/s/536411/how-machine-vision-is-reinventing-the-study-of-galaxies/)-----卷积神经网络图片分类




🌟🌟🌟

 提取特征 --- LDA 主题模型 进行 场景分类


🌟🌟🌟


模拟生成 未来的星空图

1. 提取特征 ， 特征和相应的图像训练gan模型

2.  特征使用RNN ， 预测未来的 特征

3.  未来特征 生成星空图像




----------
--------

### 2. Many-Particle System

[IPAM Program on Machine Learning & Many-Particle Systems - Recent Progress and Open Problems]()---- 2017.3



------
----

###  3.  Temporal/Sequential Data. ---- RNN 

> A powerful class of models for sequential data called Hidden Markov Models (Rabiner, 1989) that utilize dynamical programming techniques have natural statistical physics interpretations in terms of transfer matrices (see (Mehta et al., 2011) for explicit example of this). Recently, Recurrent Neural Networks (RNNs) have become an important and powerful tool for dealing with sequence data.

------
------



 ###  4. Reinforce Learning ---Recently in physics  (2017 --- now) 
 
 
 * [Learning to soar in turbulent environments](http://www.pnas.org/content/113/33/E4877)
 > 鸟类飞行--流体力学--涉及复杂的控制决策，
 
 ---------
 --------
 
 ### 5.  文本挖掘
 
 * [Machine learning for molecular and materials science](https://www.nature.com/articles/s41586-018-0337-2#ref-CR79)---Nature--2018
 
>  Although the scientific literature provides a wealth of information to researchers, it is increasingly difficult to navigate owing to the proliferation of journals, articles and databases. 

> Text mining has become a popular approach to identifying and extracting information from unstructured text sources. 

> This approach can be used to extract facts and relationships in a structured form to create specialized databases, to transfer knowledge between domains and, more generally, to support research decision-making
 
 
应用

* [Materials Synthesis Insights from Scientific Literature via Text
Extraction and Machine Learning](https://pubs.acs.org/doi/ipdf/10.1021/acs.chemmater.7b03500)---2017
> 检查了超过12,000份手稿中各种金属氧化物的合成条件。然后，d
我们应用机器学习方法来预测通过水热法合成二氧化钛纳米管所需的关键参数，并根据已知机制验证该结
 
 
 ----------
 --------
 
 
 ## 2. 复杂网络 ---网络信息挖掘
 
 ### 1.  关键节点挖掘
 > 能够在更大程度上影响网络的结构与功能的一些特殊节点
 
 
 
 * 二是提出若干评价网络中节点中心性（重要性）的指标。节点的度和核数是最常见的刻画节点影响力的中心性指标。我们指出了节点度在刻画影响力方面存在局域化程度过高的缺陷，并据此提出了基于多阶邻居[4]和考虑局部集聚特性[5]和邻居连接模式[6]的新的中心性指标
 
 
 * 实际上在不同的动力学参数条件下，网络中节点重要性的排序变化非常大，这就使得如果不考虑具体动力学的性质和参数，没有办法得到具有普适性的有效排
 
 
 
 ### 3. 推荐系统
 
 精巧混合能量扩散和热传导算法，实现了同时提升推荐效果的精确性、多样性和新颖性[51]。
 
 [Solving the apparent diversity-accuracy dilemma of recommender systems](https://arxiv.org/pdf/0808.2670.pdf)
 
 这些算法从整体上对于推荐的精确度提升并不明显，但是能够显著提高较新的用户和较不流行的商品推荐的精准度。
 
 
 
 
 
 
 
 





