import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("CodeClan Caraoke",100, 20)  #QUESTION: WHY CANT WE PUT SELF.NAME = NAME IN HERE, How many values should we have? <<<
        self.guest = Guest("Pablo", 100)
        self.capacity = []
        self.song_1 = Song("Anything is better than nothing", "The Hunna") ##added this?
        self.song_2 = Song("Man on fire", "Bury tomorrow")


    def test_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.room.name) #<< explain where this comes from and why please?

    def test_till_value(self):
        self.assertEqual(100, self.room.till) 

    def test_cost_of_entry(self):
        self.assertEqual(20, self.room.entry_cost)

    def test_capacity(self):
        self.assertEqual(0, len(self.capacity))  

    def test_add_remove_guest(self):
        self.room.add_guest(self.guest) #WHY IS IT ROOM HERE INSTEAD OF GUEST?
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.capacity))

    def test_check_capacity(self):
        self.room.add_guest(self.guest)
        self.room.check_capacity(self.capacity)
        self.assertEqual(1, len(self.room.capacity))

    def test_add_songs_to_room(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, len(self.room.playlist))

    #EXTENSIONS

    def test_room_has_till(self):
       self.assertEqual(100, self.room.till)

    def test_queue(self):
        

    
    
    
    
    
    
    # def test_remove_money_guest_then_add_money_to_till(self):
    #     self.room.remove_money(self.room.guest.money)


   
    # def test_entry_fee(self):
    #     self.room.add_guestMoney(self.guest.)





    

    
    
    
    # def test_can_check_in_guests_to_room(self):
        

      # does it hgave to be len or can it be []?

    # def test_number_of_guests(self):
    #     self.assertEqual(0,self.capacity)

    # def test_playlist(self):
    #     self.assertEqual("Uptown Funk", self.room.playlist)
    