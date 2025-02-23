import json
import xml.etree.ElementTree as et


class Song(object):
    """docstring for Song"""

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def __str__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)

    __repr__ = __str__


# Common interface
class SongSerializer(object):
    """docstring for SongSerializer"""

    def serialize(self, song, format):
        try:
            serializer = _get_serializer(format)
        except ValueError:
            print("Error: format {} not supported".format(format))
        else:
            return serializer(song)


# Factory Method
def _get_serializer(format):
    if format == "JSON":
        return _serialize_to_json
    elif format == "XML":
        return _serialize_to_xml
    else:
        raise ValueError(format)


# Product JSON
def _serialize_to_json(song):
    song_info = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(song_info)


# Product XML
def _serialize_to_xml(song):
    song_info = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_info, 'title')
    title.text = song.title
    artist = et.SubElement(song_info, 'artist')
    artist.text = song.artist
    return et.tostring(song_info, encoding='unicode')


if __name__ == '__main__':
    song = Song('1', 'Water of Love', 'Dire Straits')
    serializer = SongSerializer()
    st = serializer.serialize(song, 'JSON')
    print(st)
    st = serializer.serialize(song, 'XML')
    print(st)
    st = serializer.serialize(song, 'YAML')
