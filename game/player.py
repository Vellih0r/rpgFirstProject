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
        self.crit_chance = 0

        #added items which be available; by misha
        self.items = ["Sword", "Shield", "Trinket"]

        self.inventory = ["fishing_rod"]

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
        if "fishing_rod" == self.inventory[-1]:
            print("У вас открылось новое действие 'Рыбалка'")

#fishing mechanic
    def fishing_process(self):
        #RULES FOR FISHING
        counter = 0
        fishing_rules = input("Хотите посмотреть правила игры? Yes/no:  ")
        if "Yes" in fishing_rules:
            print("Правила Рыбалки: \n""У вас 5 попыток чтобы словить рыбку\n""После пятого раза мини-игра прекратиться\n""Вот и все правила:")
        else:
            print("Хорошей игры!")
        
        #START OF FISHING (calling main code while counter is < 5)
        while counter < 5:
          
            start = input("Чтобы закинуть удочку нажмите кнопку 2: ")
            if "2" in start and counter < 5:
                counter += 1
                self.fishing()
        else:
            print(f"Ваши 5 попыток оконченны.На вашем балансе теперь: {self.balance} голды \n""ПРОИСХОДИТ ВЫХОД")

    #MAIN FISHING CODE
    def fishing(self):
        procent = randint(1,100)
        #chance to catch a fish
        if procent < 6:                                          # 5 %
            print("Вы словили золотую рыбку!")  
            self.balance += 15
            print(f"На ваш баланс зачислено: {self.balance}")
        
        if  procent > 5 and procent < 15:                        # 10%
            print("Вы словили Тунца!")
            self.balance += 10
            print(f"На ваш баланс зачислено: {self.balance}")
        
        if procent > 15 and procent < 35:                        #20%
            print("Вы словили Скумбрию!")
            self.balance += 7
            print(f"На ваш баланс зачислено: {self.balance}")
        
        if procent > 35 and procent < 60:                        # 25%
            print("Вы словили Бычка!")
            self.balance += 5
            print(f"На ваш баланс зачислено: {self.balance}")
        
        if procent > 60 and procent < 100:                       # 40%       
            print("Вы словили Карпика :()")
            self.balance += 2
            print(f"На ваш баланс зачислено: {self.balance}")

Hero = Player("Artem")
Hero.fishing_process()
