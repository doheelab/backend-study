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

var levelOrderTraversal = function (node) {
  let queue = [];
  queue.push(node);
  while (queue.length > 0) {
    let pop_node = queue.shift();
    console.log(pop_node.val);
    if (pop_node.left) queue.push(pop_node.left);
    if (pop_node.right) queue.push(pop_node.right);
  }
};

levelOrderTraversal(root);
