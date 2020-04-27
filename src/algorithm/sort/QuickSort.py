def quickSort(inputArray, start, end):
    if (start >= end):
        return 

    pivotIdx = start
    maxIdx = start + 1
    minIdx = end

    while (maxIdx <= minIdx):
        while(maxIdx <= end and inputArray[maxIdx] <= inputArray[pivotIdx]):
            maxIdx += 1

        while(minIdx > start and inputArray[minIdx] >= inputArray[pivotIdx]):
            minIdx -= 1

        if (maxIdx > minIdx):
            inputArray[pivotIdx], inputArray[minIdx] = inputArray[minIdx], inputArray[pivotIdx]

        else:
            inputArray[maxIdx], inputArray[minIdx] = inputArray[minIdx], inputArray[maxIdx]

    quickSort(inputArray, start, minIdx - 1)
    quickSort(inputArray, minIdx + 1, end)

    return inputArray

        
if __name__ == "__main__":
    
    inputArray = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    number = len(inputArray)

    result = quickSort(inputArray, 0, number - 1)
    print(result)