n, m = list(map(int, input().split(" ")))
data = list(map(int, input().split(" ")))

result = 0
dataSize = len(data)

for i in range(dataSize):
    for j in range(i+1, dataSize):
        for k in range(j+1, dataSize):
            sumValue = data[i] + data[j] + data[k]
            if sumValue <= m:
                result = max(result, sumValue)

print(result)