"""
Random 으로 생성한 List의 수를 합하는 프로그램을 작성하시오.
재쉬함수를 활용하여 작성하시오.
"""

import random

def recursiveSumList(inputData):
    if len(inputData) == 1:
        return inputData[0]

    else:
        return inputData[0] + recursiveSumList(inputData[1:])


if __name__ == "__main__":

    data = random.sample(range(100), 10)
    print(data)

    print(recursiveSumList(data))