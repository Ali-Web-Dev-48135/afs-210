from doubleLinked import DoublyLinkedList

myList = DoublyLinkedList()
myList.add('MAY')
myList.add('THE')
myList.add('FORCE')
myList.add('BE')
myList.add('WITH')
myList.add('YOU')
myList.add('!')

print(myList)
# print('THIS IS THE COUNT', myList.size())
print(myList.indexOf('WITH'))
myList.addAtIndex('US', 4)
myList.addAtIndex('ALL', 5)
print(myList)

#print(myList.size())

