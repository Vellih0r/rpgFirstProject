from random import randint 
import enemy
import boss
from colorama import init,Fore,Style
#f
class Player:
    def __init__(self, name):

        #added init player stats and inventory; by misha
        self.name = name
        self.balance = 0 # added new var.; by artyom
        self.xp = 0
        self.skill_points = 0
        
        self.health = 100
        self.health_max = 100
        self.armor = 0
        self.phys_damage = 10
        self.ability_power = 5
        self.mana_pt = 100
        self.crit_chance = 0

        #added items which be available; by misha
        self.items = ["Клінок", "Щит", "Дрібничка", "Вудочка"]
        self.potions = ["Здоров'я", "Сили", "Прокляте"]

        self.inventory = ["Вудочка"]

        #added display stats; by misha
    def display_stats(self):
        print(f'''
| Stats {self.name}:
|
| Balance: {self.balance}
| Health: {self.health}
| Max Health: {self.health_max}
| Armor: {self.armor}
| Physical damage: {self.phys_damage}
| Magical damage: {self.ability_power}
| Crit chance: {self.crit_chance}
| Xp: {self.xp}
| Skill points: {self.skill_points}

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
            print(f"Тепер {item} у тебе в інвентарі")
        except BaseException as e:
            print("404 item not found:", e)

    def add_potion(self, item):
        try:
            self.inventory.append(item)
            print(f"Тепер {item} у тебе в інвентарі")
        except BaseException as e:
            print("404 item not found:", e)
    #skill mechanik
    def skill_information(self):
        print("У вас есть один скилл поинт!\nВы можете использоваться его в меню прокачки")
    def add_skill_points(self):
        try:
            while self.xp >= 100:
                self.skill_points += 1
                self.xp -= 100
        except BaseException as e:
            print("В вас недостатьо xp")
        
    def skill_upgrade(self):
        try:
            if self.skill_points >= 1:
                print(''' МЕНЮ ПРОКАЧКИ 
| Сила - збильшує ваш урон
| Интелект - збильщує кількість мани
| Стойкость - збильшує кількість хп 
                      ''')
                action = input("Що бажаєте прокачати?: ")
                action = action.title()
                if action == "Сила": self.phys_damage += 5; self.skill_points -= 1 ; print(f"Ваш урон збільшено на 5 зараз в вас його: {self.phys_damage}")
                if action == "Интелект": self.mana_pt += 10; self.skill_points -= 1; print(f"Ваш мана пул збільщенно на 20. Зараз в вас {self.mana_pt} мани")
                if action == "Стойкость": self.health_max += 10; self.skill_points -= 1; print (f"Ваше максимальне хп збільшенно на 10.Зараз в вас {self.health_max} макс хп")
        except BaseException as e:
            print("404 У вас недостатньо скилл поинтів", e)

                
        
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
        fishing_rules = input("Хочите подивитися правила гри? Так/ні:  ")
        fishing_rules.title()
        if "Так" in fishing_rules:
            print("Правила рибалки: \n""У вас є 5 спроб поки вудочка не зламалася\n", "Після пятої спроби міні-гра закінчиться\n", "Ось і всіправила:")
        else:
            print("Гарної гри!")
        
        #START OF FISHING (calling main code while counter is < 5)
        while counter < 5 and ("Вудочка") in self.inventory:
          
            start = input("Щоб закинути вудочку натисніть 2: ")
            if "2" in start:
                counter += 1
                self.fish_random()
        else:
            print(f"Вудочка зламалася(або її немає)!. На вашому рахунку: {self.balance} голди \n", "*Ви пішли від озера*")
            if "Вудочка" in self.inventory: self.inventory.remove("Вудочка")
    #updated fish mechanik 
    def fish_random(self):
        counter_fish_moves = 0
        counter_fish_distance = 0
        print("|Когда рыба двигается в какую то из сторон вам нужно двигать удочку в противополоную\n|У рыбы всего 6 движений,\n|У вас есть право на 2 ошибки\n|Удачи!")
        while counter_fish_moves < 6:
            random_move = randint(1,4)
            if random_move == 1:
                fish_move = input("Рыба двигается вверх [w,a,s,d]: ")
                if "s" in fish_move:
                    chance_to_lose_fish = randint(0,100)
                    if chance_to_lose_fish > 90:
                        counter_fish_moves += 1
                        print("Вы тянули рыбу не достаточно сильно\nРыба отдалилась")
                    else:
                        counter_fish_moves += 1
                        counter_fish_distance += 1
                        print(Fore.GREEN + "Вы подтянули рыбу к себе" + Style.RESET_ALL)
                else:
                    counter_fish_moves += 1
                    print("Вы двинули удочку не в ту сторону")
            if random_move == 2:
                fish_move = input("Рыба двигается вниз [w,a,s,d]: ")
                if "w" in fish_move:
                    chance_to_lose_fish = randint(0,100)
                    if chance_to_lose_fish > 90:
                        counter_fish_moves += 1
                        print("Вы тянули рыбу не достаточно сильно\nРыба отдалилась")
                    else: 
                        counter_fish_moves += 1
                        counter_fish_distance += 1
                        init()
                        print(Fore.GREEN + "Вы подтянули рыбу к себе" + Style.RESET_ALL)
                else:
                    counter_fish_moves += 1
                    print("Вы двинули удочку не в ту сторону")
            if random_move == 3:
                fish_move = input("Рыба двигается лево [w,a,s,d]: ")
                if "d" in fish_move:
                    chance_to_lose_fish = randint(0,100)
                    if chance_to_lose_fish > 90:
                        counter_fish_moves += 1
                        print("Вы тянули рыбу не достаточно сильно\nРыба отдалилась")
                    else:
                        counter_fish_moves += 1
                        counter_fish_distance += 1
                        print(Fore.GREEN + "Вы подтянули рыбу к себе" + Style.RESET_ALL)
                else:
                    counter_fish_moves += 1
                    print("Вы двинули удочку не в ту сторону")
            if random_move == 4:
                fish_move = input("Рыба двигается право [w,a,s,d]: ")
                if "a" in fish_move:
                    chance_to_lose_fish = randint(0,100)
                    if chance_to_lose_fish > 90:
                        counter_fish_moves += 1
                        print("Вы тянули рыбу не достаточно сильно\nРыба отдалилась")
                    else:
                        counter_fish_moves += 1
                        counter_fish_distance += 1
                        print(Fore.GREEN + "Вы подтянули рыбу к себе" + Style.RESET_ALL)
                else:
                    counter_fish_moves += 1
                    print("Вы двинули удочку не в ту сторону")
            if counter_fish_distance == 4: 
                self.fishing()
                break
        if counter_fish_distance != 4:
            print("вы не смогли словить рыбку(")
    #MAIN FISHING CODE
    def fishing(self):
        procent = randint(1,100)
        #chance to catch a fish
        if procent <= 5:                                          # 5 % 
          
            print("Ви зловили золоту рибку!")  
            self.balance += 30
            
        
        elif  procent <= 15:                        # 10% 
        
            print("Ви зловили Тунця!")
            self.balance += 15
        
        elif procent <= 35:                        #20%
            
            print("Ви зловили Скумбрію!")
            self.balance += 12
        
        elif procent <= 60:                        # 25%
            
            print("Ви зловили Бичка!")
            self.balance += 10
        
        elif procent <= 100:                       # 40%       
           
            print("Ви зловили Карпіка :()")
            self.balance += 5
        print(f"На ваш рахунок зараховано: {self.balance}")



    def potion_use(self):
        c = 0
        if "Здоров'я" in self.inventory:
            print("Ви маєте зілля хп")
            c += 1
        if "Сили" in self.inventory:
            print("Ви маєте зілля сили")
            c += 1
        if "Прокляте" in self.inventory:
            print("Ви маєте прокляте зілля")
            c += 1
        if c > 0:
            potion_name = input(f"Ви маєте {c} зілля! Напишіть назву зілля щоб використати:\n")
            potion_name = potion_name.title()
            if potion_name == "Хп" and "Здоров'я" in self.inventory:
                self.health = self.health_max
                print("Ваше хп поповнено до максимума!")
                self.inventory.remove("Здоров'я")
            elif potion_name == "Сили" and "Сили" in self.inventory:
                self.phys_damage += 10
                print("Ваш урон збільшено на 10!")
                self.inventory.remove("Сили")
            elif potion_name == "Прокляте" and "Прокляте" in self.inventory:
                self.health_max = self.health_max // 2
                self.health = self.health_max
                self.ability_power += 20
                print(f"Тепер ваше макс.хп - {self.health_max} -")
                print("Але ваш магічний урон збільшено на 20")
                self.inventory.remove("Прокляте")
        else:
            print("На жаль в вас немає жодного зілля")

    def hospital(self):
        print(f"Ви увійшли до госпіталю\n Ваше максимальне хп: {self.health_max}\n Ваше поточне хп: {self.health}")
        heal_price = 10
        max_price = 30
        heal = input(f"Збільшити Максимальне хп(+10) - 'Макс' ({max_price})\n Відновити поточне хп - 'Хіл' ({heal_price})")
        heal = heal.title()
        if heal == "Макс":
            if self.balance >= max_price:
                self.balance -= max_price
                self.health_max += 15
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
#босс файт
    def fight_process(self, en):
        if en == "boss": #якщо їдемо на босса 
            enem = boss.Boss()
        elif en == "enemy":           #якщо їдемо в ліс
            enem = enemy.Enemy()
        def friendly_fire(dmg):
            print("-" * 27)
            print(f"Ви хотіли зробити вертушку ногою, але впали та отримали {dmg//2} урону!")
            return dmg//2


        def flow():
            dmg = 100
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


        def potion(num):
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
                return(item)
            else:
                print("Враг хотів щось в вас вкрасти, але ваш інвентар пустий")
            
            

        def fight():

            block_counter = 0

            # цикл поки хтось не помре
            while True:
                if self.health <= 0:
                    print("\nВи померли!")
                    break

                #написати хп
                else:
                    print(f"\n{'*' * 27}\nЗдоров'я ворога - {enem.hp}")
                    print(f"Ваше здоров'я -- {self.health}\n{'*' * 27}\n")


                #вибрати дію
                move = input('''Що ви робите у бійці?\n
        Дії:
        | Атака(залежить від урону та шансу кріта)
        | Хіл(залежить від магії)
        | Імпр - імпровізація
        | Зілля - використати зілля\n''')
                
                move = move.title()
                if move == "Зілля":
                    self.potion_use()
                    block_counter += 1
                # процес атаки
                elif move == "Атака":
                    type = input("Фіз/маг?\n")
                    type = type.title()
                    if type == "Фіз":

                        # урон та розрахунок чи спрацював кріт
                        damage = 0
                        tmp_crit = randint(0,100)

                        # внести урон кріту чи без кріту
                        if tmp_crit >= (100 - self.crit_chance):
                            damage = self.phys_damage * 2.5
                            print(f"\nВи нанесли критичний удар!\nВи нанесли - {damage} - урона")
                        else:
                            damage = self.phys_damage
                            print(f"\nВи нанесли звичайний удар\nВи нанесли - {damage} - урона")
                        tmp_hp = enem.hp - damage
                        enem.hp = tmp_hp
                    elif type == "Маг":
                        
                        damage = 0
                        tmp_crit = randint(0, 100)

                        if tmp_crit >= (100 - self.crit_chance):
                            damage = self.ability_power * 2
                            print(f"\nВи нанесли критичний удар!\nВи нанесли - {damage} - урона")
                        else:
                            damage = self.ability_power
                            print(f"\nВи нанесли звичайний удар\nВи нанесли - {damage} - урона")
                        tmp_hp = enem.hp - damage
                        enem.hp = tmp_hp
                    else:
                        print("Неправильне слово")
                        continue

                    
                # potion
                #процес хілу
                elif move == "Хіл":
                    heal = randint(5, 10) + self.ability_power
                    doubleheal_chance = randint(0,100)
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
                    imp = randint(1, 4)
                    suic = randint (1, 20)
                    if suic == 4:
                        self.health -= suicide()
                    elif imp == 1:
                        self.health -= friendly_fire(self.phys_damage)
                    elif imp == 2:
                        tmp_hp = enem.hp - flow()
                        enem.hp = tmp_hp
                    elif imp == 3:
                        if "Вудочка" in self.inventory:
                            self.inventory.remove("Вудочка")
                            block(2)
                            block_counter += 2
                        else:
                            p = randint(1, 3)
                            self.inventory.append(potion(p))
                    elif imp == 4:
                        robbed = rob(self.inventory)
                        if len(self.inventory) > 0:
                            if robbed == "Здоров'я" or robbed == "Сили" or robbed == "Прокляте":
                                self.potions.append(robbed)
                            else:
                                self.update_stats(robbed)
                                self.items.append(robbed)
                    
                else:
                    print("Неправильне слово")
                    continue
                # перевірити хп(чи помер гравець чи ворог)
                if enem.hp <= 0 and en == "enemy":
                    print("\nВи вбили ворога!")
                    gold = randint(10,21)
                    xp = randint (50,100)
                    self.balance += gold
                    self.xp += xp 
                    #self.skill_points()
                    if self.xp >= 100:
                        self.skill_information()
                        self.add_skill_points()
                    print(f"Ви заробили {gold} золота та отримали {xp} xp!")
                    break
                if enem.hp <= 0 and en == "boss":
                    print(Fore.RED+"Мог повелитель крови был повержен!"+ Style.RESET_ALL)
                    gold = 450
                    xp =  600
                    self.balance += gold
                    self.xp += xp 
                    if self.xp >= 100:
                        self.add_skill_points()
                    print(f"Ви заробили {gold} золота та отримали {xp} xp!")
                    break
                
                # перевірка чи не заблокований ворог
                if block_counter == 0:
                    self.health -= enem.enemyAtack()
                else:
                    block_counter -= 1
                    print("Ворог нічого не робить")

        fight()

       