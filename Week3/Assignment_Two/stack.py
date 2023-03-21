class Stack:
    def __init__(self):
        self.dataholder = []
        
    def size(self) -> int:
        return len(self.dataholder)
    
    def push(self, element) -> None:
        self.dataholder.append(element)
    
    def pop(self):
        return self.dataholder.pop()

    def isEmpty(self):
        return len(self.dataholder) == 0 

    def peek(self):
        return self.dataholder[-1]
    
    def print(self) -> None:
        print(self.dataholder)

