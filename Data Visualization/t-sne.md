
## Introduction

- Nonlinear Dimiension Reduction for Visualization (2d, 3d)

- Gradient-based ML Algorithm

## Stochastic Neighbor Embedding

- 원공간에 존재하는 데이터 $x$의 이웃 간의 거리를 최대한 보존하는 저차원의 $y$를 학습

- stochastic이란 이름이 붙은 이유는 거리 정보를 확률적으로 나타내기 때문

$$ 
p_{j|i} = \frac{e^{\frac{-|x_i - x_j|}{2\sigma_i^2}}}{\sum_k e^{-\frac{|x_i - x_k|^2}{2\sigma_i^2}}}
$$

$$
q_{j|i} = \frac{e^{-|y_i-y_j|^2}}{\sum_k e^{-|y_i-y_k|^2}}
$$

- $p$는 **고차원 원공간에 존재**하는 $i$번째 개체 $x_i$가 주어졌을 때 $j$번째 이웃인 $x_j$가 선택될 확률

- $q$는 **저차원 임베딩에서 존재**하는 $i$번째 개체 $y_i$가 주어졌을 때 $j$번째 이웃인 $y_j$가 선택될 확률

- SNE의 목적은 p와 q의 분포 차이가 최대한 작게 하는 것

## Cost function

$$
\begin{aligned}
Cost =& \sum_i KL(P_{i} || Q_{i}) \\
 = & \sum_i \sum_j p_{j|i} \log \left(\frac{p_{j|i}}{q_{j|i}} \right)
\end{aligned}
$$

계산 속도를 높이기 위해, $\sigma_i$ 를 고정하고, $p_{i|j} = p_{j|i}$를 가정한다.

$$
p_{ij} = \frac{p_{j|i}+p_{i|j}}{2}, q_{ij} = \frac{q_{j|i}+q_{i|j}}{2}
$$

새로운 비용함수는 다음과 같다.

$$
\begin{aligned}
Cost =& \sum_i KL(P_i || Q_i) \\
 = & \sum_i \sum_j p_{ij} \log \left(\frac{p_{ij}}{q_{ij}} \right) \\
 = & 4\sum_j (y_j -y_i)(p_{ij}-q_{ij})
\end{aligned}
$$

이에 따라 gradient descent 방식으로 $y_i$들을 업데이트합니다. 


# Reference

[PR-103: Visualizing Data using t-SNE] https://www.youtube.com/watch?v=zpJwm7f7EXs

[t-SNE] https://ratsgo.github.io/machine%20learning/2017/04/28/tSNE/