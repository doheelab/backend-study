## EM 알고리즘

 latent variable이 존재하는 모델의 maximum likelihood 혹은 maximum a posterior 문제를 풀기 위한 알고리즘

> Solve
> 
>$\max_{\theta}p(X|\theta) = \sum_{Z}p(X,Z|\theta)$.

- 관측할 수 있는 parameter $\theta$
- latent variabel $Z$

만일 latent variable $Z$의 marginal distribution을 $q(Z)$라고 정의하면, 앞에서 설명한 문제의 log-likelihood는 다음과 같다.

$$
\ln p(X|\theta) = L(q, \theta) + KL(q||p)
$$
이때, $L(q, \theta)$와 KL$(q||p)$는 다음과 같이 정의된다.

$$
L(q,\theta) = \sum_{Z}q(Z) \ln \frac{p(X,Z|\theta)}{q(Z)}
$$
$$
KL(q||p) = -\sum_{Z}q(Z)\ln \frac{p(Z|X,\theta)}{q(Z)}
$$

KL diovergence는 항상 0보다 크거나 같기 때문에, $L(q,\theta)$가 log-likelihood의 lower bound가 된다. 

따라서 $L(q,\theta)$를 최대가 되도록 하는 $\theta$와 $q(Z)$ 찾는 문제로 변환된다.

이 때 $\theta$와 $q(Z)$를 번갈아가면서 update하는 알고리즘이 EM 알고리즘이다.

## MLE vs MAP


> Bayes' Rule ( Posterior = Prior * Likelihood / (const) )
> 
$$
p(\theta | x) = \frac{p(\theta)p(x|\theta)}{p(x)}
$$

여기서 $p(\theta | x)$을 `Posterior`, $p(\theta)$를 `Prior`, $p(x|\theta)$을 `Likelihood`라고 한다.

`Posterior`는 어떤 관측치 $x$가 주어졌을 때, $\theta$의 확률모형을 의미한다.

`Prior`는 우리가 추정하려는 함수의 본 모습이다. 이를 파악하는 것은 사실상 불가능하기 때문에 가정하여 사용한다.

`Likelihood`는 prams가 주어졌을 때 관측치 $x$를 얻을 확률을 의미한다. 가능도는 확률변수가 아니다.

MLE는 Likelihood를, MAP는 Posterior를 각각 Maximize시켜 추정치를 얻는 방법론입니다.

## MLE

**관측치를 얻을 수 있는 최대의 가능성을 만드는 모수를 추정하는 알고리즘**이다. 

관측치 $X$의 관점에서 Likelihood는 다음과 같이 표현할 수 있다.

$$
L(\theta; x_1,x_2,...,x_n) = L(\theta;X) = p(X|\theta)
$$

만일 $X$가 i.i.d.일 경우 $p(X|\theta) = \Pi_i p(x_i|\theta)$이다.

$$
\begin{aligned}
\theta_{MLE} &= \argmax_{\theta} \log(P(X|\theta)) \\
& = \argmax_{\theta}\log\Pi_i p(x_i|\theta) \\
& = \argmax_{\theta} \sum_i \log p(x_i|\theta)
\end{aligned}
$$

## MAP

Posterior는 Prior와 Likelihood에 비례한다.

$$
\theta_{MAP} = \argmax_{\theta} \sum_i \log p(x_i|\theta)p(\theta)
$$

$p(\theta)$가 상수함수라면 MAP는 MLE가 된다. 따라서 MLE는 MAP의 special case이다.

## Reference

[1] https://niceguy1575.tistory.com/entry/MLE-vs-MAP-Maximum-Likelihood-or-Maximum-a-Posteriori