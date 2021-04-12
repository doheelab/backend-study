## Convex optimization problem

Convex optimization problem은 optimization problem의 한 종류이다.

$$
\text{min}_{x \in D} f(x) \\
\text{subject to  } g_i(x) \le 0, i = 1,...,m \\
 h_j(x)=0, j = 1,...,r
$$
where $f$ and $g_i$ are convex, $h_j$ is affine.

>affine function
>
>$h_j(x)=a_j^Tx+b_j, j=1,...,r$

<br/>

## Lagrangian

다음 최적화 문제에 대한 Lagrangian을 살펴보자.

$$
\text{min}_{x \in D} f(x) \\
\text{subject to  } h_i(x) \le 0, i = 1,...,m \\
 l_j(x)=0, j = 1,...,r
$$

>Lagrangian
>
>$L(x,u,v)= f(x) + \sum_{i=1}^{m}{u_ih_i(x)}+\sum_{j=1}^{r}v_jl_j(x)$
>where $u \ge  0$

Lagrangian은 다음 성질을 갖는다.

>모든 $u \ge 0, v$에 대해 $f(x) \ge L(x,u,v)$ for each feasible $x$.


<br/>

## Lagrange dual function

$C$: primal feasible set일 때,

> $f^{\ast} \ge \min_{x \in C} L(x,u,v) \ge \min_{x}L(x,u,v):= g(u,v)$

여기서 $g(u,v)$를 **Lagrange dual function**이라고 하며, 임의의 $u \ge 0,v$에 대해 $f^{\ast}$의 lower bound를 제공한다.

<br/>

### Lagrange dual problem
> 
> $\max_{u,v}g(u,v)$ such that $u \ge 0$

Lagrange dual problem은 primal problem이 convex가 아니더라도 항상 convex가 된다.

## Strong duality

어떤 문제에서 $f^{\ast} = g^{\ast}$를 만족하면 **strong duality**라고 한다. **Slater** 조건은 strong duality의 충분조건이다.

> Slater 조건
> 
> 만일 primal 문제가 convex이고 strictly feasuble한 $x$가 하나 이상 있으면 stroing duality를 만족한다.



## KKT 조건

primal problem이 convex일 때, **Karush–Kuhn–Tucker (KKT) conditions**는 **strong duality의 충분조건**이 된다. 또한 primal problem의 목적함수 및 제약함수들이 미분 가능하며 strong duality를 만족할때는 primal & dual optimal points에서 항상 KKT conditions를 만족하게 된다. KKT conditions는 최적화에서 상당히 중요한 위치를 차지하고 있다. 이 조건은 몇몇 특수한 문제들을 해석적으로(analytically) 풀 수 있게끔 해주기도 하며, 또한 컨벡스 최적화의 많은 알고리즘들이 KKT conditions를 풀기 위한 방법으로 해석되기도 한다. 

## Reference

[1] 모두를 위한 컨벡스 최적화