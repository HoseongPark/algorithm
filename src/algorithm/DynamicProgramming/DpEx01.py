"""
동적 계획법을 활용하여 
피보나치 수열 문제 해결.
"""

def fibonacci(num):
    memories = [0 for i in range(num + 1)]
    memories[0] = 0
    memories[1] = 1

    for idx in range(2, num + 1):
        memories[idx] = memories[idx - 1] + memories[idx - 2]

    return memories[num]


if __name__ == "__main__":
    
    print(fibonacci(10))