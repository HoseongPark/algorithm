class Node:
    """
    Node 구성
        data : 데이터
        next : 다음 노드의 주소공간

        return Node
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    LinkedList 구조
    """
    def __init__(self, data):
        self.head = Node(data)
        

    # Node Insert
    def add(self, data):
        if self.head == '':
            self.head = Node(data)

        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(data)

    # Node Delete
    def delete(self, data):
        if self.head == '':
            print("해당 값이 없습니다.")

        else:
            if self.head.data == data:
                temp = self.head
                self.head = self.head.next
                del temp

            else:
                node = self.head
                while node.next:
                    if node.next.data == data:
                        temp = node.next
                        node.next = node.next.next
                        del temp

                    else:
                        node = node.next

    # Node들의 값 출력
    def decs(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


    # Node 검색
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            
            else:
                node = node.next


if __name__ == "__main__":

    print("------ Main Method Execute [LinkedList] ------")

    linkedList = LinkedList(0)
    for data in range(1,10):
        linkedList.add(data)

    linkedList.decs()

    print("LinkedList Delete Start")
    linkedList.delete(9)
    linkedList.decs()

    print("Linked List Search_Node")
    result = linkedList.search_node(4)
    print(result.data)

