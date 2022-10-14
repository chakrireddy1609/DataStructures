class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,prev_node,data):

        if not prev_node:
            print("there is no prev node")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node is None
            return

        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node is None


lllist = LinkedList()
lllist.append("A")
lllist.append("B")
lllist.prepend("10")
lllist.insert_after_node(lllist.head.next,"Chakri")
print(lllist.head.data)
lllist.print()
lllist.delete_node("10")
lllist.print()

