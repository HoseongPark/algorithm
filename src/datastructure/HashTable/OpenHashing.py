"""
HashTable 에서 충돌(Collision) 발생시 해결법
충돌 발생시 링크드 리스트 자료구조를 활용하여 데이터를 추가로 연결시켜 저장하는 방법
링크드리스트에 저장시 어떤 Key에대한 Value인지 알기위해 해쉬값(Hash Value)와 데이터(Data)를 동시에 저장한다.
"""

"""
Hash Table 구현
1. 해쉬함수: key % 8
2. 해쉬 키 생성 : hash(data)
"""

class hashTable:

    def __init__(self, count):
        self.hashTable = self._createTable(count)


    # HashTable 기본 생성
    def _createTable(self, count):
        table = [0 for i in range(count)]
        return table

    # Data에 대한 Hash값 생성
    def _getHash(self, data):
        return hash(data)

    
    # HashData 에대한 Key값 생성
    def _getKey(self, hashData):
        key = hashData % 8
        return key


    # Key, Value로 데이터 저장
    # Key 충돌시 Open Chaining 방법으로 해결
    def saveData(self, keyData, data):
        hashData = self._getHash(keyData)
        key = self._getKey(hashData)

        if (self.hashTable[key] != 0):
            for idx in range(len(self.hashTable[key])):
                if (self.hashTable[key][idx][0] == hashData):
                    self.hashTable[key][idx][1] = data
                    return
            
            self.hashTable[key].append([hashData, data])

        else:
            self.hashTable[key] = [[hashData, data]]


    # Key 값으로 Data 추출
    # Key 충돌시 Open Chaining 방법으로 해결
    def readData(self, keyData):
        hashData = self._getHash(keyData)
        key = self._getKey(hashData)

        if (self.hashTable[key] != 0):
            for idx in range(len(self.hashTable[key])):
                if (self.hashTable[key][idx][0] == hashData) :
                    return self.hashTable[key][idx][1]

                else:
                    return None
        return None


    # HashTable 출력
    def descTable(self):
        print("---------- Start Print HashTable ----------")
        for idx in self.hashTable:
            print(idx)
        print("---------- End Print HashTable   ----------")


if __name__ == "__main__":

    table = hashTable(10)

    table.saveData("ho", "01024567894")
    table.saveData("ha", "01078965418")
    table.descTable()

    print(table.readData("haha"))