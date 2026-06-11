class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.songs = []


    def printDetails(self):
        print("Title: " + self.title + " Artist: " + self.artist)


    def addTrack(self, track):
        self.songs.append(track)
    

    def printSongs(self):
        for track in self.songs:
            print(track.title)

