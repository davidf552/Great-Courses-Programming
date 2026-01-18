from multiprocessing import Process,Queue

class node: #node
    def __init__(self,word):
        self._word = word
        self._neighbors = []
        self._status = 0
        self._discoveredby = 0

    def getWord(self):
        return self._word

    def getNeighbors(self):
        return self._neighbors

    def addNeighbor(self,neighbor_index):
        self._neighbors.append(neighbor_index)

    def isUnseen(self):
        if self._status == 0:
            return True
        else:
            return False

    def isSeen(self):
        if self._status == 1:
            return True
        else:
            return False

    def setUnseen(self):
        self._status = 0

    def setSeen(self):
        self._status = 1

    def discover(self,n):
        self._discoveredby = n

    def discovered(self):
        return self._discoveredby


def addWordLink(wordlist, word1, word2):
    for i in range(len(wordlist)):
        if wordlist[i].getWord() == word1:
            n1 = i
        if wordlist[i].getWord() == word2:
            n2=i
    wordlist[n1].addNeighbor(n2)
    wordlist[n2].addNeighbor(n1)

def addLink(wordlist,index1,index2):
    wordlist[index1].addNeighbor(index2)
    wordlist[index2].addNeighbor(index1)

class queue:
    def __init__(self):
        self._queue = []

    def enqueue(self,x):
        self._queue.append(x)

    def dequeue(self):
        return self._queue.pop(0)

    def isEmpty(self):
        return len(self._queue) == 0

def retrievePath(nodelist,start,goal):
    if start == goal:
        path = []
        path.append(start)
        return path
    else:
        previous = nodelist[goal].discovered()
        previous_path = retrievePath(nodelist,start,previous)
        previous_path.append(goal)
        return previous_path

def BFS(nodelist,start,goal):
    to_visit = queue()
    nodelist[start].setSeen()
    to_visit.enqueue(start)

    found = False

    while(not found) and (not to_visit.isEmpty()):
        current = to_visit.dequeue()
        neighbors = nodelist[current].getNeighbors()
        for neighbor in neighbors:
            if nodelist[neighbor].isUnseen():
                nodelist[neighbor].setSeen()
                #Put the current node in the discovered list
                nodelist[neighbor].discover(current)
                if neighbor == goal:
                    found = True
                else:
                    to_visit.enqueue(neighbor)
    if found:
        return retrievePath(nodelist,start,goal)
    else:
        return []

def trial_function():

    with open("dictionary.txt",'r') as file:
        wordlist = file.readlines()
    nodelist = []
    for word in wordlist:
        nodelist.append(node(word))


def compareWords(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False

def findlinks(words,q,starti,endi):
    for i in range(starti,endi):
        for j in range(i+1,len(words)):

            #Compare word i and word j
            if compareWords(words[i].getWord(),words[j].getWord()):
                q.put((i,j)) #addLink(words,i,j)
words = []
dict = open("dictionary.txt",'r')
for line in dict:
    word= node(line.strip())
    words.append(word)

for i in range(len(words)):
    for j in range(i+1,len(words)):
        if compareWords(words[i].getWord(),words[j].getWord()):
            addLink(words,i,j)

word1 = input("The starting word is: ")
word2 = input("The ending word is: ")

index1 = -1
index2 = -1
for i in range(len(words)):
    if words[i].getWord() == word1:
        index1 = i
    if words[i].getWord() == word2:
        index2 = i
if index1 == -1:
    print(word1,"was not in the dictionary. Exiting")
    exit(0)
if index2 == -1:
    print(word2,"was not in the dictionary. Exiting")
    exit(0)

path = BFS(words,index1,index2)

if path == []:
    print("There was no chain between those words in the dictionary.")
else:
    for index in path:
        print(words[index].getWord())

dict.close()