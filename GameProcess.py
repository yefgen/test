from Game.Creating import *
from Game.Constants import *


class GameProcess():
    @staticmethod
    def create_player():
        global player
        print('\nСоздаём героя с рандомными параметрами\n')
        player = Player(input('Введи имя игрока: '), random.randint(70, 126), random.randint(75, 146))
        player.print_info()
        return player

    @staticmethod
    def choose_mob():
        global enemy
        print('\nВыбери моба для драки с ним\n')
        amount = 1
        for mob in names_mob:
            print(f'{amount}. {mob}\n')
            amount += 1

        choise = input('Введите название моба: ')
        if choise in names_mob:
            key = choise
            enemy = Hero(key, mobs[key][0], mobs[key][1])
        enemy.print_info()
        return enemy

    @staticmethod
    def create_mob():
        global enemy
        print('Создайте своего противника')
        mob_name = input('Введите название моба: ')
        new_choise = input('Зарандомить параметры моба?\nд - да\tн - нет:\n').lower()
        if new_choise == 'д':
            mob_health = random.randint(10, 150)
            mob_damage = random.randint(5, 25)
        else:
            mob_health = int(input('Введите здоровье моба: '))
            mob_damage = int(input('Введите урон моба: '))
        mobs[mob_name] = [mob_health, mob_damage]
        names_mob.append([mob_name])
        enemy = Hero(mob_name, mob_health, mob_damage)

    # def create_pair(self):
    #     self.create_player()
    #     self.choose_mob()



# player = GameProcess.create_player()
#
# enemy = GameProcess.choose_mob()