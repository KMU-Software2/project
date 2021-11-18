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
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        r = 'Error!'

    romans = [
        (1000, 'M'),
        (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    r = ''
    for value, letters in romans:
        while n >= value:
            r += letters
            n -= value
    return r

def romanToDec(numStr):
    r = 0

    decCollection = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    for i in range(len(numStr)):
        dec = numStr[i]
        if dec not in decCollection:
            return 'Error!'

    decs = {
        'M': 1000,
        'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
        'XC': 90, 'L': 50, 'XL': 400, 'X': 10,
        'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    if len(numStr) == 0:
        print(r)

    while len(numStr) > 0:
        if len(numStr) > 2:
            if numStr[0] + numStr[1] in decs.keys():
                r += decs[numStr[0] + numStr[1]]
                numStr = numStr[2:]
            elif numStr[0] in decs.keys():
                r += decs[numStr[0]]
                numStr = numStr[1:]
        elif len(numStr) == 2:
            if numStr in decs.keys():
                r += decs[numStr[0] + numStr[1]]
                numStr = ''
            elif numStr[0] in decs.keys():
                r += decs[numStr[0]]
                numStr = numStr[1:]
        else:
            if numStr in decs.keys():
                r += decs[numStr[0]]
                numStr = ''
    return str(r)