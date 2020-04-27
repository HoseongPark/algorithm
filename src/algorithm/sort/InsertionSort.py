def insertionSort(inputArray):
    
    size = len(inputArray)
    for idx in range(size):
        idx2 = idx
        while(idx2 >= 0 and (inputArray[idx2] > inputArray[idx2 + 1])):
            inputArray[idx2],inputArray[idx2 + 1] = inputArray[idx2 + 1], inputArray[idx2]
            idx2 = idx2 - 1

    return inputArray


if __name__ == "__main__":

    inputArray = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    result = insertionSort(inputArray)

    print(result)