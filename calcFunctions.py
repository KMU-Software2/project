from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

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

def romanToDec(numStr):
    romans = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    result = 0
    if (str(type(numStr)) != "<class 'str'>"):
        return "Error!"

    for i in range(len(numStr)):
        try:
            if int(numStr[i]):
                return "Error!"
        except:
            return "Error!"

    while numStr != "":
        for value, letters in romans:
            try:
                if numStr[0:len(letters)] == letters:
                    result += value
                    numStr = numStr[len(letters):]
            except:
                return "Error!"
    return result

if __name__ == '__main__':

    num = input("Enter: ")
    print(romanToDec(num))