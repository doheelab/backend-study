## Spark

## 1. Spark 소개

- 기존의 MapReduce와 비교해서 더 일반적인 데이터 프로세싱 모델을 지원
- Java, Scala, Python API 제공
- Map, Reduce로 제한된 그래프가 아니라, 다양한 operator를 제공하고, 그런 operator가 다양한 형식으로 연결될 수 있다.
- RDD(Resilient Distributed Datasets)를 통해서 In-memory 계산을 지원 -> 중간에 계산된 결과를 메모리에 저장해놓고, 후에 계산을 할 때 빠르게 access하여 사용할 수 있다.
- RDD: cluster의 여러 머신에 나눠져서 저장되어 있는 변화지 않는 object의 collection