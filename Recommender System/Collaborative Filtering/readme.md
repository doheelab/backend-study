

## 특징

1. 구현이 간단하다.
2. Model-based CF에 비해 계산량이 적다.
3. 새로운 user, item이 추가되더라도 안정적으로 작동한다.

## User-based

- 유저 간 유사도를 활용
- 유저 집단 간 유사도가 높은 경우 유리
- 새로운 데이터를 추천하기에 유리하다.

## Item-based

- 아이템 간 유사도를 활용
- 실제로 많이 활용 (아이템의 수가 크게 변하지 않을 때)
- 새로운 item을 비슷한 item의 가중 평균으로 설명할 수 있다.
- 유저는 제각각인데, item은 어느정도 비슷한 구석이 있다.
- 과거 데이터에 대해 의존도가 높아서, 새로운 데이터를 추천하기 어렵다.


## Cold-start 문제

- 충분한 데이터가 없다면 좋은 추천을 할 수 없다.
- content-based 혹은 deep-learning으로 해결

## Long-tail

- 인기있는 소수의 아이템 쏠림 현상

## 코사인, 자카드, 피어슨

- 자카드 = IOU를 통해 유사도를 계산 (예를 들어 같이 본 영화/둘 중 하나가 본 영화)
- 피어슨 유사도: 정규화 후 코사인 유사도를 구한다.
  - 예를 들어, 벡터 (5,5,5,5)와 (1,1,1,1)은 코사인 유사도는 1이지만, 피어슨 유사도는 -1이다.



## How to create a production-ready Recommender System


## The cold start problem

The very common problem when building recommender systems is the cold start problem. Every new user will not have any of their behavior recorded in the system.


## Reference

[How to create a production-ready Recommender System](https://towardsdatascience.com/how-to-create-a-production-ready-recommender-system-3c932752f8ea)