def factorial(n):
    n = int(n)  # mycalc.py에서 받아오는 n값이 처음에는 str이기 때문에 형변환
    fac = 1
    if n == 0: # 0! = 1 이므로 pass
        pass
    else:
        for i in range(1, n + 1): # for문을 이용하여 팩토리얼 구현
            fac = fac * i
    return fac # 구한 팩토리얼 값 return으로 반환

def decToBin(n):
    return bin(int(n)) # 내장함수 bin() 함수를 이용하여 10진수 -> 2진수 변환

def binToDec(n):
    return(int(n, 2)) # 2진수 -> 10진수 변환

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    if n>= 4000:
        return 'Error!'
    romans = [
(1000, 'M'), (900, 'CM'),
(500, 'D'), (400, 'CD'),
(100, 'C'), (90, 'XC'),
(50, 'L'), (40, 'XL'),
(10, 'X'), (9, 'IX'),
(5, 'V'), (4, 'IV'),
(1, 'I')
]
    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    return result

def  romanToDec(roman):
    rmnum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    now = roman[0]
    number = rmnum[now]
    for i in range(1, len(roman)):
        before = now
        now = roman[i]
        if (rmnum[before] >= rmnum[now]):
            number += rmnum[now]
        else:
            number += rmnum[now] - 2 * rmnum[before]
    return number