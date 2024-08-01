from random import randint

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
    mag_dmg = 5
    enemy_hp = 50
    player_hp = 100

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
            print(f"Здоров'я ворога - {enemy_hp}")
            print(f"Ваше здоров'я -- {player_hp}\n")


        #вибрати дію
        move = input('''Що ви робите у бійці?\n
Дії:
  | Атака(залежить від урону та шансу кріта)
  | Хіл(залежить від магії)
  | Імпр - імпровізація\n''')
        
        move = move.title()

        # процес атаки
        if move == "Атака":
            type = input("Атака фізичка або магічна?")
            type = type.title()
            if type == "Фізична":

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
            elif type == "Магічна":
                
                damage = 0
                tmp_crit = randint(0, 101)

                if tmp_crit > (100 - crit_chance):
                    damage = mag_dmg * 2.5
                    print(f"\nВи нанесли критичний удар!\n Ви нанесли - {damage} - урона")
                else:
                    damage = mag_dmg
                    print(f"\nВи нанесли звичайний удар\n Ви нанесли - {damage} - урона")
                enemy_hp -= damage
            else:
                print("Неправильне слово")
                continue


            player_hp = enemyAttack(player_hp)

            

        #процес хілу
        elif move == "Хіл":
            pass
        # процес імпровізації
        elif move == "Імпр":
            pass

fight()