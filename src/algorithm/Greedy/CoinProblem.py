def greedyCoin(inputValue, coinList):

    coin = {}

    # 가치가 큰 동전순으로 정렬.
    coinList.sort(reverse = True)

    for idx in coinList:
        value = inputValue // idx
        inputValue -= value * idx
        coin[idx] = value

    return coin


if __name__ == "__main__":
    
    inputValue = 4520
    coinList = [1, 10, 100, 200, 500]

    result = greedyCoin(inputValue, coinList)
    print(result)