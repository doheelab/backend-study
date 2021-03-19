## Purpose of Ensemble

* Goal: Reduce the error through constructing multiple learners to

    * Reduce the variance: Bagging

    * Reduce the bias: AdaBoost

    * Both: Mixture of experts

* Two key questions on the ensemble construction

    * Q1: How to generate individual components of the ensemble systems to achieve sufficient degree of **diversity**?

    * Q2: How to combine the outputs of indivisual classifiers?

## Why Ensemble works?

The average error made by M indivisual models vs. Expected eeror of the emsemble

$$
E_{Avg} = \frac{1}{M}{\sum_{m=1}^M{E_x[\epsilon_m(x)^2]}}
$$

$$
\begin{aligned}
E_{Ensemble} =& E_x\left[\left(\frac{1}{M} \sum_{m=1}^{M}{y_m(x)-f(x)} \right)^2\right] \\
=& E_x\left[\left(\frac{1}{M} \sum_{m=1}^{M}{\epsilon_m(x)} \right)^2\right]
\end{aligned}
$$

Therefore,

$$
E_{Emsemble} = \frac{1}{M}{E_{Avg}},
$$

given that **zero mean** and are **uncorrelated**.

In reality (errors are correlated), by the Cauchy's inequallity,

$$
\left[\frac{1}{M}{\sum_{m=1}^{M}{\epsilon_m(x)}}\right]^2 \le \frac{1}{M}{\sum_{m=1}^{M}{\epsilon_m(x)^2}},
$$
or
$$
E_{Emsemble} \le E_{Avg}
$$


## Reference

https://www.youtube.com/watch?v=mZwszY3kQBg&t=411s