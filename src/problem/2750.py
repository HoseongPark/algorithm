numCount = int(input())
number = []

for i in range(numCount):
    x = int(input())
    number.append(x)

for idx in range(len(number)):
    for idx2 in range(len(number)):
        if number[idx] < number[idx2]:
            number[idx], number[idx2] = number[idx2], number[idx]

for result in number:
    print(result)