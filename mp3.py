
import random

class Mp3_Playlist:
    def __init__(self,playlist_name,song):
        self.playlist_name = playlist_name
        self.tracks = []
        self. song = song
        



        
    
    def display_Tracks(self):
         self.tracks = []

    def enqueue_track(self,song):
         return self.tracks.append(song)

    def remove_track(self,song):
        if song in self.tracks:
            self.tracks.remove(song)
        else:
            print(f"{song} not found in the playlist.")
        
        
    def save_playlist_to_file(self, filename):
        with open(filename, "w") as fhand:
            for song in self.tracks:
                 fhand.write(song + "\n")
        
    def shuffle_songs(self):
         random.shuffle(self.tracks)
         print(self.tracks)
    def count_tracks(self):
        return len(self.tracks)

    def calculate_total_duration(self):
       
        total_duration = 0
        for track in self.tracks:
            total_duration += track.duration
            return total_duration
   

    def clear_playlist(self):
        self.tracks.clear()


    def is_empty(self):
        return len(self.tracks) == 0 

playlist1 = Mp3_Playlist("my_playlist","sugar")
playlist1.enqueue_track("Hit em up.mp3")
playlist1.enqueue_track("mama.mp3")
playlist1.enqueue_track("ambitionz az a ridah.mp3")
playlist1.save_playlist_to_file("music.txt")


print("\n...shuffling...\n")
print(playlist1.shuffle_songs())
playlist1.save_playlist_to_file("music.txt")
print(playlist1.count_tracks())
print(playlist1.is_empty())
print(playlist1.display_Tracks())
print(playlist1.remove_track('mama.mp3'))
