"""
재귀용법을 활용하여 피보나치 수열 해결.
"""

def fibonacci(num):
    if num <= 1:
        return num

    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == "__main__":

    print(fibonacci(10))
