import unittest
from src.song import Song #<<< check classes, src??????  

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Anything is better than nothing", "The Hunna")
        # where does song test go? here on in room test?

    def test_song_has_name(self):
        self.assertEqual("Anything is better than nothing", self.song_1.name)

    def test_song_has_artist(self):
        self.assertEqual("The Hunna", self.song_1.artist)