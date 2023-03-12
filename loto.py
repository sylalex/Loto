import random


class Ticket:
    def __init__(self):
        tck = [[], [], []]
        lst = [i for i in range(1, 91)]
        j = 0
        for k in range(len(lst)):
            number = random.choice(lst)
            lst.remove(number)
            for line in range(3):
                if len(tck[line]) > 4:
                    continue
                is_number = False
                for n in tck[line]:
                    n1 = 8 if number == 90 else number // 10
                    n2 = 8 if n == 90 else n // 10
                    if n1 == n2:
                        is_number = True
                        break
                if not is_number:
                    tck[line].append(number)
                    j += 1
                    break
            if j > 14:
                break
        for line in range(3):
            tck[line].sort()
        self.tck = tck
        self.name = 'User'
        self.is_game = True

    def name(self, name):
        self.name = name

    def remove(self, number):
        self.is_game = False
        for line in range(len(self.tck)):
            if number in self.tck[line]:
                self.tck[line].remove(number)
                self.is_game = True
                break

    def print(self):
        print(self.name)
        print('-' * 30)

        for line in range(3):
            j = 0
            for i in range(len(self.tck[line])):
                n = self.tck[line][i] // 10
                if n != j:
                    print(' ' * 3 * (n - j), end='')
                if n == 0:
                    print(' ', end='')
                print(self.tck[line][i], end=' ')
                j = n + 1
            print()
        print('-' * 30)


if __name__ == '__main__':
    comp_ticket = Ticket()
    comp_ticket.name = 'Компьютер'
    user_ticket = Ticket()
    user_ticket.name = 'Пользователь'
    bag = [i for i in range(1, 91)]
    while True:
        comp_ticket.print()
        user_ticket.print()
        number = random.choice(bag)
        bag.remove(number)
        print('Выпал номер:', number)
        print('1. Зачеркнуть')
        print('2. Продолжить')
        choise = int(input('Выберите пункт: '))
        if choise == 1:
            comp_ticket.remove(number)
            user_ticket.remove(number)
            if not user_ticket.is_game:
                print('Цифры на карточке нет. Вы проиграли и игра закончилась')
                break
        elif choise == 2:
            comp_ticket.remove(number)
            user_ticket.remove(number)
            if user_ticket.is_game:
                print('Цифра есть на карточке. Вы проиграли и игра закончилась')
                break
        if len(comp_ticket.tck[0] + comp_ticket.tck[1] + comp_ticket.tck[2]) == 0:
            print('Компьютер выиграл.')
            break
        if len(user_ticket.tck[0] + user_ticket.tck[1] + user_ticket.tck[2]) == 0:
            print('Вы выиграли.')
            break
