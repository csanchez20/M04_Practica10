# Declaracio del diccionari
myDict = {}
myDict["El millor"] = "Positivo"
myDict["Anys"] = 22
myDict["Notes"] = 10
myDict["Novias"] = 0
myDict["HorasJugadasAlLol"] = 10000
myDict["Addiciones"] = "Muchas"

def longitud(myDict):
    print(len(myDict))
def valors(myDict):
    print(myDict)
def ultim(myDict):
    print(myDict.popitem())

# cridem a les funcions
longitud(myDict)

valors(myDict)

ultim(myDict)
