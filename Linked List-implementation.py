class Node(object):

    def __init__ (self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
    #O(1)
    def insertStart(self,data):
        self.size = self.size +1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    

    def remove(self,data):
        if self.head is None:
            return
        
        self.size = self.size - 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode =currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
    def size1(self):
        return self.size
    
   #O(N)
    def insertEnd(self, data):
        self.size = self.size +1
        newNode = Node(data)
        actualNode = self.head

        #cimport pdb;pdb.set_trace()

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode
    def traverseList(self):
        

        actualNode = self.head

        while actualNode is not None:
            print( "%d" % actualNode.data)
            actualNode = actualNode.nextNode

linkedList = LinkedList()

linkedList.insertStart(5)
linkedList.insertStart(122)
linkedList.insertStart(46)
linkedList.insertStart(166)
linkedList.insertStart(78)
linkedList.remove(5)
linkedList.insertEnd(40)
linkedList.traverseList()

print(linkedList.size1())