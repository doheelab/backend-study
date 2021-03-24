// 트리 정의하기
class Tree {
  constructor(val) {
    this.val = val;
    this.leftNode = null;
    this.rightNode = null;
  }

  setVal(val) {
    this.val = val;
  }

  setLeft(node) {
    this.leftNode = node;
  }

  setRight(node) {
    this.rightNode = node;
  }

  // in-order
  inOrderTree(node) {
    if (!node) {
      return;
    }
    this.inOrderTree(node.leftNode);
    console.log(node.val);
    this.inOrderTree(node.rightNode);
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

  // post-order
  postOrderTree(node) {
    if (!node) {
      return;
    }

    this.postOrderTree(node.leftNode);
    this.postOrderTree(node.rightNode);
    console.log(node.val);
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
root.leftNode.setLeft(node4);
root.leftNode.setRight(node5);
root.rightNode.setLeft(node6);
root.rightNode.setRight(node7);

// 출력하기
console.log('>>>> InOrder Start!! ');
root.inOrderTree(root);

console.log('>>>> preOrder Start!! ');
root.preOrderTree(root);

console.log('>>>> postOrder Start!! ');
root.postOrderTree(root);

var preorderTraversal = function (root) {
  /**
   * Algorithm:
   * 1. Create an empty stack [];
   * 2. Do while stack is not empty:
   * 2.1. Pop an item from stack and add it to the 'result' array.
   * 2.2. Push 'right child' of popped item to stack.
   * 2.3. Push 'left child' of popped item to stack.
   */
  if (root == null) {
    return [];
  }

  const stack = [];
  const result = [];

  stack.push(root);

  while (stack.length > 0) {
    let current = stack.pop();
    result.push(current.val);

    if (current.right) stack.push(current.right);
    if (current.left) stack.push(current.left);
  }

  return result;
};