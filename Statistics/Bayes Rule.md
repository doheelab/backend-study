
## 베이즈 정리

베이즈 정리는 사전확률과 사후확률 사이의 관계를 나타내는 정리

$$
P(H|E) = \frac{P(E|H)P(H)}{P(E)}
$$

$P(E)$: 사전 확률, $P(H|E)$: 사후 확률

새로운 정보(E)를 토대로 어떤 사건(H)이 발생했다는 주장에 대한 신뢰도를 갱신해 나가는 방법이다.

> 가능도 (Likelihood): 관찰을 통해 얻은 모수의 확률 분포
 
> Posterior = (Likelihood $\times$ Prior)/Evidence

$$
P(w_i|x) = \frac{P(x|w_i)P(w_i)}{\sum_j P(x|w_j)P(w_j)}
$$

![BayesRule](https://raw.githubusercontent.com/angeloyeo/angeloyeo.github.io/master/pics/2020-01-09-Bayes_rule/pic1.png)

# Reference

https://angeloyeo.github.io/2020/01/09/Bayes_rule.html

https://hyeongminlee.github.io/post/bnn001_bayes_rule/