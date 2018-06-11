# This is from Python Crash Course from Chapter 8, exercise 7


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

