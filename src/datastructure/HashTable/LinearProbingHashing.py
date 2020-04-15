"""
HashTable 에서 충돌(Collision) 발생시 해결법 2
충돌 발생시 HashTable을 순차적으로 순회하여 빈공간의 Slot을 확인후 저장한다
내부 자료구조를 이용하여 처리.
Data를 저장할시 [hashData, Data] 로 저장하여야 한다.
 -> 충돌시 같은 값인지 아닌지 확인하기 위해서.
"""

"""
Hash Table 구현
1. 해쉬함수: key % 10
2. 해쉬 키 생성 : hash(data)

"""
import hashlib

class hashTable:

    def __init__(self, count):
        self.count = count
        self.hashTable = self._createTable(count)


    # HashTable 기본 생성
    def _createTable(self, count):
        table = [0 for i in range(count)]
        return table

    # Data에 대한 Hash값 생성 (SHA-256 사용)
    def _getHash(self, data):
        encodeData = data.encode()
        hashFunction = hashlib.sha256()
        hashFunction.update(encodeData)
        hexHash = hashFunction.hexdigest()

        return int(hexHash, 16)

    
    # HashData 에대한 Key값 생성
    def _getKey(self, hashData):
        key = hashData % self.count
        return key


    # Key, Value로 데이터 저장
    # Key 충돌시 Linear Probing Hashing 방법으로 해결
    def saveData(self, keyData, data):
        hashData = self._getHash(keyData)
        key = self._getKey(hashData)

        if self.hashTable[key] != 0:
            for index in range(key, len(self.hashTable)):
                if self.hashTable[index] == 0:
                    self.hashTable = [hashData, data]
                    return

                elif self.hashTable[index][0] == hashData:
                    self.hashTable[index][1] = data
                    return

        else:
            self.hashTable[key] = [hashData, data]


    # Key 값으로 Data 추출
    # Key 충돌시 Linear Probing Hashing 방법으로 해결
    def readData(self, keyData):
        hashData = self._getHash(keyData)
        key = self._getKey(hashData)

        if self.hashTable[key] != 0:
            for index in range(key, len(self.hashTable)):
                if self.hashTable[index][0] == hashData:
                    return self.hashTable[index][1]

                else:
                    return None

        else:
            return None


    # HashTable 출력
    def descTable(self):
        print("---------- Start Print HashTable ----------")
        for idx in self.hashTable:
            print(idx)
        print("---------- End Print HashTable   ----------")


if __name__ == "__main__":

    table = hashTable(50)

    table.saveData("ho", "11111111")
    table.saveData("ha", "22222222")
    table.descTable()

    print(table.readData("ha"))