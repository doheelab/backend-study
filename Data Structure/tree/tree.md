# [Python, JavaScript] 이진 트리(Binary Tree)와 트리 순회(Tree Traversal)

이번 글에서는 `이진 트리(Binary Tree)`와 `트리 순회(Tree Traversal)`에 대해서 알아보고, `Python`과 `JavaScript`를 이용해서 구현해보겠습니다.

## `그래프(Graph)`

- `노드(node)`들과 노드들을 연결하는 `간선(edge)`들로 구성되어 있습니다.
- 그래프는 `root node`가 하나 있고, 각 노드에 `child node`가 연결되어 있습니다.

## `트리(Tree)`

- 그래프의 일종으로, `cycle`이 없고, 서로 다른 두 노드를 잇는 길이 하나 뿐인 그래프를 `트리`라고 합니다.
- 노드가 `N개`인 트리는 항상 `N-1개`의 간선을 가집니다.
- `child`의 갯수가 2개로 제한되면 `Binary Tree`라고 합니다.

## 이진 트리의 종류

- `Full Binary Tree`: 각각의 노드가 `child`가 0개 혹은 2개
- `Complete Binary Tree`: 왼쪽 위에서부터 가득 차 있는 트리
- `Perfect Binary Tree`: 모든 내부 노드가 2개의 `children`을 가지고 있으며, `leaf node`의 `level`이 같은 트리

## `이진 트리 순회 알고리즘(Binary Tree Traversal)` 

이진 트리 순회 알고리즘은 트리에 저장된 모든 값을 중복이나 빠짐없이 살펴보고 싶을 때 사용합니다. 이진 트리의 순회 방법 중 `깊이 우선 순회 방법(Depth First Traversal)`으로는 `전위 순회(Pre-order traversal)`, `정위 순회(In-order traversal)`, `후위 순회(Post-order traversal)`가 있으며, `너비 우선 순회 방법(Breadth First Traversal)`으로는 `레벨 순회`가 있습니다.

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/71360682/112273731-05464480-8cc1-11eb-9316-831b34246be2.png" /></div>

<div align="center">
  <i>Binary Tree 1 (from 코드없는프로그래밍)</i>
</div>

- `Pre-order`: **N**LR
- `In-order`: L**N**R
- `Post-order`: LR**N**
- `Level-order`: **N**LR

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/71360682/112273743-0a0af880-8cc1-11eb-9953-1bf855e4dd17.png" /></div>

<div align="center">
  <i>Binary Tree 2 (from 코드없는프로그래밍)</i>
</div>

- `Pre-order`: 1 2 4 5 3 6 7
- `In-order`: 4 2 5 1 6 3 7
- `Post-order`: 4 5 2 6 7 3 1
- `Level-order`: 1 2 3 4 5 6 7

## 이진 트리 순회 알고리즘의 구현

이진 트리 순회 방법 중 `깊이 우선 순회 방법(BFS)`은 `재귀적(Recursive)` 혹은 `반복적(Iterative)` 방법으로 구현할 수 있습니다. 먼저 재귀적인 방법으로 구현해보겠습니다.

## 재귀적(Recursive) 방법

### 트리 정의하기

```python
class TreeNode:
  def __init__(self, val=0):
    self.val = val
    self.left = None
    self.right = None
```

### 전위 순회(Pre-order)

```python
def recursivePreOrder(node):
  if node is None:
    return
  print(node.val, end=' ')
  recursivePreOrder(node.left)
  recursivePreOrder(node.right)
```

### 정위 순회(In-order)

```python
def recursiveInOrder(node):
  if node is None:
    return
  recursiveInOrder(node.left)
  print(node.val, end=' ')
  recursiveInOrder(node.right)
```

### 후위 순회(Post-order)

```python
def recursivePostOrder(node):
  if node is None:
    return
  recursivePostOrder(node.left)
  recursivePostOrder(node.right)
  print(node.val, end=' ')
```

## 반복적(Iterative) 방법

반복적인 방법으로 구현하는 것은 더욱 복잡합니다. 먼저 그림을 통해 살펴보겠습니다.

<div style="text-align:center"><img src="http://108.61.119.12/wp-content/uploads/2014/10/binary-tree-1-pre-order-small.gif" /></div>
<div style="text-align:center"><img src="http://108.61.119.12/wp-content/uploads/2014/10/binary-tree-1-order-small.gif" /></div>
<div style="text-align:center"><img src="http://108.61.119.12/wp-content/uploads/2014/10/binary-tree-1-post-order-small.gif" /></div>

<img src="http://108.61.119.12/wp-content/uploads/2014/10/binary-tree-1-pre-order-small.gif" alt="" title="http://108.61.119.12/wp-content/uploads/2014/10/binary-tree-1-pre-order-small.gif" width="330px" />


```python
def iterativePreOrder(node):
  stack = []
  stack.append(node)
  while 0<len(stack):
    pop_node = stack.pop()
    print(pop_node.val, end=' ')
    if pop_node.right:
      stack.append(pop_node.right)
    if pop_node.left:
      stack.append(pop_node.left)

def iterativeInOrder(node):
  crnt_node = node
  stack = []
  while True:
    if crnt_node is not None:
      stack.append(crnt_node)
      crnt_node = crnt_node.left

    elif 0<len(stack):
      crnt_node = stack.pop()
      print(crnt_node.val, end=' ')
      crnt_node = crnt_node.right
    else:
      break;

def iterativePostOrder(node):
  stack = []
  last_visit_node = None
  crnt_node = node
  while True:
    if crnt_node is not None:
      stack.append(crnt_node)
      crnt_node = crnt_node.left

    elif 0<len(stack):
      peek_node = stack[-1]
      if peek_node.right and last_visit_node != peek_node.right:
        crnt_node = peek_node.right
      else:
        print(peek_node.val, end=' ')
        last_visit_node = stack.pop()
    else:
      break
```


## 관련문항 (LeetCode)

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## 참고자료

[1] [Inorder Preorder Postorder Traversal of Binary Tree](https://laptrinhx.com/inorder-preorder-postorder-traversal-of-binary-tree-3322436720/)

[2] [[자료구조] Javascript로 Tree와 Tree 순회 구현하기](https://gogomalibu.tistory.com/55)

[3] [코딩테스트, 기초, 트리, Tree 소개](https://www.youtube.com/watch?v=bOZhvOc5xlQ&list=PLDV-cCQnUlIaTA41swrZwgH4mX7iPxLH4&index=1)

[4] [파이썬을 사용한 이진 트리와 순회 알고리즘 구현 (2)](http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-2.html)

## 다음주제

Graph Traversal (DFS, BFS)
