# LDA 学习



* 从 Dirichlet 分布 $\alpha$ 中取样生成文档$m$ 的 主题分布 $\theta_{m}$

* 从主题的 Multinominal 分布 $\theta_{m}$ 中取样生成文档 $m$ 的第 $n$ 个词的主题$Z_{m,n}$ 

* 从 Dirichlet 分布 $\beta$ 中取样生成主题$Z_{m,n}$  的对应的词语分布 $\phi_{z_{m,n}}$

* 从词语的多项式分布$\phi_{z_{m,n}}$ 中采样最终生成词语$W_{m,n}$ 
