## 특징

- 아이템의 특징(feature, attribute)끼리 서로 독립
- 영화 장르와 영화 감독이 서로 연관이 없는 특징
- 데이터 셋이 커도 모델 예측에 관계 없다.
- 연속형 변수보다 이산형 변수에 더 적절히 사용된다.
- Laplace Smoothing 활용

## Naive Bayes Classifier

<!-- $$
\begin{align} % \begin{align\*}
y_{ui} = a_{out}(h^T(p_u \odot p_i))
\end{align}
$$ -->

$$
y_{ui} = a_{out}(h^T(p_u \odot p_i))
$$
