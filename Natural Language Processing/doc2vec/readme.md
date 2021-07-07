## Softmax regression

- 클래스가 3개 이상일 때 logistic regression을 확장한 것
- 클래스가 n개일 때, 총 n개의 대표벡터를 학습
- 대표벡터에 얼마나 가까운지를 벡터의 내적으로 측정

## Word2vec

- Softmax regression의 확장으로, 각 단어의 위치 벡터를 학습


## Doc2vec

- Doc2Vec은 기존 Word2Vec모델을 확장하기 위해 paragraph vector를 제안

- document 벡터를 다른 단어들의 벡터와 함께 평균을 취하여 context 벡터를 만들어 학습



![PM-DM](https://happygrammer.github.io/nlp/doc2vec/PV-DM.png)

# Reference

1. [Logitsic regression and Softmax regression for document classification](https://lovit.github.io/nlp/machine%20learning/2018/03/22/logistic_regression/)

2. [Doc2vec를 이용한 문서의 벡터 변환](https://happygrammer.github.io/nlp/doc2vec/)

3. [Word / Document embedding](https://lovit.github.io/nlp/representation/2018/03/26/word_doc_embedding/)
