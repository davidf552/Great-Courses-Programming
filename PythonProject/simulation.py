#Set initial conditions
time = 0
balance = 1000

#Set lists to store data
timelist = [time]
balancelist = [balance]

while time < 10:
    #Increase balance and time
    balance += balance*0.03
    time += 1

    #Store time and balance in lists
    timelist.append(time)
    balancelist.append(balance)

#Output simulation results
for i in range(len(timelist)):
    print("Year:",timelist[i], " Balance:", balancelist[i])