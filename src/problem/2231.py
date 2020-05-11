num = int(input())
inputNum = num
s = 0
x = 0
result = []

while (inputNum != 0):
    inputNum = inputNum // 10
    s += 1

for i in range(s):
    x += 9

y = num-x

while(y != num):
    temp = 0
    for i in range(1, s):
        if (i == 1):
            temp += ((y // 1) % 10) 
        temp += ((y //10 ** i) % 10)

    if (num == (y + temp)):
        break

    y += 1

print(y)