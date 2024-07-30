class Person:
    def __init__(self, name):
        self. name = name
        if self.name == 'Misha':
            print("Создан Миша")
        elif self.name == 'Artyom':
            print("Создан Артём")

misha = Person("Misha")
artyom = Person("Artyom")
