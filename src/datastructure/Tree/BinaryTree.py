"""
BinaryTree(이진 트리): Node 에 Branch 가 2개인 자료구조
Binary Search Tree(이진 탐색 트리) : Node에 Branch가 2개이면서 왼쪽은 현재보다 작은값, 오른쪽은 현재보다 큰값으로 정렬되어있는 자료구조.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, head):
        self.head = head
        

    def insert(self, data):
        currentNode = self.head
        
        while True:
            if (data < currentNode.data):
                if currentNode.left != None:
                    currentNode = currentNode.left
                
                else:
                    currentNode.left = Node(data)
                    break

            else:
                if currentNode.right != None:
                    currentNode = currentNode.right

                else:
                    currentNode.right = Node(data)
                    break


    def search(self, data):
        currentNode = self.head

        while currentNode:
            if data == currentNode.data:
                return True

            elif data < currentNode.data:
                currentNode = currentNode.left

            else:
                currentNode = currentNode.right

        return False


    def delete(self, data):
        currentNode = self.head
        parentNode = self.head
        searchNode = False

        while currentNode:
            if data == currentNode.data:
                searchNode = True
                break

            elif data < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left

            else:
                parentNode = currentNode
                currentNode = currentNode.right

        if searchNode == False:
            return False


        ### Delete Case ###
        # 1. 삭제할 Node에 Child Node가 없을때 (Leaf Node[Terminal Node])
        if (currentNode.left == None and currentNode.right == None):
            if data < parentNode.data:
                parentNode.left = None

            else:
                parentNode.right = None

            del currentNode

        # 2. 삭제할 Node에 Child Node가 1개 일때.
        elif (currentNode.left != None and currentNode.right == None):
            if data < parentNode.data:
                parentNode.left = currentNode.left

            else:
                parentNode.right = currentNode.left

        elif (currentNode.left == None and currentNode.right != None):
            if data < parentNode.data:
                parentNode.left = currentNode.right

            else:
                parentNode.right = currentNode.right

        # 3. 삭제할 Node에 Child Node가 2개 일때.
        elif (currentNode.left != None and currentNode.right != None):
            if data < parentNode.data: # 삭제할 Node가 부모의 왼쪽에 있을때.
                changeNode = currentNode.right
                changeNodeParent = currentNode.right
                while changeNode.left != None:
                    changeNodeParent = changeNode
                    changeNode = changeNode.left

                if changeNode.right != None:
                    changeNodeParent.left = changeNode.right

                else:
                    changeNodeParent.left = None

                parentNode.left = changeNode
                changeNode.left = currentNode.left
                changeNode.right = currentNode.right

            else: # 삭제할 Node가 부모의 오른쪽에 있을때.
                changeNode = currentNode.right
                changeNodeParent = currentNode.right
                while changeNode.left != None:
                    changeNodeParent = changeNode
                    changeNode = changeNode.left

                if changeNode.right != None:
                    changeNodeParent.left = changeNode.right

                else:
                    changeNodeParent.left = None

                parentNode.right = changeNode
                changeNode.left = currentNode.left
                changeNode.right = currentNode.right

        return True


if __name__ == "__main__":

    # 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
    import random

    # 0 ~ 999 중, 100 개의 숫자 랜덤 선택
    bst_nums = set()
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))
    # print (bst_nums)

    # 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
    head = Node(500)
    binary_tree = BinaryTree(head)
    for num in bst_nums:
        binary_tree.insert(num)
        
    # 입력한 100개의 숫자 검색 (검색 기능 확인)
    for num in bst_nums:
        if binary_tree.search(num) == False:
            print ('search failed', num)


    # 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])


    # 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
    for del_num in delete_nums:
        if binary_tree.delete(del_num) == False:
            print('delete failed', del_num)