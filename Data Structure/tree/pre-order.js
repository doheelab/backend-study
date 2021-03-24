// 트리 정의하기
class Tree {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }

  setVal(val) {
    this.val = val;
  }

  setLeft(node) {
    this.left = node;
  }

  setRight(node) {
    this.right = node;
  }

  // pre-order
  preOrderTree(node) {
    if (!node) {
      return;
    }

    console.log(node.val);
    this.preOrderTree(node.leftNode);
    this.preOrderTree(node.rightNode);
  }
}

// 부모, 자식 관계 정의
let root = new Tree(1);
let node2 = new Tree(2);
let node3 = new Tree(3);
let node4 = new Tree(4);
let node5 = new Tree(5);
let node6 = new Tree(6);
let node7 = new Tree(7);
root.setLeft(node2);
root.setRight(node3);
root.left.setLeft(node4);
root.left.setRight(node5);
root.right.setLeft(node6);
root.right.setRight(node7);

var preOrderTraversal = function (node) {
  if (node == null) {
    return [];
  }
  let stack = [];
  stack.push(node);
  while (stack.length > 0) {
    let pop_node = stack.pop();
    console.log(pop_node.val);
    if (pop_node.right) stack.push(pop_node.right);
    if (pop_node.left) stack.push(pop_node.left);
  }
};

var InOrderTraversal = function (node) {
  if (node == null) {
    return [];
  }
  let crnt_node = node;
  let stack = [];
  while (true) {
    if (crnt_node != null) {
      stack.push(crnt_node);
      crnt_node = crnt_node.left;
    } else if (stack.length > 0) {
      crnt_node = stack.pop();
      console.log(crnt_node.val);
      crnt_node = crnt_node.right;
    } else {
      break;
    }
  }
};

var PostOrderTraversal = function (node) {
  let crnt_node = node;
  let stack = [];
  let last_visit_node = null;
  while (true) {
    if (crnt_node != null) {
      stack.push(crnt_node);
      crnt_node = crnt_node.left;
    } else if (stack.length > 0) {
      peek_node = stack[-1];
      if (peek_node.right && last_visit_node != peek_node.right) {
        crnt_node = peek_node.right;
      } else {
        console.log(peek_node.val);
        last_visit_node = stack.pop();
      }
    } else {
      break;
    }
  }
};

PreOrderTraversal(root);
console.log("---------");
InOrderTraversal(root);
console.log("---------");
PostOrderTraversal(root);
