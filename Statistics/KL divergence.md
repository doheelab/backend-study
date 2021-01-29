## Entropy
- 불확실성의 정도
$$
\begin{aligned}
H &= \sum_i {p_i \log_2 \frac{1}{p_i}} \\
  &= -\sum_i p_i \log_2 {p_i} \\
  &= -\int p(x)\log_2p(x) dx
\end{aligned}
$$

## Cross Entropy (negative log likelihood)
- CE는 항상 양수이며, Entropy보다 크다.
$$
\begin{aligned}
H(p, q) &= \sum_i {p_i \log_2 \frac{1}{q_i}} \\
  &= -\sum_i p_i \log_2 {q_i} \\ 
  &= -\int p(x)\log_2 q(x) dx
\end{aligned}
$$

### Binary Cross Entropy
$$
\begin{aligned}
H(p, q) &= \sum -y \log \hat{y} - (1-y)\log(1-\hat{y})
\end{aligned}
$$

## KL-divergence

- $p,q$ 분포의 정보량 차이

- $H(p)$는 고정되었으므로, KL-divergence를 최소화하는 것은 CE를 최소화하는 것과 같다.

$$
\begin{aligned}
KL(p||q) & = H(p, q) - H (p) \\
 & = - \sum_i p_i \log_2 \frac{p_i}{q_i} \\
 & = -\int p(x) \log_2 \frac{p(x)}{q(x)}dx
\end{aligned}
$$

## KL-divergence 특성

- $KL(p|q) \ge 0$

- $KL(p|q) \neq KL(q|p)$ : KLD는 거리개념이 아니다. (asymmetric)

# Reference 

https://hyunw.kim/blog/2017/10/27/KL_divergence.html