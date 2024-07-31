
class Player:
    def __init__(self, name):

        #init player stats and inventory
        self.name = name

        self.health = 100
        self.armor = 0
        self.phys_damage = 10
        self.mag_damage = 0
        self.crit_chance = 0

        #items which be available
        self.items = ["Sword", "Shield", "Trinket"]

        self.inventory = []


    #display stats
    def display_stats(self):
        print(f''' Hero named {self.name}!
| Stats:
|
| Health: {self.health}
| Armor: {self.armor}
| Physical damage: {self.phys_damage}
| Magical damage: {self.mag_damage}
| Crit chance: {self.crit_chance}
| 
|
| Inventory {self.inventory}
{"-"*27}''')



    def add_item(self, item):
        pass

    
    #if new items added to items[] update states information
    def update_states(self):
        if "Sword" == self.inventory[-1]:
            phys_damage += 10
            crit_chance += 5
        if "Shield" == self.inventory[-1]:
            armor += 10
            health += 10
        if "Trinket" == self.inventory[-1]:
            mag_damage += 10
            crit_chance += 5

#creating new player with name Misha
Misha = Player("Misha")

#display info
Misha.display_stats()