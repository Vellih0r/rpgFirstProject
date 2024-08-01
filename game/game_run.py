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

# добавлено выборковая переменная для определения куда пойдет юзер  И  проверка на ошибки; by artyom
choice = int(input("введіть 1,2 чи 3 щоб обрати...\n"))

if choice == 1: Hero.display_stats()
elif choice == 2:
    shop.shopfunc(Hero.name, Hero.balance, Hero.items)
    shop.buy(Hero)
    shop.choice(Hero)
elif choice == 3: Hero.inv()
else:
    print("Невизначений вибір.")

