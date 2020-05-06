ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

arrays = list(map(int, input().split(' ')))
print(arrays)

if (arrays == ascending):
    print("ascending")

elif (arrays == descending):
    print("descending")

else:
    print("mixed")