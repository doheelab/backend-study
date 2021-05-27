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

나이브 베이즈는 조건부 확률 모델이다. 분류될 인스턴스들은 N 개의 특성 (독립변수)을 나타내는 벡터 $\textbf{x} =(x_{1},\dots ,x_{n})$ 로 표현되며, 나이브 베이즈 분류기는 이 벡터를 이용하여 $k$개의 가능한 확률적 결과들 (클래스)을 다음과 같이 할당한다.

$$
p(C_k | \textbf{x}).
$$

베이즈 정리를 이용하면,

$$
p(C_k | \textbf{x}) = \frac{p(C_k)p(\textbf{x}|C_k)}{p(\textbf{x} )}.
$$

각각의 feature가 독립이라면, 

$$
p(C_k | \textbf{x}) = \frac{p(C_k)}{p(\textbf{x})}\prod_{i=1}^{n}{p(x_k|C_k)}.
$$

따라서 클래스를 다음과 같이 예측한다.

$$
p(C_k | \textbf{x}) = \prod_{i=1}^{n}{p(x_k|C_k)}.
$$

## Laplace Smoothing

만일 $p(x_k|C_k)$ 중 하나가 0이라면, $p(C_k|\textbf{x})$가 0이 된다. 이런 경우 Laplace Smoothing을 활용할 수 있다.

$$
P(x_k|C_k) := \frac{Count(x_k, C_k)+\alpha}{N+\alpha*K}, 
$$
- $\alpha$: the smoothing parameter
- $K$: # of dim
- $N$: $|C_k|$


## 참고자료

[1] [위키피디아(나이브 베이즈 분류)](https://ko.wikipedia.org/wiki/%EB%82%98%EC%9D%B4%EB%B8%8C_%EB%B2%A0%EC%9D%B4%EC%A6%88_%EB%B6%84%EB%A5%98)

[2] [Laplace smoothing in Naïve Bayes algorithm](https://towardsdatascience.com/laplace-smoothing-in-na%C3%AFve-bayes-algorithm-9c237a8bdece)