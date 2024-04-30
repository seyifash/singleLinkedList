class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        currentNode = self.head
        if currentNode is None:
            print("Empty list")
            
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next 
            
    def listLength(self):
        count = 0
        current = self.head
        
        if self.head is None:
            print("Nothing to count")
            return
        else:
            while current:
                count += 1
                current = current.next
                
        return count
    
    def insertAtBeg(self, data):
        current = self.head
        if current is None:
            newNode = Node(data)
            self.head = newNode
            
        else:
            newNode = Node(data)
            newNode.next = current
            self.head = newNode
            
    def insertAtEnd(self, data):
        current = self.head
        if self.head is None:
            newNode = Node(data)
            current = newNode
            
        else:
            while current.next is not None:
                current = current.next
            newNode = Node(data)
            current.next = newNode
            
    def insertAtPos(self, data, pos):
        current = self.head
        count = 0
        prev = None
        
        if pos < 0 or pos > self.listLength():
            print("Position out of range")
        elif pos == 0:
            self.insertAtBeg(data)
        else:
            newNode = Node(data)    
            while current.next is not None:
                if count == pos:
                    break
                prev = current
                current = current.next
                count += 1
                
            newNode.next = prev.next
            prev.next = newNode

    def insertBet(self, previousNode, data):
        current = self.head
        
        if self.head is None:
            print("Empty list")
        
        if current.next is None:
            print("List contains only one node, it can be inserted between anything")    
        
        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode
        
    def deleteAtBeg(self):
        if self.head is None:
            print("list is empty")
        self.head = self.head.next
        
    def deleteAtEnd(self):
        current = self.head
        
        if self.head is None:
            print("list is empty")
        while current.next is not None:
            prev = current
            current = current.next
            
        current = prev
        prev.next = None    
    def deleteAtPos(self, pos):
        current = self.head
        count = 0
        prev = None
        
        if pos < 0 or pos > self.listLength():
            print("Position out of range")
        elif pos == 0:
            self.deleteAtBeg()
        else:
            while current is not None:
                if pos == count:
                    break
                prev = current
                current = current.next
                count += 1
            prev.next = current.next
            del current.data
            
    def searchList(self, data):
        current = self.head
        
        if self.head is None:
            print("Empty list")
            
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def recurSearch(self, nodeHead, data):
        if nodeHead is None:
            return False
        if nodeHead.data == data:
            return True
        return self.recurSearch(nodeHead.next, data)
    
    def sortList(self, nodeHead):
        temp = nodeHead
        if temp is None:
            print("Empty list")
            return 
        while temp.next is not None:
            min = temp
            ptr = temp.next
            while ptr is not None:
                if ptr.data < min.data:
                    min = ptr
                ptr = ptr.next 
            if temp != min:
                item = temp.data
                temp.data = min.data
                min.data = item
            temp = temp.next    
                
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        
        if self.rear is None:
            self.rear, self.front = Node(data) 
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
            
    def deque(self):
        if self.front is None:
            return "List empty"
        val = self.front.data
        self.front = self.front.next
        return val
    
    def isEmpty(self):
        return self.front is None
new = LinkedList()
new.insertAtBeg(5)
new.insertAtBeg(10)
new.insertAtBeg(15)
new.insertAtEnd(2)
new.insertAtEnd(3)
new.insertAtEnd(6)
new.printList()
print("list after insertion a position")
new.insertAtPos(17, 2)
new.printList()
new.insertBet(new.head, 25)
print("Inserted between")
new.printList()
new.deleteAtBeg()
print("Deleting the first node")
new.printList()
new.deleteAtEnd()
print("Deleting the last node")
new.printList()
new.deleteAtPos(3)
print("Deleting at given position")
new.printList()
search = new.searchList(25)
print(search)
search2 = new.recurSearch(new.head, 30)
print(search2)
new.sortList(new.head)
new.printList()



