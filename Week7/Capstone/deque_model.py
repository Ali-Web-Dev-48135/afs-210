import random
class DequeModel():
    def __init__(self):
        self.items = []
        
    def append_song(self, item):
        self.items.append(item)
        
    def append_song_left(self, item):
        self.items.insert(0, item)
        
    def clear_song(self):
        self.items.clear()
        
    def count_of_songs(self, item):
        return self.items.count(item)
    
    def insert_song(self, index, item):
        self.items.insert(index, item)
        
    def pop_song(self):
        return self.items.pop()
        
    def pop_song_left(self):
        return self.items.pop(0)
        
    def peek(self):
        return self.items[-1]
    
    def peek_left(self):
        return self.items[0]
    
    def remove_song(self, title):
        numRotation = len(self.items)-1
        for _ in range(numRotation):
            if str.lower(self.peek().getTitle()) == str.lower(title):
                self.pop_song()
            self.rotate(1)
        print("\nSong removed from playlist...\n")
        
    def reverse(self):
        self.items.reverse()
        
    def show_all_tracks(self):
        for i in self.items:
            print(i)
            
    def printDeque(self):
        numRotation = len(self.items)
        for _ in range(numRotation):
            print(self.peek())
            self.rotate(1)
            
    def get_data(self):
        cur_song = self.peek_left()  
        print("Currently playing... ")
        return cur_song
        
    def rotate(self, n):
        if n > 0:
            for _ in range(n):
                self.append_song_left(self.pop_song())
        elif n < 0:
            for _ in range(abs(n)):
                self.append_song(self.pop_song_left())
         
    def shuffle_all_tracks(self):
        for i in range(len(self.items)-1, 0, -1):
            r = random.randint(0, i)
            self.items[i], self.items[r] = self.items[r], self.items[i]
        return self.items
               
        
        
        