import player
from welcomeclass import decorator

@decorator
def shop(nickname, balance, items):
    for item in items:
        print(f"{item}\n")
    print(f'''
        Вітаємо в магазині, {nickname}!
      Твій баланс: {balance}
{items[0]}
{items[1]}
{items[2]}
''')
    