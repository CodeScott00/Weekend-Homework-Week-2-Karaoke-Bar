import unittest 
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Pablo", 100.00)

    def test_guest_name(self):
        self.assertEqual("Pablo", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.money)

    # def test_remove_money_from_wallet(self):
    #     money 
