'''
This module is created for level 1
'''
import _221_ulam as ulam
import _221_happy as happy
import _221_lucky as lucky
import random
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

def level1(tickets):
    """
    функція генерує 10 рандомних чисел (ulam, happy і lucky). Далі 3 етапи: 
    1 - перевіряє, чи введені користувачем числа є Ulam. 2 - чи є інші введені \
    числа happy, 3- lucky. В залежності від правильності вводу користувача \
    виводить "Правильно" або "Неправильна відповідь". Якщо користувач \
    помилився при введені чисел, то додається талон.
    """
    ulam_lst = ulam.generate_lst(50)
    lucky_lst = lucky.generate_lst(50)
    happy_lst = happy.generate_lst(50)
    line = []
    for _ in range(10):
        line.append(random.randint(1, 50))

    ulam_lst = [str(x) for x in sorted(list(set(line) & set(ulam_lst)))]
    happy_lst = [str(x) for x in sorted(list(set(line) & set(happy_lst)))]
    lucky_lst = [str(x) for x in sorted(list(set(line) & set(lucky_lst)))]
    # [x in sorted(set1 & set2)] is used to sort the line and exclude all repetitions
    # reassigns ulam_lst, happy_lst, lucky_lst variables to no-repetition, 
    # sorted string line of corresponding values
    line = [str(x) for x in line]
    line = " ".join(line)
    print(line)
    while True:
        # timeprint(ulam_lst)
        timeprint("Введіть всі числа улама через пробіл від меншого\
 до більшого: ")
        user_input = input()
        case.quit_func(user_input)  # if user wants to stop the execution and types 'quit'
        if user_input.split() == ulam_lst:
            timeprint("Правильно")
            break
        else:
            tickets = tickets + 1
            if case.check_tickets(tickets) == 0:
                return False
            timeprint("Неправильна відповідь")
            print("Тепер у вас", tickets, "талони")

    while True:
        # timeprint(happy_lst)
        timeprint("Введіть всі щасливі числа через пробіл від меншого\
 до більшого: ")
        user_input = input()
        case.quit_func(user_input)  # if user wants to stop the execution and types 'quit'
        if user_input.split() == happy_lst:
            timeprint("Правильно")
            break
        else:
            tickets = tickets + 1
            if case.check_tickets(tickets) == 0:  # zero stands for False
                return False
            timeprint("Неправильна відповідь")
            print("Тепер у вас", tickets, "талони")

    while True:
        # timeprint(lucky_lst)
        timeprint("Введіть всі вдалі числа через пробіл від меншого\
 до більшого: ")
        user_input = input()
        case.quit_func(user_input)  # if user wants to stop the execution and types 'quit'
        if user_input.split() == lucky_lst:
            timeprint("Правильно")
            break
        else:
            tickets = tickets + 1
            if case.check_tickets(tickets) == 0:  # zero stands for False
                return False
            timeprint("Неправильна відповідь")
            print("Тепер у вас", tickets, "талони")
    tickets = str(tickets)
    return tickets
