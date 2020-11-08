class Artist:
    '''
        Class to create an object of Artist
        
        methods:
            add_artist
                args : name of the artist
    
    '''
    def __init__(self,name):
        '''Artist Object will be created
        args :
            name(str)
        '''
        self.name=name
        self.albums_list=[]
        
    def add_albums(self,name):
        '''Method to add artist
        args
            name(str) : will have the name of the artist
        '''
        self.albums_list.append(name)
        
        
class Album:
    '''
        It's a class to represent Albums
    
        args:
            name(str)      :     Name of the album
            year(int)      :     Year in which album is published
            artist(str)    :     Artist of the album if no artist is given then it will be None
        method :
            To add song in the songs_list[]
    '''
    
    def __init__(self,name,year:int,artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist="Artist"
        else:
            self.artist = artist 
        self.tracks=[]     
        
    def add_song(self,song):
        ''' 
            This method will add the song
            
            args:
                tracks(str):Name of the song
        
        '''
        self.tracks.append(song)
        
        
class Songs:
    '''
        Class to create an object of Songs
        args:
            name(str)    :    Name of the song
            artist(str)  :    Name of the artist
            duration(int):    Duration of the song (By default it is 0)
    '''
    def __init__(self,name,artist,duration=0):
        self.name=name
        self.artist=artist
        self.duration=duration
    

def load_data():
    
    new_artist= None
    new_album = None
    new_artist_list=[]
    
    with open("albums.txt","r") as album:
        
        for line in album:
            artist_name,artist_album,year,song = tuple(line.strip("\n").split("\t"))           
            year=int(year)
            print("{}: {} :{} :{} ".format(artist_name,artist_album,year,song))
            if new_artist is None:
                new_artist=Artist(artist_name)
            
            elif new_artist.name!=artist_name:
                new_artist.add_albums(new_album)
                new_artist=Artist(artist_name)
                new_artist_list.append(new_artist)
                new_album=None
            
            
            if new_album is None:
                new_album=Album(artist_album,year,artist_name)
            elif new_album.name != artist_album:
                new_artist.add_albums(new_album)
            
            
            # Adding song to the album
            new_song = Songs(song,new_artist)
            new_album.add_song(new_song)
        # To add last artist and his album
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_albums(new_album)
            new_artist_list.append(new_artist)
    return new_artist_list
def create_new_file(new_artist_list):
    with open("albums.txt","w") as duplicate:
        for artist in new_artist_list:
            for albums in artist.albums_list:
                for songs in albums.tracks:
                    print("{} <= artists {} <= albums {} <= year {} <= songs".format(artist,albums,albums.year,songs),
                          file=duplicate)
    
    
    
if __name__ == '__main__':
    data=load_data()
