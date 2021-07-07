## 1. Chi-Squared test

$$
X^2 = \sum_{i=1}^{k}{\frac{(x_i-m_i)^2}{m_i}}
$$
$m_i$: 예측치



## 2. Cross-Entropy (KL-divergence)

$$
H(P, Q) = -\sum_x P(x) \log Q(x).
$$

$$
D_{KL}(P||Q) = -\sum_x P(x) \log \frac{P(x)}{Q(x)} = -H(P)+H(P,Q).
$$


$KL(P,Q)$ = $P$가 $Q$를 얼마나 잘 설명하는가. $p$가 $q$의 차이.

## 3. 유사도 지표

Cosine similarity, Jaccard Index