from random import randint

#імпровізації

def frendly_fire(dmg):
    print(f"Ви хотіли зробити вертушку ногою, але впали та отримали {dmg/2} урону!")
    return int(dmg/2)


def flow():
    dmg = 50
    print(f"Ви війшли в потік та нанесли {dmg} урону!")
    return dmg


def block(turns):
    print("Ви замотали ворога вудочкою і вона зламалася")
    print(f"Ворог не буде атакувати {turns} ходи")


def suicide():
    dmg = 100
    print("Ви розгнівали сили пітьми та в вас вдарила молнія!")
    print(f"Ви отримали {dmg} урону")
    return dmg


def poition(num):
    if num == 1:
        print("У ворога було зілля здоров'я - ви його вкрали!")
        return "Health"
    elif num == 2:
        print("У ворога було зілля сили - ви його вкрали!")
        return "Power"
    elif num == 3:
        print("У ворога було прокляте зілля! - ви його вкрали!")
        return "Cursed"


def rob(inventory):
    if len(inventory) > 0:
        item = inventory.pop()
        print(f"Ви відволіклися та ворог вкрав {item} з вашого інвентарю!")
    else:
        print("Враг хотів щось в вас вкрасти, але ваш інвентар пустий")
    

# атака ворога
def enemyAttack(hp):

    # змінні урона та кріта
    enemy_dmg = randint(1, 10)
    enemy_crit = randint(0, 101)

    # розрахунок шансу кріта
    if enemy_crit > 10:
        enemy_dmg *= 2
        print(f"\nВорог наносить критичний удар!\n Ви отримали - {enemy_dmg} - урону")
    else:
        print(f"\nВорог наносить удар!\n Ви отримали - {enemy_dmg} - урону")
        
    # повернути скільки нанесли урону
    return hp - enemy_dmg

def fight():

    # змінні щоб працював код
    crit_chance = 10
    phis_dmg = 10 
    ability_power = 5
    enemy_hp = 50
    player_hp = 100
    inventory = ["Вудочка"]
    counter = 0

    # цикл поки хтось не помре
    while True:

        # перевірити хп(чи помер гравець чи ворог)
        if enemy_hp <= 0:
            print("\nВи вбили ворога!")
            break
        elif player_hp <= 0:
            print("\nВи померли!")
            break

        #написати хп
        else:
            print(f"\n{'*' * 27}\nЗдоров'я ворога - {enemy_hp}")
            print(f"Ваше здоров'я -- {player_hp}\n{'*' * 27}\n")


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
            if type == "фіз":

                # урон та розрахунок чи спрацював кріт
                damage = 0
                tmp_crit = randint(0,101)

                # внести урон кріту чи без кріту
                if tmp_crit > (100 - crit_chance):
                    damage = phis_dmg * 2
                    print(f"\nВи нанесли критичний удар!\n Ви нанесли - {damage} - урона")
                else:
                    damage = phis_dmg
                    print(f"\nВи нанесли звичайний удар\n Ви нанесли - {damage} - урона")
                enemy_hp -= damage
            elif type == "маг":
                
                damage = 0
                tmp_crit = randint(0, 101)

                if tmp_crit > (100 - crit_chance):
                    damage = ability_power * 2.5
                    print(f"\nВи нанесли критичний удар!\n Ви нанесли - {damage} - урона")
                else:
                    damage = ability_power
                    print(f"\nВи нанесли звичайний удар\n Ви нанесли - {damage} - урона")
                enemy_hp -= damage
            else:
                print("Неправильне слово")
                continue

            

        #процес хілу
        elif move == "Хіл":
            heal = randint(10, 20)
            doubleheal_chance = randint(0,101)
            if doubleheal_chance > (100 - doubleheal_chance):
                heal *= 2
            if heal + player_hp > 100:
                player_hp = 100
                print("\nВи поповнили хп до 100")
            else:
                player_hp += heal
                print(f"\nВи застосували Хіл\n Було відхилено - {heal} - здоров'я")

        # процес імпровізації
        elif move == "Імпр":
            imp = randint(1, 4)
            suicide = randint (1, 50)
            if suicide == 4:
                self_dmg = suicide()
                print(self_dmg)
                player_hp -= self_dmg
            elif imp == 1:
                self_dmg = frendly_fire(phis_dmg)
                print(self_dmg)
                player_hp -= self_dmg
            elif imp == 2:
                shot_dmg = flow()
                print(shot_dmg)
                enemy_hp -= shot_dmg
            elif imp == 3:
                if "Вудочка" in inventory:
                    inventory.remove("Вудочка")
                    turns = 2
                    block(turns)
                    counter += turns
                else:
                    p = randint(1, 4)
                    inventory.append(poition(p))
            elif imp == 4:
                robbed = rob(inventory)
                if len(inventory):
                    inventory.remove(robbed)
                #update_states(robbed)
            


        # перевірка чи не заблокований ворог
        if counter == 0:
            player_hp = enemyAttack(player_hp)
        else:
            counter -= 1
            print("Враг пропустив свій хід")

fight()