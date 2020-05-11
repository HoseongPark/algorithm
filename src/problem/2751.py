def quickSort(numArrays):
    numSize = len(numArrays)
    fivotIdx = 0
    bigIdx = 0
    smallIdx = 0

    while numArrays[smallIdx] < numArrays[bigIdx]:
        for idx in range(numSize):
            if numArrays[fivotIdx] < numArrays[idx]:
                bigIdx = idx
                break

        for idx2 in reversed(range(numSize)):
            if numArrays[fivotIdx] > numArrays[idx2]:
                smallIdx = idx2
                break
        
        numArrays[idx], numArrays[idx2] = numArrays[idx2], numArrays[idx]
    
    numArrays[fivotIdx], numArrays[smallIdx] = numArrays[smallIdx], numArrays[fivotIdx]

    left = quickSort()
    


numCount = int(input())
num = []

for i in range(numCount):
    x = int(input())
    num.append(x)

result = quickSort(num)
for a in result:
    print(a)