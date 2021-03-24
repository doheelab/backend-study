
트리는 나무구조를 가지고 있다.

root 노드가 하나 있고, children 노드가 연결되어 있다.

각각의 노드는 child를 가질 수 있다.

child의 갯수가 2개로 제한되면 binary tree라고 한다.

- full binary tree: 각각의 노드가 child가 0개 혹은 2개
- complete binary tree: 왼쪽 위에서부터 가득 차 있는 tree
- perfect binary tree: 모든 내부 노드가 2개의 children을 가지고 있으며, leaf 노드의 level이 같은 tree
  

tree traverse

[NLR]

- pre-order: **N**LR
- in order: L**N**R
- post order: LR**N**

[perfect-binary-tree]

- pre-order: 1 2 4 5 3 6 7
- in order: 4 2 5 1 6 3 7
- post order: 4 5 2 6 7 3 1

## Python Implementation

```python
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

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
```