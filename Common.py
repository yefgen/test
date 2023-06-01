from Game.GameProcess import *

class Common:

    @staticmethod
    def check_exit(is_exit=False):
        print('\nХотите выйти?\nд - Выйти\tн - Остаться')
        choise = input('\nВаш выбор: ').lower()

        if choise == 'д':
            print('\nДо свидания!')
            is_exit = True

        return is_exit

    # @staticmethod
    # def check_GG(is_exit=False):
    #     print('\nВы проиграли\n')
    #     choise = input('\nНачать новую игру?\nд - Да \tн - Нет').lower()
    #     if choise == 'д':
    #         Menu().start_menu()
    #     else:
    #         print('\nДо свидания!')
    #         is_exit = True
    #     return is_exit


