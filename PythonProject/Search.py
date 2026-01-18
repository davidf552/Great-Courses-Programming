class node: #node
    def __init__(self,name):
        self._name = name
        self._friends = []
        self._status = 0
        self._discoveredby = 0

    def getName(self):
        return self._name

    def getFriends(self):
        return self._friends

    def addFriend(self,friend_index):
        self._friends.append(friend_index)

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

def makeFriends(name1,name2):
    for i in range(len(people)):
        if people[i].getName() == name1:
            n1 = i
        if people[i].getName() == name2:
            n2 = i
    people[n1].addFriend(n2)
    people[n2].addFriend(n1)


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

    return retrievePath(nodelist,start,goal)






