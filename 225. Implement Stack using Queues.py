class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, obj):
        self.arr.append(obj)

    def dequeue(self) -> int:
        return self.arr.pop(0)

    def length(self):
        return len(self.arr)


class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.active_queue = self.queue1

    def push(self, x: int) -> None:
        self.active_queue.enqueue(x)

    def pop(self) -> int:
        popped = -1
        while self.active_queue.length() > 0:
            if self.active_queue.length() > 1:
                if self.active_queue is self.queue1:
                    self.queue2.enqueue(self.active_queue.dequeue())
                else:
                    self.queue1.enqueue(self.active_queue.dequeue())
            else:
                popped = self.active_queue.dequeue()
                if self.active_queue is self.queue1:
                    self.active_queue = self.queue2
                else:
                    self.active_queue = self.queue1
                break
        return popped

    def top(self) -> int:
        last = -1
        for i in range(self.active_queue.length()):
            last = self.active_queue.dequeue()
            self.active_queue.enqueue(last)
        return last

    def empty(self) -> bool:
        return self.active_queue.length() == 0


stack = MyStack()
stack.queue1.arr = [1, 2, 3, 4, 5]
print(stack.pop())
print(stack.empty())
print(stack.pop())
print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.empty())