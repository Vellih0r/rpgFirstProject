import player
import welcomeclass
import shop
from threading import Thread
import pyglet

# функція для потоку з музикою
def music():
    music = pyglet.resource.media("dark.mp3")
    music.play()
    pyglet.app.run()
    # перевірка чи треба зупинити поток
# Создаём новый поток
th = Thread(target=music)


# добавлена переменная с запросом никнейма; by artyom
nickname = input("Введіть свій нікнейм:\n")

# запустити поток з музикою
th.start()

# создание объекта на основе класса player.Player который передаёт один аргумент; by artyom
Hero = player.Player(nickname)

# вызов фукнции 'welcome'
welcomeclass.welcome(Hero.name, Hero.balance)

# нескічненний цикл з грою поки гравец не напише "Вихід"
while True:

    # нехай буде перевірка смерті
    if Hero.health <= 0:
        print(f"Ваше здоров'я = 0, ви програли")
        # зупинити музику
        pyglet.app.exit()
        break


    # змінна щоб визначити дію гравця на цю ітерацію
    action = (input('''Що ви хочите зробити?
якщо не знаєте напишіть "допомога": '''))
    action = action.title()
    
    try:
        if action == "Стати": Hero.display_stats()
        elif action == "Магазин": 
            shop.shopfunc(Hero.name, Hero.balance, Hero.items, Hero.potions)
            shop.buy(Hero)
        elif action == "Інв": Hero.disp_invent()
        elif action == "Рибачити": Hero.fishing_process()
        elif action == "Вихід": pyglet.app.exit(); break
        elif action == "Ліс": Hero.fight_process('enemy')
        elif action == "Зілля": Hero.poition_use()
        elif action == "Босс": Hero.fight_process('boss')
        elif action == "Хіл": Hero.hospital()
        elif action == "Допомога":
            print('''Список дій:
| Стати - показати стати
| Магазин - зайти в магазин
| Інв - показати інвентар
| Рибачити - піти на рибалку щоб заробити грошей
| Зілля - використати зілля
| Босс - кинути виклик боссу                
| Хіл - піти до госпіталю                                  
| Ліс - піти у ліс для битви з ворогами
| Вихід - вийти з гри''')
        else:
            print("Такої дії неіснує")
    except BaseException as a:
        print("Помилка", a)