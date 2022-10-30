class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            currNode = self.head
            while True:
                if currNode is None:
                    break
                print(currNode.data)
                currNode = currNode.next

    def length(self):
        currNode = self.head
        length = 0
        while currNode is not None:
            length += 1
            currNode = currNode.next
        return length

    def insertAt(self,newNode,position):
        if position < 0 or position > self.length():
            print("invalid position")
        if position == 0:
            self.insertHead(newNode)
        currNode = self.head
        currPos = 0
        while True:
            if currPos == position:
                prevNode.next = newNode
                newNode.next = currNode
                break
            prevNode = currNode
            currNode = currNode.next
            currPos += 1

    def insertHead(self,newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def deleteEnd(self):
        lastNode = self.head
        while lastNode is not None:
            prevNode = lastNode
            lastNode = lastNode.next
        prevNode.next = None

    def deleteBetween(self,position):
        currNode = self.head
        currPos = 0
        while True:
            if currPos == position:
                prevNode.next = currNode.next
                currNode.next = None
                break
            prevNode = currNode
            currNode = currNode.next
            currPos += 1








