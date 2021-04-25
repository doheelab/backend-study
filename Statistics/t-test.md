## 모집단(population)과 모수(parameters)

**모집단**은 정보를 얻고자 하는 관심 대상의 전체 집합

**모수**는 모집단의 특성을 나타내는 평균, 분산, 표준편차, 분위수,...

## 표본집단과 표본 통계량

**표본**이란 모집단의 부분집합

**표본 통계량**이란 표본의 분포를 나타내는 표본 평균, 표본 표준편차,...

## 표준 오차

표본 통계량의 표준 편차

표준 오차는 모수*1/sqrt(n)

## 검정 통계량

 통계적 가설 진위 여부를 검정하기 위해 표본 통계량을 2차 가공한 것

## t-value

두 분포의 차이 / 불확실도 

값이 1보다 크면, 차이가 불확실도 보다 크다는 의미.

$$
t = \frac{\bar{x_1}-\bar{x_2}}{S_{\bar{x_1}-\bar{x_2}}} = \frac{\bar{x_1}-\bar{x_2}}{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
$$

## Student t-test

- 전체 분포의 표준편차를 모를 때 표본 표준편차 사용

$$

Z = \frac{\bar{X} - \mu}{ \sigma / \sqrt{n}}, \\ \\

t = \frac{\bar{X}-\mu}{s/\sqrt{}n}

$$


- 두 표본 간의 유의미한 통계적 차이가 있는지 확인

- Assumations: Normal distribution, Similar variance, use same numbers for two data points, 20-30+ (higher we use z-test) 


## p-value

- A measure of the strength of the evidence against the null hypothesis.

- The probability of getting the observed value of the test statistic, 
or a value with even greater evience against the null hypothesis.

- The smaller the p-value, the greater the evidence against the null hypothesis.

- Reject $H_0$ if p-value $\le \alpha$. 