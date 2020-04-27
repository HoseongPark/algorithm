def selectionSort(inputArray):
    
    for data in range(len(inputArray)):
        for index in range(data, len(inputArray) - 1):
            if inputArray[data] > inputArray[index + 1]:
                inputArray[data], inputArray[index + 1] = inputArray[index + 1], inputArray[data]

    return inputArray


if __name__ == "__main__":

    inputArray = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    result = selectionSort(inputArray)
    print(result)