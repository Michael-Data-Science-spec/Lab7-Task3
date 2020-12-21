'''
This module is created for level 2
'''
import random
import _221_lucky as lucky
import _221_happy as happy
import _221_ulam as ulam
import _221_case as case
import time

def timeprint(line):
    """
    Функція друкує літери у live режимі (кожна літера з певним інтервалом)
    """
    for i in line:
        print(i, end = "", flush = True)
        time.sleep(0.01)
    print()

def get_bin(num_type, tickets):
    """
    функція генерує 12 рандомних чисел в залежності від того типу, що обере \
    користувач. Функція видає по одному рандомному числу, а користувач повинен \
    ввести 1 чи 0 в залежності від того чи це число є вибраним типом чи ні. В \
    залежності від того, чи користувач ввів правильне число чи ні, функція \
    виводить "Неправильна відповідь" (додається талон) або "Правильно". Якщо користував ввів не 1 \
    і не 0, то виводить "Неправильний ввід, введіть '1', якщо це число", \
    num_type, ", або '0', якщо ні". Наступне завдання: із введених одиниць та \
    нуликів утворюється два бінарних числа які необхідно перевести назад \
    в десятковий вигляд та ввести через пробіл. Після правильного введення користувач \
    вводить help, а далі в залежності від чисел користувач повинен ввести літери\
    англійського алфавіту. Після успішного введення літер користувач \
    переходить до наступного рівня."
    """
    tickets = int(tickets)
    module = globals()[num_type]  # assigns module variable a function num_type (ulam, lucky or happy)
    is_ulam = [True, False]  # is used to randomly decide if next values printed will be ulam or not
    num_lst = module.generate_lst(100)  # the list of numbers requested by user
    other_lst = []
    for i in range(1, 100):
        if i not in num_lst:
            other_lst.append(i)
    # creates the list of numbers from 1 to 100 that are not present in num_lst

    bin_s = ""
    for _ in range(12):
        ulam_num = random.choice(is_ulam)  # is used to randomly decide if next values printed will be ulam or not
        if ulam_num:
            print(random.choice(num_lst))
            answer = True
            while answer:
                user_answer = input()
                case.quit_func(user_answer)  # if user wants to stop the execution and types 'quit'
                try:
                    assert (user_answer == '0' or user_answer == '1')
                    answer = False  # stops the cycle after user input is '0' or '1'
                except AssertionError:
                    print("Неправильний ввід, введіть '1', якщо це число",
                          num_type, ", або '0', якщо ні")
        else:
            print(random.choice(other_lst))
            answer = True
            while answer:
                user_answer = input()
                case.quit_func(user_answer)  # if user wants to stop the execution and types 'quit'
                try:
                    assert (user_answer == '0' or user_answer == '1')
                    answer = False  # stops the cycle after user input is '0' or '1'
                except AssertionError:
                    print("Неправильний ввід, введіть '1', якщо це число",
                          num_type, ", або '0', якщо ні")
        if int(user_answer) == ulam_num:  # checks if user answer is right
            timeprint("Правильно")
        else:
            tickets = tickets + 1
            if case.check_tickets(tickets) == 0:  # zero stands for False
                return False
            timeprint("Неправильна відповідь")
            print("Тепер у вас", tickets, "талони")\

        bin_s = '{}{}'.format(bin_s, str(int(ulam_num)))
        # creates binary string where ones represent 
        # num_type numbers and zeroes represent other numbers

    bin1 = bin_s[:6]
    bin2 = bin_s[6:]
    timeprint("Вітаємо, наступне завдання: \nЗ введених одиниць та нуликів у вас \
утворилося два бінарних числа. Переведіть їх назад в десятковий вигляд \
та введіть через пробіл.")
    print(bin1 + "\n" + bin2)
    timeprint("Введіть два числа через пробіл двічі:")
    clues = [clue1, clue2]
    while True:
        user_input = input("Подумайте краще:")
        case.quit_func(user_input)  # if user wants to stop the execution and types 'quit'
        if user_input == 'help':
            try:
                clues[0]()
                clues.pop(0)
            except IndexError:
                timeprint("Підказок до цієї частини більше немає")
        # outputs clues in case user needs clues

        elif (int(user_input.split()[0]) == int(bin1, 2)
              and int(user_input.split()[1]) == int(bin2, 2)):
              break
        else:
            pass
    timeprint("Правильно, що далі?")
    timeprint("Для підказки введіть 'help'")
    clues = [clue3]
    while True:
        user_input = input("Введіть відповідь:")
        case.quit_func(user_input)  # if user wants to stop the execution and types 'quit'
        if user_input == 'help':
            try:
                clues[0]()
                clues.pop(0)
            except IndexError:
                timeprint("Підказок до цієї частини більше немає")
        # outputs clues in case user needs clues

        elif (user_input.split()[0].upper() == chr((int(bin1, 2) % 26) + 65)
              and user_input.split()[1].upper() == chr((int(bin2, 2) % 26) + 65)):
              break
        else:
            pass
    tickets = str(tickets)
    return tickets


def clue1():
    '''
    Виводить першу підказку
    '''
    timeprint("А зараз - саме час застосувати знання про двійкову систему\
 числення:")


def clue2():
    '''
    Виводить другу підказку
    '''
    timeprint("Переведіть двійкове число в десятковий вигляд")


def clue3():
    """
    функція виводить заданиий текст у live режимі
    """
    timeprint("Числа відповідають латинським літерам в алфавіті. Введіть \
англійські літери з великої букви через пробіл, які відповідають заданим \
індексам в алфавіті (Вважайте, що А - 0, Z - 25. У випадку, коли число більше \
26, треба взяти його остачу при діленні на 26)")


# def clue4():
#     timeprint("А - 0, Z - 25, якщо число, більше 26, треба взяти його\
#  остачу при діленні на 26. Введіть букви через пробіл")

