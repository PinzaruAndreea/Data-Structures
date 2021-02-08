class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def insert (self, data):
        self.root = self.insertNode(data, self.root)
    def insertNode (self, data, node):

        if not node:
            return Node(data)
        if data< node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)
        node.height = max (self. calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        
        return self.settleViolation(data, node)
    
    def removeNode(self, data, node):

        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        
        else:

            if not node.leftChild and not node.rightChild:
                print ("Removing a leaf node...")
                del node
                return None
            
            if not node.leftChild:
                print ("Removing right Child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing left Child")
                tempNode = node.leftChild
                del node
                return tempNode
            print ("Removing node with two children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        
        if not node:
            return node #if the tree had just a single node
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        balance = self.calcBalance(node)

        #doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)

        #left right case
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        
        #right right case
        if balance < -1 and self.calcBalance(node.leftChild) <= 0:
            return self.rotateLeft(node)
        
        #right left case
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        
        return node 
    
    def getPredecessor(self, node):
        
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node  
    
    def settleViolation(self, data, node):

        balance = self.calcBalance(node)

        #case 1 -> left- left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print ("Left left heavy situation ")
            return self.rotateRight(node)
        
        #right right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print ("Right right heavy situation ")
            return self.rotateLeft(node)
        
        # left right heavy situation
        if balance > 1 and data > node.leftChild.data:
            print ("Left right heavy situation ")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        if balance < -1 and data < node.rightChild.data:
            print ("Right left heavy situation ")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node


    def calcHeight(self,node):

        if not node:
            return -1
        return node.height
    # if it returns value > 1 -> left heavy tree (solution:making a right rotation)
    # ................... < 1 -> right heavy tree (making a left rotation)

    def calcBalance(self,node):

        if not node:
            return 0
        return self.calcBalance(node.leftChild) - self.calcHeight(node.rightChild)
    
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder (self, node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        
        print ("%s" % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)


    def rotateRight (self, node):

        print ("Rotating to the right on node " , node.data)
        templeftChild = node.leftChild
        t = templeftChild.rightChild

        templeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        templeftChild.height = max(self.calcHeight(templeftChild.leftChild), self.calcHeight(templeftChild.rightChild)) + 1
        return templeftChild

    def rotateLeft (self, node):

        print ("Rotating to the left on node " , node.data)
        temprightChild = node.rightChild
        t = temprightChild.leftChild

        temprightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        temprightChild.height = max(self.calcHeight(temprightChild.leftChild), self.calcHeight(temprightChild.rightChild)) + 1
        return temprightChild    
    

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)
avl.remove(5)
avl.remove(4)

avl.traverse()