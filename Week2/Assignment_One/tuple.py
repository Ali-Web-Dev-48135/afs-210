

#Went with a Tuple
Data1 = (7,False,"Apple",True,7,98.6)

#Data 1 - Operations
def getData1Length(tuple):
    return len(tuple)

def getFourthItem(tuple):
    return tuple[3]

def getCountOfSeven(tuple):
    return tuple.count(7)

def tupleInit():        
    print(getData1Length(Data1))
    print(getFourthItem(Data1))
    print(getCountOfSeven(Data1))
