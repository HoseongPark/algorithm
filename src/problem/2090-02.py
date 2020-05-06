arrays = list(map(int, input().split(' ')))

ascending = True
descending = True

for idx in range(7):
    if arrays[idx] > arrays[idx + 1]:
        ascending = False

    elif arrays[idx] < arrays[idx + 1]:
        descending = False

if ascending == True:
    print("ascending")

elif descending == True:
    print("descending")

else:
    print("mixed")