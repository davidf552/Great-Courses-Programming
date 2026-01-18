from random import randint

goal = randint(1,100)
counter = 0

while True:
    entry = int(input("Pick a number between 1 and 100: "))
    counter += 1
    if entry == goal:
        clear = 1
        break
    elif entry < goal:
        print("Number is higher")
    elif entry > goal:
        print("Number is lower")


print("It took " ,counter, " tries")