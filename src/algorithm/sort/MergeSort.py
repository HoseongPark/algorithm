def mergeSorted(inputArrays):
    if len(inputArrays) > 1:
        middle = len(inputArrays) // 2
        left = inputArrays[:middle]
        right = inputArrays[middle:]

        l = mergeSorted(left)
        r = mergeSorted(right)
        return merge(l, r)

    else:
        return inputArrays

def merge(left, right):
    i = 0
    j = 0
    arrays = []

    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            arrays.append(left[i])
            i += 1

        else:
            arrays.append(right[j])
            j += 1

    while (i < len(left)):
        arrays.append(left[i])
        i += 1

    while (j < len(right)):
        arrays.append(right[j])
        j += 1

    return arrays

if __name__ == "__main__":
    
    inputArrays = [7, 6, 5, 8, 3, 5, 9, 1]
    print(mergeSorted(inputArrays))