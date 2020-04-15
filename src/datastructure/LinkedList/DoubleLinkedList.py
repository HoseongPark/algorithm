"""
DoubleLinkedList
[method]
  - insert (삽입)
  - delete (삭제)
  - desc (노드 데이터 조회)
  - searchFromHead (노드 조회 [head 부터])
  - searchFromTail (노드 조회 [tail 부터])

  ======== Tail부터 검색후 Insert ========
  - insertBeforData (특정 Data 앞에 Node 생성)

  ======== Head부터 검색후 Insert ========
  - insertAfterData (특정 Data 뒤에 Node 생성)
"""

class Node:
  def __init__(self, data, prev=None, next=None):
    self.prev = prev
    self.data = data
    self.next = next


class DoubleLinkedList:
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head


  def insert(self, data):
    if self.head == "":
          print("해당 값이 없습니다.")

    else:
          node = self.head
          while node.next:
                node = node.next

          newNode = Node(data)
          node.next = newNode
          newNode.prev = node
          self.tail = newNode
          

  def delete(self, data):
    pass    


  def desc(self):
    node = self.head
    while node:
          print(node.data)
          node = node.next


  def searchFromHead(self, data):
      if self.head == None:
            return False

      node = self.head
      while node:
            if node.data == data:
                  return node
            else:
                  node = node.next

      return False


  def searchFromTail(self, data):
      if self.tail == None:
            return False

      node = self.tail
      while node:
            if node.data == data:
                  return node
            else:
                  node = node.prev

      return False

  
  def insertBeforData(self, data, beforData):
      node = self.tail

      while node.data != beforData:
            node = node.prev
            if node == None:
                  return False

      newNode = Node(data)
      beforNode = node.prev
      beforNode.next = newNode
      newNode.prev = beforNode
      newNode.next = node
      node.prev = newNode
      return True


  def insertAfterData(self, data, afterData):
        node = self.head

        while node.data != afterData:
              node = node.next
              if node == None:
                    return False

        newNode = Node(data)
        afterNode = node.next
        newNode.prev = node
        node.next = newNode
        newNode.next = afterNode
        afterNode.prev = newNode


if __name__ == "__main__":
  print("------ Main Method Execute [Double Linked List] ------")

  doubleLinkedList = DoubleLinkedList(0)
  for data in range(1,10):
        doubleLinkedList.insert(data)

  doubleLinkedList.desc()

  print("Node 4 Search From Head")
  node4 = doubleLinkedList.searchFromHead(4)
  print(node4.data)

  print("Node 3 Search From Tail")
  node3 = doubleLinkedList.searchFromTail(3)
  print(node3.data)

  print("Insert Befor Node Data")
  doubleLinkedList.insertBeforData(3.5,4)
  doubleLinkedList.desc()

  print("Insert After Node Data")
  doubleLinkedList.insertAfterData(5.5, 5)
  doubleLinkedList.desc()