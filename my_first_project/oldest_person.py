names=[]
ages=[]

name_entry = input("Please enter a name: PRESS stop TO FINISH ")

while name_entry!= "stop":
    names.append(name_entry)
    age_entry = int(input("Please enter the age: "))
    ages.append(age_entry)
    name_entry= input("Please enter a name: PRESS stop TO FINISH ")

#Assuming the first entry is the oldest person
accu = ages[0]
winner = names[0]

for i in range(len(ages)):
    if accu < ages[i]:
        accu = ages[i]
        winner = names[i]

print("The oldest person has",accu,"years and is",winner)