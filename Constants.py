import random
#список мобов
names_mob = ['Skeleton', 'Gnoll', 'Spider', 'Goblin', 'Zombie']
#словарь, в котором хранятся данные по мобам
mobs = {
    'Skeleton':[random.randint(25, 101), random.randint(5, 16)],
    'Gnoll': [random.randint(30, 151), random.randint(10, 21)],
    'Spider': [random.randint(4, 96), random.randint(3, 11)],
    'Goblin': [random.randint(15, 127), random.randint(10, 26)],
    'Zombie': [random.randint(19, 196), random.randint(12, 36)]
}
#в этом классе лежат строки, которые нужно выводить в меню
class Constants:
    MENU = '\nГлавное мемню\n' \
           '1 - Играть\n' \
           '----------------------\n' \
           '0 - Выход\n'

    CREATING = '\nМеню создания персонажа\n' \
           '1 - Создать героя\n' \
           '2 - Создать моба\n' \
           '3 - Начать игру\n' \
           '-------------------------\n' \
           '0 - Выход\n'

    GAME = '\nИгровое меню\n' \
           '1 - Выбор противника\n' \
           '2 - Сражаться\n' \
           '3 - Посмотреть статистику\n' \
           '4 - Купить айтемы\n' \
           '-------------------------\n' \
           '0 - Выход\n' \

    BATTLE = '\nМеню битвы\n' \
           '1 - Атака\n' \
           '2 - Хил\n' \
           '-------------------------\n' \
           '0 - Выход\n'