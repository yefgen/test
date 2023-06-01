import random
import time


class Hero:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.health = hp
        self.damage = dmg

    def print_info(self):
        print(f'\n{self.name} с параметрами здоровья {str(self.health)} и урона {str(self.damage)}\n')

    def attack(self, enemy):

        enemy.health -= self.damage
        print(f'{self.name} наносит удар с силой {str(self.damage)} по {enemy.name}\n'
              f'Количество здоровья у {enemy.name} уменьшилось до {str(enemy.health)}\n')


class Player(Hero):
    def heal(self):
        min_heal = int(round(0.1*self.health-5,0))
        max_heal = int(round(0.2*self.health+5,0))
        healing = random.randint(min_heal, max_heal)
        self.health += healing
        print(f'{self.name} захилился на {healing} хп\n'
              f'Теперь у {self.name} уровень здоровья {self.health}\n')

    def battle(self, enemy):
        self.attack(enemy)
        time.sleep(1)

        enemy.attack(self)
        time.sleep(1)
