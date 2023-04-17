from deque_model import DequeModel
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
         
class MP3Player():
    def __init__(self):
        self.playlist = DequeModel()
        self.isPlaying = False

    def add_track(self, song):
        self.playlist.append_song_left(song)
        
    def remove_track(self, title):
        self.playlist.remove_song(title)
        
    def skip_track(self):
        self.playlist.rotate(1)
        self.play_track()
        
    def reverse_track(self):
        self.playlist.rotate(-1)
        self.play_track()
        
    def play_track(self):
        self.isPlaying = True
        current_song = self.playlist.peek_left()
        print(current_song.getTitle())
        
    def song_details(self):
        if self.isPlaying:
            print(self.playlist.get_data())
        else:
            print("No song currently playing...")
        
    def show_playlist(self):
        self.playlist.printDeque()
        
    def shuffle_track(self):
        self.playlist.shuffle_all_tracks()
        self.play_track()
        
        
        
music_player = MP3Player()
music_player.add_track(Song("Fire", "Adele"))
music_player.add_track(Song("Blank Space", "Taylor Swift"))
music_player.add_track(Song("Dear Mama", "Tupac Shakur"))
music_player.add_track(Song("Toy Soldiers", "Eminem"))
music_player.add_track(Song("Closet", "Eminem"))
music_player.add_track(Song("22", "Taylor Swift"))
music_player.add_track(Song("Skys The Limit", "Biggie"))
music_player.add_track(Song("Hello", "Adele"))


while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        title_of_song = input("Enter song title: ")
        artist_of_song = input("Enter artist: ")
        music_player.add_track(Song(title_of_song, artist_of_song))
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        print("\nSong List:\n")
        music_player.playlist.show_all_tracks()
        title_of_song = input("\nEnter song title to delete:\n")
        music_player.remove_track(title_of_song)
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....") 
        music_player.play_track()       
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing    
        music_player.skip_track()                 
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing 
        music_player.reverse_track()
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling.... Now Playing: ") 
        music_player.shuffle_track()       
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        music_player.song_details()   
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        music_player.show_playlist()
    elif choice == 0:
        print("Goodbye.")
        break


            