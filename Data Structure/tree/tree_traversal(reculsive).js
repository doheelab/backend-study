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

// in-order
var recursiveInOrder = function (node) {
  if (!node) {
    return;
  }
  this.recursiveInOrder(node.leftNode);
  console.log(node.val);
  this.recursiveInOrder(node.rightNode);
};

// pre-order
var recursivePreOrder = function (node) {
  if (!node) {
    return;
  }
  console.log(node.val);
  this.recursivePreOrder(node.leftNode);
  this.recursivePreOrder(node.rightNode);
};

// post-order
var recursivePostOrder = function (node) {
  if (!node) {
    return;
  }
  this.recursivePostOrder(node.leftNode);
  this.recursivePostOrder(node.rightNode);
  console.log(node.val);
};

// 출력하기
console.log(">>>> InOrder Start!! ");
recursiveInOrder(root);

console.log(">>>> preOrder Start!! ");
recursivePreOrder(root);

console.log(">>>> postOrder Start!! ");
recursivePostOrder(root);
