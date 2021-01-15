import unittest
from src.song import Song #<<< check classes, src??????  

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Anything is better than nothing", "The Hunna")
        

    def test_song_has_name(self):
        self.assertEqual("Anything is better than nothing", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("The Hunna", self.song.artist)