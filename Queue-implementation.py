#FIFO

class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.size_queue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print(queue.size_queue())