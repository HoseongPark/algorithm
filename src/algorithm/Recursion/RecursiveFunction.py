"""
N! 함수를 구현해라.

4! = 4 * 3 * 2 * 1
3! = 3 * 2 * 1
2! = 2 * 1
N! = N * (N-1)!
"""

def factorial(num):
    if num > 1:
        return num * factorial(num -1)

    else:
        return num

if __name__ == "__main__":

    for i in range(10):
        print(factorial(i))