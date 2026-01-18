print("Hello! This program will help you with a payment plan!")
name = input("Please enter your name:")
item = input("Enter the item you want:")

print("Ok ",name,"your item ",item)
balance = float(input("Enter the amount you want to save:"))

if balance == 0:
    print("You already have enough!")
    payment = 1
elif balance < 0:
    print("Enter a positive value")
    balance = float(input("Enter the amount you want to save:"))
    if balance < 0:
        print("You were warned about negative values. I will assume the balance is 0")
        balance = 0
        payment = 1
    else:
        payment = float(input("Enter how much you want to save each period:"))
else:
    payment = float(input("Enter how much you want to save each period:"))

if payment == 0:
    payment = float(input("You cant get something for nothing!:"))
num_remaining_payments = balance/payment

print("You must make",num_remaining_payments, "more payments")