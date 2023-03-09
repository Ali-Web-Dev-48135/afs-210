
#Went with a Set
Data2 = {"July",4,8,"Tango",4.3,"Bingo"}

#Data2 - Operations
def removeRandElement(set):
    set.pop()
    return set

def addAlpha(set):
    set.add("Alpha")
    return set

def setInit():    
    removeRandElement(Data2)
    print(addAlpha(Data2))

