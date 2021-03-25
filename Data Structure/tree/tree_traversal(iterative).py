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

def iterativePreorder(node):
    if node is None:
        return
    stack = []
    stack.append(node)
    while 0 < len(stack):
        pop_node = stack.pop()
        print(pop_node.val, end=" ")
        if pop_node.right:
            stack.append(pop_node.right)
        if pop_node.left:
            stack.append(pop_node.left)

def iterativeInorder(node):
    crnt_node = node
    stack = []
    while True:
        if crnt_node is not None:
            stack.append(crnt_node)
            crnt_node = crnt_node.left

        elif 0 < len(stack):
            crnt_node = stack.pop()
            print(crnt_node.val, end=" ")
            crnt_node = crnt_node.right

        else:
            break

def iterativePostorder(node):
    stack = []
    last_visit_node = None
    crnt_node = node
    while True:
        if crnt_node is not None:
            stack.append(crnt_node)
            crnt_node = crnt_node.left

        elif 0 < len(stack):
            peek_node = stack[-1]
            if peek_node.right and last_visit_node != peek_node.right:
                crnt_node = peek_node.right
            else:
                print(peek_node.val, end=" ")
                last_visit_node = stack.pop()
        else:
            break


iterativePreorder(node1)
print(" ")
iterativeInorder(node1)
print(" ")
iterativePostorder(node1)
