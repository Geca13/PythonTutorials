class Song:

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:

    def __init__(self, album_name, year, artist=None):
        self.album_name = album_name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.track_list = []

    def add_song(self, song, position=None):
        if position is None:
            self.track_list.append(song)
        else:
            self.track_list.insert(position, song)


class Artist:

    def __init__(self, artist_name):
        self.artist_name = artist_name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.artist_name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album is None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.album_name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_checkfile(artist_list):
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.track_list:
                    print(
                        "{0.artist_name}\t{1.album_name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                        file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print(len(artists))

    create_checkfile(artists)
