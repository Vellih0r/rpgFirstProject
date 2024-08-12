from random import randint


class Enemy():
<<<<<<< HEAD
    def __init__(self, hp = randint(20, 50), dmg = randint(5, 16), crit = randint(0, 101)):
=======
    def __init__(self, name, hp = randint(20, 50), dmg = randint(5, 16)):
        self.name = name 
>>>>>>> 0fa7c13ec51c5c2d83767155a4a07d28b59f0c8b
        #added enemy stats
        self.__hp = hp
        self.dmg = dmg

    def enemyAttack(self):

            # розрахунок шансу кріта
            crit = randint(0, 101)
            dmg = self.dmg
            if crit > 90:
                dmg *= 2
                print(f"\nВорог наносить критичний удар!\n Ви отримали - {dmg} - урону")
            else:
                print(f"\nВорог наносить удар!\n Ви отримали - {dmg} - урону")
                
            # повернути скільки нанесли урону
            return dmg
    
    @property
    def hp(self):
        return self.__hp
        
    @hp.setter
    def hp(self, hp):
        self.__hp = hp