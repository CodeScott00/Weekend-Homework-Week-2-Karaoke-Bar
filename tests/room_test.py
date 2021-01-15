import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.name = Name("CodeClan Caraoke", 20, 1, 10, "Uptown Funk")

    def test_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.room.name)

    # def test_capacity(self):
    #     self.assertEqual(20, self.room.capacity)

    # def test_number_of_guests(self):
    #     self.assertEqual(1, self.room.guest_numbers)

    # def test_cost_of_entry(self):
    #     self.assertEqual(10, self.room.entry_cost)

    # def test_playlist(self):
    #     self.assertEqual("Uptown Funk", self.room.playlist)
    