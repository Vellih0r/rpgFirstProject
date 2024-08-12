import pyglet
from random import randint 
import enemy
import boss

class Player:
    def __init__(self, name):

        #added init player stats and inventory; by misha
        self.name = name
        self.balance = 0 # added new var.; by artyom

        self.health = 100
        self.health_max = 100
        self.armor = 0
        self.phys_damage = 10
        self.ability_power = 5
        self.mana_pt = 100
        self.crit_chance = 0

        #added items which be available; by misha
        self.items = ["Клінок", "Щит", "Дрібничка", "Вудочка"]

        self.inventory = ["Прокляте"]

        #added display stats; by misha
    def display_stats(self):
        print(f'''
| Stats {self.name}:
|
| Health: {self.health}
| Armor: {self.armor}
| Physical damage: {self.phys_damage}
| Magical damage: {self.ability_power}
| Crit chance: {self.crit_chance}
{"-"*27}''')
    
    # added disp_inventory func; by artyom
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
        except BaseException as e:
            print("404 item not found:", e)

    
    #added IF new items added to items[] update stats information; by misha
    # new - if "new" - update, if item name - delete its stats
    def update_stats(self, new):
        if new == "new":
            item = self.inventory[-1]
            if "Клінок" == item:
                self.phys_damage += 10
                self.crit_chance += 5
            elif "Щит" == item:
                self.armor += 10
                self.health += 10
            elif "Дрібничка" == item:
                self.ability_power += 10
                self.crit_chance += 5
            elif "Вудочка" == item:
                print("Тепер ви можите рибачити!")
        else:
            if "Клінок" == new:
                self.phys_damage -= 10
                self.crit_chance -= 5
            elif "Щит" == new:
                    self.armor -= 10
                    self.health -= 10
            elif "Дрібничка" == new:
                    self.ability_power -= 10
                    self.crit_chance -= 5

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



    def poition_use(self):
        if "Здоров'я" in self.inventory:
            print("Ви маєте зілля хп")
        if "Сили" in self.inventory:
            print("Ви маєте зілля сили")
        if "Прокляте" in self.inventory:
            print("Ви маєте прокляте зілля")
        poition_name = input("Напишіть назву зілля щоб використати: ")
        poition_name = poition_name.title()
        if poition_name == "Хп" and "Здоров'я" in self.inventory:
            self.health = self.health_max
            print("Ваше хп поповнено до максимума!")
            self.inventory.remove("Здоров'я")
        elif poition_name == "Сили" and "Сили" in self.inventory:
            self.phys_damage += 10
            print("Ваш урон збільшено на 10!")
            self.inventory.remove("Сили")
        elif poition_name == "Прокляте" and "Прокляте" in self.inventory:
            self.health_max = self.health_max // 2
            self.health = self.health_max
            self.ability_power += 20
            print(f"Тепер ваше макс.хп - {self.health_max} -")
            print("Але ваш магічний урон збільшено на 20")
            self.inventory.remove("Прокляте")


    def hospital(self):
        print(f"Ви увійшли до госпіталю\n Ваше максимальне хп: {self.health_max}\n Ваше поточне хп: {self.health}")
        heal_price = 10
        max_price = 30
        heal = input(f"Збільшити Максимальне хп(+10) - 'Макс' ({max_price})\n Відновити поточне хп - 'Хіл' ({heal_price})")
        heal = heal.title()
        if heal == "Макс":
            if self.balance >= max_price:
                self.balance -= max_price
                self.health_max += 10
            else:
                print("Невистачає грошей")
        elif heal == "Хіл":
            if self.balance >= heal_price:
                self.balance -= heal_price
                self.health = self.health_max
            else:
                print("Невистачає грошей")
        else:
            print("Неправильна команда")



#імпровізації
    def fight_process(self, enemy_class):
        if enemy_class == "boss":
            enemy = boss.Boss()
        else:
            enemy = enemy.Enemy()
        def friendly_fire(dmg):
            print("-" * 27)
            print(f"Ви хотіли зробити вертушку ногою, але впали та отримали {dmg//2} урону!")
            return dmg//2


        def flow():
            dmg = enemy.hp//2
            print("-" * 27)
            print(f"Ви увійшли в потік та нанесли {dmg} урону!")
            return dmg


        def block(turns):
            print("-" * 27)
            print("Ви замотали ворога вудочкою і вона зламалася")
            print(f"Ворог не буде атакувати {turns} ходи")


        def suicide():
            dmg = 100
            print("-" * 27)
            print("Ви розгнівали сили пітьми та в вас вдарила молнія!")
            print(f"Ви отримали {dmg} урону")
            return dmg


        def poition(num):
            print("-" * 27)
            if num == 1:
                print("У ворога було зілля здоров'я - ви його вкрали!")
                return "Здоров'я"
            elif num == 2:
                print("У ворога було зілля сили - ви його вкрали!")
                return "Сили"
            elif num == 3:
                print("У ворога було прокляте зілля! - ви його вкрали!")
                return "Прокляте"


        def rob(inventory):
            print("-" * 27)
            if len(inventory) > 0:
                item = inventory.pop()
                print(f"Ви відволіклися та ворог вкрав {item} з вашого інвентарю!")
            else:
                print("Враг хотів щось в вас вкрасти, але ваш інвентар пустий")
            

        def fight():

            block_counter = 0

            # цикл поки хтось не помре
            while True:

                # перевірити хп(чи помер гравець чи ворог)
                if enemy.hp <= 0:
                    print("\nВи вбили ворога!")
                    gold = randint(10,21)
                    print(f"Та заробили {gold} золота!")
                    self.balance += gold
                    break

                elif self.health <= 0:
                    print("\nВи померли!")
                    break

                #написати хп
                else:
                    print(f"\n{'*' * 27}\nЗдоров'я ворога - {enemy.hp}")
                    print(f"Ваше здоров'я -- {self.health}\n{'*' * 27}\n")


                #вибрати дію
                move = input('''Що ви робите у бійці?\n
        Дії:
        | Атака(залежить від урону та шансу кріта)
        | Хіл(залежить від магії)
        | Імпр - імпровізація\n''')
                
                move = move.title()

                # процес атаки
                if move == "Атака":
                    type = input("Фіз/маг?\n")
                    type = type.title()
                    if type == "Фіз":

                        # урон та розрахунок чи спрацював кріт
                        damage = 0
                        tmp_crit = randint(0,101)

                        # внести урон кріту чи без кріту
                        if tmp_crit >= (100 - self.crit_chance):
                            damage = self.phys_damage * 2.5
                            print(f"\nВи нанесли критичний удар!\n Ви нанесли - {damage} - урона")
                        else:
                            damage = self.phys_damage
                            print(f"\nВи нанесли звичайний удар\n Ви нанесли - {damage} - урона")
                        tmp_hp = enemy.hp - damage
                        enemy.hp = tmp_hp
                    elif type == "Маг":
                        
                        damage = 0
                        tmp_crit = randint(0, 101)

                        if tmp_crit >= (100 - self.crit_chance):
                            damage = self.ability_power * 2
                            print(f"\nВи нанесли критичний удар!\n Ви нанесли - {damage} - урона")
                        else:
                            damage = self.ability_power
                            print(f"\nВи нанесли звичайний удар\n Ви нанесли - {damage} - урона")
                        tmp_hp = enemy.hp - damage
                        enemy.hp = tmp_hp
                    else:
                        print("Неправильне слово")
                        continue

                    

                #процес хілу
                elif move == "Хіл":
                    heal = randint(5, 11) + self.ability_power
                    doubleheal_chance = randint(0,101)
                    if doubleheal_chance >= 75:
                        heal *= 2
                    if heal + self.health > self.health_max:
                        self.health = self.health_max
                        print("\nВи поповнили хп до максимума")
                    else:
                        self.health += heal
                        print(f"\nВи застосували Хіл\n Було відхилено - {heal} - здоров'я")

                # процес імпровізації
                elif move == "Імпр":
                    imp = randint(1, 5)
                    suic = randint (1, 21)
                    if suic == 4:
                        self.health -= suicide()
                    elif imp == 1:
                        self.health -= friendly_fire(self.phys_damage)
                    elif imp == 2:
                        tmp_hp = enemy.hp - flow()
                        enemy.hp -= tmp_hp
                    elif imp == 3:
                        if "Вудочка" in self.inventory:
                            self.inventory.remove("Вудочка")
                            block(2)
                            block_counter += 2
                        else:
                            p = randint(1, 4)
                            self.inventory.append(poition(p))
                    elif imp == 4:
                        robbed = rob(self.inventory)
                        if len(self.inventory) > 0:
                            self.inventory.remove(robbed)
                        #update_states(robbed)
                    
                else:
                    print("Неправильне слово")
                    continue

                # перевірка чи не заблокований ворог
                if block_counter == 0:
                    self.health -= enemy.enemyAttack()
                else:
                    block_counter -= 1
                    print("Враг пропустив свій хід")

        fight()
    
    def boss_fight(self):
        while True:
            boss.Boss()
            boss.Boss.random_atack()
    boss_fight()

       