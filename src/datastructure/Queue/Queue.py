# List를 이용하여 Queue를 구현.

class Queue:
    
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        self.queue.append(data)
        return self.queue

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def display(self):
        print(self.queue)


if __name__ == "__main__":

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    queue.display()

    print(queue.dequeue())
    print(queue.dequeue())

    queue.display()