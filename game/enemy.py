from random import randint
#f
# maks priv2
class Enemy():
    def __init__(self, hp = randint(10, 35), dmg = randint(5, 16)):

        #added enemy stats
        self.__hp = hp
        self.dmg = dmg

    def enemyAtack(self):

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
     