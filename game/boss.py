from random import randint
from colorama import init,Fore,Style
class Boss():
    def __init__(self):
        self.name = "Мог повелитель крови"
        self.__hp = 300
        self.dmg = 0
        self.mag_resistance = 3 #maks priv
        #f
#атаки
    def enemyAtack(self):
        block__counter = 0
        atack = randint(1,2)
        if self.__hp > 150:
            atack = randint(1,2)
            if block__counter > 0:
<<<<<<< HEAD
                print("У вас появилось окно для удара:")
                block__counter -= 1
=======
                print(Fore.GREEN +"У вас появилось окно для удара:"+ Style.RESET_ALL)
                block__counter -= 1  
>>>>>>> cb6a9f70b26f3f1831a6d391129272bd930d723f
                return 0
            if atack == 1:
                self.dmg = 15
                print(Fore.RED + "Мог совершил круговой удар копьем вокруг себя 'вам нанесли 15 урона'" + Style.RESET_ALL)
                return  15
            if atack == 2:
                self.dmg = 25
                print(Fore.RED +"Мог нанес удар копьем в прыжке Вам нанесли 25 урона"+ Style.RESET_ALL)
                return  25
        elif self.__hp < 150:
            atack = randint(1,4) 
            if block__counter > 0:
                print(Fore.GREEN +"У вас появилось окно для удара:"+ Style.RESET_ALL)
                block__counter -= 1   
            if atack == 1:
                self.dmg = 15
                print(Fore.RED +"Мог совершил круговой удар копьем вокруг себя 'вам нанесли 15 урона'"+ Style.RESET_ALL)
                return self.dmg
            if atack == 2:
                self.dmg = 25
                print(Fore.RED +"Мог нанес удар копьем в прыжке Вам нанесли 25 урона"+ Style.RESET_ALL )
                return self.dmg
            if atack == 3:
                self.dmg = 35
                print(Fore.RED +"Мог использовал магию крови и попал в вас кровавыми лезвиями 'Вам нанесли 35 урона' "+ Style.RESET_ALL)
                return self.dmg
            if atack == 4:
                self.dmg = 25
                self.__hp += 20
                print(Fore.RED +"Мог нанес вам сокрушительный удар копьем 'Вам нанесли 25 урона' \n ВРАГ ОТХИЛИЛСЯ"+ Style.RESET_ALL)
                block__counter += 1
                return self.dmg

    @property
    def hp(self):
        return self.__hp
        
    @hp.setter
    def hp(self, __hp):
        self.__hp = __hp
        