from node import Node

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        node = Node(data)
        self.count += 1
        if(self.head == None):
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node


    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node = Node(data)
        self.count += 1
        if(self.head == None):
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail 
            self.tail.next = node
            self.tail = node

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        if(index < 0):
            raise Exception('Index cannot be a negative')
        elif(index == 0):
            self.addFirst(data)
        elif(index > self.size()):
            raise Exception("Index cannot be more than the count")
        elif(index == self.size()):
            self.addLast(data)
        else:
            current = self.head
            previous = self.head
            for n in range(index):
                previous = current
                current = current.next
            node = Node(data)
            previous.next = node
            node.prev = previous
            current.prev = node
            node.next = current


    def indexOf(self, data) -> int:
        # Search through the list. Return the index position if data is found, otherwise return -1    
        if(self.head == None):
            return -1
        else:
            temporary_node = self.head
            count = 0
            while temporary_node is not None:
                if(temporary_node.data == data):
                    return count
                else:
                    temporary_node = temporary_node.next
                count += 1
        

    def add(self, data) -> None:
        # Append an item to the end of the list//
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       
        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next.prev = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr
