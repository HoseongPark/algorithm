def countingSort(inputArrays, countNumber):
    number = {}
    result = []
    for idx in range(1, countNumber+1):
        number[idx] = 0

    for idx2 in inputArrays:
       number[idx2] += 1

    for j in number:
        for m in range(number[j]):
            result.append(j)

    return result


if __name__ == "__main__":
    
    countNumber = 5
    inputArrays = [1, 3, 2, 4, 5, 3, 2, 5, 1, 4]
    sortResult = countingSort(inputArrays, countNumber)

    print(sortResult)