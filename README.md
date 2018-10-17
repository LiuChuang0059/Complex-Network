# 复杂系统和复杂网络

-----
# Day0 --- 大佬主页和google学术 + 研究机构

### 

* [大佬采访视频](https://www.complexityexplorer.org/courses/89-introduction-to-complexity/segments/6757)
>  一个复杂系统课程的采访视频，云集了各种大佬，讲 关于复杂系统的定义（实际一点都没听懂）

*  [Cris Moore - Santa Fe Institute](http://tuvalu.santafe.edu/~moore/talks.html)------[Google-Scholar-Citations](https://scholar.google.com/citations?user=p_837e0AAAAJ&hl=zh-CN)
     > 做很多物理学思想方法在复杂网络中的应用 ；以及一些量子计算，量子算法在网络中的应用

* [Mark Newman - Santa Fe Institute](http://www-personal.umich.edu/~mejn/)------[Google-Scholar-Citations](https://scholar.google.com/citations?hl=zh-CN&user=rQ68pVwAAAAJ&view_op=list_works&sortby=pubdate)
  > 引用超高的巨佬（总150,000+，单篇17,000+）,主要做复杂网络工作，主页有很多代码和数据集

* [James Fowler](http://jhfowler.ucsd.edu/)-----[Google-Scholar-Citations](https://scholar.uulucky.com/citations?user=vcTq49gAAAAJ&hl=zh-CN)
  > 特别高产，引用也超高，主要做社会网络方向，主页同样很多源码，软件，和数据集。


* [ Albert-László Barabási个人主页](http://barabasi.com/)---[Barabási Lab
](https://www.barabasilab.com/publications)-----[Google-Scholar-Citations](https://scholar.google.com/citations?hl=zh-CN&user=vsj2slIAAAAJ&view_op=list_works&sortby=pubdate)
  > 感觉巨佬（总引189，696+，单引30，000+）和网络各个交叉方向都做，统计物理，生物医学，脑科学，表面材料等等，实验室超大组。

* [陈关荣教授--香港城市大学](http://www.ee.cityu.edu.hk/~gchen/)[Google-Scholar-Citations](https://scholar.google.com.hk/citations?user=O_Eif1YAAAAJ&hl=en&oi=ao)
  > 混沌和复杂网络

* [Jon Kleinberg](http://www.cs.cornell.edu/home/kleinber/)


* [周涛--电子科技大学--科学网博客](http://blog.sciencenet.cn/?3075)-----[Google-Scholar-Citations](https://scholar.google.com/citations?hl=en&user=MXgWgmEAAAAJ&view_op=list_works&citft=1&citft=3&email_for_op=2015301020059lc%40gmail.com&gmla=AJsN-F4Njj1bIZtqgLDXV_lKORVi7QZxbdLg2uh7rbylMYZ9whd7Ji48E5iNvbIm1b68i8FtOraU8kZdVyiNG7Pq7yveeYnykVLAay8IgUMRKCMKhk-sCaHGmpP9qz4OV-i0Iydg37dIdNuFRPJu97YLKdGc7YlqhSP6rW6sdMouZQ9IsPOGC1dhLQ3OZJQ-0oivaWyHXwfay1pX2VTUsXvCa9gvl0sZ50vvSmO2WD3uLt_7DlTMkxRcu-TcSH8yHwwlT4mp8YBk)
     > 国内做复杂网络和数据挖掘的大佬，引用超20,000; 经常在科学网博客分享一些论文资料，研究方向介绍分析。DC学院的创始人之一，有很多数据挖掘，图挖掘的课（付费）
     
* [汪秉宏----中国科学技术大学---科学网博客](http://blog.sciencenet.cn/home.php?mod=space&uid=4673&view=bhwangustc)-----[Google-Scholar-Citations]()

> 物理倾向的的复杂网络大牛，写过好的复杂网络的专著。

* [张潘 - 中科院理论物理所](http://lib.itp.ac.cn/html/panzhang/)-----[Google-Scholar-Citations](https://scholar.google.com/citations?user=MFnbrRUAAAAJ&hl=en)
  > 近几年做了很多，统计物理和机器学习，量子力学和机器学习的相关工作，都是PRx的高质量文章；个人主页附有一些处理方法的c++代码

--------

### 科研机构

* [Santa Fe Institute](https://www.santafe.edu/research/projects/social-networks-big-data-and-physics-powered-infer)
  > 上面有几位大佬工作学习过的地方，网页有很多很多很好的研究成果，研究方向等等

* [Centre for Chaos and Complex Networks---香港城市大学](http://www.ee.cityu.edu.hk/~cccn/)------[Complex Networks: Information and Resources](http://www.ee.cityu.edu.hk/~gchen/ComplexNetworks.htm)
  > 复杂网络方向，已经很多工业应用； 主页有很多有关复杂网络的资源：大学课程+书籍+软件+数据集等等
  

--------

###  学习课程，资料

* [Complexity- Explore ](https://www.complexityexplorer.org/home)

> 免费！ 复杂网络，相关基础知识，数学理论等

--------
### 汇总参考
* http://blog.sciencenet.cn/blog-583335-477254.html
* http://www.ee.cityu.edu.hk/~gchen/ComplexNetworks/PersonalWebsites.htm

-------
----------- 
---------

# Day1 -- 基础了解


## 0. 统计物理学角度研究网络

*  网络是一个包含了大量个体 以及个体之间相互作用的系统 ,是把某种现象或某类关系抽象为个体 (顶点) 以及个体之间相互作用 (边) 而形成的用来描述这一现象或关系的图 

* 研究网络中顶点与边的度值与权值等微观性质与网络的几何性质 、效率与稳定性 等宏观性质之间的关系正是复杂网络研究的核心内容


* 统计物理学研究网络更侧重于从各种实际网络的现象之上抽象出一般的网络几何量 ,并用 这些一般性质指导更多实际网络的研究


## 1. 网络的静态几何量

> 网络的统计性质称为网络静态几何


### 1. 无向网络
* 度及其分布特征，度的相关性，
  > 一个顶点的度是指与此顶点连接的边的数量
  > 分布之间的相关性: 考察度 值大的点倾向于和度值大的点连接 , 还是倾向于和度值小的点连接
* 聚集程度及其分布特征
  > 集聚程度的意义是网络集团化的程度 , 即考察连接在一起的集团各自的近邻之中有 多少是共同的近邻
  
* 最短距离及其分布特征
* 介数(Betweenness)及其分布特征
  > 顶点 u 的介数含义为网络中所 有 的 最 短 路 径 之 中 , 经 过 u 的 数 量
  > 反映了顶点的影响力
  
### 2. 有向网络
> WWW 网络 ,细胞内化学反应网络 ,食物链网 络 ,引文网络 ,电力网络 ,神经网络 。


### 3. 加权网络

> 为了研究某一学术领域的发展变化 ,某一个新的思想在此领域内的产生 、传播 ,构造一个科学家之间通过文献相互联系影响的网络 。我们认为 ,对于研究此问题而言 , 科学家之间的合作关系[66] ,引文关系[65,68]以及讨论或书信交往(经常体现在致谢中)属 于同一属性的关系 ,但是所起作用的程度有所不同 。对于交流思想而言 ,合作是最直接的 影响 ,其次是引文 ,再次为致谢 。而且 ,在同为合作的关系内 ,合作的次数的不同 ,对于交 流思想的影响也是不一样的 。因此 ,在这个科学家网络中 ,每一条边代表了综合考虑了以 上三个方面两个层次的相互作用以后的影响力程度 。并且由于引文和致谢的有向性 ,此 网络是一个加权有向网络 。


## 2. 网络机制模型

### 1. 规则网络与随机网络
* 规则网络与随机网络的典型几何性质包括 :度分布 , 平均集聚程度与平均最短距离

### 2. small world 网络
> 大聚集程度和小最短距离

<div align="center">  <img src="https://github.com/LiuChuang0059/datamining/blob/master/Image/%E5%B0%8F%E4%B8%96%E7%95%8C%E6%A8%A1%E5%9E%8B.png" width="500"/> </div><br>

### 3. Scale Free 网 络 

--------

## 网络信息挖掘和预测问题

> 这里主要涉及两个问题，一个是反问题，也就是从动力学表征挖掘网络结构；一个是预测问题，也就是如何挖掘网络中的缺失信息，并进行网络趋势预测。在反问题这个研究方向上，很多学者都强调了压缩感知的重要性，该方法最大程度反映了动力学和结构的耦合关系，具有广泛的应用价值。在预测问题这个研究方向上，较成熟也最有活力的研究是链路预测，另外，关于包含社交关系的人类行为预测，生物网络中的时间序列预测，生物网络中结构链接和功能链接之间的耦合预测等等，都是近期受到关注的发展方向。


## 复杂系统理论在实际系统中的应用问题

针对具体的实际系统和实际问题，例如实际交通系统的优化、传染病的防控等，提出具体的解决方案。在这方面，虽然暂时可能无法达到理论与实际的统一，形成一个普适性的研究方法和成果，但是对于实际系统的理解是一个认识逐渐深化的过程，需要在这方面进行逐步的探索，比如我们实际遇到的超大规模网络、智能电网、移动互联网、物联网等的研究。特别地，复杂网络分析在社会科学和生命科学领域应该大有可为！

 
 

## 参考

* [大数据时代下复杂网络的机遇与挑战](http://blog.sciencenet.cn/blog-4673-722029.html)


-------
----------
-----------

# Day2 -----交通网络数据挖掘

## 参考资料

* [大数据、数据挖掘在交通领域有哪些应用](https://www.zhihu.com/question/23615530)

* [大数据理论如何指导交通数据分析](https://www.zhihu.com/question/21374161)


----------
----------
----------

# Day3 ------社区检测

# （一）伊辛模型

## We use physics-inspired methods to find structure within large datasets.

> We are in an age of information, with nearly every scientific field awash in new data. Thus, making sense of large sets of real-world data stands as a preeminent challenge for modern science. Massive data sets, whether they record food web relationships, online friendships, or distributions of utilities like electricity, are often described by mathematical network models that give structure to the data – and help us better understand the relationships hidden within it.
>>> 我们处在一个信息时代，各个科学领域都有大量数据。因此，理解掌握大量的由真实世界数据构成的数据集是现代科学的一个巨大挑战。大量的数据集，无论他们记录的是食物链，网络社交圈，或者是店电力网络系统，都是由基于数学的网络模型给出数据的结构，从而帮助我们理解数据之间的隐藏关系


> Our project aims to use physics-inspired methods to find structure within large data sets and determine when these structures are statistically significant. We are developing elegant, flexible, and computationally efficient algorithms for investigating the underlying structures, dynamics, and attributes of real-world networks.These physics-based algorithms can point to hidden connections between spatially disparate nodes of a network. They can help us understand why a natural disaster in a given area might cause an electrical blackout hundreds of miles away. They can reveal similar relationships in different data sets, such as the keystone species in a modern food web and those from the Cambrian period. They can fill in missing data with intelligent guesses, predict missing links, and tell us the probability that a given node belongs to a given community. Moreover, these algorithms are scalable, allowing us to solve massive problems, once the domain of supercomputers, on an ordinary laptop.
>>> 这个项目的目的主要是，使用由物理启发的方法去发现大的数据集之间的结构，确定这些结构什么时候具有统计性。我们正在开发一种高效稳定的算法去挖掘真实世界网络的结构，动态变化，构成。这些基于物理的算法可以指出空间网络的不同节点之间的隐藏联系。可以帮我们理解为什么一个地方的自然疾病会导致千里外电力缺失。
他们可以反映不同数据集之间的相似形。例如不同时期的食物链之中的关键物种。他们可以填补数据集的缺失数据，预测缺失的链接，告诉我们一个给定的节点属于一个给定集团的可能性。这些算法是可延展的，允许我么解决大量的问题，不再是依托于超级计算机，而是笔记本电脑即可。


> As we seek out the structures, patterns and attributes of large data sets, we also pursue the broader question of how a network’s structure gives rise to its dynamics. In doing so, we hope to understand the similarities and differences between social networks, economies, power grids, and food web
>>> 当我们找出数据集的结构，模式，构成时，我们同时追求更深远的问题---一个网络的结构对其动态变化的影响。同时我们洗希望理解各个网络之间的相似和不同点：
社交网，经济网，电网，食物链。


#### 参考
* [idea来源link](https://www.santafe.edu/research/projects/social-networks-big-data-and-physics-powered-infer)



## Physics-Inspired Algorithmsand Phase Transitionsin Community Detection

### 1 结构
* 结构使数据区分于噪声
* 结构能够帮助压缩数据
* 结构能够根据我们现有的数据推断没有的数据
* 帮助我们粗化动态变化，减少变量数

### 2 统计推断
* 假设有一个网络，由生成模型产生， 拟合数据参数
* 能够合并部分信息
    > 一些点的构成已知
    > 一些链接已知
* 使用模型能够根据我们知道的推断我们不知道的

### 3 随机块模型
> nodes have discrete labels: k “groups” or types of nodes
k×k matrix p of connection probabilities
if i is type r and j is type s, there is a link i→j with probability prs
p is not necessarily symmetric, and we don’t assume that prr > prs
given the graph G, find the labels

* 一般差的情况下，块模型拟合到一个图是一个NP问题，
* 类比统计物理的Brelief propagation 方法 更好的解决问题，反映相位运输在社区结构检测中

### 4 [伊辛模型](https://zh.wikipedia.org/wiki/%E6%98%93%E8%BE%9B%E6%A8%A1%E5%9E%8B)
> 二维或二维以上的模型中，该系统可以历经从无序相转变成有序相的相变。基本上在β值小(高温)时，系统处在无序相，而β值大(低温)时，系统处在有序相中


* [伊辛(Ising)模型背后的故事](http://blog.sciencenet.cn/home.php?mod=space&uid=1248&do=blog&id=1843)

> 二维伊辛模型的精确解有很多解法，比较经典的、代表性的解法：
L. Onsager, Phys. Rev. 65, 117 (1944).
B. Kaufman, Phys. Rev. 76, 1232 (1949).
M. Kac and J.C. Ward, Phys. Rev. 88, 1332 (1952). 
C.A. Hurst and H.S. Green, J. Chem. Phys., 33, 1059 (1960).
E.W. Montroll, R.B. Potts and J.C. Ward, J. Math. Phys., 4, 308 (1963).
还可以参考综述文献：
G.F. Newell and E.W. Montroll, Rev. Mod. Phys. 25, 353 (1953).
C. Domb, Adv. Phys. 9, 149 (1960).
K. Huang, Statistical Mechanics, (John Wiley and Sons Inc., New York – London, 1963).
R.J. Baxter, Exactly Solved Models in Statistical Mechanics, (Academic Press, London, 1982).
S.K. Ma, Modern Theory of Critical Phenomena, (Addison – Wesley, Redwood, CA, 1976). 
B.M. McCoy and T.T. Wu, The Two – Dimensional Ising Model, (Harvard University Press, Cambridge, MA, 1973).
Phase Transitions and Critical Phenomena, C. Domb and M.S. Green, eds. (Academic Press, London, 1974).


* 伊辛模型应用
> 社会科学中，人们已经将Ising模型应用于股票市场、种族隔离、政治选择等不同的问题。另一方面，如果将小磁针比喻成神经元细胞，向上向下的状态比喻成神经元的激活与抑制，小磁针的相互作用比喻成神经元之间的信号传导，那么，Ising模型的变种还可以用来建模神经网络系统，从而搭建可适应环境、不断学习的机器（Hopfield网络或Boltzmann机）。


<div align="center">  <img src="https://github.com/LiuChuang0059/datamining/blob/master/Image/%E4%BC%8A%E8%BE%9B%E6%A8%A1%E5%9E%8B.png" width="500"/> </div><br>

### 5 基态和 illusions

* 最可能的标签，[最大后验估计](https://www.cnblogs.com/easoncheng/archive/2012/11/08/2760675.html)---基态
* 即使是随机的3正则图也只有11％的边缘标签越过切口
* many labelings, about as good as each other, with nothing in common!this is a sign there aren’t actually communities at al


### 6 统计估计 vs过拟合

### 7 最好的标记
* 对于每一个点，计算他的边缘分布，属于每个组的可能性，安排每个点去最可能的标签
* 真正的标记实现了更高的“重叠”---最大化正确标记节点的覆盖率
* the consensus of many likely solutions is better than the most-likely one


### 8 模型选择和自由能
* best model: maximize total probability of G, summed over all possible labelings

<div align="center">  <img src="https://github.com/LiuChuang0059/datamining/blob/master/Image/%E6%A8%A1%E5%9E%8B%E7%9A%84%E8%87%AA%E7%94%B1%E8%83%BD.png" width="500"/> </div><br>

* 类似于 热力学统计物理里面的自由能 自由能最小，

------------------
## Compute marginals and free energies----Monte Carlo is too slow

### Belief propagation

* 学习参考
* https://blog.csdn.net/qq_23947237/article/details/78385110
* https://blog.csdn.net/u010830324/article/details/51896570


### 近似自由能--变分法

### BP算法的其他应用
* 也是图集合的分析计算框架
* 分析信息的固定点，稳定性


### BP收敛---取决于数量
* 在相变点 极速下降

### 相变点---找出社区
<div align="center">  <img src="https://github.com/LiuChuang0059/datamining/blob/master/Image/%E6%A8%A1%E5%9D%97%E5%8C%96-%E6%A8%A1%E5%9E%8B%E7%BB%93%E6%9E%84.png" width="500"/> </div><br>



----------------


### Spectral methods and their redemption-----特征光谱法

* if there are 2 groups, label nodes according to the sign of the 2nd eigenvec

*  Wigner semicircle law


--------------

## 总结

* Statistical inference using generative models of networks lets us detect communities, classify nodes, and predict missing links

* Belief propagation and expectation-maximization algorithms let us identify these groups, and learn model parameters, often in linear time: scalable! 

* For instance, we can classify documents using their content and the links between them better than with content or links alone.

* Extending Bayesian inference to richer data is possible, but challenging We need to be agnostic about what types of structure are important

-----------------
## 参考
* Physics-Inspired Algorithmsand Phase Transitionsin Community Detection---[pdf](http://tuvalu.santafe.edu/~moore/ucsc-stanford.pdf)
* Physics-Inspired Algorithmsand Phase Transitionsin Community Detection----[youtube](https://www.youtube.com/watch?v=jzN37cqkB0c)

* Finding Hidden Structure in Networks---[pdf](https://github.com/LiuChuang0059/datamining/blob/master/PapersAndBooks/Finding%20Hidden%20Structure%20in%20Networks.pdf)


--------------------
------------

# （二） Potts 模型


## Physical Models in Community Detection with Applications to Identifying Structure in Complex Amorphous Systems

### 1. Potts 模型--Ising模型中自旋的取向自由度放宽到q个

* http://blog.sciencenet.cn/blog-485752-1106066.html

* http://micro.ustc.edu.cn/CompPhy/lecturenote/12.pdf

### 2. 摘要

* We present an exceptionally accurate spin-glass-type Potts model for the graph theoretic problem of community detection
     > potts模型用于社区检测

* It further remains a local measure on weighted and directed graphs
     > 应用于权重图和有向图

* Our multiresolution algorithm calculates correlations among multiple copies (“replicas”) of the same graph over a range of resolutions.
     > 多层算法计算同一个图多个副本之间的关联。

* We further investigate a “phase transition” effect in community detection
     > 相变点


## 参考

* Physical Models in Community Detection with Applications to Identifying Structure in Complex Amorphous Systems---[pdf](https://github.com/LiuChuang0059/datamining/blob/master/PapersAndBooks/Physical%20Models%20in%20Community%20Detection%20with%20Applications%20to%20Ident.pdf)


-----------------------
--------------

# （三）光谱分析-Spectral
## Robust Spectral Detection of Global Structures in the Data by Learning a Regularization---[pdf](https://github.com/LiuChuang0059/datamining/blob/master/PapersAndBooks/robust-spectral-detection-of-global-structures-in-the-data-by-learning-a-regularization.pdf)

### 摘要
* 检测给定数据的全局结构---数据可以用矩阵表示，
* 而且数据较为稀疏或者有噪声，会引起特征数据局域化，
* In this work, we propose a general method to solve the localization problem by learning a regularization matrix from the localized eigenvectors.
* 正则化矩阵的学习，能够抑制或者减少局部特征向量。


------------------------
------------------

# （四）社区结构对网络的影响（为什么要检测社区结构）

##  Resilience of networks with community structure behaves as if under an external field---[pdf](https://github.com/LiuChuang0059/datamining/blob/master/PapersAndBooks/%20%20Resilience%20of%20networks%20with%20community%20structure%20behaves%20as%20if%20under%20an%20external%20field.pdf)

### 摘要
* We use percolation theory to develop a framework for studying the resilience of networks with a community structure.

     > 渗透理论
  
* . We find both analytically and numerically that interlinks (the connections among communities) affect the percolation phase transition in a way similar to an external field in a ferromagnetic– paramagnetic spin system
     > 社区影响渗透相变点的作用。类似与 外场对铁磁-顺磁自选系统的作用

* We also study universality class by defining the analogous critical exponents δ and γ, and we find that their values in various models and in real-world coauthor networks follow the fundamental scaling relations found in physical phase transitions.
     > 真实社会网络的数值比例类似于物理学相变的相变指数
     
     
-----------------
----------------
---------------


# Day 4 ----复杂网络研究方向


## 0 参考

* 1. 复杂网络研究的机遇与挑战---http://blog.sciencenet.cn/blog-3075-741803.html

* 2. 复杂网络入门读物---http://blog.sciencenet.cn/blog-3075-549946.html

* 3. 复杂网络入门最佳资料：英文经典综述合集--http://blog.sciencenet.cn/blog-3075-1070466.html

* 4. 电子科大周涛教授：当时代发生巨变，一定要站在能够产生重大成果的地方---http://www.sohu.com/a/192786815_114877

## 1 数据到网络

* 收集的数据规模和种类增大，如何构建合适的网络；分析数据的质量；不完整的网络做数据分析、

* 抽样问题
     > 所用的数据大部分是抽样结果，，抽样得到网络与原网络的关系，没有明确的证明
     
 
## 2 网络工程----应用到实际问题

* 实际交通系统的优化；社会科学，生命科学等领域

* 模型建立，分析，求解----用来解释和预测真实网络的本质，特性和行为。


## 3 网络的信息挖掘和预测

* 从动力学表征挖掘网络结构

* 从观察出发，挖掘网络中缺失的信息，并进行网络结构，功能，和演化趋势预测
     * 链路预测-----网络中的链路预测是指如何通过已知的网络结构等信息预测网络中尚未产生连边的两个节点之间产生连接的可能性
     * 人类行为预测

### 1  链路预测

#### 1 分类
* existent yet unknown links

* future links

#### 2 方法：

* 基于马尔科夫链 和机器学习

* 基于节点的属性--定义节点之间的相似性
     > 节点的属性信息不一定真实
* 基于网络拓扑结构的相似性
     > 只涉及结构，不涉及节点的属性信息
     > 网络简单 计算复杂度较低
* 利用网络的 层次结构进行链路预测

#### 3 应用

* 分析数据缺失的网络

* 分析演化网络


#### 4 发展展望

* 应用层面-- 过网络的结构信息，借助复杂网络的分析工具，设 计高效的算法处理大规模网络的链路预测问题。

* 理论层面--何以网络系综理 论为基础，建立网络链路预测的理论框架，并产生 对实际预测有指导作用的理论结

* 权重网络相关研究


* 结合机器学习
     

#### 5 参考
* Link Prediction on Complex Networks---LÜ Lin-yuan


### 2 社团检测---详见 Day 3

-------------

## 4 含有时空信息的网络

* 现实的网络大多数是随时间和空间持续变化的，结构完全固定的网络非常少见。
     > 例如，实际的社会网络中，人与人之间的联系与交互是遵循一定时空统计规律出现，而不是一直保持不变的

### 人类行为时空特性----统计分析

#### 1 主要方法
* 观察-数据获取与分析-统计规律挖掘- 建模再现数据规律

* 

#### 2 应用

* 特别是长途旅行规律的理解，有助于理 解、预测和控制全球性传染病的流行

* 对人出 行和网络活动中表现出来的阵发性和记忆性的分 析，可以应用于异常行为检测，如疑似恐怖分子非 正常的频繁跨越国境的旅行和处于非正当目的的 网络舆情操控行为的检测

* 对于人类群体出行 行为时空图的分析可以为交通路网设计和道路流量 规划，包括公共服务设施和商业设施的选点提供借 鉴

* 对人网上行为的分析可以为更好地开展互联 网信息服务提供借鉴


#### 3 人类行为时间特性的实证分析

* 柏松分布---幂律分布



#### 4 人类行为空间特性的实证分析   

* 交通

* 在群体水平上，混合交 通方式使用者的移动步长分布服从幂律或截尾幂律 分布，而单一交通方式使用者的移动步长分布则服 从指数或近似指数分布

* 在个体水平上，人类的 移动步长分布呈现不规则的多样化特征，并不服从 某种特定的分布形式

* 人类的空间运动模式具有 时空规则性，如以天为周期频繁返回少数几个地点， 不同个体的空间概率密度分布定性上高度相似，移 动轨迹具有高可预测性。


     * 人类空间运动轨迹的规则性、周期性、相似 性等与行为预测问题密切相关的统计特征的研究还 很不充分

     * 孤立地挖掘人类 空间运动行为的统计特征，而对于社会化因素对人 类行为的影响考虑不足
     
 
#### 5 参考

* 周涛，韩筱璞，闫小勇, 等. 人类行为时空特性的统计力学[J].

--------------------


* 许多网络都不是孤立存在的，而是与其它网络之间存在着相互依赖、合作或竞争等关系，即“网络的网络”

####
* 研究相互依赖网络的结构，功能，鲁棒性

* 真实网络相互依赖的节点不是随机的

#### 参考

* GAO J -X, BULDYREV S V, STANLEY H E, etal. Networks formed from interdependent networks[J]. Nature Physics. 


------------




# Day 5 --- 人类行为时空特性-统计力学






