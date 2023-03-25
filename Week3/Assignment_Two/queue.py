
class Queue:
    def __init__(self):
        self.dataholder = []
            
    def enqueue(self, element) -> None:
        self.dataholder.append(element)
    
    def dequeue(self):
        return self.dataholder.pop(0) 
    
    def size(self) -> int:
        return len(self.dataholder)


    def isEmpty(self) -> bool:
        return len(self.dataholder) == 0 

    def peek(self):
        return self.dataholder[0]
    
    def print(self) -> None:
        print(self.dataholder)
