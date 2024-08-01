from random import randint


def fight():
    crit_chance = 10
    phis_dmg = 10 
    enemy_hp = 50
    player_hp = 100
    while True:
        if enemy_hp <= 0:
            print("\nВи вбили ворога!")
            break
        elif player_hp <= 0:
            print("\nВи померли!")
            break
        else:
            print(f"Здоров'я ворога - {enemy_hp}")
            print(f"Ваше здоров'я -- {player_hp}\n")


        move = input('''Що ви робите у бійці?\n
Дії:
  | Атака(залежить від урону та шансу кріта)
  | Хіл(залежить від магії)
  | Імпр - імпровізація\n''')
        
        move = move.title()


        if move == "Атака":

            damage = 0
            tmp_crit = randint(0,101)

            enemy_dmg = randint(1, 10)
            enemy_crit = randint(0, 101)

            if tmp_crit > (100 - crit_chance):
                damage = phis_dmg * 2
                print(f"\nКритичний удар!\n Ви нанесли - {damage} - урона")
            else:
                damage = phis_dmg
                print(f"\nЗвичайний удар\n Ви нанесли - {damage} - урона")
            enemy_hp -= damage

            if enemy_crit > 10:
                enemy_dmg *= 2
                print(f"\nВорог наносить критичний удар!\n Ви отримали < {enemy_dmg} > урону")
            else:
                print(f"\nВорог наносить удар!\n Ви отримали < {enemy_dmg} > урону")
            
            player_hp -= enemy_dmg

        elif move == "Хіл":
            pass
        elif move == "Імпр":
            pass

fight()