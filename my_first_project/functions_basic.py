def getGuess ():
    num = input("Pick a number: ")
    return num


def getBirthday ():
    month = input("Enter the month you were born: ")
    day = input("Enter the day you were born: ")
    year = input("Enter the year you were born: ")
    return month,day,year

def factorial(n):
    acc = 1
    while(n>1):
        acc *= n
        n -=1
    return acc

def factorial_2(n):
    acc = 1
    for i in range(1,n+1):
        acc *= i
    return acc

print(factorial_2(20))
