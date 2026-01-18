########## Read in Data #############
#Open File
filename = input("Enter the name of the data file: ")
infile = open(filename, 'r')

#Read lines from File
datalist = []

for line in infile:

    #get data from line
    #put data in list
    date,h,l,r = (line.split(','))

    lowtemp = int(l)
    hightemp = int(h)
    rainfall = float(r)

    m,d,y = date.split('/')

    month = int(m)
    day = int (d)
    year = int(y)

    datalist.append([day,month,year,lowtemp,hightemp,rainfall])

#Close File
infile.close()

######## Analyze Data ########
# Get Data
month = int(input("Enter the month for the date you want to check: "))
day = int(input("Enter the day for the date you want to check: "))

# Find historical data
gooddata = []
for singleday in datalist:
    if (singleday[0] == day) and (singleday[1] == month):
        gooddata.append([singleday[2],singleday[3],singleday[4],singleday[5]])

# Analyze historical data
minsofar = 120
maxsofar = -100
numgooddates = 0
sumofmin = 0
sumofmax = 0

for singleday in gooddata:
    numgooddates +=1
    sumofmin += singleday[1]
    sumofmax += singleday[2]

    if singleday[1] < minsofar:
        minsofar = singleday[1]
    if singleday[2] > maxsofar:
        maxsofar = singleday[2]

avglow = sumofmin / numgooddates
avghigh = sumofmax / numgooddates

######## Present results ########

print("There were",numgooddates,"days")
print("The lowest temperature on record was:",minsofar)
print("The highest temperature on record was:",maxsofar)
print("The average low has been",avglow)
print("The average high has been",avghigh)