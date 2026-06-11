class Track:
    # constrcutor
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length
    
    def show_track(self):
        print(f"Title: {self.title} - Artist: {self.artist} - Length: {self.length//60} mins and {self.length%60} secs")

