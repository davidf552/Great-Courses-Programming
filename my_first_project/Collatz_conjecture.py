final = int(input("Enter the final number:"))
i = 0
while final != 1:
    i = i + 1
    if final % 2 == 0:
        final = final/2
    else:
        final = (3*final)+1

    print(int(final))

print("The number of iterations was:",i)