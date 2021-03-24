# [Python, JavaScript] 이진 트리(Binary Tree)와 트리 순회(Tree Traversal)

이번 글에서는 `이진 트리(Binary Tree)`와 `트리 순회(Tree Traversal)`에 대해서 알아보고, `Python`과 `JavaScript`를 이용해서 구현해보겠습니다.

## `그래프(Graph)`

- `node`와 node 사이를 잇는 `path`로 구성된 자료구조
- 그래프는 `root node`가 하나 있고, 각 `node`에 `child node`가 연결되어 있습니다.

## `트리(Tree)`

- 그래프의 일종으로, `cycle`이 없고, 서로 다른 두 `node`를 잇는 길이 하나 뿐인 그래프를 트리라고 합니다.
- `child`의 갯수가 2개로 제한되면 `binary tree`라고 합니다.

## `Binary Tree`의 종류

- `full binary tree`: 각각의 `node`가 `child`가 0개 혹은 2개
- `complete binary tree`: 왼쪽 위에서부터 가득 차 있는 트리
- `perfect binary tree`: 모든 내부 `node`가 2개의 `children`을 가지고 있으며, `leaf node`의 `level`이 같은 트리

## `Binary Tree Traversal`

<!-- <div style="text-align:center"><img src="https://cdn-images-1.medium.com/max/350/0*YzOEfnGnWTPbsUkv" /></div> -->

<!-- <div align="center">
  <i>Types of Binary Tree Traversal</i>
</div>

<br/> -->

### 3가지 타입

트리의 node들을 어떤 순서로 방문하느냐에 따라 `in-order`, `pre-order`, `post-order traversal`로 구분합니다.

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/71360682/112273731-05464480-8cc1-11eb-9316-831b34246be2.png" /></div>

<div align="center">
  <i>Binary Tree 1 (from 코드없는프로그래밍)</i>
</div>

- `pre-order`: **N**LR
- `in-order`: L**N**R
- `post-order`: LR**N**

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/71360682/112273743-0a0af880-8cc1-11eb-9953-1bf855e4dd17.png" /></div>

<div align="center">
  <i>Binary Tree 2 (from 코드없는프로그래밍)</i>
</div>

- `pre-order`: 1 2 4 5 3 6 7
- `in-order`: 4 2 5 1 6 3 7
- `post-order`: 4 5 2 6 7 3 1

### 2가지 구현 방법

`tree traversal`은 `recursive` 혹은 `iterative` 하게 구현할 수 있습니다.

## Implementation in Python

```python
# 트리 정의하기
class TreeNode:
  def __init__(self, val=0):
    self.val = val
    self.left = None
    self.right = None

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# 부모, 자식 관계 만들기
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

def recursivePreOrder(node):
  if node is None:
    return
  print(node.val, end=' ')
  recursivePreOrder(node.left)
  recursivePreOrder(node.right)

def iterativePreOrder(node):
  if node is None:
    return
  stack = []
  stack.append(node)
  while 0<len(stack):
    pop_node = stack.pop()
    print(pop_node.val, end=' ')
    if pop_node.right:
      stack.append(pop_node.right)
    if pop_node.left:
      stack.append(pop_node.left)

recursivePreOrder(node1)
print(' ')
iterativePreOrder(node1)
```

```python
def recursiveInOrder(node):
  if node is None:
    return
  recursiveInOrder(node.left)
  print(node.val, end=' ')
  recursiveInOrder(node.right)

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

recursiveInOrder(node1)
print(' ')
iterativeInOrder(node1)
```

```python
def recursivePostOrder(node):
  if node is None:
    return
  recursivePostOrder(node.left)
  recursivePostOrder(node.right)
  print(node.val, end=' ')

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


recursivePostOrder(node1)
print(' ')
iterativePostOrder(node1)
```

## 관련문항 (LeetCode)

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## 참고자료

[1] [Inorder Preorder Postorder Traversal of Binary Tree](https://laptrinhx.com/inorder-preorder-postorder-traversal-of-binary-tree-3322436720/)

[2] [[자료구조] Javascript로 Tree와 Tree 순회 구현하기](https://gogomalibu.tistory.com/55)

[3] [코딩테스트, 기초, 트리, Tree 소개](https://www.youtube.com/watch?v=bOZhvOc5xlQ&list=PLDV-cCQnUlIaTA41swrZwgH4mX7iPxLH4&index=1)

## 다음주제

Graph Traversal (DFS, BFS)
