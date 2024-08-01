import player
import random
import welcomeclass
from welcomeclass import decorator




# привітати в магазині та рандомно розрахувати ціну у словник
@decorator
def shopfunc(nickname, balance, items):
    print(f'''
        Вітаємо в магазині, {nickname}!
      Твій баланс: {balance}
''')
    global pricerand
    pricerand = random.randint(10,50)
    global pricerand1
    pricerand1 = random.randint(10,50)
    global pricerand2
    pricerand2 = random.randint(10,50)
    global pricerand3
    pricerand3 = random.randint(10,50)
    towars = {'Клінок': pricerand,'Щит': pricerand1,'Дрібничка': pricerand2, 'Вудочка': pricerand3}
    for key, val in towars.items():
        print(f"Товар {key} коштує {val}\n")


# гравець вибирає та купує предмет
def buy(character):
    # вибір предмету по назві
    buying = input("Чи бажаєте ви купити щось?\n\
Якщо так, введіть назву предмета\n")

    buying = buying.title()

    if buying == 'Клінок':
        if character.balance < pricerand:
            print("Вам не вистачає грошей.")
        character.balance -= pricerand
        print(f"Ви купували Клінок!")
        character.add_item('Клінок')
        character.update_stats()
        back = input("Щоб повернутись назад, натисніть Enter\n")
    elif buying == 'Щит':
        character.balance -= pricerand1
        if character.balance < pricerand1:
            print("Вам не вистачає грошей.")
        print(f"Ви купували Щит!")
        character.add_item('Щит')
        character.update_stats()
        back = input("Щоб повернутись назад, натисніть ENTER\n")
    elif buying == 'Дрібничка':
        character.balance -= pricerand2
        if character.balance < pricerand2: print("Вам не вистачає грошей.")
        print(f"Ви купували Дрібничку!")
        character.add_item('Дрібничка')
        character.update_stats()
        back = input("Щоб повернутись назад, натисніть ENTER\n")
    elif buying == 'Вудочка':
        character.balance -= pricerand2
        if character.balance < pricerand2: print("Вам не вистачає грошей.")
        print(f"Ви купували Вудочку!")
        character.add_item('Вудочка')
        character.update_stats()
        back = input("Щоб повернутись назад, натисніть ENTER\n")
    if back == '':
        welcomeclass.welcome(character.name, character.balance)
    




