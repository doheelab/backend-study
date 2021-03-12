
## 세 개의 트리

Git은 일반적으로 세 가지 트리를 관리하는 시스템

트리 | 역할 
---|:---:
HEAD | 	마지막 커밋 스냅샷, 다음 커밋의 부모 커밋 | 
Index | 다음에 커밋할 스냅샷 |
워킹 디렉토리 | 샌드박스 |

## HEAD

HEAD는 현재 브랜치를 가리키는 포인터이며, 브랜치는 브랜치에 담긴 커밋 중 가장 마지막 커밋을 가리킨다. 지금의 HEAD가 가리키는 커밋은 바로 다음 커밋의 부모가 된다. 단순하게 생각하면 HEAD는 *현재 브랜치 마지막 커밋의 스냅샷*이다.

## Index

Index는 바로 다음에 커밋할 것들이다. 이미 앞에서 우리는 이런 개념을 `Staging Area` 라고 배운 바 있다. `Staging Area` 는 사용자가 `git commit` 명령을 실행했을 때 `Git`이 처리할 것들이 있는 곳이다.

## 워킹 디렉토리

워킹 디렉토리는 샌드박스로 생각하자. 커밋하기 전에는 Index(Staging Area)에 올려놓고 얼마든지 변경할 수 있다.

## Workflow

![git](https://git-scm.com/book/en/v2/images/reset-workflow.png)




## Reference

https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0