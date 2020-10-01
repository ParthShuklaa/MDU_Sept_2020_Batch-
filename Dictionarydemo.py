MyDict = {"MyCar" : "Merc- Benz",
            "Model" : "C-Class",
            "Color" : "Black",
            "Year" :1990}

def Display():
    for i in MyDict.values():
        print(i)

Display()
print(MyDict)

MyDict["EngineType"]= "Automatic"
MyDict["Color"] = "Red"
Display()