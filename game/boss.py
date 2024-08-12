from random import randint
class Boss():
    def __init__(self):
        self.name = "Мог повелитель крови"
        self.hp = 500
        self.dmg = 0
        self.mag_resistance = 3 #maks priv


    def enemyAtack(self):
        block_counter = 0
        atack = randint(1,3)
        if self.hp > 250:
            atack = randint(1,3)
            if block_counter > 0:
                print("У вас появилось окно для удара:")
                block_counter -= 1   
            if atack == 1:
                self.dmg = 30
                return self.dmg
            if atack == 2:
                self.dmg = 50
                return self.dmg
        if self.hp < 250:
            atack = randint(1,5) 
            if block_counter > 0:
                print("У вас появилось окно для удара:")
                block_counter -= 1   
            if atack == 1:
                self.dmg = 30
                return self.dmg
            if atack == 2:
                self.dmg = 50
                return self.dmg
            if atack == 3:
                self.dmg = 70
                return self.dmg
            if atack == 4:
                self.dmg = 50
                self.hp += 40
                block_counter += 1
                return self.dmg


    @property
    def hp(self):
        return self.__hp
        
    @hp.setter
    def hp(self, hp):
        self.__hp = hp