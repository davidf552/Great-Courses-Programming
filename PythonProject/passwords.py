passwords = {"John":"123456","Sue":"PaSsWoRd","Bill":"G9.Kf-21.-fe8ilfb"}

failed_attempts = 0
verified = False

while not verified:
    username = input("What is your username? ")
    password = input("What is your password? ")

    if (username in passwords) and (passwords[username] == password):
        print("Welcome!")
        verified = True
    else:
        print("Invalid username/password combination")
        failed_attempts += 1
        if failed_attempts > 2:
            print("Too many incorrect attempts. Goodbye")
            exit()