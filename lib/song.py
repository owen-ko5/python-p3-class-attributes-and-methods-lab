class Song:

    count = 0
    genres =[]
    genres_count={}
    artists =[]
    artist_count={}

    def __init__(self,name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
    
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):  
        if genre not in cls.genres:
            cls.genres.append(genre) 
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
          cls.artists.append(artist)
        cls.artist_count[artist] = cls.artist_count.get(artist, 0)+ 1

    @classmethod
    def add_to_artist_count(cls,increment=1):

        cls.artist_count += increment