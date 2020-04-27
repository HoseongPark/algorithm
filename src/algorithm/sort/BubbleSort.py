def bubbleSort(inputArray):

    size = len(inputArray)

    for data in range(size):
        for index in range((size - data) - 1):
            if inputArray[index] > inputArray[index + 1]:
                inputArray[index], inputArray[index + 1] = inputArray[index + 1], inputArray[index]

    return inputArray


if __name__ == "__main__":

    inputArray = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    result = bubbleSort(inputArray)

    print(result)
