#Went with a List
Data3 = ["A",7,-1,3.14,True,7]


def printInReverse(array):
    array.reverse()

def changeSecondValue(array):
    array[1] = "B"

def removeLastItem(array):
    array.pop()
    print(array)

def listInit():
    printInReverse(Data3)
    changeSecondValue(Data3)
    removeLastItem(Data3)



