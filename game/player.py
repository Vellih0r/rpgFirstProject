
class Player:
    def __init__(self, name):

        #added init player stats and inventory; by misha
        self.name = name
        self.balance = 0 # added new var.; by artyom

        self.health = 100
        self.armor = 0
        self.phys_damage = 10
        self.mag_damage = 0
        self.crit_chance = 0

        #added items which be available; by misha
        self.items = ["Клінок", "Щит", "Дрібничка"]

        self.inventory = []


    #added display stats; by misha
    def display_stats(self):
        print(f'''
| Stats {self.name}:
|
| Health: {self.health}
| Armor: {self.armor}
| Physical damage: {self.phys_damage}
| Magical damage: {self.mag_damage}
| Crit chance: {self.crit_chance}
{"-"*27}''')
    
    # added inventory func; by artyom
    def inv(self):
        print(f'''{'*' * 35}
        Your Inventory: 
        |        {self.inventory}        |
{'*' * 35}''')


    #added func to add item from [items] to [inventory]; by misha
    def add_item(self, item):
        try:
            self.inventory.append(item)
            self.items.remove(item)
            print(f"{item} now in inventory")
        except:
            print("404 item not found")

    
    #added IF new items added to items[] update states information; by misha
    def update_stats(self):
        if "Sword" == self.inventory[-1]:
            self.phys_damage += 10
            self.crit_chance += 5
        if "Shield" == self.inventory[-1]:
            self.armor += 10
            self.health += 10
        if "Trinket" == self.inventory[-1]:
            self.mag_damage += 10
            self.crit_chance += 5