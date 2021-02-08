# word2vec

- 은닉층이 하나만 존재하며, 활성화 함수를 사용하지 않는다. (딥러닝 아님)

- CBOW (Continuous Bag of Words): 주변 단어를 통해 중간 단어를 예측

![cbow](https://wikidocs.net/images/page/22660/word2vec_renew_5.PNG)

- Skip-Gram: 중심 단어에서 주변 단어를 예측

![skipgram](https://wikidocs.net/images/page/22660/word2vec_renew_6.PNG)

# Newgative Sampling

- negative sample는 몇개만 뽑아서 학습

- 자주 등장한 단어를 높은 확률로 선택되도록 샘플링: 자주 등장한 단어만큼은 제대로 학습을 하려함

- pos, neg sample의 이동량은 다르다. (크고, 작다)

# References

https://wikidocs.net/22660

https://lovit.github.io/nlp/representation/2018/03/26/word_doc_embedding/
