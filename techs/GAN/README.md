README.md


# 1. GAN 的最新进展

## 1. 自然语言处理方面 -- 离散值

### 1. 问题

* 1. GAN最开始是设计用于生成连续数据，但是自然语言处理中我们要用来生成离散tokens的序列。因为生成器(Generator，简称G)需要利用从判别器(Discriminator，简称D)得到的梯度进行训练，而G和D都需要完全可微，碰到有离散变量的时候就会有问题，只用BP不能为G提供训练的梯度。在GAN中我们通过对G的参数进行微小的改变，令其生成的数据更加“逼真”。若生成的数据是基于离散的tokens，D给出的信息很多时候都没有意义，因为和图像不同。图像是连续的，微小的改变可以在像素点上面反应出来，但是你对tokens做微小的改变，在对应的dictionary space里面可能根本就没有相应的tokens.

* 2.GAN只可以对已经生成的完整序列进行打分，而对一部分生成的序列，如何判断它现在生成的一部分的质量和之后生成整个序列的质量也是一个问题。



### 2. 


1. GAN最开始是设计用于生成连续数据，但是自然语言处理中我们要用来生成离散tokens的序列。因为生成器(Generator，简称G)需要利用从判别器(Discriminator，简称D)得到的梯度进行训练，而G和D都需要完全可微，碰到有离散变量的时候就会有问题，只用BP不能为G提供训练的梯度。在GAN中我们通过对G的参数进行微小的改变，令其生成的数据更加“逼真”。若生成的数据是基于离散的tokens，D给出的信息很多时候都没有意义，因为和图像不同。图像是连续的，微小的改变可以在像素点上面反应出来，但是你对tokens做微小的改变，在对应的dictionary space里面可能根本就没有相应的tokens.2.GAN只可以对已经生成的完整序列进行打分，而对一部分生成的序列，如何判断它现在生成的一部分的质量和之后生成整个序列的质量也是一个问题。


-----


2. 第二篇是C.Manning组大神Li Jiwei的文章：Adversarial Learning for Neural Dialogue Generation，用GAN和强化学习来做对话系统，如果我没有记错，这篇paper是最早引用SeqGAN的，有同学还说这篇是最早将RL用到GAN上的，主要是Jiwei大神名气太大，一放上Arxiv就引起无数关注。如图，文章也是用了Policy Gradient Method来对GAN进行训练，和SeqGAN的方法并没有很大的区别，主要是用在了Dialogue Generation这样困难的任务上面。还有两点就是：第一点是除了用蒙特卡罗搜索来解决部分生成序列的问题之外，因为MC Search比较耗费时间，还可以训练一个特殊的D去给部分生成的序列进行打分。但是从实验效果来看，MC Search的表现要更好一点。第二点是在训练G的时候同时还用了Teacher-Forcing（MLE）的方法，这点和后面的MaliGAN有异曲同工之处。为什么要这样做的原因是在对抗性训练的时候，G不会直接接触到真实的目标序列（gold-standard target sequence），当G生成了质量很差的序列的时候（生成质量很好的序列其实相当困难），而D又训练得很好，G就会通过得到的Reward知道自己生成的序列很糟糕，但却又不知道怎么令自己生成更好的序列， 这样就会导致训练崩溃。所以通过对抗性训练更新G的参数之后，还通过传统的MLE就是用真实的序列来更新G的参数。类似于有一个“老师”来纠正G训练过程中出现的偏差，类似于一个regularizer。



原文链接：https://arxiv.org/pdf/1701.06547.pdf

Github链接：[jiweil/Neural-Dialogue-Generation](https://link.zhihu.com/?target=https%3A//github.com/jiweil/Neural-Dialogue-Generation)

------

3. Yoshua Bengio组在二月底连续放了三篇和GAN有关的paper，其中我们最关心的是大神Tong Che和Li yanran的这篇：Maximum-Likelihood Augmented Discrete Generative Adversarial Networks（MaliGAN），简称读起来怪怪的。。。这篇文章的工作主要是两个方面：1.为G构造一个全新的目标函数，用到了Importance Sampling，将其与D的output结合起来，令训练过程更加稳定同时梯度的方差更低。尽管这个目标函数和RL的方法类似，但是相比之下更能狗降低estimator的方差（强烈建议看原文的3.2 Analysis，分析了当D最优以及D经过训练但并没有到最优两种情况下，这个新的目标函数仍然能发挥作用）2.生成较长序列的时候需要用到多次random sampling，所以文章还提出了两个降低方差的技巧：第一个是蒙特卡罗树搜索，这个大家都比较熟悉; 第二个文章称之为Mixed MLE-Mali Training，就是从真实数据中进行抽样，若序列长度大于N，则固定住前N个词，然后基于前N个词去freely run G产生M个样本，一直run到序列结束。基于前N个词生成后面的词的原因在于条件分布Pd比完整分布要简单，同时能够从真实的样本中得到较强的训练信号。然后逐渐减少N（在实验三中N=30, K=5， K为步长值，训练的时候每次迭代N-K）

-----


4. Improved Training of Wasserstein GANs, WGAN发布之后就引起轰动，比如Ian在Reddit上就点评了这篇文章，NYU的又祭出了这篇，令WGAN在NLP上也能发挥威力。

* 参考链接--https://zhuanlan.zhihu.com/p/25071913





-----


# 参考


* https://www.zhihu.com/question/52602529/answer/155743699





