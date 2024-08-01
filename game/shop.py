import player
import random
import welcomeclass
from welcomeclass import decorator

def getcharacter(character):
    global char
    char = character

@decorator
def shopfunc(nickname, balance, items):
    print(f'''
        Вітаємо в магазині, {nickname}!
      Твій баланс: {balance}
''')
    prices = {}
    for item in items:
        global pricerand
        pricerand = random.randrange(10,50,5)
        prices[item] = pricerand
    print(f"{prices}\n")

def buy(character):
    buying = input("Чи бажаєте ви купити щось?\n\
Якщо так, введіть назву предмета (в будь-якому регістрі)\n")

    buying = buying.title()
    if buying == 'Клінок':
        character.balance -= pricerand
        if character.balance < pricerand:
            print("Вам не вистачає грошей.")
        print(f"Ви купували Клінок!")
        character.add_item('Клінок')
        character.update_stats()
        back = input("Бажаєте повернутись назад... (натисніть enter)\n")
    elif buying == 'Щит':
        character.balance -= pricerand
        if character.balance < pricerand:
            print("Вам не вистачає грошей.")
        print(f"Ви купували Щит!")
        character.add_item('Щит')
        character.update_stats()
        back = input("Бажаєте повернутись назад... (натисніть enter)\n")
    elif buying == 'Дрібничка':
        character.balance -= pricerand
        if character.balance < pricerand:
            print("Вам не вистачає грошей.")
        print(f"Ви купували Дрібничку!")
        character.add_item('Дрібничка')
        character.update_stats()
        back = input("Бажаєте повернутись назад... (натисніть enter)\n")
    if back == '':
        welcomeclass.welcome(character.name, character.balance)
def choice(char):
    choice = int(input("введіть 1,2 чи 3 щоб обрати...\n"))
    if choice == 1: char.display_stats()
    elif choice == 2: 
        shopfunc(char.name, char.balance, char.items)
        buy(char)
    elif choice == 3: char.inv()
    else:
        print("Невизначений вибір.")
    




