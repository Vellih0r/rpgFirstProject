from random import randint
class Boss():
    def __init__(self):
        self.name = "Мог повелитель крови"
        self.__hp = 300
        self.dmg = 0
        self.mag_resistance = 3 #maks priv
        
#атаки
    def enemyAtack(self):
        block__counter = 0
        atack = randint(1,2)
        if self.__hp > 150:
            atack = randint(1,2)
            if block__counter > 0:
                print("У вас появилось окно для удара:")
                block__counter -= 1  
                return 0
            if atack == 1:
                self.dmg = 15
                print("Мог совершил круговой удар копьем вокруг себя 'вам нанесли 15 урона'")
                return  15
            if atack == 2:
                self.dmg = 25
                print("Мог нанес удар копьем в прыжке Вам нанесли 25 урона")
                return  25
        elif self.__hp < 150:
            atack = randint(1,4) 
            if block__counter > 0:
                print("У вас появилось окно для удара:")
                block__counter -= 1   
            if atack == 1:
                self.dmg = 15
                print("Мог совершил круговой удар копьем вокруг себя 'вам нанесли 15 урона'")
                return self.dmg
            if atack == 2:
                self.dmg = 25
                print("Мог нанес удар копьем в прыжке Вам нанесли 25 урона")
                return self.dmg
            if atack == 3:
                self.dmg = 35
                print("Мог использовал магию крови и попал в вас кровавыми лезвиями 'Вам нанесли 35 урона' ")
                return self.dmg
            if atack == 4:
                self.dmg = 25
                self.__hp += 20
                print("Мог нанес вам сокрушительный удар копьем 'Вам нанесли 25 урона' \n ВРАГ ОТХИЛИЛСЯ")
                block__counter += 1
                return self.dmg


    @property
    def hp(self):
        return self.__hp
        
    @hp.setter
    def hp(self, __hp):
        self.__hp = __hp
        