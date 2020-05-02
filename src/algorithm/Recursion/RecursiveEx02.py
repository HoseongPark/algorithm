"""
회문(palindrome) 판별하기
"""

def palindrome(inputWord):
    if len(inputWord) <= 1:
        return True

    else:
        if inputWord[0] == inputWord[-1]:
            return palindrome(inputWord[1:-1])

        else:
            return False

if __name__ == "__main__":
    
    inputWord = "level"

    print(palindrome(inputWord))