class Room:

    def __init__(self, name, till, entry_cost):

        self.name = name 
        self.till = till
        self.entry_cost = entry_cost
        self.capacity = []
        self.playlist = []
        self.queue = []
        # def bar_has_name(self):       why dont we need to check the bar name ?
    #     self.assertEqual("CodeClan Caraoke", self.name)

    def add_guest(self, guest):
        self.capacity.append(guest)
                                            ## << why cant these be one function?
    def remove_guest(self,guest):
        self.capacity.remove(guest)

    def check_capacity(self, guest):
        return self.capacity

    def add_song(self, song):
        self.playlist.append(song)

    
    
    
    
    # def remove_money(self, money):
    #     if self.guest.money <= self.entry_cost:
    #         return 
    #     self.money.remove(entry_cost)
        