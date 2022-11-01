class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data, curr_node.left)

        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node.right)

        else:
            return 'Value already exists in the tree'

    def search(self,data):
        if self.root:
            is_found = self._search(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _search(self,data,curr_node):
        if data > curr_node.data and curr_node.right:
            return self._search(data,curr_node.right)
        elif data < curr_node.data and curr_node.left:
            return self._search(data,curr_node.left)
        elif data == curr_node.data:
            return True


bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(3)

print(bst.search(4))
