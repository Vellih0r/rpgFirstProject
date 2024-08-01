import player
import random
import welcomeclass
from welcomeclass import decorator

# отримати об'єкт гравця
def getcharacter(character):
    global char
    char = character


# привітати в магазині та рандомно розрахувати ціну у словник
@decorator
def shopfunc(nickname, balance, items):
    print(f'''
        Вітаємо в магазині, {nickname}!
      Твій баланс: {balance}
''')
    
    prices = {}
    for item in items:
        pricerand = random.randrange(10,50,5) 
        prices[item] = pricerand
    print(f"{prices}\n")


# гравець вибирає та купує предмет
def buy(character):
    # вибір предмету по назві
    buying = input("Чи бажаєте ви купити щось?\n\
Якщо так, введіть назву предмета\n")

    buying = buying.title()

    if buying == 'Клінок':
        print(f"Ви купували Клінок!")
        character.add_item('Клінок')
        character.update_stats()
        back = input("Бажаєте повернутись назад... (натисніть enter)\n")
    elif buying == 'Щит':
        print(f"Ви купували Щит!")
        character.add_item('Щит')
        character.update_stats()
        back = input("Бажаєте повернутись назад... (натисніть enter)\n")
    elif buying == 'Дрібничка':
        print(f"Ви купували Дрібничку!")
        character.add_item('Дрібничка')
        character.update_stats()
        back = input("Бажаєте повернутись назад... (натисніть enter)\n")
    if back == '':
        welcomeclass.welcome(character.name, character.balance)
    




