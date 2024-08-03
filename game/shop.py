import player
from random import randint
import welcomeclass
from welcomeclass import decorator




# привітати в магазині та рандомно розрахувати ціну у словник
@decorator
def shopfunc(nickname, balance, items):
    print(f'''
        Вітаємо в магазині, {nickname}!
      Твій баланс: {balance}
''')
    global dict 
    dict = {}
    for i in items:
        pricerand = randint(10,40)
        dict[i] = pricerand
    
    for key, val in dict.items():
        print(f"Товар {key} коштує {val}\n")

# гравець вибирає та купує предмет
def buy(character):
    # вибір предмету по назві
    buying = input("Чи бажаєте ви купити щось?\n\
Якщо так, введіть назву предмета\n")

    buying = buying.title()

    if buying == 'Клінок':
        if character.balance < dict['Клінок']: 
            print("Вам не вистачає грошей.")
            back = input("Щоб повернутись назад, натисніть ENTER\n")
        else:
            character.balance -= dict['Клінок']
            print("Ви купували Клінок!")
            character.add_item('Клінок')
            character.update_stats()
            back = input("Щоб повернутись назад, натисніть Enter\n")
    elif buying == 'Щит':
        if character.balance <  dict['Щит']:  
            print("Вам не вистачає грошей.")
            back = input("Щоб повернутись назад, натисніть ENTER\n")
        else:
            character.balance -=  dict['Щит']
            print("Ви купували Щит!")
            character.add_item('Щит')
            character.update_stats()
            back = input("Щоб повернутись назад, натисніть ENTER\n")
    elif buying == 'Дрібничка':
        if character.balance < dict['Дрібничка']: 
            print("Вам не вистачає грошей.")
            back = input("Щоб повернутись назад, натисніть ENTER\n")
        else: 
            character.balance -= dict['Дрібничка']
            print("Ви купували Дрібничку!")
            character.add_item('Дрібничка')
            character.update_stats()
            back = input("Щоб повернутись назад, натисніть ENTER\n")
    elif buying == 'Вудочка':
        character.balance -= dict['Вудочка']
        if character.balance < dict['Вудочка']: 
            print("Вам не вистачає грошей.")
            back = input("Щоб повернутись назад, натисніть ENTER\n")
        else:
            character.balance -= dict['Вудочка']
            print("Ви купували Вудочку!")
            character.add_item('Вудочка')
            character.update_stats()
            back = input("Щоб повернутись назад, натисніть ENTER\n")
    if back == '':
        welcomeclass.welcome(character.name, character.balance)
    




