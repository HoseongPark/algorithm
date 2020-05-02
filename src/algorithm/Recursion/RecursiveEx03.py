"""
1. 정수 N에 대해서
2. N이 홀수이면 3 * N + 1 을하고,
3. N이 짝수이면 N / 2를 한다.
4. 이렇게 진행을해서 N이 1이될때까지 반복하며
5. 모든 과정을 출력한다.
"""

def recursiveFunc(num):
    if num <= 1:
        print(int(num))
        return num

    else:
        # 홀수이면
        if (num % 2) == 1:
            print(int(num))
            return recursiveFunc(3 * num + 1)
        
        # 짝수이면
        elif (num % 2) == 0:
            print(int(num))
            return recursiveFunc(num / 2)


if __name__ == "__main__":
    
    recursiveFunc(3)