from random import randint 
class Player:
    def __init__(self, name):

        #added init player stats and inventory; by misha
        self.name = name
        self.balance = 0 # added new var.; by artyom

        self.health = 100
        self.armor = 0
        self.phys_damage = 10
        self.mag_damage = 0
        self.mana_pt = 100
        self.crit_chance = 0

        #added items which be available; by misha
        self.items = ["Клінок", "Щит", "Дрібничка", "Вудочка"]

        self.inventory = ["Вудочка"]

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
    def disp_invent(self):
        print(f'''{'*' * 35}
        Your Inventory: 
        |        {self.inventory}        |
{'*' * 35}''')


    #added func to add item from [items] to [inventory]; by misha
    def add_item(self, item):
        try:
            self.inventory.append(item)
            self.items.remove(item)
            print(f"Тепер {item} у тебе в інвентарі")
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
        if "Вудочка" == self.inventory[-1]:
            print("Тепер ви можите рибачити!")

#fishing mechanic
    def fishing_process(self):
        #RULES FOR FISHING
        counter = 0
        fishing_rules = input("Хочите подивитися привали гри? Так/ні:  ")

        if "Так" in fishing_rules:
            print("Правила рибалки: \n""У вас є 5 спроб поки вудочка не зламалася\n", "Після пятої спроби міні-гра закінчиться\n", "Ось і всіправила:")
        else:
            print("Гарної гри!")
        
        #START OF FISHING (calling main code while counter is < 5)
        while counter < 5 and ("Вудочка") in self.inventory:
          
            start = input("Щоб закинути вудочку натисніть 2: ")
            if "2" in start:
                counter += 1
                self.fishing()
        else:
            print(f"Вудочка зламалася(або її немає)!. На вашому рахунку: {self.balance} голди \n", "*Ви пішли від озера*")
            if "Вудочка" in self.inventory: self.inventory.remove("Вудочка")

    #MAIN FISHING CODE
    def fishing(self):
        procent = randint(1,100)
        #chance to catch a fish
        if procent <= 5:                                          # 5 % 
            print("Ви зловили золоту рибку!")  
            self.balance += 15
            
        
        elif  procent <= 15:                        # 10% 
            print("Ви зловили Тунця!")
            self.balance += 10
        
        elif procent <= 35:                        #20%
            print("Ви зловили Скумбрію!")
            self.balance += 7
        
        elif procent <= 60:                        # 25%
            print("Ви зловили Бичка!")
            self.balance += 5
        
        elif procent <= 100:                       # 40%       
            print("Ви зловили Карпіка :()")
            self.balance += 2
        print(f"На ваш рахунок зараховано: {self.balance}")
