## target sum ![link](https://leetcode.com/problems/path-sum-ii/)

> root로부터 leaf까지의 합이 target sum이 되는 모든 path 찾기

(Solution) backtracking과 tree treversal을 사용

- time complexity = O(n)

- space complexity = O(depth)

```python
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(7)
node2n = TreeNode(-2)
node5 = TreeNode(5)
node3 = TreeNode(3)
node15 = TreeNode(15)
node8 = TreeNode(8)
node5n = TreeNode(-1)

root.left = node2n
root.right = node5
node2n.left = node3
node2n.right = node15
node5.left = node8
node5.right = node5n

def treeLevelPrint(node):
  if node is None:
    return
  q = deque()
  q.append(node)
  while 0<len(q):
    level_count = len(q)
    for _ in range(level_count):
      crnt_node = q.popleft()
      print(crnt_node.val, end = ' ')
      if crnt_node.left:
        q.append(crnt_node.left)
      if crnt_node.right:
        q.append(crnt_node.right)
    print('')

treeLevelPrint(root)
```