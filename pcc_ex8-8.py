# This is from Python Crash Course from Chapter 8, exercise 8


def make_album(artist_name, album_title, num_tracks=''):
    if num_tracks:
        album_dic = {
            'Artist': artist_name,
            'Title': album_title,
            'Number of Tracks': num_tracks
        }
    else:
        album_dic = {
            'Artist': artist_name,
            'Title': album_title
        }
    return album_dic

while True:
    message = "Please tell me about your album: "
    message += "\n(write 'q' to quit'"
    artist_name = input("Name of artist: ")
    if artist_name == 'q':
        break
    album_title = input("Name of album: ")
    num_tracks = input("Number of tracks: ")
    print(make_album(artist_name, album_title, num_tracks))