from Game.Common import *
from Game.GameProcess import *

class Menu:

    @staticmethod
    def check_GG(is_exit=False):
        print('\nВы проиграли\n')
        choise = input('\nНачать новую игру?\nд - Да \tн - Нет').lower()
        if choise == 'д':
            Menu().start_menu()
        else:
            print('\nДо свидания!')
            is_exit = True
        return is_exit

    def start_menu(self, is_exit=False):
        print(Constants.MENU)
        while not is_exit:

            try:
                match int(input('Ваш выбор: ')):
                    case 1: Menu().creating_menu()
                    case 0: Common().check_exit()
                    case _: print("Неверный выбор")
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')

    def creating_menu(self):
        global player
        print(Constants.CREATING)
        while True:

            try:
                match int(input('Ваш выбор: ')):
                    case 1: player = GameProcess().create_player() #создание персонажа
                    case 2: GameProcess().create_mob() #создание моба
                    case 3: Menu().game_menu()
                    case 0: break
                    case _: print("Неверный выбор")
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')

    def game_menu(self):
        global enemy
        while True:
            print(Constants.GAME)

            try:
                match int(input('\nВаш выбор: ')):
                    case 1: enemy = GameProcess().choose_mob()
                    case 2: Menu().battle_menu()
                    case 3: pass
                    case 4: pass
                    case 0: break
                    case _: print("Неверный выбор")
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')

    def battle_menu(self):
        while True:
            if enemy.health <= 0:
                print(f'GG! {player.name} затащил в соляново!')
                break
            elif player.health <= 0:
                print(f'GG! {enemy.name} отправил в могилу {player.name}!')
                Common.check_GG()

            print(Constants.BATTLE)

            try:
                match int(input('\nВаш выбор: ')):
                    case 1: player.attack(enemy)
                    case 2: player.heal()
                    case 0: Common.check_exit()
                    case _: print("Неверный выбор")
            except ValueError:
                print('Неверный ввод! Попробуйте ещё раз.')


Menu().start_menu()
