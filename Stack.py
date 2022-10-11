class Stack:

    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)

    def remove(self):
        if not self.len():
            return self.items.pop()

    def len(self):
        return len(self.items)==0

    def peek(self):
        if not self.len():
            return self.items[-1]

    def getItems(self):
        return self.items


s1 = Stack()
s1.add(10)
s1.add(32)
print(s1.getItems())
print(s1.peek())
print(s1.remove())
print(s1.peek())
print(s1.remove())
print(s1.peek())
print(s1.remove())




