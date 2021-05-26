## Likelihood (가능도)

- 확률 분포의 모수가, 어떤 확률변수의 표집값과 일관되는 정도를 나타내는 값
- **주어진 표집값에 대한 모수의 가능도**
- 이 모수를 따르는 분포가 주어진 관측값에 대하여 부여하는 확률

가능도 함수는 확률 분포가 아니며, 합하여 1이 되지 않을 수 있다.

## 정의

확률변수 $X$가 모수 $\theta$에 대한 확률분포 $P_{\theta}(X)$를 가지며, $X$가 특정한 값 $x$으로 표집되었을 경우, $\theta$의 가능도 함수 $L(\theta|x)$는 다음과 같이 정의된다.

$$
L(\theta|x) = Pr(X=x|\theta)
$$

로그 가능도는 가능도 함수의 로그이며, 확률 변수가 독립 확률 변수로 나누어지는 경우에 계산의 편의성을 위해 사용된다.

$$
L(\theta|x) = P_{\theta}(X=x) = P_{1,\theta}(X_1=x_1)P_{2,\theta}(X_2=x_2)\cdots P_{n,\theta}(X_n=x_n) 
$$
$$
\log L(\theta|x) = \log P_{1,\theta}(X_1=x_1)+ \log P_{2,\theta}(X_2=x_2)+\cdots+\log P_{n,\theta}(X_n=x_n) = \sum_{i}\log P_{1,\theta}(X_i=x_i)
$$

## 예 1

어떤 동전을 던져서 나오는 결과를 확률 변수 $X$라고 한다면, 이 변수는 앞(F)과 뒤(B)의 두 값을 가질 수 있다. 동전을 던져 앞이 나올 확률이 

$$
Pr_{\theta} (X=F) = \theta
$$
로 주어지는 경우, 동전을 세 번 던져 앞, 뒤, 앞이 나왔을 때의 $\theta$의 가능도는
$$
L(\theta|FBF) = \theta^2 (1-\theta)
$$
가 된다. 가능도 함수를 적분하면
$$
\int_{0}^{1} L(\theta|FBF) = \int_{0}^{1} \theta^2(1-\theta) d\theta = 1/12
$$
이므로, 가능도는 확률 분포가 아니다.

## 베이즈 정리 (Bayes' Theorem)

사후 확률 (밀도)이 가능도 (Likelihood)과 사전확률에 비례한다.

## Reference

https://ko.wikipedia.org/wiki/%EA%B0%80%EB%8A%A5%EB%8F%84