import json
import pickle

length = 20.0
width = 15
outfile = open("datafile1.dat","w")

json_string = json.dumps(length)
outfile.write(json_string+'\n')
json_string = json.dumps(width)
outfile.write(json_string+'\n')
json_string = json.dumps("Data for an example")
outfile.write(json_string+'\n')

outfile.close()


infile = open("datafile1.dat",'r')
for i in infile:
    print(json.loads(i))
infile.close()


account = 134218954
owner = "John Smith"
balance = 1783.45

#put into BankAccount.dat
bfile = open("BankAccount.dat","wb")
pickle.dump(account, bfile)
pickle.dump(owner, bfile)
pickle.dump(balance, bfile)


bfile.close()