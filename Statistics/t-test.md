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

---

## t-value

두 분포의 차이 / 불확실도 

값이 1보다 크면, 차이가 유의미 (차이가 불확실도 보다 크다)

---

## t-test for one mean

- 영가설: 평균이 $\mu_0$ 이다.

- 표준편차가 알려진 경우, z-test를 사용

- 표준편차가 알려지지 않은 경우, $t = \frac{\bar{X}-\mu}{s/\sqrt{n}}$를 사용 


---

## t-test for two means

- 가정: 정규분포, 비슷한 분산, 데이터 갯수 동일, 데이터 갯수 (20-30, 그 이상은 z-test)

- 통계적으로 유의미한 차이가 있는가? (p=0.05, 95% 확률로)


$$
t-value = \frac{\bar{x_1}-\bar{x_2}}{S_{\bar{x_1}-\bar{x_2}}} = \frac{\bar{x_1}-\bar{x_2}}{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
$$

---

## Student t-test

$$

Z = \frac{\bar{X} - \mu}{ \sigma / \sqrt{n}}, \\ \\

$$


만일 $\sigma$를 모른다면, 표본의 표준편차 사용한다.

$$

t = \frac{\bar{X}-\mu}{s/\sqrt{n}}

$$

$s$ 값은 샘플에 따라 변하기에, $t$는 더 이상 정규분포를 따르지 않는다.

이 때 $t$ 값이 따르는 분포를 $t$ 분포라고 한다 (자유도 $n-1$).


---

- 두 표본 간의 유의미한 통계적 차이가 있는지 확인

- Assumations: Normal distribution, Similar variance, use same numbers for two data points, 20-30+ (higher we use z-test) 


--- 

## p-value

- 영가설이 성립할 때 관측값 혹은 더 극단적인 것이 나올 확률
- A measure of the strength of the evidence against the **null hypothesis**.






- The probability of getting the observed value of the test statistic, 
or a value with even greater evience against the null hypothesis.

- The smaller the p-value, the greater the evidence against the null hypothesis.

- Reject $H_0$ if p-value $\le \alpha$. 