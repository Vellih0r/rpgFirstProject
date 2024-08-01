import player
import welcomeclass
import shop


# ВСЁ, что ниже мы можем закинуть в бесконечный игровой цикл ↓ ↓ ↓


# добавлена переменная с запросом никнейма; by artyom
nickname = input("Введіть свій нікнейм:\n")

# создание объекта на основе класса player.Player который передаёт один аргумент; by artyom
Hero = player.Player(nickname)

# вызов фукнции 'welcome'
welcomeclass.welcome(Hero.name, Hero.balance)


# нескічненний цикл з грою поки гравец не напише "Вихід"
while True:

    # нехай буде перевірка смерті
    if Hero.health <= 0:
        print(f"Ваше здоров'я = {Hero.health}, ви програли")
        break


    # змінна щоб визначити дію гравця на цю ітерацію
    action = (input('''Що ви хочите зробити?
якщо не знаєте напишіть "допомога": '''))
    action = action.title()
    
    try:
        if action == "Стати": Hero.display_stats()
        elif action == "Магазин": 
            shop.shopfunc(Hero.name, Hero.balance, Hero.items)
            shop.buy(Hero)
        elif action == "Інв": Hero.inventory()
        elif action == "Рибачити": Hero.fishing_process()
        elif action == "Вихід": break
        elif action == "Допомога":
            print('''Список дій:
| Стати - показати стати
| Магазин - зайти в магазин
| Інв - показати інвентар
| Рибачити - піти на рибалку щоб заробити грошей
| Ліс - піти у ліс для битви з ворогами
| Вихід - вийти з гри''')
        else:
            print("Такої дії неіснує")
    except BaseException as a:
        print("Помилка", a)