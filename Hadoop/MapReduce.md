## MapReduce Programming Model

## 1. Map 함수

입력으로 하나의 key/value 쌍을 받아서 여러 개 또는 하나의 key/value 쌍을 만들어내는 함수

## 2. Reduce 함수

같은 중간 key를 갖는 여러 중간 value들을 합하여 특정 연산을 실행

## 3. MapReduce 프로그래밍의 예시

### 3-1. Wordcount 프로그램

여러 document가 있을 때, 모든 document에 각각의 단어가 몇 번 나왔는지 계산하기

이때 Map, Reduce 함수를 다음과 같이 정의해보자.

- Map: word -> (word, 1)
- Reduce (a, b) -> a+b

reduce task는 앞에 있는 모든 map task로부터 데이터를 받아온 후(Shuffle), 받은 데이터들에 대해 Reduce 함수를 수행하여 최종적인 결과를 만들어낸다.


