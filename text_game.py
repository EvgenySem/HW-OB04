from abc import ABC, abstractmethod

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = Fists()

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f'Боец {self.name} подобрал новое оружие: {new_weapon.weapon_name}')


class Monster:
    def __init__(self, monster_type):
        self.monster_type = monster_type

    def defeated(self):
        print(f'{self.monster_type} был повержен!')


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self):
        self.weapon_name = 'Меч'

    def attack(self):
        print('Врагу нанесен рассекающий удар мечем!')


class Bow(Weapon):
    def __init__(self):
        self.weapon_name = 'Лук'

    def attack(self):
        print('Враг получил урон стрелой!')


class Shotgun(Weapon):
    def __init__(self):
        self.weapon_name = 'Дробовик'

    def attack(self):
        print('Враг получил критический урон дробью!')


class Fists(Weapon):
    def __init__(self):
        self.weapon_name = 'Кулаки'

    def attack(self):
        print('Врага поколотили кулаками!')


def fight(fighter, weapon, monster):
    fighter.change_weapon(weapon)
    weapon.attack()
    monster.defeated()


fighter_Jack = Fighter('Jack')
zombie = Monster('Зомби')
werewolf = Monster('Оборотень')

fight(fighter_Jack, Bow(), zombie)
fight(fighter_Jack, Sword(), zombie)
fight(fighter_Jack, Shotgun(), werewolf)
