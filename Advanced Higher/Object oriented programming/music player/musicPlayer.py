from Album import Album
from albumTrack import AlbumTrack


BAlbum = Album("Happier than ever", "Billie Eilish")
BAlbum.addTrack(AlbumTrack("Your power", "Billie Eilish", 1000000000000000000, "Happier than ever"))
BAlbum.addTrack(AlbumTrack("NDA", "Billie Eilish", 999, "Happier than ever"))
BAlbum.addTrack(AlbumTrack("Overheated", "Billie Eilish", 12097, "Happier than ever"))


TAlbum = Album("folklore","Taylor Swift")
TAlbum.addTrack(AlbumTrack("seven", "Taylor Swift", 900, "folklore"))
TAlbum.addTrack(AlbumTrack("this is me trying", "Taylor Swift", 568536, "folklore"))
TAlbum.addTrack(AlbumTrack("mad woman", "Taylor Swift", 80, "folklore"))