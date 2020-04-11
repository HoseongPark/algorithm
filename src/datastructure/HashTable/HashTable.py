"""
Hash Table 구현
1. 해쉬 키 생성 : key % count
2. 해쉬 값 생성 : hash(data)
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
    def saveData(self, keyData, data):
        hashData = self._getHash(keyData)
        key = self._getKey(hashData)
        self.hashTable[key] = data

        return True

    # Key 값으로 Data 추출
    def readData(self, keyData):
        hashData = self._getHash(keyData)
        key = self._getKey(hashData)

        return self.hashTable[key]


    # HashTable 출력
    def descTable(self):
        print("---------- Start Print HashTable ----------")
        for idx in self.hashTable:
            print(idx)
        print("---------- End Print HashTable   ----------")


if __name__ == "__main__":

    table = hashTable(10)
    table.saveData("hoseong", '01023456784')
    table.saveData("hohoho", "01055558884")


    print(table.readData("hoseong"))
    print(table.readData("hohoho"))