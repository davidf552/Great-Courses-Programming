class node:
    def __init__(self,name,population=0):
        self._name = name
        self._pop = population

    def getName(self):
        return self._name

    def getPopulation(self):
        return self._pop

class edge:
    def __init__(self,index1,index2,weight=0):
        self._city1 = index1
        self._city2 = index2
        self._distance = weight

    def getIndex1(self):
        return self._city1

    def getIndex2(self):
        return self._city2

    def getIndexes(self):
        return (self._city1,self._city2)

    def getWeight(self):
        return self._distance


cities = []
roads = []

city = node('Rivertown',100)
cities.append(city)
city = node('Brookside',1500)
cities.append(city)
city = node('Hillsview',500)
cities.append(city)
city = node('Forrest City', 800)
cities.append(city)
city = node('Lakeside',1100)
cities.append(city)

road = edge(0,1,100)
roads.append(road)
road = edge(0,2,50)
roads.append(road)
road = edge(2,1,130)
roads.append(road)
road = edge(2,3,40)
roads.append(road)
road = edge(3,4,80)
roads.append(road)


def sum_pop(roads):
    road = roads[0]
    pop1 = 0
    pop2 = 0
    for city in cities:
        if city.getName() == road.getName1():
            pop1 = city.getPopulation()
        if city.getName() == road.getName2():
            pop2 = city.getPopulation()
    total_population = pop1 + pop2
    return total_population

def getPopulation2(edge,cities):
    names = edge.getNames()
    acc = 0
    for i in cities:
        city_name = i.getName()
        population = i.getPopulation()
        for j in names:
            if city_name == j:
                acc += population

    return acc

def getPopulationIndex():
    road = roads[0]
    pop1 = cities[road.getIndex1()].getPopulation()
    pop2 = cities[road.getIndex2()].getPopulation()

    return pop1+pop2
