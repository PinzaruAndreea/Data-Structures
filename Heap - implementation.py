#the maximum number of items that can be stored in the heap
CAPACITY = 10

class Heap(object):
    def __init__(self):
        #create an array with as many slot as the CAPACITY
        self.heap = [0] * CAPACITY
        #we want to track the size(the number of items in the heap)
        self.heap_size = 0

    #insertion takes O(1) running time BUT we have to make sure that the heap
    #properties are not violated (O(log(N) because of the fixUp())
    def insert(self, item):
        #we are not able to insert more items than the value of the capacity
        if CAPACITY == self.heap_size:
            return
        
        #insert the item +increment the counter
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        #we insert the item in the last position of the array(heap)
        #properties may be violated so we have to fix it, if necessary
        
        self.fix_up(self.heap_size - 1)
    
    #we consider the last item and check wether swaps are needed
    # O(logN)
    def fix_up(self, index):

        #the parent index of the given node in the heap (it is stored like an array)
        parent_index = (index - 1) //2

        #while the index > 0 means until we consider all the items "above" the node we inserted
        #we have to swap the node with the parent if there are violations
        #it is a max heap: largest items at the top
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)
        
    #we return the root node
    # O(1)
    #this is the peek()
    def get_max(self):
        return self.heap[0]
    
    #it returns the max item + remove it from the heap
    #O(log(N))
    def poll(self):
        max = self.get_max()

        self.swap(0, self.heap_size - 1)
        self.heap_size = self.heap_size - 1
        
        self.fix_down(0)

        return max
    
    #we have a given item in the heap and we consider all the items below for violations
    def fix_down(self, index):

        #every node has 2 children
        #in the array, the node i has left child with index 2i+1 and right child with index 2i+2
        index_left = 2*index +1
        index_right = 2*index +2
        #max heap so the parent node is always greater than the children
        index_largest = index

        #if the left child > parent: left child = largest
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left
        
        #if the right child > parent: right child = largest
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index]:
            index_largest = index_right
        
        #we dont want to swap items with themselves
        if index != index_largest:
            self.swap(index, index_largest)
            self.fix_down(index_largest)

    #we have N items and we want to sort them in a heap
    #poll takes O(NlogN) because of the fix_down method = heap_sort = O(NlogN)
    def heap_sort(self):
        #we decrease the size in the poll() so we have to store it
        size = self.heap_size

        for i in range(0,size):
            max = self.poll()
            print(max)

        #swap two items with (index1, index2)
    
    def swap(self, index1, index2):
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]

heap = Heap()

heap.insert(10)
heap.insert(8)
heap.insert(12)
heap.insert(20)
heap.insert(-2)
heap.insert(0)
heap.insert(1)
heap.insert(321)

heap.heap_sort()

