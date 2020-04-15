"""
Heap 자료구조
 1: 자료구조 안에서 최소값 or 최대값을 찾기위해 사용 되는 자료구조이다.
 2: 완전 이진트리 형태를 가지고있다.
 3: 노드의 부모노드는 최대 값을 가지고있다. (Max Heap의 경우) [Min Heap 경우에는 반대.]

Node Index 표현식
 1. Current Index 기준으로 Parent Index는 (CurrentIndex // 2)
 2. Current Index 기준으로 Left Child Index는 (CurrentIndex * 2)
 3. Current Index 기준으로 Right Child Index는 ((CurrentIndex * 2) + 1)
"""

class Heap:    
    def __init__(self, data):
        self.heap = list()
        self.heap.append(None)
        self.heap.append(data)

    
    def _moving(self, currentIndex):
        parentIndex = currentIndex // 2

        if currentIndex <= 1: # Root Index
            return False

        if (self.heap[currentIndex] > self.heap[parentIndex]):
            return True

        else:
            return False


    def insert(self, data):
        if len(self.heap) == 0:
            self.heap.append(None)
            self.heap.append(data)

        self.heap.append(data)

        currentIndex = len(self.heap) - 1

        while self._moving(currentIndex):
            parentIndex = currentIndex // 2
            self.heap[currentIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[currentIndex]
            currentIndex = parentIndex

        return True


if __name__ == "__main__":

    heap = Heap(15)
    heap.insert(10)
    heap.insert(8)
    heap.insert(5)
    heap.insert(4)
    heap.insert(20)

    print(heap.heap)