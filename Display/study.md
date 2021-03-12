
## CNC 공정

컴퓨터 소프트웨어가 기계의 이동을 제어하는 공정

전류데이터 분석을 통해, 불량품 감지 프로젝트

Random forest, Decision tree


## 유한차분법 vs 유한요소법

### FDM

efficient quadrature-free implementation

solution is only defined pointwise, so reconstruction at arbitrary locations is not uniquely defined

boundary conditions tend to be complicated to implement

### FEM

1. Convert the original BVP into its weak form.

2. Discretization, where the weak form is discretized in a finite-dimensional space $V$ (piecewise polynomial functions).

3. To complete the discretization, we must select a basis of $V$.

4. 1, 3을 결합하여 linear system을 얻을 수 있다.

## 행렬부호함수 (JCF)

복수수에서의 부호함수를 일반화한 함수

### 조르당 표준형

주어진 행렬과 닮고, 대각행렬에 가장 가까운 행렬

조르당 표준형은 다른 정리를 증명하는 데 자주 쓰이고, 행렬의 여러 성질을 쉽게 계산 가능

### 대각화 가능의 필요충분 조건

algebraic multiplicity (근의 중복도) = geometric multiplicity (고유 공간의 차원)



## Riccati 방정식

비선형미분방정식 중, 1, 2차항이 존재하는 미분방정식

![](https://ssl.pstatic.net/images.se2/smedit/2018/10/30/jnvov16l66h01v.jpg)

## 확률미분방정식

- 하나 이상의 항이 Stochastic process인 미분방정식

- 해가 확률과정이 된다.

### Stochastic process

a family of random variables

### 확률 공간

전체 측도가 1인 측도 공간 $(\omega, F, Pr), Pr(\Omega)= 1$

### Random variables

Probability space에 정의된 measurable real-valued function 

## P 문제

결정론적 튜링 기계를 사용해 다항시간 내에 답을 구할 수 있는 문제

## NP 문제

비결정론적 튜링 기계를 사용해 다항시간 내에 답을 구할 수 있는 문제

## NP-난해

모든 NP 문제를 다항시간 내에 어떤 문제 A로 환원가능 할 때, 그 A.

## NP-완전

NP-난해 문제이면서 동시에 NP 문제

## P NP 문제

P 집합과 NP-완전 집합이 같은 집합인지를 묻는 문제