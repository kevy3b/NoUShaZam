# Genre Picker
import json
import os


class SongPicker:
    script_dir = os.path.dirname(__file__)

    @classmethod
    def loadName(cls, num, genre):
        relative_path = "../../music/" + genre + "/songsLib.json"
        abs_filepath = os.path.join(cls.script_dir, relative_path)
        song = json.load(open(abs_filepath))
        songName = song[str(num)]
        return songName

    @classmethod
    def loadLyrics(cls, num, genre):
        relative_path = "../../music/" + genre + "/lyricsLib.json"
        abs_filepath = os.path.join(cls.script_dir, relative_path)
        lyrics = json.load(open(abs_filepath))
        songLyrics = lyrics[str(num)]
        return songLyrics

    @classmethod
    def loadPath(cls, num, genre):
        return '../songs/' + genre + '/' + cls.loadName(num, genre) + '.mp3'


'''class picker():
    parser = reqparse.ReqquestParser()'''
