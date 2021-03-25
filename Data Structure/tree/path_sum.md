## target sum ![link](https://leetcode.com/problems/path-sum-ii/)

> root로부터 leaf까지의 합이 target sum이 되는 모든 path 찾기

(Solution) backtracking과 tree treversal을 사용

- time complexity = O(n)

- space complexity = O(depth)

```javascript
var pathSum = function(root, sum) {
  var res = [];
  helper(root, sum, [], res);
  return res;
};

var helper = function (root, sum, now, res) {
  if (!root) return;

  now.push(root.val);

  if (root.val === sum && !root.left && !root.right) res.push(now);

  helper(root.left, sum - root.val, Array.from(now), res);
  helper(root.right, sum - root.val, Array.from(now), res);
};
```