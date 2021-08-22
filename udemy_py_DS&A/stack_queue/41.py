# FIFO First item we insert is the first one we take out

class Queue:
    def __init__(self) -> None:
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    # O(1)
    def size_queue(self):
        return len(self.queue)
    
    # Add data to end of queue. O(1)
    def enqueue(self, data):
        self.queue.append(data)
    
    # Get the first in queue, then remove it, O(n)
    def dequeue(self):
        if self.is_empty():
            return
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        if self.is_empty():
            return
        return self.queue[0]
    

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(f"dequeue: {queue.dequeue()}")
print(f"size: {queue.size_queue()}")
print(f"dequeue: {queue.dequeue()}")
print(f"size: {queue.size_queue()}")
print(f"dequeue: {queue.dequeue()}")
print(f"size: {queue.size_queue()}")
print(f"dequeue: {queue.dequeue()}")
print(f"size: {queue.size_queue()}")
print(f"peek: {queue.peek()}")
