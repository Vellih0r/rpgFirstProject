

# перенёс функцию welcome() в отдельный класс
# добавил декорацию для текста приветствия; by artyom
# просто звёздочки)))
# отъебитесь, просто это красиво)
def decorator(insidefunc):
    def outfunc(*args):
        print('*' *  60)
        insidefunc(*args)
        print('*' *  60)
    return outfunc

# добавлено примерное начало игры; by artyom
@decorator
def welcome(nickname, balance):
    print(f'''
        Вітаємо в нашій грі, {nickname}!
      Твій баланс: {balance}
    У тебе є:
| Стати
| Інвентар
| Ти можеш купити предмети в магазині
| Заробити гроші можеш рибалкою
''')