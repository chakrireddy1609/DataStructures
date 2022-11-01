class Stack:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preOrder(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preOrder(start.left,traversal)
            traversal = self.preOrder(start.right,traversal)
        return traversal

    def inOrder(self,start,traversal):
        if start:
            traversal = self.inOrder(start.left,traversal)
            traversal += (str(start.value)+"-")
            traversal = self.inOrder(start.right,traversal)
        return traversal

    def postOrder(self,start,traversal):
        if start:
            traversal = self.postOrder(start.left,traversal)
            traversal = self.postOrder(start.right,traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def lvlOrderTraversal(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_lvlordertraversal(self,start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.enqueue(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.dequeue()
            traversal += str(node.value) + "-"
        return traversal

    def printTree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preOrder(tree.root, "")
        elif traversal_type == "inorder":
            return self.inOrder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postOrder(tree.root, "")
        elif traversal_type == "lvlorder":
            return self.lvlOrderTraversal(tree.root)
        elif traversal_type == "reverse_lvlordertraversal":
            return self.reverse_lvlordertraversal(tree.root)
        else:
            return "Traversal Type is invalid"

    def size_iterative(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.enqueue(self.root)
        size = 1
        while stack:
            node = stack.dequeue()
            if node.left:
                size += 1
                stack.enqueue(node.left)
            if node.right:
                size += 1
                stack.enqueue(node.right)
        return size

    def size_recursive(self,node):
        if self.node is None:
            return 0

        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.printTree("reverse_lvlordertraversal"))


