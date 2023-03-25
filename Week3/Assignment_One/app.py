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
print(myList.indexOf('WITH'))
indexOfYou = myList.indexOf('YOU')
myList.deleteAtIndex(indexOfYou)
myList.addAtIndex('US', indexOfYou)
indexOfExp = myList.indexOf('!')

print(myList)
