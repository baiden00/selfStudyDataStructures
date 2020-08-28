from collections import deque

class Node:
    def __init__(self, value=None):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self, root):
        self.root=Node(root)

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if not cur_node.right:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree")

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def height(self, node):
        if not node:
            return 0
        l = self.height(node.left)
        r = self.height(node.right)
        return max(l,r)+1

    def search(self, val, node):
        def help(node, val):
            if not node:
                return False

            if node.value == val:
                return True
            elif val < node.value:
                return help(node.left, val)
            else:
                return help(node.right, val)
        return help(node, val)



tree = BST(5)
nums = [6,9,20,32,35,43,54,59,97]
#nodes = [5,12,16,29,35,43,51,57,62,77,82,90]

for num in nums:
    tree.insert(num)

print(tree.print_tree())
print("")
#print(tree.height(tree.root))
print(tree.search(70, tree.root))
print(tree.search(59, tree.root))
print("")



''' Custom tree
               5
             /   \
            /     \
           21       3
          /      /  \
         /      /    \
        4      15      11
              / \
             /   \
            7     13
'''

roooot = Node(5)
roooot.left = Node(21)
roooot.right = Node(3)
roooot.left.left = Node(4)
roooot.right.left = Node(15)
roooot.right.right = Node(11)
roooot.right.left.left = Node(7)
roooot.right.left.right = Node(13)

testNode = Node(1)
testNode.left = Node(2)
testNode.right = Node(3)
testNode.left.left = Node(4)
testNode.left.right = Node(5)

'''

      1
     / \
    2   3
   / \
  4   5

'''


#######TREE TRAVERSAL FUNCTIONS################

def recursivePreOrder(root):
    output = ""
    if root:
        output += str(root.value) + "-"
        output+= recursivePreOrder(root.left)
        output+= recursivePreOrder(root.right)
    return output

def iterativePreOrder(root):
    if not root:
        return
    stack = deque()
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.value, end = "-")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def recursiveInorder(root):
    output = ""

    if root:
        output+= recursiveInorder(root.left)
        output+=str(root.value) + "-"
        output+=recursiveInorder(root.right)

    return output

def iterativeInOrder(root):
    stack = deque()
    output = deque()
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr=curr.left
        else:
            curr = stack.pop()
            output += [str(curr.value)] + ["-"]
            curr=curr.right

    return ''.join(val for val in output)

def recursivePostOrder(root):
    arr = deque()
    if root:
        arr+=recursivePostOrder(root.left)
        arr+=recursivePostOrder(root.right)
        arr+=[str(root.value)] + ["-"]
    return ''.join(val for val in arr)

def iterativePostOrder(root):
    out = []
    stack = deque()
    stack.append(root)

    while stack:
        curr = stack.pop()
        out.extend(["-",str(curr.value)])

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return ''.join(val for val in out[::-1])


def levelOrder(root):
    stack = deque()
    output = []

    if not root:
        return

    stack.append(root)
    while stack:
        curr = stack.pop()
        output.extend([str(curr.value), "-"])

        if curr.left:
            stack.appendleft(curr.left)
        if curr.right:
            stack.appendleft(curr.right)

    return ''.join(val for val in output)


## Some random functions
def height(root):
    if not root:
        return 0
    l = height(root.left)
    r = height(root.right)
    return max(l,r)+1

def summ(root):
    if not root:
        return 0
    return int(root.value) + summ(root.left) + summ(root.right)

def prod(root):
    if not root:
        return 1
    return int(root.value) * prod(root.left) * prod(root.right)

print(recursivePreOrder(roooot))
print(iterativePreOrder(roooot))
print("")
print(recursiveInorder(roooot))
print(iterativeInOrder(roooot))
print("")
print(recursivePostOrder(roooot))
print(iterativePostOrder(roooot))
print(iterativePostOrder(testNode))


print("")
print(levelOrder(testNode))
print(levelOrder(roooot))

print("")
print(height(testNode))
print(height(roooot))

print(summ(testNode))
print(prod(testNode))

print(iterativeInOrder(tree.root))
