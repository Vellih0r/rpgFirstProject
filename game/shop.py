from random import randint
from welcomeclass import decorator

#f
# привітати в магазині та рандомно розрахувати ціну у словник
@decorator
def shopfunc(nickname, balance, items, potions):
    print(f'''
        Вітаємо в магазині, {nickname}!
      Твій баланс: {balance}
''')
    global dict, dict2
    dict = {}
    dict2 = {}
    for i in items:
        pricerand = randint(10,40)
        dict[i] = pricerand
    for i in potions:
        pricerand = randint(50, 70)
        dict2[i] = pricerand
    dict['Вудочка'] = 25
    
    for key, val in dict.items():
        print(f"Товар {key} коштує {val}\n")

    for key, val in dict2.items():
        print(f"Зілля {key} коштує {val}\n")


def display():
    for key, val in dict.items():
        print(f"Товар {key} коштує {val}\n")

    for key, val in dict2.items():
        print(f"Зілля {key} коштує {val}\n")


# гравець вибирає та купує предмет
def buy(character):
    # вибір предмету по назві
    buying = input("Чи бажаєте ви купити щось?\n\
Якщо так, введіть назву предмета\n")

    buying = buying.title()
    print(buying)
    if buying == 'Клінок':
        if character.balance < dict['Клінок']: 
            print("Вам не вистачає грошей.")
        else:
            character.balance -= dict['Клінок']
            print("Ви купували Клінок!")
            character.add_item('Клінок')
            character.update_stats("new")
    elif buying == 'Щит':
        if character.balance <  dict['Щит']:  
            print("Вам не вистачає грошей.")
        else:
            character.balance -=  dict['Щит']
            print("Ви купували Щит!")
            character.add_item('Щит')
            character.update_stats("new")
    elif buying == 'Дрібничка':
        if character.balance < dict['Дрібничка']: 
            print("Вам не вистачає грошей.")
        else: 
            character.balance -= dict['Дрібничка']
            print("Ви купували Дрібничку!")
            character.add_item('Дрібничка')
            character.update_stats("new")
    elif buying == 'Вудочка':
        if character.balance < dict['Вудочка']: 
            print("Вам не вистачає грошей.")
        else:
            character.balance -= dict['Вудочка']
            print("Ви купували Вудочку!")
            character.add_item('Вудочка')
            character.update_stats("new")
    elif buying == "Зілля Здоров'Я":
        if character.balance < dict2["Здоров'я"]:
            print("Вам не вистачає грошей.")
        else:
            character.balance -= dict2["Здоров'я"]
            print("Ви купували зілля здоров'я!")
            character.add_potion("Здоров'я")
    elif buying == "Зілля Прокляте":
        if character.balance < dict2["Прокляте"]:
            print("Вам не вистачає грошей.")
        else:
            character.balance -= dict2["Прокляте"]
            print("Ви купували прокляте зілля!")
            character.add_potion("Прокляте")
    elif buying == "Зілля Сили":
        if character.balance < dict2["Сили"]:
            print("Вам не вистачає грошей.")
        else:
            character.balance -= dict2["Сили"]
            print("Ви купували зілля сили!")
            character.add_potion("Cили")
    




