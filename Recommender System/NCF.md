## Neural Collaborative Filtering

## Introduction

1. 기존 Linear Matrix Factorization의 한계점을 개선한다.
2. NN 기반의 Collaborative Filtering을 사용한다.
3. user와 item의 관계를 보다 복잡하게 모델링한다.

## Contributions

1. User와 item의 latent features를 모델링 (General Framework NCF)
2. Matrix Factorization을 NCF의 special case로 포함

## Learning from Implicit Data

1. Interaction이 있는지에 따라 user와 item 간의 값을 0 또는 1로 표현
2. User가 item와 interaction이 있을 확률을 예측
3. 2가지 objective function
   -  Point-wise: 실제값과 예측값 차이를 최소화.
   -  Pair-wise: BPR에서 사용했으며, 1이 0보다 큰 값을 갖도록 마진을 최대화

## Generalized Matrix Factorization

1. Matrix Factorization

$$
\phi_1(p_u, q_i) = p_u
$$

2. Neural CF

$h$ 가 1이면 MF와 같다.

$$
\hat{y_{ui}} = a_{out}(h^T(p_u \odot q_i))
$$

## Multi-Layer Perceptron

GMF보다 더 간단하게 user-item interaction을 학습할 수 있다.

$$
 \begin{aligned}
 z_1 &= \phi_1(p_u, q_i) = \begin{bmatrix}
p_u\\
q_i
\end{bmatrix}, \\
 \phi_2(z_1) &= a_{2}(W_2^T z_1+b_2), \\ 
 &...... \\
 \phi_L(z_{L-1}) &= a_{L}(W_L^T \textbf{z}_{L-1}+\textbf{b}_L), \\ 
 \hat{y}_{ui} &= \rho(\textbf{h}^T \phi_L(\textbf{z}_{L-1})), \\ 
 \end{aligned}
$$

## Neural Matrix Factorization (NMF)

GMF와 mLP를 결합한 최종 모델

![nmf](https://user-images.githubusercontent.com/57972646/118063714-950c9300-b3d4-11eb-8557-69847ed9a71f.png))