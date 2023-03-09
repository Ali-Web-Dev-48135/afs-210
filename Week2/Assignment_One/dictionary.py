
#Went with a dictionary
Data4 = {
    "name": "Joe",
    "age":26,
    "active": True,
    "hourly_wage": 14.75
    }


def activeToFalse(dict):
    dict['active'] = False


def addAddress(dict):
    dict['address'] = '123 West Main Street'


def printJoesSalary(dict):
    print(dict['hourly_wage'] * 40)

def printMyDict(dict):
    print(dict)


def dictionaryInit():
    activeToFalse(Data4)
    addAddress(Data4)
    printJoesSalary(Data4)
    printMyDict(Data4)



