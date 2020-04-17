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

    
    # Current Index Value 와 Parent Index Value 의 값을 비교해서 바꿔야하는지 확인하는 Method
    def _movingiUp(self, currentIndex): 
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

        while self._movingiUp(currentIndex):
            parentIndex = currentIndex // 2
            self.heap[currentIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[currentIndex]
            currentIndex = parentIndex

        return True

    
    def _movingDown(self, currentIndex):
        leftChildIndex = currentIndex * 2
        rightChildIndex = currentIndex * 2 + 1

        if leftChildIndex >= len(self.heap): # Left Child Data가 없을때.
            return False

        elif rightChildIndex >= len(self.heap): # Right Child Data가 없을때 (Left Child Data 만 있을때.)
            if self.heap[leftChildIndex] > self.heap[currentIndex]:
                return True
            else:
                return False

        else: # Left Child Data 와 Right Child Data 둘다 있을때.
            if self.heap[leftChildIndex] > self.heap[rightChildIndex]: # Left Child Data > Right Child Data
                if self.heap[leftChildIndex] > self.heap[currentIndex]:
                    return True
                else:
                    return False

            else: # Right Child Data > Left Child Data
                if self.heap[rightChildIndex] > self.heap[currentIndex]:
                    return True
                else:
                    return False


    def pop(self):
        if len(self.heap) <= 1:
            return None

        popData = self.heap[1]
        self.heap[1] = self.heap[-1] # 마지막 Data를 Root Data로 바꿈.
        del self.heap[-1] # 마지막 Data 삭제.
        
        currentIndex = 1
        while self._movingDown(currentIndex):
            leftChildIndex = currentIndex * 2
            rightChildIndex = currentIndex * 2 + 1

            if rightChildIndex >= len(self.heap):
                if self.heap[leftChildIndex] > self.heap[currentIndex]:
                    self.heap[leftChildIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[leftChildIndex]
                    currentIndex = leftChildIndex
                    
            else:
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex] > self.heap[currentIndex]:
                        self.heap[leftChildIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[leftChildIndex]
                        currentIndex = leftChildIndex
                else:
                    if self.heap[rightChildIndex] > self.heap[currentIndex]:
                        self.heap[rightChildIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[rightChildIndex]
                        currentIndex = rightChildIndex

        return popData


if __name__ == "__main__":

    heap = Heap(15)
    heap.insert(10)
    heap.insert(8)
    heap.insert(5)
    heap.insert(4)
    heap.insert(20)
    heap.insert(30)

    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())

    print(heap.heap)