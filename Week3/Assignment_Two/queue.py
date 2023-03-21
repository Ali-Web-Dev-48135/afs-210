
class Queue:
    def __init__(self):
        self.dataholder = []
            
    def enqueue(self, element) -> None:
        self.dataholder.append(element)
    
    def dequeue(self, element) -> object:
        try:
            return self.dataholder.remove(element)
        except:
            print("Element does not exist.") 
    
    def size(self) -> int:
        return len(self.dataholder)


    def isEmpty(self) -> bool:
        return len(self.dataholder) == 0 

    def peek(self) -> object:
        return self.dataholder[0]
    
    def print(self) -> None:
        print(self.dataholder)
