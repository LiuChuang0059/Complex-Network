

#from Colors import *
from collections import defaultdict
import re
import datetime
from sklearn import datasets
import nltk
from gensim import corpora
from gensim import models
import numpy as np
from scipy import spatial
#from CorePyPro.Fun.TimeStump import totalTime


def load_texts(dataset_type='train', groups=None):
    """
    load datasets to bytes list
    :return:train_dataset_bunch.data bytes list
    """
    if groups == 'small':
        groups = ['comp.graphics', 'comp.os.ms-windows.misc']  # 仅用于小数据测试时用, #1368
    elif groups == 'medium':
        groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.ma c.hardware',
                  'comp.windows.x', 'sci.space']  # 中量数据时用    #3414
    train_dataset_bunch = datasets.load_mlcomp('20news-18828', dataset_type, mlcomp_root='./datasets',
                                               categories=groups)  # 13180
    return train_dataset_bunch.data



def preprocess_texts(texts, test_doc_id=1):
    """
    texts preprocessing
    :param texts: bytes list
    :return:bytes list
    """
    texts = [t.decode(errors='ignore') for t in texts]  # bytes2str
    # print(REDH, 'original texts[%d]: ' % test_doc_id, DEFAULT, '\n',texts[test_doc_id])
    # split_texts = [t.lower().split() for t in texts]
    # print(REDH, 'split texts[%d]: #%d' % (test_doc_id, len(split_texts)), DEFAULT, '\n',split_texts[test_doc_id])


    # lower str & split str 2 word list with sep=... & delete None
    SEPS = '[\s()-/,:.?!]\s*'
    texts = [re.split(SEPS, t.lower()) for t in texts]
    for t in texts:
        while '' in t:
            t.remove('')
    # print(REDH, 'texts[%d] lower & split(seps= %s) & delete None: #%d' % (test_doc_id, SEPS, len(texts[test_doc_id])), DEFAULT, '\n',texts[test_doc_id])


    # nltk.download()   #then choose the corpus.stopwords
    stopwords = set(nltk.corpus.stopwords.words('english'))  # #127
    stopwords.update(['from', 'subject', 'writes'])  # #129
    word_usage = defaultdict(int)
    for t in texts:
        for w in t:
            word_usage[w] += 1
    COMMON_LINE = len(texts) / 10
    too_common_words = [w for w in t if word_usage[w] > COMMON_LINE]  # set(too_common_words)
    # print('too_common_words: #', len(too_common_words), '\n', too_common_words)   #68
    stopwords.update(too_common_words)
    # print('stopwords: #', len(stopwords), '\n', stopwords)  #   #147
    english_stemmer = nltk.SnowballStemmer('english')
    MIN_WORD_LEN = 3  # 4
    texts = [[english_stemmer.stem(w) for w in t if
              not set(w) & set('@+>0123456789*') and w not in stopwords and len(w) >= MIN_WORD_LEN] for t in
             texts]  # set('+-.?!()>@0123456789*/')
    # print(REDH, 'texts[%d] delete ^alphanum & stopwords & len<%d & stemmed: #' % (test_doc_id, MIN_WORD_LEN),
    # len(texts[test_doc_id]), DEFAULT, '\n', texts[test_doc_id])
    return texts

def build_corpus(texts):
    """
    build corpora
    :param texts: bytes list
    :return: corpus DirectTextCorpus(corpora.TextCorpus)
    """

    class DirectTextCorpus(corpora.TextCorpus):
        def get_texts(self):
            return self.input

        def __len__(self):
            return len(self.input)

    corpus = DirectTextCorpus(texts)
    return corpus

def build_id2word(corpus):
    """
    from corpus build id2word=dict
    :param corpus:
    :return:dict = corpus.dictionary
    """
    dict = corpus.dictionary  # gensim.corpora.dictionary.Dictionary
    # print(dict.id2token)
    try:
        dict['anything']
    except:
        pass
        # print("dict.id2token is not {} now")
    # print(dict.id2token)
    return dict


def save_corpus_dict(dict, corpus, dictDir='./LDA/id_word.dict', corpusDir='./LDA/corpus.mm'):
    dict.save(dictDir)
    print(GREENL, 'dict saved into %s successfully ...' % dictDir, DEFAULT)
    corpora.MmCorpus.serialize(corpusDir, corpus)
    print(GREENL, 'corpus saved into %s successfully ...' % corpusDir, DEFAULT)
    # corpus.save(fname='./LDA/corpus.mm')  # stores only the (tiny) iteration object


def load_ldamodel(modelDir='./lda.pkl'):
    model = models.LdaModel.load(fname=modelDir)
    print(GREENL, 'ldamodel load from %s successfully ...' % modelDir, DEFAULT)
    return model

def load_corpus_dict(dictDir='./LDA/id_word.dict', corpusDir='./LDA/corpus.mm'):
    dict = corpora.Dictionary.load(fname=dictDir)
    print(GREENL, 'dict load from %s successfully ...' % dictDir, DEFAULT)
    # dict = corpora.Dictionary.load_from_text('./id_word.txt')
    corpus = corpora.MmCorpus(corpusDir)  # corpora.mmcorpus.MmCorpus
    print(GREENL, 'corpus load from %s successfully ...' % corpusDir, DEFAULT)
    return dict, corpus


def build_doc_word_mat(corpus, model, num_topics):
    """
    build doc_word_mat in topic space
    :param corpus:
    :param model:
    :param num_topics: int
    :return:doc_word_mat np.array (len(topics) * num_topics)
    """
    topics = [model[c] for c in corpus]  # (word_id, weight) list
    doc_word_mat = np.zeros((len(topics), num_topics))
    for doc, topic in enumerate(topics):
        for word_id, weight in topic:
            doc_word_mat[doc, word_id] += weight
    return doc_word_mat


def compute_pairwise_dist(doc_word_mat):
    """
    compute pairwise dist
    :param doc_word_mat: np.array (len(topics) * num_topics)
    :return:pairwise_dist <class 'numpy.ndarray'>
    """
    pairwise_dist = spatial.distance.squareform(spatial.distance.pdist(doc_word_mat))
    max_weight = pairwise_dist.max() + 1
    for i in list(range(len(pairwise_dist))):
        pairwise_dist[i, i] = max_weight
    return pairwise_dist


def closest_texts(corpus, model, num_topics, test_doc_id=1, topn=5):
    """
    find the closest_doc_ids for  doc[test_doc_id]
    :param corpus:
    :param model:
    :param num_topics:
    :param test_doc_id:
    :param topn:
    :return:
    """
    doc_word_mat = build_doc_word_mat(corpus, model, num_topics)
    pairwise_dist = compute_pairwise_dist(doc_word_mat)
    # print(REDH, 'original texts[%d]: ' % test_doc_id, DEFAULT, '\n', original_texts[test_doc_id])
    closest_doc_ids = pairwise_dist[test_doc_id].argsort()
    # return closest_doc_ids[:topn]
    for closest_doc_id in closest_doc_ids[:topn]:
        print(RED, 'closest doc[%d]' % closest_doc_id, DEFAULT, '\n', original_texts[closest_doc_id])


def evaluate_model(model):
    """
    計算模型在test data的Perplexity
    :param model:
    :return:model.log_perplexity float
    """
    test_texts = load_texts(dataset_type='test', groups='small')
    test_texts = preprocess_texts(test_texts)
    test_corpus = build_corpus(test_texts)
    return model.log_perplexity(test_corpus)


def test_num_topics():
    dict, corpus = load_corpus_dict()
    print("#corpus_items:", len(corpus))
    for num_topics in [3, 5, 10, 30, 50, 100, 150, 200, 300]:
        start_time = datetime.datetime.now()
        model = models.LdaModel(corpus, num_topics=num_topics, id2word=dict)
        end_time = datetime.datetime.now()
        print("total running time = ", end_time - start_time)
        print(REDL, 'model.log_perplexity for test_texts with num_topics=%d : ' % num_topics, evaluate_model(model),
              DEFAULT)

def test():
    texts = load_texts(dataset_type='train', groups='small')
    original_texts = texts
    test_doc_id = 1

    # texts = preprocess_texts(texts, test_doc_id=test_doc_id)
    # corpus = build_corpus(texts=texts)  # corpus DirectTextCorpus(corpora.TextCorpus)
    # dict = build_id2word(corpus)
    # save_corpus_dict(dict, corpus)
    dict, corpus = load_corpus_dict()
    # print(len(corpus))

    num_topics = 100
    model = models.LdaModel(corpus, num_topics=num_topics, id2word=dict)  # 每次结果不同
    model.show_topic(0)
    # model.save(fname='./lda.pkl')

    # model = load_ldamodel()
    # closest_texts(corpus, model, num_topics, test_doc_id=1, topn=3)

    print(REDL, 'model.log_perplexity for test_texts', evaluate_model(model), DEFAULT)


if __name__ == '__main__':
    test()


















