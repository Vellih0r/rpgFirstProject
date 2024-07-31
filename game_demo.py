
class Player:
    def __init__(self, name):

        #init player stats and inventori
        self.name = name

        self.health = 100
        self.armor = 0
        self.f_damage = 10
        self.krit_chanse = 0
        self.m_damage = 0

        #items which be available
        self.items = ["Sword", "Shield", "Trinket"]

        self.inventory = []


    #display stats
    def display_stats(self):
        print(f''' Hero named {self.name}!
| Stats:
|
| Healt: {self.health}
| Armor: {self.armor}
| Physical damage: {self.f_damage}
| Magical damage: {self.m_damage}
| Krit chance: {self.krit_chanse}
| 
|
| Inventory {self.inventory}
{"-"*27}''')



    def add_item(self, item):
        pass

    
    #if new items added to items[] update states information
    def update_states(self):
        if "Sword" == self.inventory[-1]:
            f_damage += 10
            krit_chanse += 5
        if "Shield" == self.inventory[-1]:
            armor += 10
            health += 10
        if "Trinket" == self.inventory[-1]:
            m_damage += 10
            krit_chanse += 5

#creating new player with name Misha
Misha = Player("Misha")

#display info
Misha.display_stats()